"""Typed, object-granular resource wrappers (vendored by phantasos).

Each ``<Object>Resource`` wraps the backing generated ``*Api`` with clean,
typed methods. A method may collapse several raw operations (e.g. by-id and
by-type-and-id) into one call; the ``_bindings`` table records, per verb, every
backing op and how a wrapper call maps onto it. ``_select`` picks the
most-specific binding whose required args are all present; ``_to_raw`` renames
wrapper params to the chosen op's raw names (and ``body`` to its raw body-param)
and coerces enum strings.
"""

from __future__ import annotations

import inspect
from typing import Any, ClassVar
from ..models.access_and_data_rule_detailed import AccessAndDataRuleDetailed
from ..models.application_group import ApplicationGroup
from ..models.application_item import ApplicationItem
from ..models.bulk_delete_applications_request import BulkDeleteApplicationsRequest
from ..models.cloud_storage_provider import CloudStorageProvider
from ..models.create_access_and_data_rule_request import CreateAccessAndDataRuleRequest
from ..models.create_application_plugin201_response import CreateApplicationPlugin201Response
from ..models.create_cloud_storage_provider_request import CreateCloudStorageProviderRequest
from ..models.create_customization_rule_request import CreateCustomizationRuleRequest
from ..models.create_device_group201_response import CreateDeviceGroup201Response
from ..models.create_or_replace_app_group_input import CreateOrReplaceAppGroupInput
from ..models.create_or_replace_app_input import CreateOrReplaceAppInput
from ..models.create_security_rule_request import CreateSecurityRuleRequest
from ..models.create_sign_in_rule_request import CreateSignInRuleRequest
from ..models.create_user_group201_response import CreateUserGroup201Response
from ..models.create_user_group_request import CreateUserGroupRequest
from ..models.created_id_response import CreatedIdResponse
from ..models.customization_rule_detailed import CustomizationRuleDetailed
from ..models.delete_application_plugin200_response import DeleteApplicationPlugin200Response
from ..models.delete_user_group200_response import DeleteUserGroup200Response
from ..models.device import Device
from ..models.device_archive_response import DeviceArchiveResponse
from ..models.device_delete_response import DeviceDeleteResponse
from ..models.device_force_reauth_response import DeviceForceReauthResponse
from ..models.device_group import DeviceGroup
from ..models.device_group_patch_request import DeviceGroupPatchRequest
from ..models.device_group_platform import DeviceGroupPlatform
from ..models.device_group_request import DeviceGroupRequest
from ..models.device_restore_response import DeviceRestoreResponse
from ..models.device_resume_response import DeviceResumeResponse
from ..models.device_status_change_request import DeviceStatusChangeRequest
from ..models.device_suspend_response import DeviceSuspendResponse
from ..models.get_sign_in_policy200_response import GetSignInPolicy200Response
from ..models.list_application_categories200_response import ListApplicationCategories200Response
from ..models.list_application_groups200_response import ListApplicationGroups200Response
from ..models.list_application_groups_sort_parameter import ListApplicationGroupsSortParameter
from ..models.list_application_plugins200_response import ListApplicationPlugins200Response
from ..models.list_applications200_response import ListApplications200Response
from ..models.list_applications_sort_parameter import ListApplicationsSortParameter
from ..models.list_applications_type_parameter import ListApplicationsTypeParameter
from ..models.list_cloud_storage_providers200_response import ListCloudStorageProviders200Response
from ..models.list_device_groups200_response import ListDeviceGroups200Response
from ..models.list_device_groups_sort_parameter import ListDeviceGroupsSortParameter
from ..models.list_devices200_response import ListDevices200Response
from ..models.list_devices_sort_parameter import ListDevicesSortParameter
from ..models.list_user_groups200_response import ListUserGroups200Response
from ..models.list_user_requests200_response import ListUserRequests200Response
from ..models.list_user_requests_request_status_parameter import ListUserRequestsRequestStatusParameter
from ..models.list_user_requests_request_type_parameter import ListUserRequestsRequestTypeParameter
from ..models.list_user_requests_sort_parameter import ListUserRequestsSortParameter
from ..models.list_users200_response import ListUsers200Response
from ..models.list_users_sort_parameter import ListUsersSortParameter
from ..models.order import Order
from ..models.patch_access_and_data_rule_by_id_request import PatchAccessAndDataRuleByIDRequest
from ..models.patch_app_group_input import PatchAppGroupInput
from ..models.patch_app_input import PatchAppInput
from ..models.patch_application_by_type_and_id200_response import PatchApplicationByTypeAndID200Response
from ..models.patch_customization_rule_by_id_request import PatchCustomizationRuleByIDRequest
from ..models.patch_positions_request import PatchPositionsRequest
from ..models.patch_security_rule_by_id200_response import PatchSecurityRuleByID200Response
from ..models.patch_security_rule_by_id_request import PatchSecurityRuleByIDRequest
from ..models.patch_sign_in_rule_by_id200_response import PatchSignInRuleByID200Response
from ..models.patch_sign_in_rule_by_id_request import PatchSignInRuleByIDRequest
from ..models.plugin_response import PluginResponse
from ..models.positions_success_response import PositionsSuccessResponse
from ..models.publish_draft_configuration_request import PublishDraftConfigurationRequest
from ..models.request_action import RequestAction
from ..models.revoke_request_action import RevokeRequestAction
from ..models.section_detailed import SectionDetailed
from ..models.section_patch_request import SectionPatchRequest
from ..models.section_post_request import SectionPostRequest
from ..models.section_update_request import SectionUpdateRequest
from ..models.security_rule_detailed import SecurityRuleDetailed
from ..models.sign_in_rule_detailed import SignInRuleDetailed
from ..models.update_application_plugin200_response import UpdateApplicationPlugin200Response
from ..models.update_application_plugin_request import UpdateApplicationPluginRequest
from ..models.update_device_group200_response import UpdateDeviceGroup200Response
from ..models.update_sign_in_positions_request import UpdateSignInPositionsRequest
from ..models.update_sign_in_section_by_id200_response import UpdateSignInSectionByID200Response
from ..models.update_user_group200_response import UpdateUserGroup200Response
from ..models.update_user_group_request import UpdateUserGroupRequest
from ..models.user import User
from ..models.user_force_reauth_response import UserForceReauthResponse
from ..models.user_group import UserGroup
from ..models.user_request import UserRequest
from ..models.user_resume_response import UserResumeResponse
from ..models.user_status import UserStatus
from ..models.user_status_change_request import UserStatusChangeRequest
from ..models.user_suspend_response import UserSuspendResponse
from ..api.access_and_data_policy_api import AccessAndDataPolicyApi
from ..api.access_and_data_policy_api import AccessAndDataPolicyApi
from ..api.access_and_data_policy_api import AccessAndDataPolicyApi
from ..api.application_groups_api import ApplicationGroupsApi
from ..api.applications_api import ApplicationsApi
from ..api.applications_api import ApplicationsApi
from ..api.configuration_management_api import ConfigurationManagementApi
from ..api.customization_policy_api import CustomizationPolicyApi
from ..api.customization_policy_api import CustomizationPolicyApi
from ..api.customization_policy_api import CustomizationPolicyApi
from ..api.device_groups_api import DeviceGroupsApi
from ..api.devices_api import DevicesApi
from ..api.integrations_api import IntegrationsApi
from ..api.plugins_api import PluginsApi
from ..api.security_policy_api import SecurityPolicyApi
from ..api.security_policy_api import SecurityPolicyApi
from ..api.security_policy_api import SecurityPolicyApi
from ..api.sign_in_policy_api import SignInPolicyApi
from ..api.sign_in_policy_api import SignInPolicyApi
from ..api.sign_in_policy_api import SignInPolicyApi
from ..api.user_groups_api import UserGroupsApi
from ..api.user_requests_api import UserRequestsApi
from ..api.users_api import UsersApi
from .pagination import paginate



