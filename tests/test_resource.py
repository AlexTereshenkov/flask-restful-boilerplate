import pytest
import os
import sys
sys.path.append(os.getcwd())

from requests import get

from api import secrets
from api.resource import Sum, SumEndpoints
from src.config import HOSTNAME, PORT, PROTOCOL
from api.constants import HTTPCodes, ResponseFields

base_cases = [
    # edge cases
    ('0', 0),
    ('1', 1),
    # positive values
    ('1,2,3', 6),
    ('3,2,1', 6),
    # negative values
    ('-1,2,3', 4),
    ('-1,-2,-3', -6),
]

invalid_cases = [
    ('', 0, 0),
    ('7-6', 0, 0),
    ('7/6,8.5', 0, 0),
    ('8.5.5,9', 0, 0),
]

base_params = 'values, expected'


@pytest.mark.parametrize(base_params, base_cases)
def test_valid_values(values, expected):
    res = get(
        f'{PROTOCOL}://{HOSTNAME}:{PORT}/{SumEndpoints.GETSUM.value}'
        f'?{Sum.Values.name}={values}',
        headers={Sum.Token.name: secrets.TOKEN})
    assert res.json()[ResponseFields.RESULT] == expected
    assert res.status_code == HTTPCodes.OK
    return


def test_wrong_token():
    res = get(
        f'{PROTOCOL}://{HOSTNAME}:{PORT}/{SumEndpoints.GETSUM.value}'
        f'?{Sum.Values.name}={[1,2,3]}',
        headers={Sum.Token.name: 'invalid token string'})
    assert res.status_code == HTTPCodes.UNAUTHORIZED
    return
