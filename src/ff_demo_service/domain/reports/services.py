from typing import Any

from src.ff_demo_service.domain.reports.interfaces import ReportService


class ReportServiceImpl(ReportService):
    async def generate_report(self, report_name: str, /) -> dict[str, Any]:
        return {"name": report_name, "version": 1}

    async def generate_report_v2(self, report_name: str, /) -> dict[str, Any]:
        return {"name": report_name, "version": 2}
