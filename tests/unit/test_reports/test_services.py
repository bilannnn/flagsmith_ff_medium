from pytest import fixture, mark

from src.ff_demo_service.domain.reports.interfaces import ReportService
from src.ff_demo_service.domain.reports.services import ReportServiceImpl


class TestReportServiceImpl:
    @fixture
    def service(self) -> ReportService:
        return ReportServiceImpl()

    async def test_generate_report(self, service: ReportService) -> None:
        report = await service.generate_report("test")
        assert report == {"name": "test", "version": 1}

    async def test_generate_report_v2(self, service: ReportService) -> None:
        report = await service.generate_report_v2("test")
        assert report == {"name": "test", "version": 2}
