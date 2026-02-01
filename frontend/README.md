# 🚀 Frontend React – Hướng dẫn khởi động môi trường

Tài liệu này hướng dẫn **cách khởi động và chạy môi trường Frontend React cho dự án đã được tạo sẵn** (không bao gồm bước tạo project mới).

---

## 📦 Yêu cầu hệ thống

Trước khi chạy project, hãy đảm bảo máy bạn đã cài:

* **Node.js** ≥ 18.x (khuyến nghị LTS)
* **npm** ≥ 9.x *(hoặc yarn / pnpm)*
* **Git**

Kiểm tra phiên bản:

```bash
node -v
npm -v
git --version
```

---

## 📥 Bước 1: Clone source code

```bash
git clone <repository-url>
cd <ten-thu-muc-project>
```

---

## 📦 Bước 2: Cài đặt dependencies

Chạy lệnh sau để cài các thư viện cần thiết:

```bash
npm install
```

> ⚠️ Bước này **bắt buộc** sau khi clone project hoặc khi `package.json` có thay đổi.

---

## 🔐 Bước 3: Cấu hình biến môi trường

Tạo file `.env` ở thư mục gốc (nếu chưa có):

```
VITE_API_URL=http://localhost:8000
```

Nếu project có file mẫu:

```
.env.example
```

→ copy sang `.env` và chỉnh lại cho phù hợp.

Sử dụng trong code:

```js
import.meta.env.VITE_API_URL
```

⚠️ **Không commit file `.env` lên Git**

---

## ▶️ Bước 4: Chạy môi trường development

```bash
npm run dev
```

Mặc định project sẽ chạy tại:

```
http://localhost:5173
```

(Nếu port khác, xem log trong terminal)

---

## 🧪 Các lệnh thường dùng

```bash
npm run dev      # chạy môi trường dev
npm run build    # build production
npm run preview  # xem bản build sau khi build
```

---

## 🛑 Một số lỗi thường gặp

### ❌ Không chạy được `npm run dev`

* Kiểm tra đã chạy `npm install` chưa
* Kiểm tra version Node có đúng yêu cầu không
* Xoá cache và cài lại:

```bash
rm -rf node_modules package-lock.json
npm install
```

---

## 📌 Ghi chú

* Luôn pull code mới nhất trước khi chạy
* Nếu có backend, đảm bảo backend đang chạy trước
* Kiểm tra README hoặc tài liệu riêng của project nếu có cấu hình đặc biệt

---

## 🤝 Đóng góp

Pull request và góp ý luôn được chào đón ❤️

---

## 📄 License

MIT License
