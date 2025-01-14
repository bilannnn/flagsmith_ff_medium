from dependency_injector.providers import Container
from fastapi import FastAPI
from httpx import ASGITransport, AsyncClient
from pytest import fixture

from src.ff_demo_service.containers import MainContainer
from src.ff_demo_service.settings import Settings


@fixture
def api_prefix(
    settings: Settings,
) -> str:
    return str(settings.misc.base_api_path)


@fixture
def fastapi_app(
    container: Container[MainContainer],
) -> FastAPI:
    return container.fastapi_app()


@fixture
def client_without_auth(
    fastapi_app: FastAPI,
) -> AsyncClient:
    return AsyncClient(transport=ASGITransport(app=fastapi_app), base_url="http://test")
