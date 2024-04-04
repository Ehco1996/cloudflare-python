# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ..shared import UnnamedSchemaRef78

__all__ = ["AnalyzeCreateParams"]


class AnalyzeCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    bundle_method: UnnamedSchemaRef78
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    certificate: str
    """The zone's SSL certificate or certificate and the intermediate(s)."""
