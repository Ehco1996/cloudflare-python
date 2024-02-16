# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["WebhookStreamWebhookCreateWebhooksParams"]


class WebhookStreamWebhookCreateWebhooksParams(TypedDict, total=False):
    notification_url: Required[Annotated[str, PropertyInfo(alias="notificationUrl")]]
    """The URL where webhooks will be sent."""
