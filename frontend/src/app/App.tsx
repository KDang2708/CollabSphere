import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext';
import { LoginPage } from './components/LoginPage';
import { MainLayout } from './components/MainLayout';
import { StudentDashboard } from './components/dashboards/StudentDashboard';
import { LecturerDashboard } from './components/dashboards/LecturerDashboard';
import { AdminDashboard } from './components/dashboards/AdminDashboard';
import { StaffDashboard } from './components/dashboards/StaffDashboard';
import { HeadDepartmentDashboard } from './components/dashboards/HeadDepartmentDashboard';
import { TeamWorkspace } from './components/workspace/TeamWorkspace';
import { VideoMeeting } from './components/communication/VideoMeeting';
import { AIAssistant } from './components/ai/AIAssistant';
import { UserProfile } from './components/profile/UserProfile';
import { Settings } from './components/settings/Settings';
import { NotificationsList } from './components/notifications/NotificationsList';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './components/ui/tabs';
import { Button } from './components/ui/button';
import { Toaster } from './components/ui/sonner';
import {
  LayoutDashboard,
  Users,
  FolderKanban,
  Video,
  Bot,
  Presentation,
  FileText,
} from 'lucide-react';

function AppContent() {
  const { currentUser, isAuthenticated } = useAuth();

  if (!isAuthenticated || !currentUser) {
    return <LoginPage />;
  }

  const getDashboard = () => {
    switch (currentUser.role) {
      case 'admin':
        return <AdminDashboard />;
      case 'staff':
        return <StaffDashboard />;
      case 'head_department':
        return <HeadDepartmentDashboard />;
      case 'lecturer':
        return <LecturerDashboard />;
      case 'student':
        return <StudentDashboard />;
      default:
        return <div>Dashboard không tồn tại</div>;
    }
  };

  return (
    <Routes>
      <Route path="/" element={<Navigate to={`/${currentUser.role}`} replace />} />
      <Route path="/admin" element={<MainLayout>{<AdminDashboard />}</MainLayout>} />
      <Route path="/staff" element={<MainLayout>{<StaffDashboard />}</MainLayout>} />
      <Route path="/head_department" element={<MainLayout>{<HeadDepartmentDashboard />}</MainLayout>} />
      <Route path="/lecturer" element={<MainLayout>{<LecturerDashboard />}</MainLayout>} />
      <Route path="/student" element={<MainLayout>{<StudentDashboard />}</MainLayout>} />
      <Route path="/profile" element={<MainLayout>{<UserProfile />}</MainLayout>} />
      <Route path="/settings" element={<MainLayout>{<Settings />}</MainLayout>} />
      <Route path="/notifications" element={<MainLayout>{<NotificationsList />}</MainLayout>} />
      <Route path="/workspace" element={<MainLayout>{<TeamWorkspace />}</MainLayout>} />
      <Route path="/meeting" element={<MainLayout>{<VideoMeeting />}</MainLayout>} />
      <Route path="/ai" element={<MainLayout>{<AIAssistant />}</MainLayout>} />
    </Routes>
  );
}

export default function App() {
  return (
    <Router>
      <AuthProvider>
        <AppContent />
        <Toaster />
      </AuthProvider>
    </Router>
  );
}
