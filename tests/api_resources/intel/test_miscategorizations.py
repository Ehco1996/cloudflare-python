# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.intel import MiscategorizationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMiscategorizations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        miscategorization = client.intel.miscategorizations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        miscategorization = client.intel.miscategorizations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            content_adds=[82],
            content_removes=[155],
            indicator_type="domain",
            ip={},
            security_adds=[117, 131],
            security_removes=[83],
            url="string",
        )
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.intel.miscategorizations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        miscategorization = response.parse()
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.intel.miscategorizations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            miscategorization = response.parse()
            assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.intel.miscategorizations.with_raw_response.create(
                account_id="",
            )


class TestAsyncMiscategorizations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        miscategorization = await async_client.intel.miscategorizations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        miscategorization = await async_client.intel.miscategorizations.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            content_adds=[82],
            content_removes=[155],
            indicator_type="domain",
            ip={},
            security_adds=[117, 131],
            security_removes=[83],
            url="string",
        )
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.intel.miscategorizations.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        miscategorization = await response.parse()
        assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.intel.miscategorizations.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            miscategorization = await response.parse()
            assert_matches_type(MiscategorizationCreateResponse, miscategorization, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.intel.miscategorizations.with_raw_response.create(
                account_id="",
            )
