# File generated from our OpenAPI spec by Stainless.

from typing import List
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["AseListResponse", "Meta", "MetaDateRange", "Top0"]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")


class Top0(BaseModel):
    asn: int

    as_name: str = FieldInfo(alias="ASName")

    value: str
    """
    Percentage of updates by this AS out of the total updates by all autonomous
    systems.
    """


class AseListResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
