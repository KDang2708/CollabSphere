import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';
import { Button } from './ui/button';
import { Avatar, AvatarFallback } from './ui/avatar';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from './ui/dropdown-menu';
import {
  AlertDialog,
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogFooter,
  AlertDialogHeader,
  AlertDialogTitle,
} from './ui/alert-dialog';
import { Badge } from './ui/badge';
import {
  Bell,
  LogOut,
  Menu,
  User,
  X,
  Home,
  Users,
  BookOpen,
  FolderKanban,
  Calendar,
  MessageSquare,
  Video,
  FileText,
  BarChart3,
  Settings,
  Bot,
} from 'lucide-react';
import { NotificationCenter } from './notifications/NotificationCenter';

interface MainLayoutProps {
  children: React.ReactNode;
}

export const MainLayout: React.FC<MainLayoutProps> = ({ children }) => {
  const { currentUser, logout } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [showLogoutDialog, setShowLogoutDialog] = useState(false);

  const handleLogout = () => {
    logout();
    setShowLogoutDialog(false);
  };

  const handleMenuClick = (path: string) => {
    navigate(`/${path}`);
  };

  const getNavigationItems = () => {
    const role = currentUser?.role;

    const commonItems = [
      { icon: Home, label: 'Trang chủ', path: role || 'dashboard' },
    ];

    if (role === 'admin') {
      return [
        ...commonItems,
        { icon: Users, label: 'Quản lý Tài khoản', path: 'accounts' },
        { icon: BarChart3, label: 'Báo cáo Hệ thống', path: 'reports' },
      ];
    }

    if (role === 'staff') {
      return [
        ...commonItems,
        { icon: BookOpen, label: 'Môn học & Đề cương', path: 'subjects' },
        { icon: Users, label: 'Quản lý Lớp học', path: 'classes' },
        { icon: Users, label: 'Tài khoản', path: 'accounts' },
      ];
    }

    if (role === 'head_department') {
      return [
        ...commonItems,
        { icon: FolderKanban, label: 'Quản lý Dự án', path: 'projects' },
        { icon: Users, label: 'Lớp học', path: 'classes' },
        { icon: BookOpen, label: 'Môn học & Đề cương', path: 'subjects' },
      ];
    }

    if (role === 'lecturer') {
      return [
        ...commonItems,
        { icon: FolderKanban, label: 'Dự án của tôi', path: 'my-projects' },
        { icon: Users, label: 'Lớp học của tôi', path: 'my-classes' },
        { icon: Users, label: 'Nhóm', path: 'teams' },
        { icon: MessageSquare, label: 'Tin nhắn', path: 'messages' },
        { icon: Video, label: 'Cuộc họp', path: 'meeting' },
        { icon: FileText, label: 'Tài nguyên', path: 'resources' },
        { icon: Bot, label: 'AI Assistant', path: 'ai' },
      ];
    }

    if (role === 'student') {
      return [
        ...commonItems,
        { icon: Users, label: 'Lớp học', path: 'classes' },
        { icon: Users, label: 'Nhóm của tôi', path: 'my-team' },
        { icon: FolderKanban, label: 'Không gian làm việc', path: 'workspace' },
        { icon: MessageSquare, label: 'Tin nhắn', path: 'messages' },
        { icon: Video, label: 'Cuộc họp', path: 'meeting' },
        { icon: Calendar, label: 'Lịch trình', path: 'schedule' },
        { icon: FileText, label: 'Tài nguyên', path: 'resources' },
        { icon: Bot, label: 'AI Assistant', path: 'ai' },
      ];
    }

    return commonItems;
  };

  const getInitials = (name: string) => {
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  const getRoleLabel = (role: string) => {
    const labels: Record<string, string> = {
      admin: 'Quản trị viên',
      staff: 'Nhân viên',
      head_department: 'Trưởng khoa',
      lecturer: 'Giảng viên',
      student: 'Sinh viên',
    };
    return labels[role] || role;
  };

  return (
    <div className="h-screen flex overflow-hidden bg-gray-50">
      {/* Sidebar */}
      <aside
        className={`${
          sidebarOpen ? 'w-64' : 'w-0'
        } bg-white border-r border-gray-200 transition-all duration-300 overflow-hidden flex flex-col`}
      >
        <div className="p-4 border-b border-gray-200 flex items-center gap-3">
          <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center flex-shrink-0">
            <Users className="w-6 h-6 text-white" />
          </div>
          <div className="flex-1 min-w-0">
            <h2 className="font-semibold text-gray-900 truncate">CollabSphere</h2>
            <p className="text-xs text-gray-500">COSRE System</p>
          </div>
        </div>

        <nav className="flex-1 p-4 space-y-1 overflow-y-auto">
          {getNavigationItems().map((item) => {
            const Icon = item.icon;
            const isActive = location.pathname === `/${item.path}`;
            return (
              <button
                key={item.path}
                onClick={() => handleMenuClick(item.path)}
                className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg transition-colors ${
                  isActive
                    ? 'bg-blue-50 text-blue-600'
                    : 'text-gray-700 hover:bg-blue-50 hover:text-blue-600'
                }`}
              >
                <Icon className="w-5 h-5 flex-shrink-0" />
                <span className="truncate">{item.label}</span>
              </button>
            );
          })}
        </nav>

        <div className="p-4 border-t border-gray-200">
          <div className="flex items-center gap-3 p-2 rounded-lg bg-gray-50">
            <Avatar className="w-8 h-8">
              <AvatarFallback className="bg-blue-600 text-white text-sm">
                {getInitials(currentUser?.name || 'U')}
              </AvatarFallback>
            </Avatar>
            <div className="flex-1 min-w-0">
              <p className="text-sm font-medium text-gray-900 truncate">{currentUser?.name}</p>
              <p className="text-xs text-gray-500">{getRoleLabel(currentUser?.role || '')}</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <div className="flex-1 flex flex-col overflow-hidden">
        {/* Top Bar */}
        <header className="bg-white border-b border-gray-200 px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setSidebarOpen(!sidebarOpen)}
            >
              {sidebarOpen ? <X className="w-5 h-5" /> : <Menu className="w-5 h-5" />}
            </Button>
            <div>
              <h1 className="font-semibold text-gray-900">
                {currentUser?.role === 'admin' && 'Quản trị Hệ thống'}
                {currentUser?.role === 'staff' && 'Quản lý Học vụ'}
                {currentUser?.role === 'head_department' && 'Quản lý Khoa'}
                {currentUser?.role === 'lecturer' && 'Giảng viên'}
                {currentUser?.role === 'student' && 'Sinh viên'}
              </h1>
              <p className="text-sm text-gray-500">
                Chào mừng trở lại, {currentUser?.name}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            {/* Notifications - Using NotificationCenter component */}
            <NotificationCenter onViewAll={() => handleMenuClick('notifications')} />

            {/* User Menu */}
            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button variant="ghost" size="sm">
                  <Avatar className="w-8 h-8">
                    <AvatarFallback className="bg-blue-600 text-white">
                      {getInitials(currentUser?.name || 'U')}
                    </AvatarFallback>
                  </Avatar>
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end">
                <DropdownMenuLabel>Tài khoản</DropdownMenuLabel>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={() => handleMenuClick('profile')}>
                  <User className="w-4 h-4 mr-2" />
                  Hồ sơ cá nhân
                </DropdownMenuItem>
                <DropdownMenuItem onClick={() => handleMenuClick('settings')}>
                  <Settings className="w-4 h-4 mr-2" />
                  Cài đặt
                </DropdownMenuItem>
                <DropdownMenuSeparator />
                <DropdownMenuItem onClick={() => setShowLogoutDialog(true)} className="text-red-600">
                  <LogOut className="w-4 h-4 mr-2" />
                  Đăng xuất
                </DropdownMenuItem>
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </header>

        {/* Page Content */}
        <main className="flex-1 overflow-y-auto p-6">
          {children}
        </main>
      </div>

      {/* Logout Confirmation Dialog */}
      <AlertDialog open={showLogoutDialog} onOpenChange={setShowLogoutDialog}>
        <AlertDialogContent>
          <AlertDialogHeader>
            <AlertDialogTitle>Xác nhận đăng xuất</AlertDialogTitle>
            <AlertDialogDescription>
              Bạn có chắc chắn muốn đăng xuất khỏi hệ thống? Tất cả công việc chưa lưu sẽ bị mất.
            </AlertDialogDescription>
          </AlertDialogHeader>
          <AlertDialogFooter>
            <AlertDialogCancel>Hủy</AlertDialogCancel>
            <AlertDialogAction onClick={handleLogout} className="bg-red-600 hover:bg-red-700">
              Đăng xuất
            </AlertDialogAction>
          </AlertDialogFooter>
        </AlertDialogContent>
      </AlertDialog>
    </div>
  );
};