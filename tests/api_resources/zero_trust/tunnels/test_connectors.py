# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.tunnels import TunnelTunnelClient

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConnectors:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        connector = client.zero_trust.tunnels.connectors.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(TunnelTunnelClient, connector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.tunnels.connectors.with_raw_response.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = response.parse()
        assert_matches_type(TunnelTunnelClient, connector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.tunnels.connectors.with_streaming_response.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = response.parse()
            assert_matches_type(TunnelTunnelClient, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.tunnels.connectors.with_raw_response.get(
                "1bedc50d-42b3-473c-b108-ff3d10c0d925",
                account_id="",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            client.zero_trust.tunnels.connectors.with_raw_response.get(
                "1bedc50d-42b3-473c-b108-ff3d10c0d925",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            client.zero_trust.tunnels.connectors.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )


class TestAsyncConnectors:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        connector = await async_client.zero_trust.tunnels.connectors.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(TunnelTunnelClient, connector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.tunnels.connectors.with_raw_response.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        connector = await response.parse()
        assert_matches_type(TunnelTunnelClient, connector, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.tunnels.connectors.with_streaming_response.get(
            "1bedc50d-42b3-473c-b108-ff3d10c0d925",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            connector = await response.parse()
            assert_matches_type(TunnelTunnelClient, connector, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.tunnels.connectors.with_raw_response.get(
                "1bedc50d-42b3-473c-b108-ff3d10c0d925",
                account_id="",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_id` but received ''"):
            await async_client.zero_trust.tunnels.connectors.with_raw_response.get(
                "1bedc50d-42b3-473c-b108-ff3d10c0d925",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `connector_id` but received ''"):
            await async_client.zero_trust.tunnels.connectors.with_raw_response.get(
                "",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )
