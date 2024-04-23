# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_transit.gre_tunnel_get_response import GRETunnelGetResponse
from cloudflare.types.magic_transit.gre_tunnel_list_response import GRETunnelListResponse
from cloudflare.types.magic_transit.gre_tunnel_create_response import GRETunnelCreateResponse
from cloudflare.types.magic_transit.gre_tunnel_delete_response import GRETunnelDeleteResponse
from cloudflare.types.magic_transit.gre_tunnel_update_response import GRETunnelUpdateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGRETunnels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.magic_transit.gre_tunnels.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.magic_transit.gre_tunnels.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.create(
                account_id="",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            mtu=0,
            ttl=0,
        )
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.magic_transit.gre_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.magic_transit.gre_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.magic_transit.gre_tunnels.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.magic_transit.gre_tunnels.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.magic_transit.gre_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.magic_transit.gre_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        gre_tunnel = client.magic_transit.gre_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.magic_transit.gre_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = response.parse()
        assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.magic_transit.gre_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = response.parse()
            assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            client.magic_transit.gre_tunnels.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncGRETunnels:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.gre_tunnels.with_raw_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.gre_tunnels.with_streaming_response.create(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GRETunnelCreateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.create(
                account_id="",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
            description="Tunnel for ISP X",
            health_check={
                "direction": "bidirectional",
                "enabled": True,
                "rate": "low",
                "target": "203.0.113.1",
                "type": "request",
            },
            mtu=0,
            ttl=0,
        )
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.gre_tunnels.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.gre_tunnels.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cloudflare_gre_endpoint="203.0.113.1",
            customer_gre_endpoint="203.0.113.1",
            interface_address="192.0.2.0/31",
            name="GRE_1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GRETunnelUpdateResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                cloudflare_gre_endpoint="203.0.113.1",
                customer_gre_endpoint="203.0.113.1",
                interface_address="192.0.2.0/31",
                name="GRE_1",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.gre_tunnels.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.gre_tunnels.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GRETunnelListResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.list(
                account_id="",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )
        assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.gre_tunnels.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.gre_tunnels.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GRETunnelDeleteResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        gre_tunnel = await async_client.magic_transit.gre_tunnels.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_transit.gre_tunnels.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gre_tunnel = await response.parse()
        assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_transit.gre_tunnels.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gre_tunnel = await response.parse()
            assert_matches_type(GRETunnelGetResponse, gre_tunnel, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `tunnel_identifier` but received ''"):
            await async_client.magic_transit.gre_tunnels.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
