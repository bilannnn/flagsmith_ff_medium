import logging
from typing import Any

from httpx import AsyncClient

from src.ff_demo_service.flagsmith.interfaces import (FeatureFlags, Flag,
                                                      FlagsmithClient)
from src.ff_demo_service.flagsmith.utils import flag_from_response


class HTTPXFlagsmithClient(FlagsmithClient):
    def __init__(
        self,
        environment_key: str,
        base_url: str,
        flags_path: str,
    ) -> None:
        self.environment_key = environment_key
        self.base_url = base_url
        self.flags_path = flags_path

    def _client(self) -> AsyncClient:
        return AsyncClient(
            headers={"X-Environment-Key": self.environment_key},
            base_url=self.base_url,
        )

    async def flag_list(self) -> list[Flag]:
        async with self._client() as client:
            response = await client.get(self.flags_path)
            try:
                response.raise_for_status()

                data: list[dict[str, Any]] = response.json()
                return [flag_from_response(fs) for fs in data]
            except Exception as e:
                logging.error(e)
                logging.error("Failed to fetch feature flags")
                return []


class FlagsmithFeatureFlags(FeatureFlags):

    client: FlagsmithClient
    flags: dict[str, bool]

    def __init__(
        self,
        client: FlagsmithClient,
    ) -> None:
        self.client = client
        self.flags = {}

    async def is_set(self, name: str, /) -> bool:
        await self._refresh()

        return self.flags.get(name, False)

    async def _refresh(self) -> None:
        flag_list = await self.client.flag_list()

        for flag in flag_list:
            self.flags[flag.name] = flag.enabled
