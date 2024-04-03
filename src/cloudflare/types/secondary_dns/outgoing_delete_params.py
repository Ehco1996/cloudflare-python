# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OutgoingDeleteParams"]


class OutgoingDeleteParams(TypedDict, total=False):
    zone_id: Required[str]

    body: Required[object]
