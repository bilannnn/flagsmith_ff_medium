import json

from dependency_injector.containers import (DeclarativeContainer,
                                            WiringConfiguration)
from dependency_injector.providers import Configuration, Factory, Self
from fastapi import FastAPI

from src.ff_demo_service.application import make_fastapi_app
from src.ff_demo_service.domain.reports.interfaces import (
    GenerateReportUseCase, ReportService)
from src.ff_demo_service.domain.reports.services import ReportServiceImpl
from src.ff_demo_service.domain.reports.use_case import \
    GenerateReportUseCaseImpl
from src.ff_demo_service.flagsmith.interfaces import (FeatureFlags,
                                                      FlagsmithClient)
from src.ff_demo_service.flagsmith.services import (FlagsmithFeatureFlags,
                                                    HTTPXFlagsmithClient)
from src.ff_demo_service.settings import Settings

WIRING_MODULES = [
    "src.ff_demo_service.views.routers.reports",
]


class MainContainer(DeclarativeContainer):
    __self__ = Self()
    config: Configuration = Configuration()
    wiring_config = WiringConfiguration(modules=WIRING_MODULES)

    ff_client: Factory[FlagsmithClient] = Factory(
        HTTPXFlagsmithClient,
        environment_key=config.flagsmith.environment_key,
        base_url=config.flagsmith.base_url,
        flags_path=config.flagsmith.flags_path,
    )

    ff: Factory[FeatureFlags] = Factory(
        FlagsmithFeatureFlags,
        client=ff_client,
    )

    fastapi_app: Factory[FastAPI] = Factory(
        make_fastapi_app,
        title=config.misc.title,
        base_api_path=config.misc.base_api_path,
    )

    report_service: Factory[ReportService] = Factory(
        ReportServiceImpl,
    )

    generate_report_use_case: Factory[GenerateReportUseCase] = Factory(
        GenerateReportUseCaseImpl,
        ff=ff,
        report_service=report_service,
    )


def bootstrap(init_resources: bool = False) -> MainContainer:
    container = MainContainer()
    settings = Settings()

    container.config.from_dict(settings.model_dump())

    if init_resources:
        container.init_resources()

    return container
