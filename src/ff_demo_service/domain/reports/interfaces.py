from abc import ABCMeta, abstractmethod
from typing import Any, Protocol


class ReportService(metaclass=ABCMeta):
    @abstractmethod
    async def generate_report(self, report_name: str, /) -> dict[str, Any]:
        """
        Generate some report data
        """

    @abstractmethod
    async def generate_report_v2(self, report_name: str, /) -> dict[str, Any]:
        """
        Generate new report data
        """


class GenerateReportUseCase(Protocol):
    async def __call__(self, report_name: str, /) -> dict[str, Any]:
        """
        Generate report
        """
