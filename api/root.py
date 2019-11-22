"""API Root endpoint resource."""

import json
from typing import Tuple
from flask_restful import Resource
from collections import OrderedDict
from api.resource import Sum, SumEndpoints
from api.constants import HTTPCodes, Messages, ResponseFields


class Root(Resource):
    """API Root endpoint resource."""
    def get(self) -> Tuple[dict, int]:
        help = OrderedDict([
            ('/', 'Sample API.'),
            (f'/{SumEndpoints.GETSUM.value}', {
                'description': 'Get sum of values.',
                'inputs': {
                    f'{Sum.Values.name}: Array[Real]': 'Input values.',
                },
                'example': {
                    'call': f'/{SumEndpoints.GETSUM.value}?'
                    f'{Sum.Values.name}=1,2,3,4,5',
                    'response': {
                        ResponseFields.CODE: HTTPCodes.OK,
                        ResponseFields.MESSAGE: Messages.DONE,
                        ResponseFields.RESULT: 15
                    }
                }
            }),
        ])
        return json.loads(json.dumps(help)), HTTPCodes.OK
