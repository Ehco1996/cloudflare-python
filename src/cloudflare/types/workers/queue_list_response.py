# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["QueueListResponse", "QueueListResponseItem"]


class QueueListResponseItem(BaseModel):
    consumers: Optional[object] = None

    consumers_total_count: Optional[object] = None

    created_on: Optional[object] = None

    modified_on: Optional[object] = None

    producers: Optional[object] = None

    producers_total_count: Optional[object] = None

    queue_id: Optional[object] = None

    queue_name: Optional[str] = None


QueueListResponse = List[QueueListResponseItem]
