@app.get("/lop-hoc/{id}")
def get_chi_tiet_lop(id: str):
    # 1. Chuẩn bị input cho use case
    lop_hoc = LopHoc(id=id)

    # 2. Gọi use case
    ket_qua = use_case.execute(lop_hoc)

    # 3. MAP sang response cho FE
    return {
        "lopHoc": {
            "id": ket_qua["lop_hoc"].id,
            "ten": ket_qua["lop_hoc"].ten,
        },
        "mocQuanTrong": [
            {
                "id": m.id,
                "noiDung": m.noi_dung
            }
            for m in ket_qua["ds_moc_quan_trong"]
        ],
        "baiKiemTra": [
            {
                "id": b.id,
                "ten": b.ten
            }
            for b in ket_qua["ds_bai_kiem_tra"]
        ]
    }