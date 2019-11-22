"""Constants to be reused by the API endpoints operations."""


class Location:
    FORM = 'form'
    ARGS = 'args'
    HEADERS = 'headers'
    COOKIES = 'cookies'


class Messages:
    INVALID_TOKEN = 'Invalid token'
    DONE = 'Done'


class HTTPCodes:
    OK = 200
    BADINPUT = 400
    UNAUTHORIZED = 401


class ResponseFields:
    CODE = 'code'
    MESSAGE = 'message'
    RESULT = 'result'
