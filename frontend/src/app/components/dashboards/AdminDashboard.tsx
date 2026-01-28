import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Users, UserCheck, UserX, BarChart3, AlertTriangle, Shield } from 'lucide-react';
import { mockUsers } from '../../data/mockData';

export const AdminDashboard: React.FC = () => {
  const totalUsers = mockUsers.length;
  const activeUsers = mockUsers.filter(u => u.isActive).length;
  const inactiveUsers = mockUsers.filter(u => !u.isActive).length;

  const usersByRole = {
    admin: mockUsers.filter(u => u.role === 'admin').length,
    staff: mockUsers.filter(u => u.role === 'staff').length,
    head_department: mockUsers.filter(u => u.role === 'head_department').length,
    lecturer: mockUsers.filter(u => u.role === 'lecturer').length,
    student: mockUsers.filter(u => u.role === 'student').length,
  };

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-gray-800 to-gray-900 rounded-xl p-6 text-white">
        <div className="flex items-center gap-3 mb-2">
          <Shield className="w-8 h-8" />
          <h1 className="text-3xl font-bold">Quản trị Hệ thống</h1>
        </div>
        <p className="text-gray-300">Tổng quan và quản lý toàn bộ hệ thống CollabSphere</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Tổng người dùng</p>
                <p className="text-2xl font-bold">{totalUsers}</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <Users className="w-6 h-6 text-blue-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Đang hoạt động</p>
                <p className="text-2xl font-bold text-green-600">{activeUsers}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <UserCheck className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Đã vô hiệu hóa</p>
                <p className="text-2xl font-bold text-red-600">{inactiveUsers}</p>
              </div>
              <div className="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center">
                <UserX className="w-6 h-6 text-red-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Báo cáo hệ thống</p>
                <p className="text-2xl font-bold">0</p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                <AlertTriangle className="w-6 h-6 text-orange-600" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Người dùng theo vai trò</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {Object.entries(usersByRole).map(([role, count]) => {
                const roleLabels: Record<string, string> = {
                  admin: 'Quản trị viên',
                  staff: 'Nhân viên',
                  head_department: 'Trưởng khoa',
                  lecturer: 'Giảng viên',
                  student: 'Sinh viên',
                };
                const percentage = (count / totalUsers) * 100;
                
                return (
                  <div key={role}>
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm font-medium">{roleLabels[role]}</span>
                      <span className="text-sm text-gray-500">{count} người</span>
                    </div>
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-blue-600 h-2 rounded-full"
                        style={{ width: `${percentage}%` }}
                      />
                    </div>
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Danh sách người dùng</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {mockUsers.slice(0, 6).map((user) => (
                <div key={user.id} className="flex items-center justify-between p-3 border rounded-lg">
                  <div className="flex-1">
                    <p className="font-medium">{user.name}</p>
                    <p className="text-sm text-gray-500">{user.email}</p>
                  </div>
                  <div className="flex items-center gap-2">
                    <Badge variant={user.isActive ? 'default' : 'secondary'}>
                      {user.isActive ? 'Hoạt động' : 'Vô hiệu hóa'}
                    </Badge>
                    {user.isActive && (
                      <Button variant="outline" size="sm">
                        Vô hiệu hóa
                      </Button>
                    )}
                  </div>
                </div>
              ))}
            </div>
            <Button variant="outline" className="w-full mt-4">
              Xem tất cả
            </Button>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Thống kê hệ thống</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-center">
            <div className="p-4 border rounded-lg">
              <BarChart3 className="w-8 h-8 mx-auto mb-2 text-blue-600" />
              <p className="text-2xl font-bold">0</p>
              <p className="text-sm text-gray-500">Báo cáo trong tuần</p>
            </div>
            <div className="p-4 border rounded-lg">
              <Users className="w-8 h-8 mx-auto mb-2 text-green-600" />
              <p className="text-2xl font-bold">{activeUsers}</p>
              <p className="text-sm text-gray-500">Người dùng online</p>
            </div>
            <div className="p-4 border rounded-lg">
              <AlertTriangle className="w-8 h-8 mx-auto mb-2 text-orange-600" />
              <p className="text-2xl font-bold">0</p>
              <p className="text-sm text-gray-500">Cảnh báo</p>
            </div>
            <div className="p-4 border rounded-lg">
              <Shield className="w-8 h-8 mx-auto mb-2 text-purple-600" />
              <p className="text-2xl font-bold">100%</p>
              <p className="text-sm text-gray-500">Uptime</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
