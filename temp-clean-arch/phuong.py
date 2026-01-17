# tạo dự án
import os 
def create_project(project_name):
    try:
        os.makedirs(project_name)
        print(f"Dự án '{project_name}' đã được tạo thành công.")
    except FileExistsError:
        print(f"Dự án '{project_name}' đã tồn tại.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")        
# ví dụ sử dụng
create_project("Dự_án_Mới") 
#kêt thúc tạo dự án
# thêm chức năng khác ở đây nếu cần
