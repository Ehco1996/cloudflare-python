# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.api_gateways.discovery import OperationUpdateResponse, operation_update_params

__all__ = ["Operations", "AsyncOperations"]


class Operations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        body: Dict[str, operation_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update the `state` on one or more discovered operations

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            body=maybe_transform(body, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )


class AsyncOperations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        body: Dict[str, operation_update_params.Body],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OperationUpdateResponse:
        """
        Update the `state` on one or more discovered operations

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/api_gateway/discovery/operations",
            body=maybe_transform(body, operation_update_params.OperationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[OperationUpdateResponse], ResultWrapper[OperationUpdateResponse]),
        )


class OperationsWithRawResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.update = to_raw_response_wrapper(
            operations.update,
        )


class AsyncOperationsWithRawResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.update = async_to_raw_response_wrapper(
            operations.update,
        )


class OperationsWithStreamingResponse:
    def __init__(self, operations: Operations) -> None:
        self._operations = operations

        self.update = to_streamed_response_wrapper(
            operations.update,
        )


class AsyncOperationsWithStreamingResponse:
    def __init__(self, operations: AsyncOperations) -> None:
        self._operations = operations

        self.update = async_to_streamed_response_wrapper(
            operations.update,
        )