class AccessAndDataRuleResource:
    """Typed wrapper for ``access_and_data_rule`` (backed by ``AccessAndDataPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_access_and_data_rule', 'serialize_name': '_create_access_and_data_rule_serialize', 'requires': [], 'param_map': {}, 'body': 'create_access_and_data_rule_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_access_and_data_rule_by_id', 'serialize_name': '_delete_access_and_data_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_access_and_data_rule_by_id', 'serialize_name': '_get_access_and_data_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "update": [{'raw_method': 'patch_access_and_data_rule_by_id', 'serialize_name': '_patch_access_and_data_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'patch_access_and_data_rule_by_id_request', 'enums': {}}],
    }

    def __init__(self, api: AccessAndDataPolicyApi) -> None:
        self._api = api

    def create(self, body: CreateAccessAndDataRuleRequest | None = None) -> CreatedIdResponse:
        """Creates a new access and data policy rule.

        **Example:**

        ```python
        client.access_and_data_rule.create(
            body=CreateAccessAndDataRuleRequest(
                name="example",
                mode="active",
                applications=AccessAndDataPostApplications(
                ),
                access=AccessInput(
                    action="allow",
                ),
                tracking=AccessAndDataTracking(
                    log_level="off",
                    session_recording=False,
                ),
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> None:
        """Delete an Access and Data policy rule.

        **Example:**

        ```python
        client.access_and_data_rule.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> AccessAndDataRuleDetailed:
        """Retrieve an Access and Data Rule by ID.

        **Example:**

        ```python
        client.access_and_data_rule.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def update(self, id: str | None = None, body: PatchAccessAndDataRuleByIDRequest | None = None) -> PatchSecurityRuleByID200Response:
        """Partially update an Access and Data policy rule. All fields are optional.

        **Example:**

        ```python
        client.access_and_data_rule.update(
            id="<id>",
            body=PatchAccessAndDataRuleByIDRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class AccessAndDataSectionResource:
    """Typed wrapper for ``access_and_data_section`` (backed by ``AccessAndDataPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_access_and_data_section', 'serialize_name': '_create_access_and_data_section_serialize', 'requires': [], 'param_map': {}, 'body': 'section_post_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_access_and_data_section_by_id', 'serialize_name': '_delete_access_and_data_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'delete_rules': 'delete_rules'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_access_and_data_section_by_id', 'serialize_name': '_get_access_and_data_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "reorder": [{'raw_method': 'update_access_and_data_positions', 'serialize_name': '_update_access_and_data_positions_serialize', 'requires': [], 'param_map': {}, 'body': 'update_sign_in_positions_request', 'enums': {}}],
    "replace": [{'raw_method': 'update_access_and_data_section_by_id', 'serialize_name': '_update_access_and_data_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_update_request', 'enums': {}}],
    "update": [{'raw_method': 'patch_access_and_data_section_by_id', 'serialize_name': '_patch_access_and_data_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_patch_request', 'enums': {}}],
    }

    def __init__(self, api: AccessAndDataPolicyApi) -> None:
        self._api = api

    def create(self, body: SectionPostRequest | None = None) -> SectionDetailed:
        """Creates a new Access and Data section.

        **Example:**

        ```python
        client.access_and_data_section.create(
            body=SectionPostRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None, delete_rules: bool | None = None) -> None:
        """Delete an access and data rule section.

        **Example:**

        ```python
        client.access_and_data_section.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id, "delete_rules": delete_rules}.items() if v is not None}, {"id": id, "delete_rules": delete_rules})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SectionDetailed:
        """Retrieve an Access and Data Section by ID.

        **Example:**

        ```python
        client.access_and_data_section.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def reorder(self, body: UpdateSignInPositionsRequest | None = None) -> PositionsSuccessResponse:
        """Update rule and section positions in the access-and-data policy.

        **Example:**

        ```python
        client.access_and_data_section.reorder(
            body=UpdateSignInPositionsRequest(
                positions=[
                    PositionItem(PositionItemSection(
                            type="Section",
                            id="example",
                        )),
                ],
            ),
        )
        ```"""
        return self._call("reorder", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def replace(self, id: str | None = None, body: SectionUpdateRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Updates an access-and-data rule section.

        **Example:**

        ```python
        client.access_and_data_section.replace(
            id="<id>",
            body=SectionUpdateRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def update(self, id: str | None = None, body: SectionPatchRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Partially update an access-and-data rule section.

        **Example:**

        ```python
        client.access_and_data_section.update(
            id="<id>",
            body=SectionPatchRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class AccessAndDataPolicyResource:
    """Typed wrapper for ``access_and_data_policy`` (backed by ``AccessAndDataPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "get": [{'raw_method': 'get_access_and_data_policy', 'serialize_name': '_get_access_and_data_policy_serialize', 'requires': [], 'param_map': {'configuration_version': 'configuration_version', 'limit': 'limit', 'cursor': 'cursor'}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: AccessAndDataPolicyApi) -> None:
        self._api = api

    def get(self, configuration_version: str | None = None, limit: int | None = None, cursor: str | None = None) -> GetSignInPolicy200Response:
        """Retrieve the Access and Data Policy.

        **Example:**

        ```python
        client.access_and_data_policy.get()
        ```"""
        return self._fetch("get", {k for k, v in {"configuration_version": configuration_version, "limit": limit, "cursor": cursor}.items() if v is not None}, {"configuration_version": configuration_version, "limit": limit, "cursor": cursor})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class ApplicationGroupResource:
    """Typed wrapper for ``application_group`` (backed by ``ApplicationGroupsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_application_group', 'serialize_name': '_create_application_group_serialize', 'requires': [], 'param_map': {}, 'body': 'create_or_replace_app_group_input', 'enums': {}}],
    "delete": [{'raw_method': 'delete_application_group_by_id', 'serialize_name': '_delete_application_group_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_application_group_by_id', 'serialize_name': '_get_application_group_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_application_groups', 'serialize_name': '_list_application_groups_serialize', 'requires': [], 'param_map': {'configuration_version': 'configuration_version', 'name': 'name', 'cursor': 'cursor', 'limit': 'limit', 'sort': 'sort', 'order': 'order'}, 'body': None, 'enums': {'sort': 'ListApplicationGroupsSortParameter', 'order': 'Order'}}],
    "update": [{'raw_method': 'patch_application_group_by_id', 'serialize_name': '_patch_application_group_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'patch_app_group_input', 'enums': {}}],
    }

    def __init__(self, api: ApplicationGroupsApi) -> None:
        self._api = api

    def create(self, body: CreateOrReplaceAppGroupInput | None = None) -> CreatedIdResponse:
        """Creates an application group.

        **Example:**

        ```python
        client.application_group.create(
            body=CreateOrReplaceAppGroupInput(
                name="example",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> None:
        """Deletes an application group.

        **Example:**

        ```python
        client.application_group.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> ApplicationGroup:
        """Returns an application group.

        **Example:**

        ```python
        client.application_group.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def list(self, configuration_version: str | None = None, name: str | None = None, cursor: str | None = None, limit: int | None = None, sort: ListApplicationGroupsSortParameter | None = None, order: Order | None = None, *, all_pages: bool = False) -> ListApplicationGroups200Response:
        """Returns a list of application groups.

        **Example:**

        ```python
        client.application_group.list()
        ```"""
        return self._list("list", {k for k, v in {"configuration_version": configuration_version, "name": name, "cursor": cursor, "limit": limit, "sort": sort, "order": order}.items() if v is not None}, {"configuration_version": configuration_version, "name": name, "cursor": cursor, "limit": limit, "sort": sort, "order": order}, all_pages)

    def update(self, id: str | None = None, body: PatchAppGroupInput | None = None) -> PatchApplicationByTypeAndID200Response:
        """Updates an application group.

        **Example:**

        ```python
        client.application_group.update(
            id="<id>",
            body=PatchAppGroupInput(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class ApplicationResource:
    """Typed wrapper for ``application`` (backed by ``ApplicationsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "bulk_create": [{'raw_method': 'bulk_create_applications', 'serialize_name': '_bulk_create_applications_serialize', 'requires': ['create_or_replace_app_input', 'type'], 'param_map': {'type': 'type', 'create_or_replace_app_input': 'create_or_replace_app_input'}, 'body': None, 'enums': {'type': 'ListApplicationsTypeParameter'}}],
    "bulk_delete": [{'raw_method': 'bulk_delete_applications', 'serialize_name': '_bulk_delete_applications_serialize', 'requires': [], 'param_map': {}, 'body': 'bulk_delete_applications_request', 'enums': {}}],
    "create": [{'raw_method': 'create_application', 'serialize_name': '_create_application_serialize', 'requires': ['type'], 'param_map': {'type': 'type'}, 'body': 'create_or_replace_app_input', 'enums': {'type': 'ListApplicationsTypeParameter'}}],
    "delete": [{'raw_method': 'delete_application_by_id', 'serialize_name': '_delete_application_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}, {'raw_method': 'delete_application_by_type_and_id', 'serialize_name': '_delete_application_by_type_and_id_serialize', 'requires': ['id', 'type'], 'param_map': {'type': 'type', 'id': 'id'}, 'body': None, 'enums': {'type': 'ListApplicationsTypeParameter'}}],
    "get": [{'raw_method': 'get_application_by_id', 'serialize_name': '_get_application_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}, {'raw_method': 'get_application_by_type_and_id', 'serialize_name': '_get_application_by_type_and_id_serialize', 'requires': ['id', 'type'], 'param_map': {'type': 'type', 'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {'type': 'ListApplicationsTypeParameter'}}],
    "list": [{'raw_method': 'list_applications', 'serialize_name': '_list_applications_serialize', 'requires': [], 'param_map': {'type': 'type', 'name': 'name', 'url': 'url', 'include_catalog_attributes': 'include_catalog_attributes', 'limit': 'limit', 'cursor': 'cursor', 'sort': 'sort', 'order': 'order', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {'type': 'ListApplicationsTypeParameter', 'sort': 'ListApplicationsSortParameter', 'order': 'Order'}}, {'raw_method': 'list_applications_by_type', 'serialize_name': '_list_applications_by_type_serialize', 'requires': ['type'], 'param_map': {'type': 'type', 'name': 'name', 'url': 'url', 'include_catalog_attributes': 'include_catalog_attributes', 'configuration_version': 'configuration_version', 'cursor': 'cursor', 'limit': 'limit', 'sort': 'sort', 'order': 'order'}, 'body': None, 'enums': {'type': 'ListApplicationsTypeParameter', 'sort': 'ListApplicationsSortParameter', 'order': 'Order'}}],
    "update": [{'raw_method': 'patch_application_by_type_and_id', 'serialize_name': '_patch_application_by_type_and_id_serialize', 'requires': ['id', 'type'], 'param_map': {'type': 'type', 'id': 'id'}, 'body': 'patch_app_input', 'enums': {'type': 'ListApplicationsTypeParameter'}}],
    }

    def __init__(self, api: ApplicationsApi) -> None:
        self._api = api

    def bulk_create(self, type: ListApplicationsTypeParameter | None = None, create_or_replace_app_input: str | None = None) -> None:
        """Creates multiple applications.

        **Example:**

        ```python
        client.application.bulk_create(
            type="custom",
            create_or_replace_app_input="<create_or_replace_app_input>",
        )
        ```"""
        return self._call("bulk_create", {k for k, v in {"type": type, "create_or_replace_app_input": create_or_replace_app_input}.items() if v is not None}, {"type": type, "create_or_replace_app_input": create_or_replace_app_input})

    def bulk_delete(self, body: BulkDeleteApplicationsRequest | None = None) -> None:
        """Delete multiple applications atomically.

        **Example:**

        ```python
        client.application.bulk_delete(
            body=BulkDeleteApplicationsRequest(
                app_ids=["example"],
            ),
        )
        ```"""
        return self._call("bulk_delete", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def create(self, type: ListApplicationsTypeParameter | None = None, body: CreateOrReplaceAppInput | None = None) -> CreatedIdResponse:
        """Creates an application.

        **Example:**

        ```python
        created = client.application.create(
            type="custom",
            body=CustomApplicationInput(
                name="Acme Wiki",
                type="custom",
                urls=[UrlInput(url="https://wiki.acme.com/*")],
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"type": type, "body": body}.items() if v is not None}, {"type": type, "body": body})

    def delete(self, id: str | None = None, type: ListApplicationsTypeParameter | None = None) -> None:
        """Delete an application.

        **Example:**

        ```python
        client.application.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id, "type": type}.items() if v is not None}, {"id": id, "type": type})

    def get(self, id: str | None = None, configuration_version: str | None = None, type: ListApplicationsTypeParameter | None = None) -> ApplicationItem:
        """Get an application.

        **Example:**

        ```python
        client.application.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version, "type": type}.items() if v is not None}, {"id": id, "configuration_version": configuration_version, "type": type})

    def list(self, type: ListApplicationsTypeParameter | None = None, name: str | None = None, url: str | None = None, include_catalog_attributes: bool | None = None, limit: int | None = None, cursor: str | None = None, sort: ListApplicationsSortParameter | None = None, order: Order | None = None, configuration_version: str | None = None, *, all_pages: bool = False) -> ListApplications200Response:
        """List applications.

        **Example:**

        ```python
        client.application.list()
        ```"""
        return self._list("list", {k for k, v in {"type": type, "name": name, "url": url, "include_catalog_attributes": include_catalog_attributes, "limit": limit, "cursor": cursor, "sort": sort, "order": order, "configuration_version": configuration_version}.items() if v is not None}, {"type": type, "name": name, "url": url, "include_catalog_attributes": include_catalog_attributes, "limit": limit, "cursor": cursor, "sort": sort, "order": order, "configuration_version": configuration_version}, all_pages)

    def update(self, type: ListApplicationsTypeParameter | None = None, id: str | None = None, body: PatchAppInput | None = None) -> PatchApplicationByTypeAndID200Response:
        """Updates an application.

        **Example:**

        ```python
        client.application.update(
            type="custom",
            id="<id>",
            body=PatchAppInput(CustomPatchApplicationInput(
                    type="custom",
                )),
        )
        ```"""
        return self._call("update", {k for k, v in {"type": type, "id": id, "body": body}.items() if v is not None}, {"type": type, "id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class ApplicationCategoryResource:
    """Typed wrapper for ``application_category`` (backed by ``ApplicationsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "list": [{'raw_method': 'list_application_categories', 'serialize_name': '_list_application_categories_serialize', 'requires': [], 'param_map': {}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: ApplicationsApi) -> None:
        self._api = api

    def list(self, *, all_pages: bool = False) -> ListApplicationCategories200Response:
        """Returns a list of available application categories.

        **Example:**

        ```python
        client.application_category.list()
        ```"""
        return self._list("list", {k for k, v in {}.items() if v is not None}, {}, all_pages)

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class ConfigurationResource:
    """Typed wrapper for ``configuration`` (backed by ``ConfigurationManagementApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "publish": [{'raw_method': 'publish_draft_configuration', 'serialize_name': '_publish_draft_configuration_serialize', 'requires': [], 'param_map': {}, 'body': 'publish_draft_configuration_request', 'enums': {}}],
    }

    def __init__(self, api: ConfigurationManagementApi) -> None:
        self._api = api

    def publish(self, body: PublishDraftConfigurationRequest | None = None) -> None:
        """Publish Draft.

        **Example:**

        ```python
        client.configuration.publish(
            body=PublishDraftConfigurationRequest(),  # all fields optional
        )
        ```"""
        return self._call("publish", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class CustomizationRuleResource:
    """Typed wrapper for ``customization_rule`` (backed by ``CustomizationPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_customization_rule', 'serialize_name': '_create_customization_rule_serialize', 'requires': [], 'param_map': {}, 'body': 'create_customization_rule_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_customization_rule_by_id', 'serialize_name': '_delete_customization_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_customization_rule_by_id', 'serialize_name': '_get_customization_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "update": [{'raw_method': 'patch_customization_rule_by_id', 'serialize_name': '_patch_customization_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'patch_customization_rule_by_id_request', 'enums': {}}],
    }

    def __init__(self, api: CustomizationPolicyApi) -> None:
        self._api = api

    def create(self, body: CreateCustomizationRuleRequest | None = None) -> CreatedIdResponse:
        """Creates a new customization policy rule.

        **Example:**

        ```python
        client.customization_rule.create(
            body=CreateCustomizationRuleRequest(
                name="example",
                mode="active",
                controls=CustomizationControls(
                ),
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> None:
        """Delete a Customization policy rule.

        **Example:**

        ```python
        client.customization_rule.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> CustomizationRuleDetailed:
        """Retrieve a Customization Rule by ID.

        **Example:**

        ```python
        client.customization_rule.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def update(self, id: str | None = None, body: PatchCustomizationRuleByIDRequest | None = None) -> PatchSecurityRuleByID200Response:
        """Partially update a Customization policy rule. All fields are optional.

        **Example:**

        ```python
        client.customization_rule.update(
            id="<id>",
            body=PatchCustomizationRuleByIDRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class CustomizationSectionResource:
    """Typed wrapper for ``customization_section`` (backed by ``CustomizationPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_customization_section', 'serialize_name': '_create_customization_section_serialize', 'requires': [], 'param_map': {}, 'body': 'section_post_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_customization_section_by_id', 'serialize_name': '_delete_customization_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'delete_rules': 'delete_rules'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_customization_section_by_id', 'serialize_name': '_get_customization_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "reorder": [{'raw_method': 'update_customization_positions', 'serialize_name': '_update_customization_positions_serialize', 'requires': [], 'param_map': {}, 'body': 'update_sign_in_positions_request', 'enums': {}}],
    "replace": [{'raw_method': 'update_customization_section_by_id', 'serialize_name': '_update_customization_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_update_request', 'enums': {}}],
    "update": [{'raw_method': 'patch_customization_section_by_id', 'serialize_name': '_patch_customization_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_patch_request', 'enums': {}}],
    }

    def __init__(self, api: CustomizationPolicyApi) -> None:
        self._api = api

    def create(self, body: SectionPostRequest | None = None) -> SectionDetailed:
        """Creates a new customization section.

        **Example:**

        ```python
        client.customization_section.create(
            body=SectionPostRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None, delete_rules: bool | None = None) -> None:
        """Delete a customization rule section.

        **Example:**

        ```python
        client.customization_section.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id, "delete_rules": delete_rules}.items() if v is not None}, {"id": id, "delete_rules": delete_rules})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SectionDetailed:
        """Retrieve a Customization Section by ID.

        **Example:**

        ```python
        client.customization_section.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def reorder(self, body: UpdateSignInPositionsRequest | None = None) -> PositionsSuccessResponse:
        """Update rule and section positions in the customization policy.

        **Example:**

        ```python
        client.customization_section.reorder(
            body=UpdateSignInPositionsRequest(
                positions=[
                    PositionItem(PositionItemSection(
                            type="Section",
                            id="example",
                        )),
                ],
            ),
        )
        ```"""
        return self._call("reorder", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def replace(self, id: str | None = None, body: SectionUpdateRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Updates a customization rule section.

        **Example:**

        ```python
        client.customization_section.replace(
            id="<id>",
            body=SectionUpdateRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def update(self, id: str | None = None, body: SectionPatchRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Partially update a customization policy section.

        **Example:**

        ```python
        client.customization_section.update(
            id="<id>",
            body=SectionPatchRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class CustomizationPolicyResource:
    """Typed wrapper for ``customization_policy`` (backed by ``CustomizationPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "get": [{'raw_method': 'get_customization_policy', 'serialize_name': '_get_customization_policy_serialize', 'requires': [], 'param_map': {'configuration_version': 'configuration_version', 'limit': 'limit', 'cursor': 'cursor'}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: CustomizationPolicyApi) -> None:
        self._api = api

    def get(self, configuration_version: str | None = None, limit: int | None = None, cursor: str | None = None) -> GetSignInPolicy200Response:
        """Retrieve the Customization Policy.

        **Example:**

        ```python
        client.customization_policy.get()
        ```"""
        return self._fetch("get", {k for k, v in {"configuration_version": configuration_version, "limit": limit, "cursor": cursor}.items() if v is not None}, {"configuration_version": configuration_version, "limit": limit, "cursor": cursor})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class DeviceGroupResource:
    """Typed wrapper for ``device_group`` (backed by ``DeviceGroupsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_device_group', 'serialize_name': '_create_device_group_serialize', 'requires': [], 'param_map': {}, 'body': 'device_group_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_device_group', 'serialize_name': '_delete_device_group_serialize', 'requires': ['device_group_id'], 'param_map': {'device_group_id': 'device_group_id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_device_group_by_id', 'serialize_name': '_get_device_group_by_id_serialize', 'requires': ['device_group_id'], 'param_map': {'device_group_id': 'device_group_id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_device_groups', 'serialize_name': '_list_device_groups_serialize', 'requires': [], 'param_map': {'limit': 'limit', 'device_group_name': 'device_group_name', 'device_group_platform': 'device_group_platform', 'device_group_created_at_gte': 'device_group_created_at_gte', 'device_group_created_at_lte': 'device_group_created_at_lte', 'device_group_updated_at_gte': 'device_group_updated_at_gte', 'device_group_updated_at_lte': 'device_group_updated_at_lte', 'cursor': 'cursor', 'sort': 'sort', 'order': 'order', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {'device_group_platform': 'DeviceGroupPlatform', 'sort': 'ListDeviceGroupsSortParameter', 'order': 'Order'}}],
    "replace": [{'raw_method': 'update_device_group', 'serialize_name': '_update_device_group_serialize', 'requires': ['device_group_id'], 'param_map': {'device_group_id': 'device_group_id'}, 'body': 'device_group_request', 'enums': {}}],
    "update": [{'raw_method': 'patch_device_group', 'serialize_name': '_patch_device_group_serialize', 'requires': ['device_group_id'], 'param_map': {'device_group_id': 'device_group_id'}, 'body': 'device_group_patch_request', 'enums': {}}],
    }

    def __init__(self, api: DeviceGroupsApi) -> None:
        self._api = api

    def create(self, body: DeviceGroupRequest | None = None) -> CreateDeviceGroup201Response:
        """Create a new device group.

        **Example:**

        ```python
        client.device_group.create(
            body=DeviceGroupRequest(
                name="example",
                platform="Desktop Browser",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, device_group_id: str | None = None) -> None:
        """Deletes a device group.

        **Example:**

        ```python
        client.device_group.delete(
            device_group_id="<device_group_id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"device_group_id": device_group_id}.items() if v is not None}, {"device_group_id": device_group_id})

    def get(self, device_group_id: str | None = None, configuration_version: str | None = None) -> DeviceGroup:
        """Returns a device group by ID.

        **Example:**

        ```python
        client.device_group.get(
            device_group_id="<device_group_id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"device_group_id": device_group_id, "configuration_version": configuration_version}.items() if v is not None}, {"device_group_id": device_group_id, "configuration_version": configuration_version})

    def list(self, limit: int | None = None, device_group_name: str | None = None, device_group_platform: DeviceGroupPlatform | None = None, device_group_created_at_gte: str | None = None, device_group_created_at_lte: str | None = None, device_group_updated_at_gte: str | None = None, device_group_updated_at_lte: str | None = None, cursor: str | None = None, sort: ListDeviceGroupsSortParameter | None = None, order: Order | None = None, configuration_version: str | None = None, *, all_pages: bool = False) -> ListDeviceGroups200Response:
        """Returns a list of device groups.

        **Example:**

        ```python
        client.device_group.list()
        ```"""
        return self._list("list", {k for k, v in {"limit": limit, "device_group_name": device_group_name, "device_group_platform": device_group_platform, "device_group_created_at_gte": device_group_created_at_gte, "device_group_created_at_lte": device_group_created_at_lte, "device_group_updated_at_gte": device_group_updated_at_gte, "device_group_updated_at_lte": device_group_updated_at_lte, "cursor": cursor, "sort": sort, "order": order, "configuration_version": configuration_version}.items() if v is not None}, {"limit": limit, "device_group_name": device_group_name, "device_group_platform": device_group_platform, "device_group_created_at_gte": device_group_created_at_gte, "device_group_created_at_lte": device_group_created_at_lte, "device_group_updated_at_gte": device_group_updated_at_gte, "device_group_updated_at_lte": device_group_updated_at_lte, "cursor": cursor, "sort": sort, "order": order, "configuration_version": configuration_version}, all_pages)

    def replace(self, device_group_id: str | None = None, body: DeviceGroupRequest | None = None) -> UpdateDeviceGroup200Response:
        """Replace entire device group.

        **Example:**

        ```python
        client.device_group.replace(
            device_group_id="<device_group_id>",
            body=DeviceGroupRequest(
                name="example",
                platform="Desktop Browser",
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"device_group_id": device_group_id, "body": body}.items() if v is not None}, {"device_group_id": device_group_id, "body": body})

    def update(self, device_group_id: str | None = None, body: DeviceGroupPatchRequest | None = None) -> UpdateDeviceGroup200Response:
        """Partially update device group.

        **Example:**

        ```python
        client.device_group.update(
            device_group_id="<device_group_id>",
            body=DeviceGroupPatchRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"device_group_id": device_group_id, "body": body}.items() if v is not None}, {"device_group_id": device_group_id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class DeviceResource:
    """Typed wrapper for ``device`` (backed by ``DevicesApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "archive": [{'raw_method': 'archive_devices', 'serialize_name': '_archive_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_devices', 'serialize_name': '_delete_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    "force_reauth": [{'raw_method': 'force_reauth_devices', 'serialize_name': '_force_reauth_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    "get": [{'raw_method': 'get_device_by_id', 'serialize_name': '_get_device_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_devices', 'serialize_name': '_list_devices_serialize', 'requires': [], 'param_map': {'limit': 'limit', 'device_hostname': 'device_hostname', 'user_name': 'user_name', 'device_os_type': 'device_os_type', 'device_first_seen_gte': 'device_first_seen_gte', 'device_last_seen_lte': 'device_last_seen_lte', 'device_last_seen_gte': 'device_last_seen_gte', 'device_type': 'device_type', 'device_firewall_status': 'device_firewall_status', 'device_screen_lock_status': 'device_screen_lock_status', 'device_disk_encryption_status': 'device_disk_encryption_status', 'cursor': 'cursor', 'sort': 'sort', 'order': 'order'}, 'body': None, 'enums': {'sort': 'ListDevicesSortParameter', 'order': 'Order'}}],
    "restore": [{'raw_method': 'restore_devices', 'serialize_name': '_restore_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    "resume": [{'raw_method': 'resume_devices', 'serialize_name': '_resume_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    "suspend": [{'raw_method': 'suspend_devices', 'serialize_name': '_suspend_devices_serialize', 'requires': [], 'param_map': {}, 'body': 'device_status_change_request', 'enums': {}}],
    }

    def __init__(self, api: DevicesApi) -> None:
        self._api = api

    def archive(self, body: DeviceStatusChangeRequest | None = None) -> DeviceArchiveResponse:
        """Archive devices.

        **Example:**

        ```python
        client.device.archive(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("archive", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, body: DeviceStatusChangeRequest | None = None) -> DeviceDeleteResponse:
        """Delete devices.

        **Example:**

        ```python
        client.device.delete(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("delete", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def force_reauth(self, body: DeviceStatusChangeRequest | None = None) -> DeviceForceReauthResponse:
        """Force re-authentication for devices.

        **Example:**

        ```python
        client.device.force_reauth(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("force_reauth", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def get(self, id: str | None = None) -> Device:
        """Returns a device by ID.

        **Example:**

        ```python
        client.device.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def list(self, limit: int | None = None, device_hostname: str | None = None, user_name: str | None = None, device_os_type: str | None = None, device_first_seen_gte: str | None = None, device_last_seen_lte: str | None = None, device_last_seen_gte: str | None = None, device_type: str | None = None, device_firewall_status: str | None = None, device_screen_lock_status: str | None = None, device_disk_encryption_status: str | None = None, cursor: str | None = None, sort: ListDevicesSortParameter | None = None, order: Order | None = None, *, all_pages: bool = False) -> ListDevices200Response:
        """Returns a list of devices.

        **Example:**

        ```python
        client.device.list()
        ```"""
        return self._list("list", {k for k, v in {"limit": limit, "device_hostname": device_hostname, "user_name": user_name, "device_os_type": device_os_type, "device_first_seen_gte": device_first_seen_gte, "device_last_seen_lte": device_last_seen_lte, "device_last_seen_gte": device_last_seen_gte, "device_type": device_type, "device_firewall_status": device_firewall_status, "device_screen_lock_status": device_screen_lock_status, "device_disk_encryption_status": device_disk_encryption_status, "cursor": cursor, "sort": sort, "order": order}.items() if v is not None}, {"limit": limit, "device_hostname": device_hostname, "user_name": user_name, "device_os_type": device_os_type, "device_first_seen_gte": device_first_seen_gte, "device_last_seen_lte": device_last_seen_lte, "device_last_seen_gte": device_last_seen_gte, "device_type": device_type, "device_firewall_status": device_firewall_status, "device_screen_lock_status": device_screen_lock_status, "device_disk_encryption_status": device_disk_encryption_status, "cursor": cursor, "sort": sort, "order": order}, all_pages)

    def restore(self, body: DeviceStatusChangeRequest | None = None) -> DeviceRestoreResponse:
        """Restore archived devices.

        **Example:**

        ```python
        client.device.restore(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("restore", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def resume(self, body: DeviceStatusChangeRequest | None = None) -> DeviceResumeResponse:
        """Resume suspended devices.

        **Example:**

        ```python
        client.device.resume(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("resume", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def suspend(self, body: DeviceStatusChangeRequest | None = None) -> DeviceSuspendResponse:
        """Suspend devices.

        **Example:**

        ```python
        client.device.suspend(
            body=DeviceStatusChangeRequest(
                device_ids=["example"],
            ),
        )
        ```"""
        return self._call("suspend", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class CloudStorageProviderResource:
    """Typed wrapper for ``cloud_storage_provider`` (backed by ``IntegrationsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_cloud_storage_provider', 'serialize_name': '_create_cloud_storage_provider_serialize', 'requires': [], 'param_map': {}, 'body': 'create_cloud_storage_provider_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_cloud_storage_provider_by_id', 'serialize_name': '_delete_cloud_storage_provider_by_id_serialize', 'requires': ['provider_id'], 'param_map': {'provider_id': 'provider_id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_cloud_storage_provider_by_id', 'serialize_name': '_get_cloud_storage_provider_by_id_serialize', 'requires': ['provider_id'], 'param_map': {'provider_id': 'provider_id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_cloud_storage_providers', 'serialize_name': '_list_cloud_storage_providers_serialize', 'requires': [], 'param_map': {}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: IntegrationsApi) -> None:
        self._api = api

    def create(self, body: CreateCloudStorageProviderRequest | None = None) -> CloudStorageProvider:
        """Create a cloud storage provider.

        **Example:**

        ```python
        client.cloud_storage_provider.create(
            body=CreateCloudStorageProviderRequest(
                display_name="example",
                type="microsoft",
                enabled=False,
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, provider_id: str | None = None) -> None:
        """Delete a cloud storage provider.

        **Example:**

        ```python
        client.cloud_storage_provider.delete(
            provider_id="<provider_id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"provider_id": provider_id}.items() if v is not None}, {"provider_id": provider_id})

    def get(self, provider_id: str | None = None) -> CloudStorageProvider:
        """Get a cloud storage provider by ID.

        **Example:**

        ```python
        client.cloud_storage_provider.get(
            provider_id="<provider_id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"provider_id": provider_id}.items() if v is not None}, {"provider_id": provider_id})

    def list(self, *, all_pages: bool = False) -> ListCloudStorageProviders200Response:
        """List all cloud storage providers.

        **Example:**

        ```python
        client.cloud_storage_provider.list()
        ```"""
        return self._list("list", {k for k, v in {}.items() if v is not None}, {}, all_pages)

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class ApplicationPluginResource:
    """Typed wrapper for ``application_plugin`` (backed by ``PluginsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_application_plugin', 'serialize_name': '_create_application_plugin_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'update_application_plugin_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_application_plugin', 'serialize_name': '_delete_application_plugin_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_application_plugin', 'serialize_name': '_get_application_plugin_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_application_plugins', 'serialize_name': '_list_application_plugins_serialize', 'requires': [], 'param_map': {}, 'body': None, 'enums': {}}],
    "replace": [{'raw_method': 'update_application_plugin', 'serialize_name': '_update_application_plugin_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'update_application_plugin_request', 'enums': {}}],
    }

    def __init__(self, api: PluginsApi) -> None:
        self._api = api

    def create(self, id: str | None = None, body: UpdateApplicationPluginRequest | None = None) -> CreateApplicationPlugin201Response:
        """Creates a new plugin associated with the application ID.

        **Example:**

        ```python
        client.application_plugin.create(
            id="<id>",
            body=UpdateApplicationPluginRequest(
                plugin=Plugin(
                ),
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def delete(self, id: str | None = None) -> DeleteApplicationPlugin200Response:
        """Deletes the plugin associated with the application ID.

        **Example:**

        ```python
        client.application_plugin.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None) -> PluginResponse:
        """Returns the plugin associated with the application ID.

        **Example:**

        ```python
        client.application_plugin.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def list(self, *, all_pages: bool = False) -> ListApplicationPlugins200Response:
        """Returns a list of application plugins.

        **Example:**

        ```python
        client.application_plugin.list()
        ```"""
        return self._list("list", {k for k, v in {}.items() if v is not None}, {}, all_pages)

    def replace(self, id: str | None = None, body: UpdateApplicationPluginRequest | None = None) -> UpdateApplicationPlugin200Response:
        """Updates the plugin associated with the application ID.

        **Example:**

        ```python
        client.application_plugin.replace(
            id="<id>",
            body=UpdateApplicationPluginRequest(
                plugin=Plugin(
                ),
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SecurityRuleResource:
    """Typed wrapper for ``security_rule`` (backed by ``SecurityPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_security_rule', 'serialize_name': '_create_security_rule_serialize', 'requires': [], 'param_map': {}, 'body': 'create_security_rule_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_security_rule_by_id', 'serialize_name': '_delete_security_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_security_rule_by_id', 'serialize_name': '_get_security_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "update": [{'raw_method': 'patch_security_rule_by_id', 'serialize_name': '_patch_security_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'patch_security_rule_by_id_request', 'enums': {}}],
    }

    def __init__(self, api: SecurityPolicyApi) -> None:
        self._api = api

    def create(self, body: CreateSecurityRuleRequest | None = None) -> CreatedIdResponse:
        """Creates a new security policy rule.

        **Example:**

        ```python
        client.security_rule.create(
            body=CreateSecurityRuleRequest(
                name="example",
                mode="active",
                controls=SecurityControls(
                ),
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> None:
        """Delete a Security policy rule.

        **Example:**

        ```python
        client.security_rule.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SecurityRuleDetailed:
        """Retrieve a Security Rule by ID.

        **Example:**

        ```python
        client.security_rule.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def update(self, id: str | None = None, body: PatchSecurityRuleByIDRequest | None = None) -> PatchSecurityRuleByID200Response:
        """Partially update a Security policy rule. All fields are optional.

        **Example:**

        ```python
        client.security_rule.update(
            id="<id>",
            body=PatchSecurityRuleByIDRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SecuritySectionResource:
    """Typed wrapper for ``security_section`` (backed by ``SecurityPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_security_section', 'serialize_name': '_create_security_section_serialize', 'requires': [], 'param_map': {}, 'body': 'section_post_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_security_section_by_id', 'serialize_name': '_delete_security_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'delete_rules': 'delete_rules'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_security_section_by_id', 'serialize_name': '_get_security_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "reorder": [{'raw_method': 'update_security_positions', 'serialize_name': '_update_security_positions_serialize', 'requires': [], 'param_map': {}, 'body': 'update_sign_in_positions_request', 'enums': {}}],
    "reorder_patch": [{'raw_method': 'patch_security_positions', 'serialize_name': '_patch_security_positions_serialize', 'requires': [], 'param_map': {}, 'body': 'patch_positions_request', 'enums': {}}],
    "replace": [{'raw_method': 'update_security_section_by_id', 'serialize_name': '_update_security_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_update_request', 'enums': {}}],
    "update": [{'raw_method': 'patch_security_section_by_id', 'serialize_name': '_patch_security_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_patch_request', 'enums': {}}],
    }

    def __init__(self, api: SecurityPolicyApi) -> None:
        self._api = api

    def create(self, body: SectionPostRequest | None = None) -> SectionDetailed:
        """Creates a new security section.

        **Example:**

        ```python
        client.security_section.create(
            body=SectionPostRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None, delete_rules: bool | None = None) -> None:
        """Delete a security rule section.

        **Example:**

        ```python
        client.security_section.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id, "delete_rules": delete_rules}.items() if v is not None}, {"id": id, "delete_rules": delete_rules})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SectionDetailed:
        """Retrieve a Security Section by ID.

        **Example:**

        ```python
        client.security_section.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def reorder(self, body: UpdateSignInPositionsRequest | None = None) -> PositionsSuccessResponse:
        """Update rule and section positions in the security policy.

        **Example:**

        ```python
        client.security_section.reorder(
            body=UpdateSignInPositionsRequest(
                positions=[
                    PositionItem(PositionItemSection(
                            type="Section",
                            id="example",
                        )),
                ],
            ),
        )
        ```"""
        return self._call("reorder", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def reorder_patch(self, body: PatchPositionsRequest | None = None) -> PositionsSuccessResponse:
        """Apply partial positional changes (moves) to the security policy.

        **Example:**

        ```python
        client.security_section.reorder_patch(
            body=PatchPositionsRequest(
                moves=[
                    PositionMove(
                        subject=PositionMoveSubject(
                            type="Rule",
                            id="example",
                        ),
                        target=PositionMoveTarget(
                            position="top",
                        ),
                    ),
                ],
            ),
        )
        ```"""
        return self._call("reorder_patch", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def replace(self, id: str | None = None, body: SectionUpdateRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Updates a security rule section.

        **Example:**

        ```python
        client.security_section.replace(
            id="<id>",
            body=SectionUpdateRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def update(self, id: str | None = None, body: SectionPatchRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Partially update a security policy section.

        **Example:**

        ```python
        client.security_section.update(
            id="<id>",
            body=SectionPatchRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SecurityPolicyResource:
    """Typed wrapper for ``security_policy`` (backed by ``SecurityPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "get": [{'raw_method': 'get_security_policy', 'serialize_name': '_get_security_policy_serialize', 'requires': [], 'param_map': {'configuration_version': 'configuration_version', 'limit': 'limit', 'cursor': 'cursor'}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: SecurityPolicyApi) -> None:
        self._api = api

    def get(self, configuration_version: str | None = None, limit: int | None = None, cursor: str | None = None) -> GetSignInPolicy200Response:
        """Retrieve the Security Policy.

        **Example:**

        ```python
        client.security_policy.get()
        ```"""
        return self._fetch("get", {k for k, v in {"configuration_version": configuration_version, "limit": limit, "cursor": cursor}.items() if v is not None}, {"configuration_version": configuration_version, "limit": limit, "cursor": cursor})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SignInRuleResource:
    """Typed wrapper for ``sign_in_rule`` (backed by ``SignInPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_sign_in_rule', 'serialize_name': '_create_sign_in_rule_serialize', 'requires': [], 'param_map': {}, 'body': 'create_sign_in_rule_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_sign_in_rule_by_id', 'serialize_name': '_delete_sign_in_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_sign_in_rule_by_id', 'serialize_name': '_get_sign_in_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "update": [{'raw_method': 'patch_sign_in_rule_by_id', 'serialize_name': '_patch_sign_in_rule_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'patch_sign_in_rule_by_id_request', 'enums': {}}],
    }

    def __init__(self, api: SignInPolicyApi) -> None:
        self._api = api

    def create(self, body: CreateSignInRuleRequest | None = None) -> CreatedIdResponse:
        """Creates a new sign-in rule in the policy.

        **Example:**

        ```python
        client.sign_in_rule.create(
            body=CreateSignInRuleRequest(
                name="example",
                mode="active",
                action="allow",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> None:
        """Delete a Sign-In policy rule.

        **Example:**

        ```python
        client.sign_in_rule.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SignInRuleDetailed:
        """Retrieve a Sign-In Rule by ID.

        **Example:**

        ```python
        client.sign_in_rule.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def update(self, id: str | None = None, body: PatchSignInRuleByIDRequest | None = None) -> PatchSignInRuleByID200Response:
        """Partially update a Sign-In policy rule. All fields are optional.

        **Example:**

        ```python
        client.sign_in_rule.update(
            id="<id>",
            body=PatchSignInRuleByIDRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SignInSectionResource:
    """Typed wrapper for ``sign_in_section`` (backed by ``SignInPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_sign_in_section', 'serialize_name': '_create_sign_in_section_serialize', 'requires': [], 'param_map': {}, 'body': 'section_post_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_sign_in_section_by_id', 'serialize_name': '_delete_sign_in_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'delete_rules': 'delete_rules'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_sign_in_section_by_id', 'serialize_name': '_get_sign_in_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id', 'configuration_version': 'configuration_version'}, 'body': None, 'enums': {}}],
    "reorder": [{'raw_method': 'update_sign_in_positions', 'serialize_name': '_update_sign_in_positions_serialize', 'requires': [], 'param_map': {}, 'body': 'update_sign_in_positions_request', 'enums': {}}],
    "replace": [{'raw_method': 'update_sign_in_section_by_id', 'serialize_name': '_update_sign_in_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_update_request', 'enums': {}}],
    "update": [{'raw_method': 'patch_sign_in_section_by_id', 'serialize_name': '_patch_sign_in_section_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'section_patch_request', 'enums': {}}],
    }

    def __init__(self, api: SignInPolicyApi) -> None:
        self._api = api

    def create(self, body: SectionPostRequest | None = None) -> SectionDetailed:
        """Creates a new sign-in rule section for grouping rules.

        **Example:**

        ```python
        client.sign_in_section.create(
            body=SectionPostRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None, delete_rules: bool | None = None) -> None:
        """Delete a sign-in rule section.

        **Example:**

        ```python
        client.sign_in_section.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id, "delete_rules": delete_rules}.items() if v is not None}, {"id": id, "delete_rules": delete_rules})

    def get(self, id: str | None = None, configuration_version: str | None = None) -> SectionDetailed:
        """Retrieve a Sign-In Section by ID.

        **Example:**

        ```python
        client.sign_in_section.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id, "configuration_version": configuration_version}.items() if v is not None}, {"id": id, "configuration_version": configuration_version})

    def reorder(self, body: UpdateSignInPositionsRequest | None = None) -> PositionsSuccessResponse:
        """Update rule and section positions in the sign-in policy.

        **Example:**

        ```python
        client.sign_in_section.reorder(
            body=UpdateSignInPositionsRequest(
                positions=[
                    PositionItem(PositionItemSection(
                            type="Section",
                            id="example",
                        )),
                ],
            ),
        )
        ```"""
        return self._call("reorder", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def replace(self, id: str | None = None, body: SectionUpdateRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Updates a sign-in rule section.

        **Example:**

        ```python
        client.sign_in_section.replace(
            id="<id>",
            body=SectionUpdateRequest(
                name="example",
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def update(self, id: str | None = None, body: SectionPatchRequest | None = None) -> UpdateSignInSectionByID200Response:
        """Partially update a sign-in policy section.

        **Example:**

        ```python
        client.sign_in_section.update(
            id="<id>",
            body=SectionPatchRequest(),  # all fields optional
        )
        ```"""
        return self._call("update", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class SignInPolicyResource:
    """Typed wrapper for ``sign_in_policy`` (backed by ``SignInPolicyApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "get": [{'raw_method': 'get_sign_in_policy', 'serialize_name': '_get_sign_in_policy_serialize', 'requires': [], 'param_map': {'configuration_version': 'configuration_version', 'limit': 'limit', 'cursor': 'cursor'}, 'body': None, 'enums': {}}],
    }

    def __init__(self, api: SignInPolicyApi) -> None:
        self._api = api

    def get(self, configuration_version: str | None = None, limit: int | None = None, cursor: str | None = None) -> GetSignInPolicy200Response:
        """Retrieve the Sign-In Policy.

        **Example:**

        ```python
        client.sign_in_policy.get()
        ```"""
        return self._fetch("get", {k for k, v in {"configuration_version": configuration_version, "limit": limit, "cursor": cursor}.items() if v is not None}, {"configuration_version": configuration_version, "limit": limit, "cursor": cursor})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class UserGroupResource:
    """Typed wrapper for ``user_group`` (backed by ``UserGroupsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "create": [{'raw_method': 'create_user_group', 'serialize_name': '_create_user_group_serialize', 'requires': [], 'param_map': {}, 'body': 'create_user_group_request', 'enums': {}}],
    "delete": [{'raw_method': 'delete_user_group', 'serialize_name': '_delete_user_group_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "get": [{'raw_method': 'get_user_group_by_id', 'serialize_name': '_get_user_group_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_user_groups', 'serialize_name': '_list_user_groups_serialize', 'requires': [], 'param_map': {'limit': 'limit', 'cursor': 'cursor'}, 'body': None, 'enums': {}}],
    "replace": [{'raw_method': 'update_user_group', 'serialize_name': '_update_user_group_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'update_user_group_request', 'enums': {}}],
    }

    def __init__(self, api: UserGroupsApi) -> None:
        self._api = api

    def create(self, body: CreateUserGroupRequest | None = None) -> CreateUserGroup201Response:
        """Creates a new user group.

        **Example:**

        ```python
        client.user_group.create(
            body=CreateUserGroupRequest(
                name="example",
                user_ids=["example"],
            ),
        )
        ```"""
        return self._call("create", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def delete(self, id: str | None = None) -> DeleteUserGroup200Response:
        """Deletes a user group.

        **Example:**

        ```python
        client.user_group.delete(
            id="<id>",
        )
        ```"""
        return self._call("delete", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def get(self, id: str | None = None) -> UserGroup:
        """Returns a single user group by ID.

        **Example:**

        ```python
        client.user_group.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def list(self, limit: int | None = None, cursor: str | None = None, *, all_pages: bool = False) -> ListUserGroups200Response:
        """Returns a list of user groups.

        **Example:**

        ```python
        client.user_group.list()
        ```"""
        return self._list("list", {k for k, v in {"limit": limit, "cursor": cursor}.items() if v is not None}, {"limit": limit, "cursor": cursor}, all_pages)

    def replace(self, id: str | None = None, body: UpdateUserGroupRequest | None = None) -> UpdateUserGroup200Response:
        """Updates a user group.

        **Example:**

        ```python
        client.user_group.replace(
            id="<id>",
            body=UpdateUserGroupRequest(
                users=[
                    UpdateUserGroupRequestUsersInner(
                        user_id="example",
                        action="add",
                    ),
                ],
            ),
        )
        ```"""
        return self._call("replace", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class UserRequestResource:
    """Typed wrapper for ``user_request`` (backed by ``UserRequestsApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "action": [{'raw_method': 'action_user_request', 'serialize_name': '_action_user_request_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'request_action', 'enums': {}}],
    "get": [{'raw_method': 'get_user_request_by_id', 'serialize_name': '_get_user_request_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_user_requests', 'serialize_name': '_list_user_requests_serialize', 'requires': [], 'param_map': {'limit': 'limit', 'request_type': 'request_type', 'request_user_id': 'request_user_id', 'request_device_id': 'request_device_id', 'request_rule_id': 'request_rule_id', 'request_url': 'request_url', 'request_responded_by': 'request_responded_by', 'request_status': 'request_status', 'cursor': 'cursor', 'sort': 'sort', 'order': 'order'}, 'body': None, 'enums': {'request_type': 'ListUserRequestsRequestTypeParameter', 'request_status': 'ListUserRequestsRequestStatusParameter', 'sort': 'ListUserRequestsSortParameter', 'order': 'Order'}}],
    "revoke": [{'raw_method': 'revoke_user_request', 'serialize_name': '_revoke_user_request_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': 'revoke_request_action', 'enums': {}}],
    }

    def __init__(self, api: UserRequestsApi) -> None:
        self._api = api

    def action(self, id: str | None = None, body: RequestAction | None = None) -> UserRequest:
        """Act upon a user request.

        **Example:**

        ```python
        client.user_request.action(
            id="<id>",
            body=RequestAction(
                action="approve",
            ),
        )
        ```"""
        return self._call("action", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def get(self, id: str | None = None) -> UserRequest:
        """Returns a request by ID.

        **Example:**

        ```python
        client.user_request.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def list(self, limit: int | None = None, request_type: ListUserRequestsRequestTypeParameter | None = None, request_user_id: str | None = None, request_device_id: str | None = None, request_rule_id: str | None = None, request_url: str | None = None, request_responded_by: str | None = None, request_status: ListUserRequestsRequestStatusParameter | None = None, cursor: str | None = None, sort: ListUserRequestsSortParameter | None = None, order: Order | None = None, *, all_pages: bool = False) -> ListUserRequests200Response:
        """Returns a list of user requests.

        **Example:**

        ```python
        client.user_request.list()
        ```"""
        return self._list("list", {k for k, v in {"limit": limit, "request_type": request_type, "request_user_id": request_user_id, "request_device_id": request_device_id, "request_rule_id": request_rule_id, "request_url": request_url, "request_responded_by": request_responded_by, "request_status": request_status, "cursor": cursor, "sort": sort, "order": order}.items() if v is not None}, {"limit": limit, "request_type": request_type, "request_user_id": request_user_id, "request_device_id": request_device_id, "request_rule_id": request_rule_id, "request_url": request_url, "request_responded_by": request_responded_by, "request_status": request_status, "cursor": cursor, "sort": sort, "order": order}, all_pages)

    def revoke(self, id: str | None = None, body: RevokeRequestAction | None = None) -> UserRequest:
        """Revoke already approved request.

        **Example:**

        ```python
        client.user_request.revoke(
            id="<id>",
            body=RevokeRequestAction(),  # all fields optional
        )
        ```"""
        return self._call("revoke", {k for k, v in {"id": id, "body": body}.items() if v is not None}, {"id": id, "body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


class UserResource:
    """Typed wrapper for ``user`` (backed by ``UsersApi``)."""

    _bindings: ClassVar[dict[str, list[dict[str, Any]]]] = {
    "force_reauth": [{'raw_method': 'force_reauth_users', 'serialize_name': '_force_reauth_users_serialize', 'requires': [], 'param_map': {}, 'body': 'user_status_change_request', 'enums': {}}],
    "get": [{'raw_method': 'get_user_by_id', 'serialize_name': '_get_user_by_id_serialize', 'requires': ['id'], 'param_map': {'id': 'id'}, 'body': None, 'enums': {}}],
    "list": [{'raw_method': 'list_users', 'serialize_name': '_list_users_serialize', 'requires': [], 'param_map': {'limit': 'limit', 'include_deleted': 'include_deleted', 'user_name': 'user_name', 'user_email': 'user_email', 'user_first_seen_gte': 'user_first_seen_gte', 'user_last_seen_lte': 'user_last_seen_lte', 'user_status': 'user_status', 'group_id': 'group_id', 'cursor': 'cursor', 'sort': 'sort', 'order': 'order'}, 'body': None, 'enums': {'user_status': 'UserStatus', 'sort': 'ListUsersSortParameter', 'order': 'Order'}}],
    "resume": [{'raw_method': 'resume_users', 'serialize_name': '_resume_users_serialize', 'requires': [], 'param_map': {}, 'body': 'user_status_change_request', 'enums': {}}],
    "suspend": [{'raw_method': 'suspend_users', 'serialize_name': '_suspend_users_serialize', 'requires': [], 'param_map': {}, 'body': 'user_status_change_request', 'enums': {}}],
    }

    def __init__(self, api: UsersApi) -> None:
        self._api = api

    def force_reauth(self, body: UserStatusChangeRequest | None = None) -> UserForceReauthResponse:
        """Force re-authentication for users.

        **Example:**

        ```python
        client.user.force_reauth(
            body=UserStatusChangeRequest(
                user_ids=["example"],
            ),
        )
        ```"""
        return self._call("force_reauth", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def get(self, id: str | None = None) -> User:
        """Returns a user by ID.

        **Example:**

        ```python
        client.user.get(
            id="<id>",
        )
        ```"""
        return self._fetch("get", {k for k, v in {"id": id}.items() if v is not None}, {"id": id})

    def list(self, limit: int | None = None, include_deleted: bool | None = None, user_name: str | None = None, user_email: str | None = None, user_first_seen_gte: str | None = None, user_last_seen_lte: str | None = None, user_status: UserStatus | None = None, group_id: str | None = None, cursor: str | None = None, sort: ListUsersSortParameter | None = None, order: Order | None = None, *, all_pages: bool = False) -> ListUsers200Response:
        """Returns a list of users.

        **Example:**

        ```python
        client.user.list()
        ```"""
        return self._list("list", {k for k, v in {"limit": limit, "include_deleted": include_deleted, "user_name": user_name, "user_email": user_email, "user_first_seen_gte": user_first_seen_gte, "user_last_seen_lte": user_last_seen_lte, "user_status": user_status, "group_id": group_id, "cursor": cursor, "sort": sort, "order": order}.items() if v is not None}, {"limit": limit, "include_deleted": include_deleted, "user_name": user_name, "user_email": user_email, "user_first_seen_gte": user_first_seen_gte, "user_last_seen_lte": user_last_seen_lte, "user_status": user_status, "group_id": group_id, "cursor": cursor, "sort": sort, "order": order}, all_pages)

    def resume(self, body: UserStatusChangeRequest | None = None) -> UserResumeResponse:
        """Resume suspended users.

        **Example:**

        ```python
        client.user.resume(
            body=UserStatusChangeRequest(
                user_ids=["example"],
            ),
        )
        ```"""
        return self._call("resume", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def suspend(self, body: UserStatusChangeRequest | None = None) -> UserSuspendResponse:
        """Suspend users.

        **Example:**

        ```python
        client.user.suspend(
            body=UserStatusChangeRequest(
                user_ids=["example"],
            ),
        )
        ```"""
        return self._call("suspend", {k for k, v in {"body": body}.items() if v is not None}, {"body": body})

    def _select(self, verb: str, present: set[str]) -> dict[str, Any]:
        cands = [b for b in self._bindings[verb] if set(b["requires"]) <= present]
        if not cands:
            raise ValueError(f"{verb}: missing required arg(s)")
        return max(cands, key=lambda b: len(b["requires"]))

    def _to_raw(self, kwargs: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
        raw: dict[str, Any] = {}
        enums = b["enums"]
        for wrapper_name, raw_name in b["param_map"].items():
            value = kwargs.get(wrapper_name)
            if value is None:
                continue
            if wrapper_name in enums and isinstance(value, str):
                value = globals()[enums[wrapper_name]](value)
            raw[raw_name] = value
        if b["body"] is not None and kwargs.get("body") is not None:
            raw[b["body"]] = kwargs["body"]
        return raw

    def _call(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        b = self._select(verb, present)
        return getattr(self._api, b["raw_method"])(**self._to_raw(kwargs, b))

    def _fetch(self, verb: str, present: set[str], kwargs: dict[str, Any]) -> Any:
        return self._call(verb, present, kwargs)

    def _list(
        self, verb: str, present: set[str], kwargs: dict[str, Any], all_pages: bool
    ) -> Any:
        b = self._select(verb, present)
        fn = getattr(self._api, b["raw_method"])
        raw = self._to_raw(kwargs, b)
        page = fn(**raw)
        if not all_pages:
            return page
        items = list(paginate(fn, **raw))
        return page.model_copy(update={"data": items})

    def _serialize(self, verb: str, **kwargs: Any) -> Any:
        present = {k for k, v in kwargs.items() if v is not None}
        b = self._select(verb, present)
        fn = getattr(self._api, b["serialize_name"])
        params = {
            k: (0 if k == "_host_index" else None)
            for k in inspect.signature(fn).parameters
            if k != "self"
        }
        params.update(self._to_raw(kwargs, b))
        return fn(**params)


