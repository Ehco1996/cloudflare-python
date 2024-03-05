# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast
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
from ...._base_client import (
    make_request_options,
)
from ....types.zones.settings import ZonesMinTLSVersion, min_tls_version_edit_params

__all__ = ["MinTLSVersion", "AsyncMinTLSVersion"]


class MinTLSVersion(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MinTLSVersionWithRawResponse:
        return MinTLSVersionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MinTLSVersionWithStreamingResponse:
        return MinTLSVersionWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["1.0", "1.1", "1.2", "1.3"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesMinTLSVersion]:
        """
        Changes Minimum TLS Version setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/min_tls_version",
            body=maybe_transform({"value": value}, min_tls_version_edit_params.MinTLSVersionEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesMinTLSVersion]], ResultWrapper[ZonesMinTLSVersion]),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesMinTLSVersion]:
        """
        Gets Minimum TLS Version setting.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/min_tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesMinTLSVersion]], ResultWrapper[ZonesMinTLSVersion]),
        )


class AsyncMinTLSVersion(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMinTLSVersionWithRawResponse:
        return AsyncMinTLSVersionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMinTLSVersionWithStreamingResponse:
        return AsyncMinTLSVersionWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["1.0", "1.1", "1.2", "1.3"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesMinTLSVersion]:
        """
        Changes Minimum TLS Version setting.

        Args:
          zone_id: Identifier

          value: Value of the zone setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/min_tls_version",
            body=await async_maybe_transform({"value": value}, min_tls_version_edit_params.MinTLSVersionEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesMinTLSVersion]], ResultWrapper[ZonesMinTLSVersion]),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ZonesMinTLSVersion]:
        """
        Gets Minimum TLS Version setting.

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/min_tls_version",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ZonesMinTLSVersion]], ResultWrapper[ZonesMinTLSVersion]),
        )


class MinTLSVersionWithRawResponse:
    def __init__(self, min_tls_version: MinTLSVersion) -> None:
        self._min_tls_version = min_tls_version

        self.edit = to_raw_response_wrapper(
            min_tls_version.edit,
        )
        self.get = to_raw_response_wrapper(
            min_tls_version.get,
        )


class AsyncMinTLSVersionWithRawResponse:
    def __init__(self, min_tls_version: AsyncMinTLSVersion) -> None:
        self._min_tls_version = min_tls_version

        self.edit = async_to_raw_response_wrapper(
            min_tls_version.edit,
        )
        self.get = async_to_raw_response_wrapper(
            min_tls_version.get,
        )


class MinTLSVersionWithStreamingResponse:
    def __init__(self, min_tls_version: MinTLSVersion) -> None:
        self._min_tls_version = min_tls_version

        self.edit = to_streamed_response_wrapper(
            min_tls_version.edit,
        )
        self.get = to_streamed_response_wrapper(
            min_tls_version.get,
        )


class AsyncMinTLSVersionWithStreamingResponse:
    def __init__(self, min_tls_version: AsyncMinTLSVersion) -> None:
        self._min_tls_version = min_tls_version

        self.edit = async_to_streamed_response_wrapper(
            min_tls_version.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            min_tls_version.get,
        )
