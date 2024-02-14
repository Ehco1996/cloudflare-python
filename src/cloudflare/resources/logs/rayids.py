# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

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
from ...types.logs import RayidGetResponse, rayid_get_params
from ..._base_client import (
    make_request_options,
)

__all__ = ["Rayids", "AsyncRayids"]


class Rayids(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RayidsWithRawResponse:
        return RayidsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RayidsWithStreamingResponse:
        return RayidsWithStreamingResponse(self)

    def get(
        self,
        ray_identifier: str,
        *,
        zone_identifier: str,
        fields: str | NotGiven = NOT_GIVEN,
        timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RayidGetResponse:
        """The `/rayids` api route allows lookups by specific rayid.

        The rayids route will
        return zero, one, or more records (ray ids are not unique).

        Args:
          zone_identifier: Identifier

          ray_identifier: Ray identifier.

          fields: The `/received` route by default returns a limited set of fields, and allows
              customers to override the default field set by specifying individual fields. The
              reasons for this are: 1. Most customers require only a small subset of fields,
              but that subset varies from customer to customer; 2. Flat schema is much easier
              to work with downstream (importing into BigTable etc); 3. Performance (time to
              process, file size). If `?fields=` is not specified, default field set is
              returned. This default field set may change at any time. When `?fields=` is
              provided, each record is returned with the specified fields. `fields` must be
              specified as a comma separated list without any whitespaces, and all fields must
              exist. The order in which fields are specified does not matter, and the order of
              fields in the response is not specified.

          timestamps: By default, timestamps in responses are returned as Unix nanosecond integers.
              The `?timestamps=` argument can be set to change the format in which response
              timestamps are returned. Possible values are: `unix`, `unixnano`, `rfc3339`.
              Note that `unix` and `unixnano` return timestamps as integers; `rfc3339` returns
              timestamps as strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not ray_identifier:
            raise ValueError(f"Expected a non-empty value for `ray_identifier` but received {ray_identifier!r}")
        return cast(
            RayidGetResponse,
            self._get(
                f"/zones/{zone_identifier}/logs/rayids/{ray_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "fields": fields,
                            "timestamps": timestamps,
                        },
                        rayid_get_params.RayidGetParams,
                    ),
                ),
                cast_to=cast(Any, RayidGetResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncRayids(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRayidsWithRawResponse:
        return AsyncRayidsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRayidsWithStreamingResponse:
        return AsyncRayidsWithStreamingResponse(self)

    async def get(
        self,
        ray_identifier: str,
        *,
        zone_identifier: str,
        fields: str | NotGiven = NOT_GIVEN,
        timestamps: Literal["unix", "unixnano", "rfc3339"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RayidGetResponse:
        """The `/rayids` api route allows lookups by specific rayid.

        The rayids route will
        return zero, one, or more records (ray ids are not unique).

        Args:
          zone_identifier: Identifier

          ray_identifier: Ray identifier.

          fields: The `/received` route by default returns a limited set of fields, and allows
              customers to override the default field set by specifying individual fields. The
              reasons for this are: 1. Most customers require only a small subset of fields,
              but that subset varies from customer to customer; 2. Flat schema is much easier
              to work with downstream (importing into BigTable etc); 3. Performance (time to
              process, file size). If `?fields=` is not specified, default field set is
              returned. This default field set may change at any time. When `?fields=` is
              provided, each record is returned with the specified fields. `fields` must be
              specified as a comma separated list without any whitespaces, and all fields must
              exist. The order in which fields are specified does not matter, and the order of
              fields in the response is not specified.

          timestamps: By default, timestamps in responses are returned as Unix nanosecond integers.
              The `?timestamps=` argument can be set to change the format in which response
              timestamps are returned. Possible values are: `unix`, `unixnano`, `rfc3339`.
              Note that `unix` and `unixnano` return timestamps as integers; `rfc3339` returns
              timestamps as strings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not ray_identifier:
            raise ValueError(f"Expected a non-empty value for `ray_identifier` but received {ray_identifier!r}")
        return cast(
            RayidGetResponse,
            await self._get(
                f"/zones/{zone_identifier}/logs/rayids/{ray_identifier}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "fields": fields,
                            "timestamps": timestamps,
                        },
                        rayid_get_params.RayidGetParams,
                    ),
                ),
                cast_to=cast(Any, RayidGetResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class RayidsWithRawResponse:
    def __init__(self, rayids: Rayids) -> None:
        self._rayids = rayids

        self.get = to_raw_response_wrapper(
            rayids.get,
        )


class AsyncRayidsWithRawResponse:
    def __init__(self, rayids: AsyncRayids) -> None:
        self._rayids = rayids

        self.get = async_to_raw_response_wrapper(
            rayids.get,
        )


class RayidsWithStreamingResponse:
    def __init__(self, rayids: Rayids) -> None:
        self._rayids = rayids

        self.get = to_streamed_response_wrapper(
            rayids.get,
        )


class AsyncRayidsWithStreamingResponse:
    def __init__(self, rayids: AsyncRayids) -> None:
        self._rayids = rayids

        self.get = async_to_streamed_response_wrapper(
            rayids.get,
        )
