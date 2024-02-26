# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["OutgoingUpdateParams"]


class OutgoingUpdateParams(TypedDict, total=False):
    name: Required[str]
    """Zone name."""

    peers: Required[Iterable[object]]
    """A list of peer tags."""
