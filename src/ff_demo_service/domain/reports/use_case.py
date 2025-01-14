from typing import Any

from src.ff_demo_service.domain.reports.interfaces import (
    GenerateReportUseCase, ReportService)
from src.ff_demo_service.flagsmith.interfaces import FeatureFlags


class GenerateReportUseCaseImpl(GenerateReportUseCase):
    def __init__(self, ff: FeatureFlags, report_service: ReportService) -> None:
        self.ff = ff
        self.report_service = report_service

    async def __call__(self, report_name: str, /) -> dict[str, Any]:
        if await self.ff.is_set("support_report_v2"):
            return await self.report_service.generate_report_v2(report_name)

        return await self.report_service.generate_report(report_name)
