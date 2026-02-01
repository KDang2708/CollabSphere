from fastapi import HTTPException, status

from services.Doc_Bao_Cao import DocBaoCaoUseCase
from api.schemas.responses.Bao_cao import BaoCaoResponse

class AdminController:
    def __init__(self , bao_cao : DocBaoCaoUseCase):
          self.ser_doc_bao_cao = bao_cao
    def lay_danh_sach_bao_cao(self) ->list[BaoCaoResponse]:
        dsBC = self.ser_doc_bao_cao.execute()
        return [
            BaoCaoResponse(
                id = BC.id,
                ten_nguoi_gui=BC.nguoi_gui.ten_dang_nhap, # UC sẽ trả về tài khoản 
                id_nguoi_gui=BC.nguoi_gui.id,
                noi_dung=BC.noi_dung,
                ngay_gui=BC.ngay_gui,
                phan_hoi=BC.phan_hoi.noi_dung
            )
            for BC in dsBC
        ]
        