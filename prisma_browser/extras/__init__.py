"""Hand-written conveniences vendored by phantasos. Do not edit in place — edit the
framework templates and rebuild."""

from .auth import (
    DEFAULT_BASE_URL,
    DEFAULT_TOKEN_URL,
    PrismaSaseConfiguration,
    TokenManager,
    api_client_from_credentials,
    api_client_from_env,
)

from .errors import (
    ApiException,
    BadRequestException,
    ForbiddenException,
    NotFoundException,
    RateLimitException,
    ServiceException,
    UnauthorizedException,
    error_message,
)

from .facade import Client

from .pagination import paginate

from .retry import JitteredRetry, default_retry

__all__ = [
    "Client",
    "api_client_from_env", "api_client_from_credentials",
    "PrismaSaseConfiguration", "TokenManager", "DEFAULT_BASE_URL", "DEFAULT_TOKEN_URL",
    "paginate",
    "ApiException", "BadRequestException", "UnauthorizedException",
    "ForbiddenException", "NotFoundException", "RateLimitException", "ServiceException",
    "error_message",
    "JitteredRetry", "default_retry",
]
