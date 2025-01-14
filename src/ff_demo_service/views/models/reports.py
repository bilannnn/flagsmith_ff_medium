from pydantic import BaseModel


class ReportResponseSchema(BaseModel):
    name: str
    version: int
