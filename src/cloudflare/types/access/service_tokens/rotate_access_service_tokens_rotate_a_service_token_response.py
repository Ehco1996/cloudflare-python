# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["RotateAccessServiceTokensRotateAServiceTokenResponse"]


class RotateAccessServiceTokensRotateAServiceTokenResponse(BaseModel):
    id: Optional[object] = None
    """The ID of the service token."""

    client_id: Optional[str] = None
    """The Client ID for the service token.

    Access will check for this value in the `CF-Access-Client-ID` request header.
    """

    client_secret: Optional[str] = None
    """The Client Secret for the service token.

    Access will check for this value in the `CF-Access-Client-Secret` request
    header.
    """

    created_at: Optional[datetime] = None

    duration: Optional[str] = None
    """The duration for how long the service token will be valid.

    Must be in the format `300ms` or `2h45m`. Valid time units are: ns, us (or µs),
    ms, s, m, h. The default is 1 year in hours (8760h).
    """

    name: Optional[str] = None
    """The name of the service token."""

    updated_at: Optional[datetime] = None
