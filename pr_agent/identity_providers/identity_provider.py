from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum


class Eligibility(Enum):
    NOT_ELIGIBLE = 0
    ELIGIBLE = 1
    TRIAL = 2


class IdentityProvider(ABC):
    @abstractmethod
    def verify_eligibility(self, git_provider, git_provider_id, pr_url):  # pyright: ignore[reportUnknownParameterType,reportMissingParameterType,reportUnknownMemberType]
        pass

    @abstractmethod
    def inc_invocation_count(self, git_provider, git_provider_id):  # pyright: ignore[reportUnknownParameterType,reportMissingParameterType,reportUnknownMemberType]
        pass
