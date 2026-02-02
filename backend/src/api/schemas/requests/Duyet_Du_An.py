from pydantic import BaseModel , Field

class DuyetDuAnRequest(BaseModel):
    id_du_an : str = Field(...,)