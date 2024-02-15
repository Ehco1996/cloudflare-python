# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["SettingUpdateResponse"]


class SettingUpdateResponse(BaseModel):
    enabled: Optional[bool] = None
    """
    Disabling Universal SSL removes any currently active Universal SSL certificates
    for your zone from the edge and prevents any future Universal SSL certificates
    from being ordered. If there are no advanced certificates or custom certificates
    uploaded for the domain, visitors will be unable to access the domain over
    HTTPS.

    By disabling Universal SSL, you understand that the following Cloudflare
    settings and preferences will result in visitors being unable to visit your
    domain unless you have uploaded a custom certificate or purchased an advanced
    certificate.

    - HSTS
    - Always Use HTTPS
    - Opportunistic Encryption
    - Onion Routing
    - Any Page Rules redirecting traffic to HTTPS

    Similarly, any HTTP redirect to HTTPS at the origin while the Cloudflare proxy
    is enabled will result in users being unable to visit your site without a valid
    certificate at Cloudflare's edge.

    If you do not have a valid custom or advanced certificate at Cloudflare's edge
    and are unsure if any of the above Cloudflare settings are enabled, or if any
    HTTP redirects exist at your origin, we advise leaving Universal SSL enabled for
    your domain.
    """
