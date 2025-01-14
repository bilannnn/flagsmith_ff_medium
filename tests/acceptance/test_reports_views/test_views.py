from typing import Iterator
from unittest.mock import AsyncMock

from dependency_injector.providers import Container
from httpx import AsyncClient
from pytest import fixture

from src.ff_demo_service.containers import MainContainer


class TestGetReportView:
    @fixture(autouse=True)
    def override_ff(
        self,
        container: Container[MainContainer],
    ) -> Iterator[AsyncMock]:
        ff_obj = AsyncMock()
        ff_obj.is_set.return_value = False

        with container.ff.override(ff_obj):
            yield ff_obj

    async def test_positive(
        self, client_without_auth: AsyncClient, api_prefix: str, override_ff: AsyncMock
    ) -> None:

        response = await client_without_auth.get(
            f"{api_prefix}/report/", params={"report_name": "test"}
        )

        assert response.status_code == 200
        assert response.json() == {"name": "test", "version": 1}

    async def test_positive_v2(
        self,
        client_without_auth: AsyncClient,
        api_prefix: str,
        override_ff: AsyncMock,
    ) -> None:
        override_ff.is_set.return_value = True
        response = await client_without_auth.get(
            f"{api_prefix}/report/", params={"report_name": "test"}
        )

        assert response.status_code == 200
        assert response.json() == {"name": "test", "version": 2}
