# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CfdTunnelDeleteParams"]


class CfdTunnelDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    body: Required[object]
