import React, { useState } from 'react';
import { login } from '../js/auth_signup_password';

const LoginPage = ({ onLogin }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const user = await login(email, password); // Assume returns { role: 'Admin', ... }
      onLogin(user.role); // Pass role to App.jsx for navigation
    } catch (err) {
      setError(err.message || 'Đăng nhập thất bại. Vui lòng thử lại.');
    }
  };

  // ── MISSING FUNCTION ── Added back
  const handleForgotPassword = (e) => {
    e.preventDefault();
    console.log('Yêu cầu quên mật khẩu cho email:', email);
    
    // Placeholder - bạn có thể thay bằng modal hoặc redirect thật
    alert('Chức năng quên mật khẩu đang được phát triển. Vui lòng liên hệ admin!');
    
    // Ví dụ redirect nếu bạn đã có route:
    // window.location.href = '/forgot-password';
  };

  // ── MISSING FUNCTION ── Added back (for demo quick login buttons)
  const handleQuickLogin = (role) => {
    console.log(`Quick login as: ${role}`);
    // Gọi onLogin giống như login thật → sẽ chuyển đến dashboard tương ứng
    onLogin(role);
  };

  return (
    <div
      style={{
        display: 'flex',
        height: '100vh',
        backgroundColor: '#31ae20',
        color: '#fff',
        fontFamily: 'Arial, sans-serif',
      }}
    >
      {/* Phần bên trái - Giới thiệu */}
      <div
        style={{
          flex: 1,
          padding: '40px 60px',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'center',
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', marginBottom: '20px' }}>
          <div
            style={{
              width: '60px',
              height: '60px',
              backgroundColor: '#fff',
              borderRadius: '50%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              fontSize: '32px',
              fontWeight: 'bold',
              color: '#31ae20',
              marginRight: '15px',
            }}
          >
            CS
          </div>
          <h1 style={{ margin: 0, fontSize: '28px' }}>CollabSphere COSRE</h1>
        </div>

        <h2 style={{ fontSize: '24px', marginBottom: '16px' }}>
          Hệ thống Hỗ trợ Học tập theo Phương pháp Dự án
        </h2>
        <p style={{ fontSize: '16px', lineHeight: '1.5', marginBottom: '24px' }}>
          Nền tảng tích hợp toàn diện cho quản lý dự án, công tác nhóm, và đánh giá trong môi trường Học tập Dựa trên Dự án (PBL)
        </p>

        <ul style={{ fontSize: '15px', lineHeight: '1.8', paddingLeft: '20px' }}>
          <li>Công tác theo thời gian thực với bảng trắng, chat, video call</li>
          <li>Quản lý dự án và theo dõi tiến độ minh bạch</li>
          <li>Hệ thống đánh giá và phản hồi toàn diện</li>
        </ul>
      </div>

      {/* Phần bên phải - Form đăng nhập */}
      <div
        style={{
          flex: 1,
          backgroundColor: '#fff',
          color: '#333',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          padding: '53px',
        }}
      >
        <div style={{ width: '380px', maxWidth: '100%' }}>
          <h2 style={{ textAlign: 'center', marginBottom: '30px', color: '#31ae20' }}>
            Đăng nhập
          </h2>
          <p style={{ textAlign: 'center', marginBottom: '25px', color: '#555' }}>
            Nhập thông tin để truy cập hệ thống
          </p>

          <form onSubmit={handleSubmit}>
            <input
              type="email"
              placeholder="example@cosre.edu"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
              style={{
                width: '93.5%',
                padding: '12px',
                marginBottom: '16px',
                border: '1px solid #ccc',
                borderRadius: '6px',
                fontSize: '16px',
              }}
            />

            <input
              type="password"
              placeholder="Mật khẩu"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              style={{
                width: '93.5%',
                padding: '12px',
                marginBottom: '16px',
                border: '1px solid #ccc',
                borderRadius: '6px',
                fontSize: '16px',
              }}
            />

            {error && (
              <p style={{ color: 'red', textAlign: 'center', marginBottom: '16px' }}>
                {error}
              </p>
            )}

            <button
              type="submit"
              style={{
                width: '100%',
                padding: '14px',
                backgroundColor: '#000000',
                color: '#fff',
                border: 'none',
                borderRadius: '6px',
                fontSize: '16px',
                fontWeight: 'bold',
                cursor: 'pointer',
                marginBottom: '12px',
              }}
            >
              Đăng nhập
            </button>

            {/* Link Quên mật khẩu - giờ đã có hàm xử lý */}
            <div style={{ textAlign: 'center', marginBottom: '30px' }}>
              <a
                href="#"
                onClick={handleForgotPassword}
                style={{
                  color: '#31ae20',
                  textDecoration: 'none',
                  fontSize: '14px',
                  fontWeight: '500',
                }}
              >
                Quên mật khẩu?
              </a>
            </div>
          </form>

          <hr style={{ margin: '20px 0', borderColor: '#ddd' }} />

          <p style={{ textAlign: 'center', marginBottom: '15px', color: '#555' }}>
            DEMO - ĐĂNG NHẬP NHANH
          </p>

          <div
            style={{
              display: 'flex',
              flexWrap: 'wrap',
              gap: '10px',
              justifyContent: 'center',
            }}
          >
            {['Admin', 'Staff', 'Head Dept', 'Lecturer', 'Student'].map((role) => (
              <button
                key={role}
                onClick={() => handleQuickLogin(role)}
                style={{
                  padding: '10px 18px',
                  backgroundColor: '#f0f0f0',
                  border: '1px solid #ccc',
                  borderRadius: '6px',
                  cursor: 'pointer',
                  fontSize: '14px',
                  minWidth: '100px',
                }}
              >
                {role}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginPage;