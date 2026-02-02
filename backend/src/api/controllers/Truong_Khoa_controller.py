from fastapi import HTTPException , status

from api.schemas.requests.Duyet_Du_An import DuyetDuAnRequest
from services.Duyet_Du_An import DuyetDuAnUseCase
from api.schemas.responses.Xem_Du_An import XemDuAnResponse
from services.Xem_Du_An import XemDuAnUseCase
from api.schemas.requests.Bac_Bo_Du_An import BacBoDuAnRequest
class TruongKhoaController:
    def __init__(self, duyet_du_an : DuyetDuAnUseCase , xem_du_an : XemDuAnUseCase):
        self.ser_duyet_du_an = duyet_du_an
        self.ser_xem_du_an = xem_du_an
    def duyet_du_an(self , request : DuyetDuAnRequest):
        try:
            self.ser_duyet_du_an.duyet_du_an(request.id_du_an)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def xem_du_an(self)->list[XemDuAnResponse]:
        try:
            dsDA = self.ser_xem_du_an.execute()
            return [
                XemDuAnResponse(
                    id_du_an=DA.id,
                    noi_dung=DA.noi_dung,
                    trang_thai=DA.trang_thai,
                    id_giang_vien=DA.nguoi_tao.id,
                    ten_giang_vien=DA.nguoi_tao.ten
                )
                for DA in dsDA
            ]
        except ValueError as e :
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )
    def huy_du_an(self , request : BacBoDuAnRequest):
        try:
            self.ser_duyet_du_an.huy_duyet_du_an(request.id_du_an)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e)
            )