from typing import Iterator

from dependency_injector.providers import Container
from pytest import fixture

from src.ff_demo_service.containers import MainContainer, bootstrap
from src.ff_demo_service.settings import Settings


@fixture(scope="session")
def settings() -> Settings:
    return Settings()


@fixture(scope="session")
def _container() -> Iterator[MainContainer]:
    container = bootstrap(init_resources=False)
    yield container


@fixture
def container(
    _container: Container[MainContainer],
) -> Iterator[Container[MainContainer]]:
    with _container.reset_singletons():
        _container.init_resources()
        yield _container
        _container.shutdown_resources()
