# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit import (
    IPSECTunnelGetResponse,
    IPSECTunnelListResponse,
    IPSECTunnelCreateResponse,
    IPSECTunnelDeleteResponse,
    IPSECTunnelUpdateResponse,
    IPSECTunnelPSKGenerateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIPSECTunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.create(
                "",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_psk_generate(self, client: Cloudflare) -> None:
        ipsec_tunnel = client.magic_transit.ipsec_tunnels.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_psk_generate(self, client: Cloudflare) -> None:
        response = client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = response.parse()
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_psk_generate(self, client: Cloudflare) -> None:
        with client.magic_transit.ipsec_tunnels.with_streaming_response.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = response.parse()
            assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_psk_generate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncIPSECTunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.create(
            "023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelCreateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.create(
                "",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
            customer_endpoint="203.0.113.1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            psk="O3bwKSjnaoCxDoUxjcq4Rk8ZKkezQUiy",
            replay_protection=False,
        )
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="IPsec_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelUpdateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.update(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="IPsec_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelListResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.list(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelDeleteResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.delete(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelGetResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.get(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_psk_generate(self, async_client: AsyncCloudflare) -> None:
        ipsec_tunnel = await async_client.magic_transit.ipsec_tunnels.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_psk_generate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ipsec_tunnel = await response.parse()
        assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_psk_generate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.ipsec_tunnels.with_streaming_response.psk_generate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ipsec_tunnel = await response.parse()
            assert_matches_type(IPSECTunnelPSKGenerateResponse, ipsec_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_psk_generate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.ipsec_tunnels.with_raw_response.psk_generate(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
