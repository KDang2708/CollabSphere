from pydantic import BaseModel , Field

class BacBoDuAnRequest(BaseModel):
    id_du_an : str = Field(...,)