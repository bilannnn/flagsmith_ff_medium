from fastapi import FastAPI

from src.ff_demo_service.views.routers.reports import router as reports_router


def make_fastapi_app(
    title: str,
    base_api_path: str,
) -> FastAPI:
    app = FastAPI(
        title=title,
        openapi_url=f"{base_api_path}/docs/json/",
        docs_url=f"{base_api_path}/docs/swagger/",
        redoc_url=f"{base_api_path}/docs/redoc/",
    )

    app.include_router(reports_router)

    return app
