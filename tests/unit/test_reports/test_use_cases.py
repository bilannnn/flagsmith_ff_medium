from unittest.mock import AsyncMock

from pytest import fixture

from src.ff_demo_service.domain.reports.interfaces import GenerateReportUseCase
from src.ff_demo_service.domain.reports.use_case import \
    GenerateReportUseCaseImpl


class TestGenerateReportUseCaseImpl:
    @fixture
    def ff_mock(self) -> AsyncMock:
        ff_obj = AsyncMock()
        ff_obj.is_set.return_value = False
        return ff_obj

    @fixture
    def service(self) -> AsyncMock:
        service = AsyncMock()
        service.generate_report.return_value = {"name": "test", "version": 1}
        service.generate_report_v2.return_value = {"name": "test", "version": 2}
        return service

    @fixture
    def use_case(self, service: AsyncMock, ff_mock: AsyncMock) -> GenerateReportUseCase:
        return GenerateReportUseCaseImpl(
            report_service=service,
            ff=ff_mock,
        )

    async def test_positive(
        self,
        use_case: GenerateReportUseCase,
        ff_mock: AsyncMock,
        service: AsyncMock,
    ) -> None:
        report = await use_case("test")
        assert report == {"name": "test", "version": 1}
        ff_mock.is_set.assert_called_once_with("support_report_v2")
        service.generate_report.assert_called_once_with("test")
        service.generate_report_v2.assert_not_called()

    async def test_positive_v2(
        self,
        use_case: GenerateReportUseCase,
        ff_mock: AsyncMock,
        service: AsyncMock,
    ) -> None:
        ff_mock.is_set.return_value = True
        report = await use_case("test")
        assert report == {"name": "test", "version": 2}
        ff_mock.is_set.assert_called_once_with("support_report_v2")
        service.generate_report.assert_not_called()
        service.generate_report_v2.assert_called_once_with("test")
