# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
from ....types.zones.settings import opportunistic_onion_edit_params
from ....types.zones.settings.opportunistic_onion import OpportunisticOnion

__all__ = ["OpportunisticOnionResource", "AsyncOpportunisticOnionResource"]


class OpportunisticOnionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OpportunisticOnionResourceWithRawResponse:
        return OpportunisticOnionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OpportunisticOnionResourceWithStreamingResponse:
        return OpportunisticOnionResourceWithStreamingResponse(self)

    def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            body=maybe_transform({"value": value}, opportunistic_onion_edit_params.OpportunisticOnionEditParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OpportunisticOnion]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OpportunisticOnion]], ResultWrapper[OpportunisticOnion]),
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
    ) -> Optional[OpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

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
            f"/zones/{zone_id}/settings/opportunistic_onion",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OpportunisticOnion]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OpportunisticOnion]], ResultWrapper[OpportunisticOnion]),
        )


class AsyncOpportunisticOnionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOpportunisticOnionResourceWithRawResponse:
        return AsyncOpportunisticOnionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOpportunisticOnionResourceWithStreamingResponse:
        return AsyncOpportunisticOnionResourceWithStreamingResponse(self)

    async def edit(
        self,
        *,
        zone_id: str,
        value: Literal["on", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Default value depends on the zone's plan
              level.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/opportunistic_onion",
            body=await async_maybe_transform(
                {"value": value}, opportunistic_onion_edit_params.OpportunisticOnionEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OpportunisticOnion]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OpportunisticOnion]], ResultWrapper[OpportunisticOnion]),
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
    ) -> Optional[OpportunisticOnion]:
        """
        Add an Alt-Svc header to all legitimate requests from Tor, allowing the
        connection to use our onion services instead of exit nodes.

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
            f"/zones/{zone_id}/settings/opportunistic_onion",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OpportunisticOnion]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[OpportunisticOnion]], ResultWrapper[OpportunisticOnion]),
        )


class OpportunisticOnionResourceWithRawResponse:
    def __init__(self, opportunistic_onion: OpportunisticOnionResource) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = to_raw_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = to_raw_response_wrapper(
            opportunistic_onion.get,
        )


class AsyncOpportunisticOnionResourceWithRawResponse:
    def __init__(self, opportunistic_onion: AsyncOpportunisticOnionResource) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = async_to_raw_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = async_to_raw_response_wrapper(
            opportunistic_onion.get,
        )


class OpportunisticOnionResourceWithStreamingResponse:
    def __init__(self, opportunistic_onion: OpportunisticOnionResource) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = to_streamed_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = to_streamed_response_wrapper(
            opportunistic_onion.get,
        )


class AsyncOpportunisticOnionResourceWithStreamingResponse:
    def __init__(self, opportunistic_onion: AsyncOpportunisticOnionResource) -> None:
        self._opportunistic_onion = opportunistic_onion

        self.edit = async_to_streamed_response_wrapper(
            opportunistic_onion.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            opportunistic_onion.get,
        )
