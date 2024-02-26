# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["MonitorReferencesResponse", "MonitorReferencesResponseItem"]


class MonitorReferencesResponseItem(BaseModel):
    reference_type: Optional[Literal["*", "referral", "referrer"]] = None

    resource_id: Optional[str] = None

    resource_name: Optional[str] = None

    resource_type: Optional[str] = None


MonitorReferencesResponse = List[MonitorReferencesResponseItem]
