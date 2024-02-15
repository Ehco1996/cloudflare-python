# File generated from our OpenAPI spec by Stainless.

from typing import List

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["LocationListResponse", "Top0"]


class Top0(BaseModel):
    client_country_alpha2: str = FieldInfo(alias="clientCountryAlpha2")

    client_country_name: str = FieldInfo(alias="clientCountryName")

    value: str


class LocationListResponse(BaseModel):
    top_0: List[Top0]
