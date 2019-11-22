"""Sum class used to serve HTTP requests 
that demand getting a sum of values."""

from typing import Callable, Tuple
from enum import Enum
from collections import namedtuple
from flask_restful import Resource, reqparse
from api.constants import (
    Location,
    Messages,
    HTTPCodes,
    ResponseFields,
)
from api import secrets


class SumEndpoints(str, Enum):
    GETSUM = 'getSumValue'


class Sum(Resource):
    """Sum class used to serve HTTP requests."""
    RequestParameter = namedtuple(
        'RequestParam',
        ['name', 'datatype', 'default'],
    )
    Values = RequestParameter('values', str, [])
    Token = RequestParameter('token', None, None)

    def get(self) -> Tuple[dict, int]:
        parser = reqparse.RequestParser()
        parser.add_argument(
            name=Sum.Values.name,
            type=Sum.Values.datatype,
            default=Sum.Values.datatype,
        )
        parser.add_argument(
            Sum.Token.name,
            location=Location.HEADERS,
        )
        result = parser.parse_args()

        token = result.get(Sum.Token.name)
        if not self._validate_token(token):
            return {
                ResponseFields.CODE: HTTPCodes.UNAUTHORIZED,
                ResponseFields.MESSAGE: Messages.INVALID_TOKEN,
                ResponseFields.RESULT: '',
            }, HTTPCodes.UNAUTHORIZED

        raw_values = result[Sum.Values.name]
        try:
            values = self._parse_items(
                raw_values,
                output_type=int,
            )
        except ValueError as err:
            return {
                ResponseFields.CODE: err.args[1],
                ResponseFields.MESSAGE: err.args[0],
                ResponseFields.RESULT: '',
            }, err.args[1]

        result = sum(values)
        return {
            ResponseFields.CODE: HTTPCodes.OK,
            ResponseFields.MESSAGE: Messages.DONE,
            ResponseFields.RESULT: result,
        }, HTTPCodes.OK

    @staticmethod
    def _validate_token(token: str) -> bool:
        """Validate token against a token store."""
        return token == secrets.TOKEN

    @staticmethod
    def _parse_items(items: str, output_type: Callable) -> list:
        """
        Attempt to parse a list of strings into a list of items of given type.
        '6,7,8,9', int => [6,7,8,9]
        '6.2,7.4,8,9', float => [6.2,7.4,8.0,9.0]
        """
        if not items:
            raise ValueError('Values are required', HTTPCodes.BADINPUT)

        raw_sequence = items.split(',')
        if len(raw_sequence) == 1:
            try:
                number = output_type(raw_sequence[0])
                return [number]
            except ValueError:
                raise ValueError('Invalid number in values',
                                 HTTPCodes.BADINPUT)

        try:
            numbers = [output_type(num) for num in items.split(',')]
            return numbers
        except ValueError:
            raise ValueError('Invalid numbers', HTTPCodes.BADINPUT)
