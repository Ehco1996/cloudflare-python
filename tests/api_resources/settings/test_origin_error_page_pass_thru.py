# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.settings import (
    OriginErrorPagePassThruGetResponse,
    OriginErrorPagePassThruEditResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginErrorPagePassThru:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        origin_error_page_pass_thru = client.settings.origin_error_page_pass_thru.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.settings.origin_error_page_pass_thru.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_error_page_pass_thru = response.parse()
        assert_matches_type(
            Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.settings.origin_error_page_pass_thru.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_error_page_pass_thru = response.parse()
            assert_matches_type(
                Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.origin_error_page_pass_thru.with_raw_response.edit(
                "",
                value="on",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        origin_error_page_pass_thru = client.settings.origin_error_page_pass_thru.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.settings.origin_error_page_pass_thru.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_error_page_pass_thru = response.parse()
        assert_matches_type(
            Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.settings.origin_error_page_pass_thru.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_error_page_pass_thru = response.parse()
            assert_matches_type(
                Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.settings.origin_error_page_pass_thru.with_raw_response.get(
                "",
            )


class TestAsyncOriginErrorPagePassThru:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        origin_error_page_pass_thru = await async_client.settings.origin_error_page_pass_thru.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )
        assert_matches_type(
            Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.origin_error_page_pass_thru.with_raw_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_error_page_pass_thru = await response.parse()
        assert_matches_type(
            Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.origin_error_page_pass_thru.with_streaming_response.edit(
            "023e105f4ecef8ad9ca31a8372d0c353",
            value="on",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_error_page_pass_thru = await response.parse()
            assert_matches_type(
                Optional[OriginErrorPagePassThruEditResponse], origin_error_page_pass_thru, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.origin_error_page_pass_thru.with_raw_response.edit(
                "",
                value="on",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        origin_error_page_pass_thru = await async_client.settings.origin_error_page_pass_thru.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.settings.origin_error_page_pass_thru.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_error_page_pass_thru = await response.parse()
        assert_matches_type(
            Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.settings.origin_error_page_pass_thru.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_error_page_pass_thru = await response.parse()
            assert_matches_type(
                Optional[OriginErrorPagePassThruGetResponse], origin_error_page_pass_thru, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.settings.origin_error_page_pass_thru.with_raw_response.get(
                "",
            )
