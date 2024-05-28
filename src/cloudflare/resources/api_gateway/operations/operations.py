# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Type, Iterable, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .schema_validation import (
    SchemaValidationResource,
    AsyncSchemaValidationResource,
    SchemaValidationResourceWithRawResponse,
    AsyncSchemaValidationResourceWithRawResponse,
    SchemaValidationResourceWithStreamingResponse,
    AsyncSchemaValidationResourceWithStreamingResponse,
)
from ....types.api_gateway import operation_get_params, operation_list_params, operation_create_params
from ....types.api_gateway.api_shield import APIShield
from ....types.api_gateway.operation_create_response import OperationCreateResponse
from ....types.api_gateway.operation_delete_response import OperationDeleteResponse

__all__ = ["OperationsResource", "AsyncOperationsResource"]


class OperationsResource(SyncAPIResource):
    @cached_property
    def schema_validation(self) -> SchemaValidationResource:
        return SchemaValidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        body: Iterable[operation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationCreateResponse]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/api_gateway/operations",
            body=maybe_transform(body, operation_create_params.OperationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OperationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationCreateResponse]], ResultWrapper[OperationCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[APIShield]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Number of results to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=SyncSinglePage[APIShield],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=APIShield,
        )

    def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return cast(
            OperationDeleteResponse,
            self._delete(
                f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[OperationDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OperationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShield:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper[APIShield]._unwrapper,
            ),
            cast_to=cast(Type[APIShield], ResultWrapper[APIShield]),
        )


class AsyncOperationsResource(AsyncAPIResource):
    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResource:
        return AsyncSchemaValidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        body: Iterable[operation_create_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OperationCreateResponse]:
        """Add one or more operations to a zone.

        Endpoints can contain path variables.
        Host, method, endpoint will be normalized to a canoncial form when creating an
        operation and must be unique on the zone. Inserting an operation that matches an
        existing one will return the record of the already existing operation and update
        its last_updated date.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/api_gateway/operations",
            body=await async_maybe_transform(body, operation_create_params.OperationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OperationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OperationCreateResponse]], ResultWrapper[OperationCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        endpoint: str | NotGiven = NOT_GIVEN,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        host: List[str] | NotGiven = NOT_GIVEN,
        method: List[str] | NotGiven = NOT_GIVEN,
        order: Literal["method", "host", "endpoint", "thresholds.$key"] | NotGiven = NOT_GIVEN,
        page: object | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[APIShield, AsyncSinglePage[APIShield]]:
        """
        Retrieve information about all operations on a zone

        Args:
          zone_id: Identifier

          direction: Direction to order results.

          endpoint: Filter results to only include endpoints containing this pattern.

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          host: Filter results to only include the specified hosts.

          method: Filter results to only include the specified HTTP methods.

          order: Field to order by. When requesting a feature, the feature keys are available for
              ordering as well, e.g., `thresholds.suggested_threshold`.

          page: Page number of paginated results.

          per_page: Number of results to return per page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/api_gateway/operations",
            page=AsyncSinglePage[APIShield],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "endpoint": endpoint,
                        "feature": feature,
                        "host": host,
                        "method": method,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                    },
                    operation_list_params.OperationListParams,
                ),
            ),
            model=APIShield,
        )

    async def delete(
        self,
        operation_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationDeleteResponse:
        """
        Delete an operation

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return cast(
            OperationDeleteResponse,
            await self._delete(
                f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[OperationDeleteResponse]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OperationDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        operation_id: str,
        *,
        zone_id: str,
        feature: List[Literal["thresholds", "parameter_schemas", "schema_info"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> APIShield:
        """
        Retrieve information about an operation

        Args:
          zone_id: Identifier

          feature: Add feature(s) to the results. The feature name that is given here corresponds
              to the resulting feature object. Have a look at the top-level object description
              for more details on the specific meaning.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not operation_id:
            raise ValueError(f"Expected a non-empty value for `operation_id` but received {operation_id!r}")
        return await self._get(
            f"/zones/{zone_id}/api_gateway/operations/{operation_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"feature": feature}, operation_get_params.OperationGetParams),
                post_parser=ResultWrapper[APIShield]._unwrapper,
            ),
            cast_to=cast(Type[APIShield], ResultWrapper[APIShield]),
        )


class OperationsResourceWithRawResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_raw_response_wrapper(
            operations.create,
        )
        self.list = to_raw_response_wrapper(
            operations.list,
        )
        self.delete = to_raw_response_wrapper(
            operations.delete,
        )
        self.get = to_raw_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithRawResponse:
        return SchemaValidationResourceWithRawResponse(self._operations.schema_validation)


class AsyncOperationsResourceWithRawResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_raw_response_wrapper(
            operations.create,
        )
        self.list = async_to_raw_response_wrapper(
            operations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            operations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithRawResponse:
        return AsyncSchemaValidationResourceWithRawResponse(self._operations.schema_validation)


class OperationsResourceWithStreamingResponse:
    def __init__(self, operations: OperationsResource) -> None:
        self._operations = operations

        self.create = to_streamed_response_wrapper(
            operations.create,
        )
        self.list = to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = to_streamed_response_wrapper(
            operations.delete,
        )
        self.get = to_streamed_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> SchemaValidationResourceWithStreamingResponse:
        return SchemaValidationResourceWithStreamingResponse(self._operations.schema_validation)


class AsyncOperationsResourceWithStreamingResponse:
    def __init__(self, operations: AsyncOperationsResource) -> None:
        self._operations = operations

        self.create = async_to_streamed_response_wrapper(
            operations.create,
        )
        self.list = async_to_streamed_response_wrapper(
            operations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            operations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            operations.get,
        )

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationResourceWithStreamingResponse:
        return AsyncSchemaValidationResourceWithStreamingResponse(self._operations.schema_validation)
