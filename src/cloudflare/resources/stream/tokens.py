# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Iterable, cast

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
from ...types.stream import (
    TokenStreamVideosCreateSignedURLTokensForVideosResponse,
    token_stream_videos_create_signed_url_tokens_for_videos_params,
)

__all__ = ["Tokens", "AsyncTokens"]


class Tokens(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TokensWithRawResponse:
        return TokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TokensWithStreamingResponse:
        return TokensWithStreamingResponse(self)

    def stream_videos_create_signed_url_tokens_for_videos(
        self,
        identifier: str,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        access_rules: Iterable[token_stream_videos_create_signed_url_tokens_for_videos_params.AccessRule]
        | NotGiven = NOT_GIVEN,
        downloadable: bool | NotGiven = NOT_GIVEN,
        exp: int | NotGiven = NOT_GIVEN,
        nbf: int | NotGiven = NOT_GIVEN,
        pem: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenStreamVideosCreateSignedURLTokensForVideosResponse:
        """Creates a signed URL token for a video.

        If a body is not provided in the
        request, a token is created with default values.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          id: The optional ID of a Stream signing key. If present, the `pem` field is also
              required.

          access_rules: The optional list of access rule constraints on the token. Access can be blocked
              or allowed based on an IP, IP range, or by country. Access rules are evaluated
              from first to last. If a rule matches, the associated action is applied and no
              further rules are evaluated.

          downloadable: The optional boolean value that enables using signed tokens to access MP4
              download links for a video.

          exp: The optional unix epoch timestamp that specficies the time after a token is not
              accepted. The maximum time specification is 24 hours from issuing time. If this
              field is not set, the default is one hour after issuing.

          nbf: The optional unix epoch timestamp that specifies the time before a the token is
              not accepted. If this field is not set, the default is one hour before issuing.

          pem: The optional base64 encoded private key in PEM format associated with a Stream
              signing key. If present, the `id` field is also required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return self._post(
            f"/accounts/{account_id}/stream/{identifier}/token",
            body=maybe_transform(
                {
                    "id": id,
                    "access_rules": access_rules,
                    "downloadable": downloadable,
                    "exp": exp,
                    "nbf": nbf,
                    "pem": pem,
                },
                token_stream_videos_create_signed_url_tokens_for_videos_params.TokenStreamVideosCreateSignedURLTokensForVideosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TokenStreamVideosCreateSignedURLTokensForVideosResponse],
                ResultWrapper[TokenStreamVideosCreateSignedURLTokensForVideosResponse],
            ),
        )


class AsyncTokens(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTokensWithRawResponse:
        return AsyncTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTokensWithStreamingResponse:
        return AsyncTokensWithStreamingResponse(self)

    async def stream_videos_create_signed_url_tokens_for_videos(
        self,
        identifier: str,
        *,
        account_id: str,
        id: str | NotGiven = NOT_GIVEN,
        access_rules: Iterable[token_stream_videos_create_signed_url_tokens_for_videos_params.AccessRule]
        | NotGiven = NOT_GIVEN,
        downloadable: bool | NotGiven = NOT_GIVEN,
        exp: int | NotGiven = NOT_GIVEN,
        nbf: int | NotGiven = NOT_GIVEN,
        pem: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TokenStreamVideosCreateSignedURLTokensForVideosResponse:
        """Creates a signed URL token for a video.

        If a body is not provided in the
        request, a token is created with default values.

        Args:
          account_id: The account identifier tag.

          identifier: A Cloudflare-generated unique identifier for a media item.

          id: The optional ID of a Stream signing key. If present, the `pem` field is also
              required.

          access_rules: The optional list of access rule constraints on the token. Access can be blocked
              or allowed based on an IP, IP range, or by country. Access rules are evaluated
              from first to last. If a rule matches, the associated action is applied and no
              further rules are evaluated.

          downloadable: The optional boolean value that enables using signed tokens to access MP4
              download links for a video.

          exp: The optional unix epoch timestamp that specficies the time after a token is not
              accepted. The maximum time specification is 24 hours from issuing time. If this
              field is not set, the default is one hour after issuing.

          nbf: The optional unix epoch timestamp that specifies the time before a the token is
              not accepted. If this field is not set, the default is one hour before issuing.

          pem: The optional base64 encoded private key in PEM format associated with a Stream
              signing key. If present, the `id` field is also required.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identifier:
            raise ValueError(f"Expected a non-empty value for `identifier` but received {identifier!r}")
        return await self._post(
            f"/accounts/{account_id}/stream/{identifier}/token",
            body=maybe_transform(
                {
                    "id": id,
                    "access_rules": access_rules,
                    "downloadable": downloadable,
                    "exp": exp,
                    "nbf": nbf,
                    "pem": pem,
                },
                token_stream_videos_create_signed_url_tokens_for_videos_params.TokenStreamVideosCreateSignedURLTokensForVideosParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[TokenStreamVideosCreateSignedURLTokensForVideosResponse],
                ResultWrapper[TokenStreamVideosCreateSignedURLTokensForVideosResponse],
            ),
        )


class TokensWithRawResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.stream_videos_create_signed_url_tokens_for_videos = to_raw_response_wrapper(
            tokens.stream_videos_create_signed_url_tokens_for_videos,
        )


class AsyncTokensWithRawResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.stream_videos_create_signed_url_tokens_for_videos = async_to_raw_response_wrapper(
            tokens.stream_videos_create_signed_url_tokens_for_videos,
        )


class TokensWithStreamingResponse:
    def __init__(self, tokens: Tokens) -> None:
        self._tokens = tokens

        self.stream_videos_create_signed_url_tokens_for_videos = to_streamed_response_wrapper(
            tokens.stream_videos_create_signed_url_tokens_for_videos,
        )


class AsyncTokensWithStreamingResponse:
    def __init__(self, tokens: AsyncTokens) -> None:
        self._tokens = tokens

        self.stream_videos_create_signed_url_tokens_for_videos = async_to_streamed_response_wrapper(
            tokens.stream_videos_create_signed_url_tokens_for_videos,
        )
