# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PseudoIPV4EditParams"]


class PseudoIPV4EditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    value: Required[Literal["off", "add_header", "overwrite_header"]]
    """Value of the Pseudo IPv4 setting."""
