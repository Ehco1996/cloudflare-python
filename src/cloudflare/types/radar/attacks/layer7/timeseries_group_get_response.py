# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ....unnamed_schema_ref_174 import UnnamedSchemaRef174
from ....unnamed_schema_ref_175 import UnnamedSchemaRef175

__all__ = ["TimeseriesGroupGetResponse", "Meta", "MetaConfidenceInfo", "Serie0"]


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[UnnamedSchemaRef174]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[UnnamedSchemaRef175] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Serie0(BaseModel):
    access_rules: List[str] = FieldInfo(alias="ACCESS_RULES")

    api_shield: List[str] = FieldInfo(alias="API_SHIELD")

    bot_management: List[str] = FieldInfo(alias="BOT_MANAGEMENT")

    data_loss_prevention: List[str] = FieldInfo(alias="DATA_LOSS_PREVENTION")

    ddos: List[str] = FieldInfo(alias="DDOS")

    ip_reputation: List[str] = FieldInfo(alias="IP_REPUTATION")

    timestamps: List[datetime]

    waf: List[str] = FieldInfo(alias="WAF")


class TimeseriesGroupGetResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
