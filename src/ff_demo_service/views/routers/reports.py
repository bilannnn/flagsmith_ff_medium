from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from src.ff_demo_service.domain.reports.interfaces import GenerateReportUseCase
from src.ff_demo_service.settings import settings
from src.ff_demo_service.views.models.reports import ReportResponseSchema

router = APIRouter(
    prefix=f"{settings.misc.base_api_path}/report",
)


@router.get(
    "/",
    status_code=200,
)
@inject
async def generate_report(
    report_name: str,
    generate_report_use_case: GenerateReportUseCase = Depends(
        Provide["generate_report_use_case"]
    ),
) -> ReportResponseSchema:
    report_data = await generate_report_use_case(report_name)
    return ReportResponseSchema(**report_data)
