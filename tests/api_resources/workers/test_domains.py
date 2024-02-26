# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.workers import (
    DomainGetResponse,
    DomainListResponse,
    DomainUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDomains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        domain = client.workers.domains.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        domain = client.workers.domains.list(
            "9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        domain = client.workers.domains.list(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
            zone_name="example.com",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.list(
            "9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.list(
            "9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        domain = client.workers.domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        domain = client.workers.domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.workers.domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.workers.domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDomains:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainUpdateResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.update(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainUpdateResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.list(
            "9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.list(
            "9a7806061c88ada191ed06f989cc3dac",
            environment="production",
            hostname="foo.example.com",
            service="foo",
            zone_id="593c9c94de529bbbfaac7c53ced0447d",
            zone_name="example.com",
        )
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.list(
            "9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainListResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.list(
            "9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainListResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert domain is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.delete(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert domain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        domain = await async_client.workers.domains.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.domains.with_raw_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        domain = await response.parse()
        assert_matches_type(DomainGetResponse, domain, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.domains.with_streaming_response.get(
            "dbe10b4bc17c295377eabd600e1787fd",
            account_id="9a7806061c88ada191ed06f989cc3dac",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            domain = await response.parse()
            assert_matches_type(DomainGetResponse, domain, path=["response"])

        assert cast(Any, response.is_closed) is True
