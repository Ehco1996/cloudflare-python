# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from ....types.mnms.configs import FullListResponse

__all__ = ["Fulls", "AsyncFulls"]


class Fulls(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FullsWithRawResponse:
        return FullsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FullsWithStreamingResponse:
        return FullsWithStreamingResponse(self)

    def list(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullListResponse:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_identifier}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FullListResponse], ResultWrapper[FullListResponse]),
        )


class AsyncFulls(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFullsWithRawResponse:
        return AsyncFullsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFullsWithStreamingResponse:
        return AsyncFullsWithStreamingResponse(self)

    async def list(
        self,
        account_identifier: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullListResponse:
        """
        Lists default sampling, router IPs, and rules for account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_identifier}/mnm/config/full",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[FullListResponse], ResultWrapper[FullListResponse]),
        )


class FullsWithRawResponse:
    def __init__(self, fulls: Fulls) -> None:
        self._fulls = fulls

        self.list = to_raw_response_wrapper(
            fulls.list,
        )


class AsyncFullsWithRawResponse:
    def __init__(self, fulls: AsyncFulls) -> None:
        self._fulls = fulls

        self.list = async_to_raw_response_wrapper(
            fulls.list,
        )


class FullsWithStreamingResponse:
    def __init__(self, fulls: Fulls) -> None:
        self._fulls = fulls

        self.list = to_streamed_response_wrapper(
            fulls.list,
        )


class AsyncFullsWithStreamingResponse:
    def __init__(self, fulls: AsyncFulls) -> None:
        self._fulls = fulls

        self.list = async_to_streamed_response_wrapper(
            fulls.list,
        )
