# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["PeerUpdateParams"]


class PeerUpdateParams(TypedDict, total=False):
    account_identifier: Required[object]

    name: Required[str]
    """The name of the peer."""

    ip: str
    """
    IPv4/IPv6 address of primary or secondary nameserver, depending on what zone
    this peer is linked to. For primary zones this IP defines the IP of the
    secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary
    zones this IP defines the IP of the primary nameserver Cloudflare will send
    AXFR/IXFR requests to.
    """

    ixfr_enable: bool
    """Enable IXFR transfer protocol, default is AXFR.

    Only applicable to secondary zones.
    """

    port: float
    """
    DNS port of primary or secondary nameserver, depending on what zone this peer is
    linked to.
    """

    tsig_id: str
    """TSIG authentication will be used for zone transfer if configured."""
