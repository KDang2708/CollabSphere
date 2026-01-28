import React, { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Label } from './ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { useAuth } from '../contexts/AuthContext';
import { Users, GraduationCap, BookOpen, Info } from 'lucide-react';
import { demoAccounts } from '../data/demoHelpers';
import { Badge } from './ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';

export const LoginPage: React.FC = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { login } = useAuth();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    
    const success = login(email, password);
    if (!success) {
      setError('Email hoặc mật khẩu không đúng hoặc tài khoản đã bị vô hiệu hóa');
    }
  };

  const quickLoginOptions = [
    { role: 'Admin', email: 'admin@cosre.edu', icon: Users },
    { role: 'Staff', email: 'staff@cosre.edu', icon: Users },
    { role: 'Head Dept', email: 'head@cosre.edu', icon: BookOpen },
    { role: 'Lecturer', email: 'lecturer1@cosre.edu', icon: GraduationCap },
    { role: 'Student', email: 'student1@cosre.edu', icon: GraduationCap },
  ];

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
      <div className="w-full max-w-5xl grid md:grid-cols-2 gap-8 items-center">
        {/* Left side - Branding */}
        <div className="text-center md:text-left">
          <div className="flex items-center justify-center md:justify-start gap-3 mb-6">
            <div className="w-16 h-16 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-2xl flex items-center justify-center">
              <Users className="w-10 h-10 text-white" />
            </div>
            <div>
              <h1 className="text-4xl font-bold text-gray-900">CollabSphere</h1>
              <p className="text-sm text-gray-600">COSRE</p>
            </div>
          </div>
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">
            Hệ thống Hỗ trợ Học tập theo Phương pháp Dự án
          </h2>
          <p className="text-gray-600 mb-6">
            Nền tảng tích hợp toàn diện cho quản lý dự án, cộng tác nhóm, 
            và đánh giá trong môi trường Học tập Dựa trên Dự án (PBL)
          </p>
          <div className="space-y-3 text-left">
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 bg-blue-600 rounded-full mt-2" />
              <p className="text-sm text-gray-700">Cộng tác theo thời gian thực với bảng trắng, chat, video call</p>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 bg-blue-600 rounded-full mt-2" />
              <p className="text-sm text-gray-700">Quản lý dự án và theo dõi tiến độ minh bạch</p>
            </div>
            <div className="flex items-start gap-3">
              <div className="w-2 h-2 bg-blue-600 rounded-full mt-2" />
              <p className="text-sm text-gray-700">Hệ thống đánh giá và phản hồi toàn diện</p>
            </div>
          </div>
        </div>

        {/* Right side - Login Form */}
        <Card className="shadow-2xl">
          <CardHeader>
            <CardTitle>Đăng nhập</CardTitle>
            <CardDescription>Nhập thông tin để truy cập hệ thống</CardDescription>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input
                  id="email"
                  type="email"
                  placeholder="example@cosre.edu"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                />
              </div>
              <div className="space-y-2">
                <Label htmlFor="password">Mật khẩu</Label>
                <Input
                  id="password"
                  type="password"
                  placeholder="••••••••"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
              </div>
              {error && (
                <div className="text-sm text-red-600 bg-red-50 p-3 rounded-md">
                  {error}
                </div>
              )}
              <Button type="submit" className="w-full">
                Đăng nhập
              </Button>
            </form>

            {/* Quick Login Demo */}
            <div className="mt-6">
              <div className="relative">
                <div className="absolute inset-0 flex items-center">
                  <span className="w-full border-t" />
                </div>
                <div className="relative flex justify-center text-xs uppercase">
                  <span className="bg-white px-2 text-gray-500">Demo - Đăng nhập nhanh</span>
                </div>
              </div>
              <div className="mt-4 grid grid-cols-2 gap-2">
                {quickLoginOptions.map((option) => {
                  const Icon = option.icon;
                  return (
                    <Button
                      key={option.email}
                      variant="outline"
                      size="sm"
                      onClick={() => {
                        setEmail(option.email);
                        setPassword('demo');
                        login(option.email, 'demo');
                      }}
                      className="flex items-center gap-2"
                    >
                      <Icon className="w-4 h-4" />
                      <span>{option.role}</span>
                    </Button>
                  );
                })}
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};