# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .locations import Locations, AsyncLocations

from ...._compat import cached_property

from ....types.radar import TrafficAnomalyListResponse

from typing import Type, Union

from datetime import datetime

from typing_extensions import Literal

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from ....types.radar import traffic_anomaly_list_params
from .locations import (
    Locations,
    AsyncLocations,
    LocationsWithRawResponse,
    AsyncLocationsWithRawResponse,
    LocationsWithStreamingResponse,
    AsyncLocationsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["TrafficAnomalies", "AsyncTrafficAnomalies"]


class TrafficAnomalies(SyncAPIResource):
    @cached_property
    def locations(self) -> Locations:
        return Locations(self._client)

    @cached_property
    def with_raw_response(self) -> TrafficAnomaliesWithRawResponse:
        return TrafficAnomaliesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrafficAnomaliesWithStreamingResponse:
        return TrafficAnomaliesWithStreamingResponse(self)

    def list(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: Literal[
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
        | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficAnomalyListResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the latest alerts.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/radar/traffic_anomalies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                        "status": status,
                    },
                    traffic_anomaly_list_params.TrafficAnomalyListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TrafficAnomalyListResponse], ResultWrapper[TrafficAnomalyListResponse]),
        )


class AsyncTrafficAnomalies(AsyncAPIResource):
    @cached_property
    def locations(self) -> AsyncLocations:
        return AsyncLocations(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTrafficAnomaliesWithRawResponse:
        return AsyncTrafficAnomaliesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrafficAnomaliesWithStreamingResponse:
        return AsyncTrafficAnomaliesWithStreamingResponse(self)

    async def list(
        self,
        *,
        asn: int | NotGiven = NOT_GIVEN,
        date_end: Union[str, datetime] | NotGiven = NOT_GIVEN,
        date_range: Literal[
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
        | NotGiven = NOT_GIVEN,
        date_start: Union[str, datetime] | NotGiven = NOT_GIVEN,
        format: Literal["JSON", "CSV"] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        status: Literal["VERIFIED", "UNVERIFIED"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrafficAnomalyListResponse:
        """
        Internet traffic anomalies are signals that might point to an outage, These
        alerts are automatically detected by Radar and then manually verified by our
        team. This endpoint returns the latest alerts.

        Args:
          asn: Single ASN as integer.

          date_end: End of the date range (inclusive).

          date_range: Shorthand date ranges for the last X days - use when you don't need specific
              start and end dates.

          date_start: Start of the date range (inclusive).

          format: Format results are returned in.

          limit: Limit the number of objects in the response.

          location: Location Alpha2 code.

          offset: Number of objects to skip before grabbing results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/radar/traffic_anomalies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "asn": asn,
                        "date_end": date_end,
                        "date_range": date_range,
                        "date_start": date_start,
                        "format": format,
                        "limit": limit,
                        "location": location,
                        "offset": offset,
                        "status": status,
                    },
                    traffic_anomaly_list_params.TrafficAnomalyListParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[TrafficAnomalyListResponse], ResultWrapper[TrafficAnomalyListResponse]),
        )


class TrafficAnomaliesWithRawResponse:
    def __init__(self, traffic_anomalies: TrafficAnomalies) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.list = to_raw_response_wrapper(
            traffic_anomalies.list,
        )

    @cached_property
    def locations(self) -> LocationsWithRawResponse:
        return LocationsWithRawResponse(self._traffic_anomalies.locations)


class AsyncTrafficAnomaliesWithRawResponse:
    def __init__(self, traffic_anomalies: AsyncTrafficAnomalies) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.list = async_to_raw_response_wrapper(
            traffic_anomalies.list,
        )

    @cached_property
    def locations(self) -> AsyncLocationsWithRawResponse:
        return AsyncLocationsWithRawResponse(self._traffic_anomalies.locations)


class TrafficAnomaliesWithStreamingResponse:
    def __init__(self, traffic_anomalies: TrafficAnomalies) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.list = to_streamed_response_wrapper(
            traffic_anomalies.list,
        )

    @cached_property
    def locations(self) -> LocationsWithStreamingResponse:
        return LocationsWithStreamingResponse(self._traffic_anomalies.locations)


class AsyncTrafficAnomaliesWithStreamingResponse:
    def __init__(self, traffic_anomalies: AsyncTrafficAnomalies) -> None:
        self._traffic_anomalies = traffic_anomalies

        self.list = async_to_streamed_response_wrapper(
            traffic_anomalies.list,
        )

    @cached_property
    def locations(self) -> AsyncLocationsWithStreamingResponse:
        return AsyncLocationsWithStreamingResponse(self._traffic_anomalies.locations)
