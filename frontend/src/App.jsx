import React from 'react';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useNavigate,
  Navigate,
} from 'react-router-dom';
import LoginPage from './pages/LoginPage'; // điều chỉnh path nếu cần

// Import các dashboard (sửa typo "AdminDaskboard" → "AdminDashboard")
import AdminDashboard from './components/AdminDashboard';
import StaffDashboard from './components/StaffDashboard';
import HeadDeptDashboard from './components/HeadDeptDashboard';
import LecturerDashboard from './components/LecturerDashboard';
import StudentDashboard from './components/StudentDashboard';

// Component bảo vệ route: chỉ cho vào dashboard nếu đã login
const ProtectedDashboard = ({ children, requiredRole }) => {
  // Ở đây bạn sẽ thay bằng logic thực tế (ví dụ: từ context, localStorage, state toàn cục)
  // Hiện tại dùng demo đơn giản: kiểm tra localStorage (bạn có thể thay bằng useContext sau)
  const loggedInRole = localStorage.getItem('userRole');

  if (!loggedInRole) {
    // Chưa login → đẩy về trang login
    return <Navigate to="/" replace />;
  }

  if (requiredRole && loggedInRole !== requiredRole) {
    // Role không khớp → có thể đẩy về trang lỗi hoặc dashboard mặc định
    return <Navigate to={`/dashboard/${loggedInRole}`} replace />;
  }

  return children;
};

// Wrapper cho trang login (xử lý navigate sau login thành công)
const LoginWrapper = () => {
  const navigate = useNavigate();

  const handleLoginSuccess = (role) => {
  if (!role || typeof role !== 'string') {
    console.error('Invalid or missing role:', role);
    alert('Đăng nhập thất bại: Không xác định được vai trò người dùng.');
    return;
  }

  const normalized = role.toLowerCase().replace(' ', '-');
  localStorage.setItem('userRole', normalized);
  navigate(`/dashboard/${normalized}`, { replace: true });
};

  return <LoginPage onLogin={handleLoginSuccess} />;
};

const App = () => {
  return (
    <Router>
      <Routes>
        {/* Trang login luôn hiển thị đầu tiên */}
        <Route path="/" element={<LoginWrapper />} />

        {/* Các dashboard được bảo vệ */}
        <Route
          path="/dashboard/admin"
          element={
            <ProtectedDashboard requiredRole="admin">
              <AdminDashboard />
            </ProtectedDashboard>
          }
        />
        <Route
          path="/dashboard/staff"
          element={
            <ProtectedDashboard requiredRole="staff">
              <StaffDashboard />
            </ProtectedDashboard>
          }
        />
        <Route
          path="/dashboard/head-dept"
          element={
            <ProtectedDashboard requiredRole="head-dept">
              <HeadDeptDashboard />
            </ProtectedDashboard>
          }
        />
        <Route
          path="/dashboard/lecturer"
          element={
            <ProtectedDashboard requiredRole="lecturer">
              <LecturerDashboard />
            </ProtectedDashboard>
          }
        />
        <Route
          path="/dashboard/student"
          element={
            <ProtectedDashboard requiredRole="student">
              <StudentDashboard />
            </ProtectedDashboard>
          }
        />

        {/* Nếu truy cập route lạ → về login */}
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </Router>
  );
};

export default App;