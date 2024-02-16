# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = [
    "DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse",
    "DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponseItem",
]


class DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponseItem(BaseModel):
    id: Optional[str] = None
    """Delegation identifier tag."""

    cidr: Optional[str] = None
    """IP Prefix in Classless Inter-Domain Routing format."""

    created_at: Optional[datetime] = None

    delegated_account_id: Optional[str] = None
    """Account identifier for the account to which prefix is being delegated."""

    modified_at: Optional[datetime] = None

    parent_prefix_id: Optional[str] = None
    """Identifier"""


DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponse = List[
    DelegationIPAddressManagementPrefixDelegationListPrefixDelegationsResponseItem
]
