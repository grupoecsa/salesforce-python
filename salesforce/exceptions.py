class BaseError(Exception):
    pass


class UnknownError(BaseError):
    pass


class AccessTokenRequired(BaseError):
    pass


class BadOAuthTokenError(BaseError):
    pass