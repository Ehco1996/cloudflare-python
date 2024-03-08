# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["D1QueryResult", "Meta"]


class Meta(BaseModel):
    changed_db: Optional[bool] = None

    changes: Optional[float] = None

    duration: Optional[float] = None

    last_row_id: Optional[float] = None

    rows_read: Optional[float] = None

    rows_written: Optional[float] = None

    size_after: Optional[float] = None


class D1QueryResult(BaseModel):
    meta: Optional[Meta] = None

    results: Optional[List[object]] = None

    success: Optional[bool] = None
