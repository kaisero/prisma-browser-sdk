"""Resource-oriented facade (vendored by phantasos).

`client.<object>` is the typed resource wrapper for that object — clean, verb-named
methods backed privately by the generated `*Api`. Objects are discovered from the
generated `api/` package and classified at build time.
"""

from __future__ import annotations

from typing import Any, Callable, Iterator

from ..api.access_and_data_policy_api import AccessAndDataPolicyApi
from ..api.application_groups_api import ApplicationGroupsApi
from ..api.applications_api import ApplicationsApi
from ..api.assets_api import AssetsApi
from ..api.configuration_management_api import ConfigurationManagementApi
from ..api.customization_policy_api import CustomizationPolicyApi
from ..api.device_groups_api import DeviceGroupsApi
from ..api.devices_api import DevicesApi
from ..api.integrations_api import IntegrationsApi
from ..api.plugins_api import PluginsApi
from ..api.security_policy_api import SecurityPolicyApi
from ..api.sign_in_policy_api import SignInPolicyApi
from ..api.user_groups_api import UserGroupsApi
from ..api.user_requests_api import UserRequestsApi
from ..api.users_api import UsersApi
from .resources import AccessAndDataRuleResource
from .resources import AccessAndDataSectionResource
from .resources import AccessAndDataPolicyResource
from .resources import ApplicationGroupResource
from .resources import ApplicationResource
from .resources import ApplicationCategoryResource
from .resources import ConfigurationResource
from .resources import CustomizationRuleResource
from .resources import CustomizationSectionResource
from .resources import CustomizationPolicyResource
from .resources import DeviceGroupResource
from .resources import DeviceResource
from .resources import CloudStorageProviderResource
from .resources import ApplicationPluginResource
from .resources import SecurityRuleResource
from .resources import SecuritySectionResource
from .resources import SecurityPolicyResource
from .resources import SignInRuleResource
from .resources import SignInSectionResource
from .resources import SignInPolicyResource
from .resources import UserGroupResource
from .resources import UserRequestResource
from .resources import UserResource
from .auth import api_client_from_credentials, api_client_from_env
from .pagination import paginate
from .retry import default_retry

__all__ = ["Client"]

# Raw `*Api` classes keyed by their api-class attr. Retained as the in-process
# introspection target (`registry_attr="_RESOURCES"`); NOT the client's public
# surface — the wrappers below are.
_RESOURCES = {
    "access_and_data_policy": AccessAndDataPolicyApi,
    "application_groups": ApplicationGroupsApi,
    "applications": ApplicationsApi,
    "assets": AssetsApi,
    "configuration_management": ConfigurationManagementApi,
    "customization_policy": CustomizationPolicyApi,
    "device_groups": DeviceGroupsApi,
    "devices": DevicesApi,
    "integrations": IntegrationsApi,
    "plugins": PluginsApi,
    "security_policy": SecurityPolicyApi,
    "sign_in_policy": SignInPolicyApi,
    "user_groups": UserGroupsApi,
    "user_requests": UserRequestsApi,
    "users": UsersApi,
}

# Object -> (wrapper class, backing `_RESOURCES` api-class attr). The CLI's
# wrapper introspection keys off this map.
_WRAPPERS = {
    "access_and_data_rule": (AccessAndDataRuleResource, "access_and_data_policy"),
    "access_and_data_section": (AccessAndDataSectionResource, "access_and_data_policy"),
    "access_and_data_policy": (AccessAndDataPolicyResource, "access_and_data_policy"),
    "application_group": (ApplicationGroupResource, "application_groups"),
    "application": (ApplicationResource, "applications"),
    "application_category": (ApplicationCategoryResource, "applications"),
    "configuration": (ConfigurationResource, "configuration_management"),
    "customization_rule": (CustomizationRuleResource, "customization_policy"),
    "customization_section": (CustomizationSectionResource, "customization_policy"),
    "customization_policy": (CustomizationPolicyResource, "customization_policy"),
    "device_group": (DeviceGroupResource, "device_groups"),
    "device": (DeviceResource, "devices"),
    "cloud_storage_provider": (CloudStorageProviderResource, "integrations"),
    "application_plugin": (ApplicationPluginResource, "plugins"),
    "security_rule": (SecurityRuleResource, "security_policy"),
    "security_section": (SecuritySectionResource, "security_policy"),
    "security_policy": (SecurityPolicyResource, "security_policy"),
    "sign_in_rule": (SignInRuleResource, "sign_in_policy"),
    "sign_in_section": (SignInSectionResource, "sign_in_policy"),
    "sign_in_policy": (SignInPolicyResource, "sign_in_policy"),
    "user_group": (UserGroupResource, "user_groups"),
    "user_request": (UserRequestResource, "user_requests"),
    "user": (UserResource, "users"),
}


class Client:
    """Resource-oriented entry point. Each object attribute is a typed wrapper."""

    def __init__(self, api_client):
        self._api_client = api_client
        if getattr(api_client.configuration, "retries", None) is None:
            api_client.configuration.retries = default_retry()
        # One `*Api` per backing class, SHARED across every object it backs
        # (e.g. access_and_data_rule/_section/_policy reuse one instance).
        _apis = {attr: cls(api_client) for attr, cls in _RESOURCES.items()}
        for obj, (wrapper_cls, api_attr) in _WRAPPERS.items():
            setattr(self, obj, wrapper_cls(_apis[api_attr]))

    access_and_data_rule: AccessAndDataRuleResource
    access_and_data_section: AccessAndDataSectionResource
    access_and_data_policy: AccessAndDataPolicyResource
    application_group: ApplicationGroupResource
    application: ApplicationResource
    application_category: ApplicationCategoryResource
    configuration: ConfigurationResource
    customization_rule: CustomizationRuleResource
    customization_section: CustomizationSectionResource
    customization_policy: CustomizationPolicyResource
    device_group: DeviceGroupResource
    device: DeviceResource
    cloud_storage_provider: CloudStorageProviderResource
    application_plugin: ApplicationPluginResource
    security_rule: SecurityRuleResource
    security_section: SecuritySectionResource
    security_policy: SecurityPolicyResource
    sign_in_rule: SignInRuleResource
    sign_in_section: SignInSectionResource
    sign_in_policy: SignInPolicyResource
    user_group: UserGroupResource
    user_request: UserRequestResource
    user: UserResource

    @classmethod
    def from_env(cls, **kwargs) -> "Client":
        return cls(api_client_from_env(**kwargs))

    @classmethod
    def from_credentials(cls, **kwargs) -> "Client":
        return cls(api_client_from_credentials(**kwargs))

    def paginate(self, list_method: Callable[..., Any], **filters: Any) -> Iterator[Any]:
        return paginate(list_method, **filters)

    @property
    def api_client(self):
        return self._api_client

    def close(self) -> None:
        self._api_client.__exit__(None, None, None)

    def __enter__(self) -> "Client":
        return self

    def __exit__(self, exc_type=None, exc_value=None, traceback=None) -> None:
        self._api_client.__exit__(exc_type, exc_value, traceback)
