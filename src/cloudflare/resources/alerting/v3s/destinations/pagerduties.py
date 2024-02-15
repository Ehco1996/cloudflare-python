# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ....._compat import cached_property

from .....types.alerting.v3s.destinations import (
    PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse,
)

from typing import Type, Optional

from ....._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from ....._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["Pagerduties", "AsyncPagerduties"]


class Pagerduties(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagerdutiesWithRawResponse:
        return PagerdutiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagerdutiesWithStreamingResponse:
        return PagerdutiesWithStreamingResponse(self)

    def notification_destinations_with_pager_duty_list_pager_duty_services(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse]:
        """
        Get a list of all configured PagerDuty services.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse]],
                ResultWrapper[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            ),
        )


class AsyncPagerduties(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagerdutiesWithRawResponse:
        return AsyncPagerdutiesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagerdutiesWithStreamingResponse:
        return AsyncPagerdutiesWithStreamingResponse(self)

    async def notification_destinations_with_pager_duty_list_pager_duty_services(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse]:
        """
        Get a list of all configured PagerDuty services.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse]],
                ResultWrapper[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            ),
        )


class PagerdutiesWithRawResponse:
    def __init__(self, pagerduties: Pagerduties) -> None:
        self._pagerduties = pagerduties

        self.notification_destinations_with_pager_duty_list_pager_duty_services = to_raw_response_wrapper(
            pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services,
        )


class AsyncPagerdutiesWithRawResponse:
    def __init__(self, pagerduties: AsyncPagerduties) -> None:
        self._pagerduties = pagerduties

        self.notification_destinations_with_pager_duty_list_pager_duty_services = async_to_raw_response_wrapper(
            pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services,
        )


class PagerdutiesWithStreamingResponse:
    def __init__(self, pagerduties: Pagerduties) -> None:
        self._pagerduties = pagerduties

        self.notification_destinations_with_pager_duty_list_pager_duty_services = to_streamed_response_wrapper(
            pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services,
        )


class AsyncPagerdutiesWithStreamingResponse:
    def __init__(self, pagerduties: AsyncPagerduties) -> None:
        self._pagerduties = pagerduties

        self.notification_destinations_with_pager_duty_list_pager_duty_services = async_to_streamed_response_wrapper(
            pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services,
        )
