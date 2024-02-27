# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar.dns import TopAsesResponse, TopLocationsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ases(self, client: Cloudflare) -> None:
        top = client.radar.dns.top.ases(
            domain=["string", "string", "string"],
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ases_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.dns.top.ases(
            domain=["string", "string", "string"],
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ases(self, client: Cloudflare) -> None:
        response = client.radar.dns.top.with_raw_response.ases(
            domain=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ases(self, client: Cloudflare) -> None:
        with client.radar.dns.top.with_streaming_response.ases(
            domain=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopAsesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_locations(self, client: Cloudflare) -> None:
        top = client.radar.dns.top.locations(
            domain=["string", "string", "string"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_locations_with_all_params(self, client: Cloudflare) -> None:
        top = client.radar.dns.top.locations(
            domain=["string", "string", "string"],
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_locations(self, client: Cloudflare) -> None:
        response = client.radar.dns.top.with_raw_response.locations(
            domain=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = response.parse()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_locations(self, client: Cloudflare) -> None:
        with client.radar.dns.top.with_streaming_response.locations(
            domain=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = response.parse()
            assert_matches_type(TopLocationsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ases(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.dns.top.ases(
            domain=["string", "string", "string"],
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ases_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.dns.top.ases(
            domain=["string", "string", "string"],
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ases(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.top.with_raw_response.ases(
            domain=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopAsesResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ases(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.top.with_streaming_response.ases(
            domain=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopAsesResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_locations(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.dns.top.locations(
            domain=["string", "string", "string"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_locations_with_all_params(self, async_client: AsyncCloudflare) -> None:
        top = await async_client.radar.dns.top.locations(
            domain=["string", "string", "string"],
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            limit=5,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_locations(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.dns.top.with_raw_response.locations(
            domain=["string", "string", "string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        top = await response.parse()
        assert_matches_type(TopLocationsResponse, top, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_locations(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.dns.top.with_streaming_response.locations(
            domain=["string", "string", "string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            top = await response.parse()
            assert_matches_type(TopLocationsResponse, top, path=["response"])

        assert cast(Any, response.is_closed) is True
