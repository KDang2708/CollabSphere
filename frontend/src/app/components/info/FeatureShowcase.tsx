import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../ui/card';
import { Badge } from '../ui/badge';
import { 
  Users, 
  FolderKanban, 
  Video, 
  MessageSquare, 
  Bot, 
  CheckCircle2, 
  BarChart3,
  Zap,
  Shield,
  Globe,
  Sparkles,
} from 'lucide-react';

export const FeatureShowcase: React.FC = () => {
  const features = [
    {
      icon: FolderKanban,
      title: 'Quản lý Dự án PBL',
      description: 'Tạo, phê duyệt và theo dõi dự án với workflow hoàn chỉnh. Hỗ trợ AI tạo milestone và mục tiêu.',
      color: 'bg-blue-100 text-blue-600',
    },
    {
      icon: Users,
      title: 'Cộng tác Nhóm',
      description: 'Workspace với Kanban board, quản lý task, checkpoint và theo dõi đóng góp của từng thành viên.',
      color: 'bg-green-100 text-green-600',
    },
    {
      icon: Video,
      title: 'Video Conferencing',
      description: 'Cuộc họp video chất lượng cao với chat, screen sharing và lên lịch meeting.',
      color: 'bg-purple-100 text-purple-600',
    },
    {
      icon: Bot,
      title: 'AI Assistant',
      description: 'Chatbot thông minh hỗ trợ brainstorming, phân tích tiến độ và tư vấn công nghệ.',
      color: 'bg-pink-100 text-pink-600',
    },
    {
      icon: CheckCircle2,
      title: 'Đánh giá & Feedback',
      description: 'Hệ thống đánh giá giảng viên và peer review giữa các thành viên nhóm.',
      color: 'bg-orange-100 text-orange-600',
    },
    {
      icon: BarChart3,
      title: 'Analytics & Tracking',
      description: 'Theo dõi tiến độ, phân tích contribution và dashboard thống kê chi tiết.',
      color: 'bg-indigo-100 text-indigo-600',
    },
  ];

  const roles = [
    {
      role: 'Admin',
      description: 'Quản trị hệ thống, quản lý tài khoản và xem báo cáo',
      features: ['Account Management', 'System Reports', 'Security Control'],
    },
    {
      role: 'Staff',
      description: 'Quản lý học vụ, môn học, lớp học và tài khoản',
      features: ['Subject Management', 'Class Management', 'Account Import'],
    },
    {
      role: 'Head Department',
      description: 'Phê duyệt dự án và giám sát hoạt động khoa',
      features: ['Project Approval', 'Class Oversight', 'Department Analytics'],
    },
    {
      role: 'Lecturer',
      description: 'Tạo dự án, quản lý lớp học và hỗ trợ sinh viên',
      features: ['Create Projects', 'Manage Teams', 'Evaluate Students', 'AI Support'],
    },
    {
      role: 'Student',
      description: 'Tham gia nhóm, làm việc trên dự án PBL',
      features: ['Team Workspace', 'Submit Work', 'Peer Review', 'Collaboration Tools'],
    },
  ];

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <div className="text-center">
        <div className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full mb-4">
          <Sparkles className="w-4 h-4" />
          <span className="text-sm font-medium">Project-Based Learning Management System</span>
        </div>
        <h1 className="text-4xl font-bold mb-4">CollabSphere (COSRE)</h1>
        <p className="text-xl text-gray-600 max-w-3xl mx-auto">
          Hệ thống hỗ trợ học tập dựa trên dự án với các công cụ cộng tác 
          theo thời gian thực và AI assistant thông minh
        </p>
      </div>

      {/* Key Features */}
      <div>
        <h2 className="text-2xl font-bold mb-6">Tính năng chính</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {features.map((feature) => {
            const Icon = feature.icon;
            return (
              <Card key={feature.title} className="hover:shadow-lg transition-shadow">
                <CardContent className="p-6">
                  <div className={`w-12 h-12 ${feature.color} rounded-lg flex items-center justify-center mb-4`}>
                    <Icon className="w-6 h-6" />
                  </div>
                  <h3 className="font-semibold text-lg mb-2">{feature.title}</h3>
                  <p className="text-sm text-gray-600">{feature.description}</p>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>

      {/* User Roles */}
      <div>
        <h2 className="text-2xl font-bold mb-6">Vai trò người dùng</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {roles.map((roleInfo) => (
            <Card key={roleInfo.role}>
              <CardHeader>
                <CardTitle className="text-lg">{roleInfo.role}</CardTitle>
                <CardDescription>{roleInfo.description}</CardDescription>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  {roleInfo.features.map((feature) => (
                    <div key={feature} className="flex items-center gap-2 text-sm">
                      <CheckCircle2 className="w-4 h-4 text-green-600" />
                      <span>{feature}</span>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      </div>

      {/* Tech Stack */}
      <Card>
        <CardHeader>
          <CardTitle>Công nghệ sử dụng</CardTitle>
          <CardDescription>Tech stack cho hệ thống CollabSphere</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h4 className="font-semibold mb-3 flex items-center gap-2">
                <Globe className="w-5 h-5 text-blue-600" />
                Frontend
              </h4>
              <div className="flex flex-wrap gap-2">
                {['React', 'TypeScript', 'Tailwind CSS', 'Shadcn/ui', 'React DnD'].map(tech => (
                  <Badge key={tech} variant="outline">{tech}</Badge>
                ))}
              </div>
            </div>
            <div>
              <h4 className="font-semibold mb-3 flex items-center gap-2">
                <Shield className="w-5 h-5 text-green-600" />
                Backend (Planned)
              </h4>
              <div className="flex flex-wrap gap-2">
                {['Python Web API', 'PostgreSQL', 'Redis', 'WebRTC', 'Socket.IO'].map(tech => (
                  <Badge key={tech} variant="outline">{tech}</Badge>
                ))}
              </div>
            </div>
            <div>
              <h4 className="font-semibold mb-3 flex items-center gap-2">
                <Zap className="w-5 h-5 text-purple-600" />
                Cloud Services
              </h4>
              <div className="flex flex-wrap gap-2">
                {['Azure', 'AWS', 'Cloudinary', 'AWS Bedrock'].map(tech => (
                  <Badge key={tech} variant="outline">{tech}</Badge>
                ))}
              </div>
            </div>
            <div>
              <h4 className="font-semibold mb-3 flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-pink-600" />
                AI & Real-time
              </h4>
              <div className="flex flex-wrap gap-2">
                {['AWS Bedrock AI', 'WebRTC', 'Signal', 'Socket.IO'].map(tech => (
                  <Badge key={tech} variant="outline">{tech}</Badge>
                ))}
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Demo Info */}
      <Card className="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
        <CardContent className="p-6">
          <div className="flex items-start gap-4">
            <div className="w-12 h-12 bg-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
              <Sparkles className="w-6 h-6 text-white" />
            </div>
            <div className="flex-1">
              <h3 className="font-semibold text-lg text-blue-900 mb-2">Demo Mode</h3>
              <p className="text-blue-700 mb-4">
                Đây là phiên bản demo frontend với dữ liệu mô phỏng. Bạn có thể đăng nhập 
                với bất kỳ vai trò nào để trải nghiệm các tính năng tương ứng.
              </p>
              <div className="flex flex-wrap gap-2">
                <Badge className="bg-blue-600">Fully Interactive</Badge>
                <Badge className="bg-purple-600">Mock Data</Badge>
                <Badge className="bg-green-600">All Features Available</Badge>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
