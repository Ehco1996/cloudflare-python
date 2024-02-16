# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ...._compat import cached_property

from ....types.load_balancers.pools import ReferenceListResponse

from typing import Type, Optional

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
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast

__all__ = ["References", "AsyncReferences"]


class References(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReferencesWithRawResponse:
        return ReferencesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReferencesWithStreamingResponse:
        return ReferencesWithStreamingResponse(self)

    def list(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceListResponse]:
        """
        Get the list of resources that reference the provided pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReferenceListResponse]], ResultWrapper[ReferenceListResponse]),
        )


class AsyncReferences(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReferencesWithRawResponse:
        return AsyncReferencesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReferencesWithStreamingResponse:
        return AsyncReferencesWithStreamingResponse(self)

    async def list(
        self,
        pool_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ReferenceListResponse]:
        """
        Get the list of resources that reference the provided pool.

        Args:
          account_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not pool_id:
            raise ValueError(f"Expected a non-empty value for `pool_id` but received {pool_id!r}")
        return await self._get(
            f"/accounts/{account_id}/load_balancers/pools/{pool_id}/references",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[ReferenceListResponse]], ResultWrapper[ReferenceListResponse]),
        )


class ReferencesWithRawResponse:
    def __init__(self, references: References) -> None:
        self._references = references

        self.list = to_raw_response_wrapper(
            references.list,
        )


class AsyncReferencesWithRawResponse:
    def __init__(self, references: AsyncReferences) -> None:
        self._references = references

        self.list = async_to_raw_response_wrapper(
            references.list,
        )


class ReferencesWithStreamingResponse:
    def __init__(self, references: References) -> None:
        self._references = references

        self.list = to_streamed_response_wrapper(
            references.list,
        )


class AsyncReferencesWithStreamingResponse:
    def __init__(self, references: AsyncReferences) -> None:
        self._references = references

        self.list = async_to_streamed_response_wrapper(
            references.list,
        )
