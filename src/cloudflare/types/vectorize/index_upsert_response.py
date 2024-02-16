# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["IndexUpsertResponse"]


class IndexUpsertResponse(BaseModel):
    count: Optional[int] = None
    """Specifies the count of the vectors successfully inserted."""

    ids: Optional[List[str]] = None
    """Array of vector identifiers of the vectors successfully inserted."""
