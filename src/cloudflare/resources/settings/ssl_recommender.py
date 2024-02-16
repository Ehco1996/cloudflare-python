# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import (
    make_request_options,
)
from ...types.settings import SSLRecommenderGetResponse, SSLRecommenderUpdateResponse, ssl_recommender_update_params

__all__ = ["SSLRecommender", "AsyncSSLRecommender"]


class SSLRecommender(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSLRecommenderWithRawResponse:
        return SSLRecommenderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLRecommenderWithStreamingResponse:
        return SSLRecommenderWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: ssl_recommender_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommenderUpdateResponse]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

        Args:
          zone_id: Identifier

          value: Enrollment in the SSL/TLS Recommender service which tries to detect and
              recommend (by sending periodic emails) the most secure SSL/TLS setting your
              origin servers support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ssl_recommender",
            body=maybe_transform({"value": value}, ssl_recommender_update_params.SSLRecommenderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommenderUpdateResponse]], ResultWrapper[SSLRecommenderUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommenderGetResponse]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

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
            f"/zones/{zone_id}/settings/ssl_recommender",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommenderGetResponse]], ResultWrapper[SSLRecommenderGetResponse]),
        )


class AsyncSSLRecommender(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSLRecommenderWithRawResponse:
        return AsyncSSLRecommenderWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLRecommenderWithStreamingResponse:
        return AsyncSSLRecommenderWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: ssl_recommender_update_params.Value,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommenderUpdateResponse]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

        Args:
          zone_id: Identifier

          value: Enrollment in the SSL/TLS Recommender service which tries to detect and
              recommend (by sending periodic emails) the most secure SSL/TLS setting your
              origin servers support.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ssl_recommender",
            body=maybe_transform({"value": value}, ssl_recommender_update_params.SSLRecommenderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommenderUpdateResponse]], ResultWrapper[SSLRecommenderUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLRecommenderGetResponse]:
        """
        Enrollment in the SSL/TLS Recommender service which tries to detect and
        recommend (by sending periodic emails) the most secure SSL/TLS setting your
        origin servers support.

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
            f"/zones/{zone_id}/settings/ssl_recommender",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLRecommenderGetResponse]], ResultWrapper[SSLRecommenderGetResponse]),
        )


class SSLRecommenderWithRawResponse:
    def __init__(self, ssl_recommender: SSLRecommender) -> None:
        self._ssl_recommender = ssl_recommender

        self.update = to_raw_response_wrapper(
            ssl_recommender.update,
        )
        self.get = to_raw_response_wrapper(
            ssl_recommender.get,
        )


class AsyncSSLRecommenderWithRawResponse:
    def __init__(self, ssl_recommender: AsyncSSLRecommender) -> None:
        self._ssl_recommender = ssl_recommender

        self.update = async_to_raw_response_wrapper(
            ssl_recommender.update,
        )
        self.get = async_to_raw_response_wrapper(
            ssl_recommender.get,
        )


class SSLRecommenderWithStreamingResponse:
    def __init__(self, ssl_recommender: SSLRecommender) -> None:
        self._ssl_recommender = ssl_recommender

        self.update = to_streamed_response_wrapper(
            ssl_recommender.update,
        )
        self.get = to_streamed_response_wrapper(
            ssl_recommender.get,
        )


class AsyncSSLRecommenderWithStreamingResponse:
    def __init__(self, ssl_recommender: AsyncSSLRecommender) -> None:
        self._ssl_recommender = ssl_recommender

        self.update = async_to_streamed_response_wrapper(
            ssl_recommender.update,
        )
        self.get = async_to_streamed_response_wrapper(
            ssl_recommender.get,
        )
