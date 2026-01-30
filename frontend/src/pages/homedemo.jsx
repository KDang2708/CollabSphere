import React from 'react';

const HomeDemo = ({ onLogout }) => {
  return (
    <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', height: '100vh', backgroundColor: '#f5f5f5' }}>
      <h1>Chào mừng đến với CollabSphere!</h1>
      <p>Bạn đã đăng nhập thành công.</p>
      <button onClick={onLogout} style={{ padding: '10px 20px', backgroundColor: '#dc3545', color: 'white', border: 'none', borderRadius: '4px', cursor: 'pointer' }}>
        Đăng Xuất
      </button>
    </div>
  );
};

export default HomeDemo;
