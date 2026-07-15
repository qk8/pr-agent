from __future__ import annotations
from pr_agent.identity_providers.identity_provider import (Eligibility,
                                                           IdentityProvider)


class DefaultIdentityProvider(IdentityProvider):
    def verify_eligibility(self, git_provider, git_provider_id, pr_url):  # pyright: ignore[reportUnknownParameterType,reportMissingParameterType,reportUnknownMemberType]  # pyright: ignore[reportIncompatibleMethodOverride]
        return Eligibility.ELIGIBLE

    def inc_invocation_count(self, git_provider, git_provider_id):  # pyright: ignore[reportUnknownParameterType,reportMissingParameterType,reportUnknownMemberType]
        pass
