from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Flag:
    name: str
    value: str | int | float | bool | None = None
    enabled: bool = False


class FlagsmithClient(metaclass=ABCMeta):
    """Public Flagsmith API client."""

    @abstractmethod
    async def flag_list(self) -> list[Flag]:
        """Retrieve global feature flags"""


class FeatureFlags(metaclass=ABCMeta):
    """Core feature flags abstraction."""

    @abstractmethod
    async def is_set(self, name: str, /) -> bool:
        """Check if feature flag is set.

        Args:
            name: Flag name.

        Returns:
            ``True`` if flag is set, ``False`` otherwise.
        """

    @abstractmethod
    async def _refresh(self) -> None:
        """Receive fresh feature flag states for identity and traits.

        Warning:
            Intended for use by middlewares/integrations/auth services, you
            generally do not want to call it manually in you code.
        """
