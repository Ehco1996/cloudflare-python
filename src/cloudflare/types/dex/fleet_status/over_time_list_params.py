# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OverTimeListParams"]


class OverTimeListParams(TypedDict, total=False):
    time_end: Required[str]
    """Timestamp in ISO format"""

    time_start: Required[str]
    """Timestamp in ISO format"""

    colo: str
    """Cloudflare colo"""

    device_id: str
    """Device-specific ID, given as UUID v4"""
