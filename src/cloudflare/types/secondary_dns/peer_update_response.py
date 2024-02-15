# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["PeerUpdateResponse"]


class PeerUpdateResponse(BaseModel):
    id: object

    name: str
    """The name of the peer."""

    ip: Optional[str] = None
    """
    IPv4/IPv6 address of primary or secondary nameserver, depending on what zone
    this peer is linked to. For primary zones this IP defines the IP of the
    secondary nameserver Cloudflare will NOTIFY upon zone changes. For secondary
    zones this IP defines the IP of the primary nameserver Cloudflare will send
    AXFR/IXFR requests to.
    """

    ixfr_enable: Optional[bool] = None
    """Enable IXFR transfer protocol, default is AXFR.

    Only applicable to secondary zones.
    """

    port: Optional[float] = None
    """
    DNS port of primary or secondary nameserver, depending on what zone this peer is
    linked to.
    """

    tsig_id: Optional[str] = None
    """TSIG authentication will be used for zone transfer if configured."""
