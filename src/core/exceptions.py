from requests.exceptions import ConnectionError


class BaseException(Exception):
    pass


class PostNotFound(BaseException):
    pass


class ShitpostConnectionError(ConnectionError):
    pass
