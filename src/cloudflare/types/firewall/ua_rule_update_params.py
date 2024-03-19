# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["UARuleUpdateParams"]


class UARuleUpdateParams(TypedDict, total=False):
    zone_identifier: Required[str]
    """Identifier"""

    body: Required[object]
