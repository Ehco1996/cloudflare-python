# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .tokens import Permission
from ..._models import BaseModel

__all__ = ["Invite", "Role"]


class Role(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[Permission]
    """Access permissions for this User."""


class Invite(BaseModel):
    invited_member_id: Optional[str] = None
    """ID of the user to add to the organization."""

    organization_id: str
    """ID of the organization the user will be added to."""

    id: Optional[str] = None
    """Invite identifier tag."""

    expires_on: Optional[datetime] = None
    """When the invite is no longer active."""

    invited_by: Optional[str] = None
    """The email address of the user who created the invite."""

    invited_member_email: Optional[str] = None
    """Email address of the user to add to the organization."""

    invited_on: Optional[datetime] = None
    """When the invite was sent."""

    organization_name: Optional[str] = None
    """Organization name."""

    roles: Optional[List[Role]] = None
    """Roles to be assigned to this user."""

    status: Optional[Literal["pending", "accepted", "rejected", "expired"]] = None
    """Current status of the invitation."""
