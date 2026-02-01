from fastapi import APIRouter, Depends

from api.controllers.Admin_controller import AdminController
from services.Doc_Bao_Cao import DocBaoCaoUseCase
from api.schemas.responses.Bao_cao import BaoCaoResponse
from infrastructure.security.dependency import get_current_user

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_bao_cao_controller():
    service = DocBaoCaoUseCase()
    return AdminController(service)

@router.get("/doc_bao_cao", response_model = list[BaoCaoResponse] , status_code= 200 )
def doc_bao_cao(
    controller : AdminController = Depends(get_bao_cao_controller),
    user = Depends(get_current_user)
):
    
    return controller.lay_danh_sach_bao_cao()