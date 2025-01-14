from fastapi import FastAPI

from src.ff_demo_service.containers import bootstrap


def build_app() -> FastAPI:
    container = bootstrap(
        init_resources=True,
    )

    return container.fastapi_app()
