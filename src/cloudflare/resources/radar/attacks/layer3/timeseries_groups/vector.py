# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Type, Union, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ......_types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ......_utils import maybe_transform
from ......_compat import cached_property
from ......_resource import SyncAPIResource, AsyncAPIResource
from ......_response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ......_wrappers import ResultWrapper
from ......_base_client import (
    make_request_options,
)
from ......types.radar.attacks.layer3.timeseries_groups import VectorListResponse, vector_list_params

__all__ = ["Vector", "AsyncVector"]


class Vector(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VectorWithRawResponse:
        return VectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VectorWithStreamingResponse:
        return VectorWithStreamingResponse(self)

    def list(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorListResponse:
        """
        Percentage distribution of attacks by vector used over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          direction: Together with the `location` parameter, will apply the filter to origin or
              target location.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit_per_group: Limit the number of objects (eg browsers, verticals, etc) to the top items over
              the time range.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/attacks/layer3/timeseries_groups/vector",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    vector_list_params.VectorListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VectorListResponse], ResultWrapper[VectorListResponse]),
        )


class AsyncVector(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVectorWithRawResponse:
        return AsyncVectorWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVectorWithStreamingResponse:
        return AsyncVectorWithStreamingResponse(self)

    async def list(
        self,
        *,
        agg_interval: Literal["15m", "1h", "1d", "1w"] | NotGiven = NOT_GIVEN,
        date_end: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        date_range: List[
            Literal[
                "1d",
                "2d",
                "7d",
                "14d",
                "28d",
                "12w",
                "24w",
                "52w",
                "1dControl",
                "2dControl",
                "7dControl",
                "14dControl",
                "28dControl",
                "12wControl",
                "24wControl",
            ]
        ]
        | NotGiven = NOT_GIVEN,
        date_start: List[Union[str, datetime]] | NotGiven = NOT_GIVEN,
        direction: Literal["ORIGIN", "TARGET"] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        ip_version: List[Literal["IPv4", "IPv6"]] | NotGiven = NOT_GIVEN,
        limit_per_group: int | NotGiven = NOT_GIVEN,
        location: List[str] | NotGiven = NOT_GIVEN,
        name: List[str] | NotGiven = NOT_GIVEN,
        normalization: Literal["PERCENTAGE", "MIN0_MAX"] | NotGiven = NOT_GIVEN,
        protocol: List[Literal["UDP", "TCP", "ICMP", "GRE"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VectorListResponse:
        """
        Percentage distribution of attacks by vector used over time.

        Args:
          agg_interval: Aggregation interval results should be returned in (for example, in 15 minutes
              or 1 hour intervals). Refer to
              [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).

          date_end: End of the date range (inclusive).

          date_range: For example, use `7d` and `7dControl` to compare this week with the previous
              week. Use this parameter or set specific start and end dates (`dateStart` and
              `dateEnd` parameters).

          date_start: Array of datetimes to filter the start of a series.

          direction: Together with the `location` parameter, will apply the filter to origin or
              target location.

          format: Format results are returned in.

          ip_version: Filter for ip version.

          limit_per_group: Limit the number of objects (eg browsers, verticals, etc) to the top items over
              the time range.

          location: Array of comma separated list of locations (alpha-2 country codes). Start with
              `-` to exclude from results. For example, `-US,PT` excludes results from the US,
              but includes results from PT.

          name: Array of names that will be used to name the series in responses.

          normalization: Normalization method applied. Refer to
              [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).

          protocol: Array of L3/4 attack types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/attacks/layer3/timeseries_groups/vector",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "agg_interval": agg_interval,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "direction": direction,
                        "format": format,
                        "ip_version": ip_version,
                        "limit_per_group": limit_per_group,
                        "location": location,
                        "name": name,
                        "normalization": normalization,
                        "protocol": protocol,
                    },
                    vector_list_params.VectorListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[VectorListResponse], ResultWrapper[VectorListResponse]),
        )


class VectorWithRawResponse:
    def __init__(self, vector: Vector) -> None:
        self._vector = vector

        self.list = to_raw_response_wrapper(
            vector.list,
        )


class AsyncVectorWithRawResponse:
    def __init__(self, vector: AsyncVector) -> None:
        self._vector = vector

        self.list = async_to_raw_response_wrapper(
            vector.list,
        )


class VectorWithStreamingResponse:
    def __init__(self, vector: Vector) -> None:
        self._vector = vector

        self.list = to_streamed_response_wrapper(
            vector.list,
        )


class AsyncVectorWithStreamingResponse:
    def __init__(self, vector: AsyncVector) -> None:
        self._vector = vector

        self.list = async_to_streamed_response_wrapper(
            vector.list,
        )
