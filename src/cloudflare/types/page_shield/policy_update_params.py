# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["PolicyUpdateParams"]


class PolicyUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    action: Literal["allow", "log"]
    """The action to take if the expression matches"""

    description: str
    """A description for the policy"""

    enabled: bool
    """Whether the policy is enabled"""

    expression: str
    """
    The expression which must match for the policy to be applied, using the
    Cloudflare Firewall rule expression syntax
    """

    value: str
    """The policy which will be applied"""
