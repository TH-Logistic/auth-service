from pydantic import BaseModel, Field


class BaseResponse(BaseModel):
    success: bool = Field(default=True)
    message: str | None = None
    data: object | None = None

    # def __init__(self, success: bool, message: str | None, data: object | None) -> None:
    #     self.success = success
    #     self.message = message
    #     self.data = data
