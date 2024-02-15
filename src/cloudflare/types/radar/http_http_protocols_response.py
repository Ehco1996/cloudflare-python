# File generated from our OpenAPI spec by Stainless.

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["HTTPHTTPProtocolsResponse", "Serie0"]


class Serie0(BaseModel):
    http: List[str]

    https: List[str]

    timestamps: List[str]


class HTTPHTTPProtocolsResponse(BaseModel):
    meta: object

    serie_0: Serie0
