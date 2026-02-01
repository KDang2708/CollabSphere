from pydantic import BaseModel

class DangNhapResponse(BaseModel):
    access_token : str
    token_type: str = "bearer"