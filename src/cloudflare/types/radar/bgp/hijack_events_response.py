# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["HijackEventsResponse", "AsnInfo", "Event", "EventTag"]


class AsnInfo(BaseModel):
    asn: int

    country_code: str

    org_name: str


class EventTag(BaseModel):
    name: str

    score: int


class Event(BaseModel):
    id: int

    confidence_score: int

    duration: int

    event_type: int

    hijack_msgs_count: int

    hijacker_asn: int

    hijacker_country: str

    is_stale: bool

    max_hijack_ts: str

    max_msg_ts: str

    min_hijack_ts: str

    on_going_count: int

    peer_asns: List[int]

    peer_ip_count: int

    prefixes: List[str]

    tags: List[EventTag]

    victim_asns: List[int]

    victim_countries: List[str]


class HijackEventsResponse(BaseModel):
    asn_info: List[AsnInfo]

    events: List[Event]

    total_monitors: int
