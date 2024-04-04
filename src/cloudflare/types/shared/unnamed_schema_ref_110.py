# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.



from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef110"]


class UnnamedSchemaRef110(BaseModel):
    search_engine_crawler_bypass: bool
    """
    Whether to allow verified search engine crawlers to bypass all waiting rooms on
    this zone. Verified search engine crawlers will not be tracked or counted by the
    waiting room system, and will not appear in waiting room analytics.
    """
