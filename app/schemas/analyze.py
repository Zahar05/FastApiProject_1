from pydantic import BaseModel, EmailStr


class AnalyzeDocumentRequest(BaseModel):
    image_id: int
    email: EmailStr


class AnalyzeDocumentResponse(BaseModel):
    detail: str
    task_id: str
    