from fastapi import APIRouter , Depends

from api.controllers.Truong_Khoa_controller import TruongKhoaController
from services.Duyet_Du_An import DuyetDuAnUseCase
from infrastructure.security.dependency import get_current_user
from api.schemas.requests.Duyet_Du_An import DuyetDuAnRequest
from services.Xem_Du_An import XemDuAnUseCase
from api.schemas.responses.Xem_Du_An import XemDuAnResponse

router = APIRouter(prefix="/truong_khoa",tags=["TruongKhoa"])

def get_truong_khoa_controller():
    return TruongKhoaController(
        duyet_du_an=DuyetDuAnUseCase(),
        xem_du_an= XemDuAnUseCase(),
    )

@router.put("/duyet_du_an",status_code=200)
def duyet_du_an(
    request : DuyetDuAnRequest,
    user = Depends(get_current_user),
    controller : TruongKhoaController = Depends(get_truong_khoa_controller)
):
    return controller.duyet_du_an(request)
@router.get("/xem_du_an",response_model=list[XemDuAnResponse],status_code=200)
def xem_du_an(
    user = Depends(get_current_user),
    controller : TruongKhoaController = Depends(get_truong_khoa_controller)
):
    return controller.xem_du_an()