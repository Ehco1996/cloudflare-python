# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CaptionListResponse", "CaptionListResponseItem"]


class CaptionListResponseItem(BaseModel):
    label: Optional[str] = None
    """The language label displayed in the native language to users."""

    language: Optional[str] = None
    """The language tag in BCP 47 format."""


CaptionListResponse = List[CaptionListResponseItem]
