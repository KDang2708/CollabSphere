import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Progress } from '../ui/progress';
import { Avatar, AvatarFallback } from '../ui/avatar';
import {
  Users,
  FolderKanban,
  CheckCircle2,
  Clock,
  TrendingUp,
  AlertCircle,
  BarChart3,
  Plus,
  Eye,
  MessageSquare,
  FileText,
} from 'lucide-react';
import { mockTeams, mockClasses, mockProjects, mockUsers } from '../../data/mockData';
import { useAuth } from '../../contexts/AuthContext';

export const LecturerDashboard: React.FC = () => {
  const { currentUser } = useAuth();

  // Get lecturer's classes
  const lecturerClasses = mockClasses.filter(c => c.lecturerId === currentUser?.id);
  const allTeams = mockTeams.filter(t => lecturerClasses.some(c => c.id === t.classId));
  
  // Get lecturer's projects
  const lecturerProjects = mockProjects.filter(p => p.createdBy === currentUser?.id);
  const approvedProjects = lecturerProjects.filter(p => p.status === 'approved');
  const pendingProjects = lecturerProjects.filter(p => p.status === 'pending');

  // Calculate average progress
  const avgProgress = allTeams.length > 0
    ? Math.round(allTeams.reduce((sum, t) => sum + t.progress, 0) / allTeams.length)
    : 0;

  // Teams needing attention (low progress)
  const teamsNeedingAttention = allTeams.filter(t => t.progress < 40);

  return (
    <div className="space-y-6">
      {/* Welcome Section */}
      <div className="bg-gradient-to-r from-indigo-600 to-purple-600 rounded-xl p-6 text-white">
        <h1 className="text-3xl font-bold mb-2">Bảng điều khiển Giảng viên</h1>
        <p className="text-indigo-100">
          Quản lý các lớp học, dự án và hỗ trợ sinh viên của bạn
        </p>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Tổng lớp học</p>
                <p className="text-2xl font-bold">{lecturerClasses.length}</p>
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
                <p className="text-sm text-gray-500">Tổng nhóm</p>
                <p className="text-2xl font-bold">{allTeams.length}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <Users className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Dự án đã duyệt</p>
                <p className="text-2xl font-bold">{approvedProjects.length}</p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                <FolderKanban className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Tiến độ trung bình</p>
                <p className="text-2xl font-bold">{avgProgress}%</p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-orange-600" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-6">
          {/* My Projects */}
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle>Dự án của tôi</CardTitle>
                  <CardDescription>Quản lý và tạo dự án mới</CardDescription>
                </div>
                <Button>
                  <Plus className="w-4 h-4 mr-2" />
                  Tạo dự án
                </Button>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {lecturerProjects.length > 0 ? (
                  lecturerProjects.map((project) => (
                    <div key={project.id} className="border rounded-lg p-4">
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex-1">
                          <h4 className="font-medium">{project.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">{project.description}</p>
                        </div>
                        <Badge
                          variant={
                            project.status === 'approved'
                              ? 'default'
                              : project.status === 'pending'
                              ? 'secondary'
                              : 'destructive'
                          }
                        >
                          {project.status === 'approved' && 'Đã duyệt'}
                          {project.status === 'pending' && 'Chờ duyệt'}
                          {project.status === 'rejected' && 'Bị từ chối'}
                        </Badge>
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-500 mt-3">
                        <CheckCircle2 className="w-4 h-4" />
                        <span>{project.milestones.length} cột mốc</span>
                      </div>
                      <div className="flex gap-2 mt-3">
                        <Button size="sm" variant="outline">
                          <Eye className="w-4 h-4 mr-2" />
                          Xem chi tiết
                        </Button>
                        {project.status === 'approved' && (
                          <Button size="sm">Giao cho lớp</Button>
                        )}
                      </div>
                    </div>
                  ))
                ) : (
                  <div className="text-center py-8 text-gray-500">
                    <FolderKanban className="w-12 h-12 mx-auto mb-3 text-gray-400" />
                    <p>Chưa có dự án nào</p>
                    <Button className="mt-4">
                      <Plus className="w-4 h-4 mr-2" />
                      Tạo dự án đầu tiên
                    </Button>
                  </div>
                )}
              </div>
            </CardContent>
          </Card>

          {/* Teams Overview */}
          <Card>
            <CardHeader>
              <CardTitle>Tổng quan các nhóm</CardTitle>
              <CardDescription>Theo dõi tiến độ và hoạt động của nhóm</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {allTeams.map((team) => {
                  const teamClass = mockClasses.find(c => c.id === team.classId);
                  const teamLeader = mockUsers.find(u => u.id === team.leaderId);
                  const completedMilestones = team.milestones.filter(m => m.completed).length;

                  return (
                    <div key={team.id} className="border rounded-lg p-4">
                      <div className="flex items-start justify-between mb-3">
                        <div className="flex-1">
                          <div className="flex items-center gap-2 mb-1">
                            <h4 className="font-medium">{team.name}</h4>
                            <Badge variant="outline">{teamClass?.code}</Badge>
                          </div>
                          <div className="flex items-center gap-2 text-sm text-gray-500">
                            <span>Trưởng nhóm: {teamLeader?.name}</span>
                            <span>•</span>
                            <span>{team.memberIds.length} thành viên</span>
                          </div>
                        </div>
                        {team.progress < 40 && (
                          <Badge variant="destructive" className="flex items-center gap-1">
                            <AlertCircle className="w-3 h-3" />
                            Cần chú ý
                          </Badge>
                        )}
                      </div>

                      <div className="space-y-2">
                        <div className="flex items-center justify-between text-sm">
                          <span className="text-gray-600">Tiến độ</span>
                          <span className="font-medium">{team.progress}%</span>
                        </div>
                        <Progress value={team.progress} />
                        <div className="flex items-center justify-between text-sm text-gray-500">
                          <span>{completedMilestones}/{team.milestones.length} cột mốc hoàn thành</span>
                          <span>{team.checkpoints.filter(c => c.completed).length}/{team.checkpoints.length} checkpoints</span>
                        </div>
                      </div>

                      <div className="flex gap-2 mt-4">
                        <Button size="sm" variant="outline">
                          <Eye className="w-4 h-4 mr-2" />
                          Xem chi tiết
                        </Button>
                        <Button size="sm" variant="outline">
                          <MessageSquare className="w-4 h-4 mr-2" />
                          Nhắn tin
                        </Button>
                        <Button size="sm" variant="outline">
                          <BarChart3 className="w-4 h-4 mr-2" />
                          Đánh giá
                        </Button>
                      </div>
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Attention Required */}
          {teamsNeedingAttention.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2 text-orange-600">
                  <AlertCircle className="w-5 h-5" />
                  Cần chú ý
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {teamsNeedingAttention.map((team) => {
                    const teamClass = mockClasses.find(c => c.id === team.classId);
                    return (
                      <div key={team.id} className="p-3 bg-orange-50 rounded-lg border border-orange-200">
                        <div className="flex items-center justify-between mb-2">
                          <h4 className="font-medium text-sm">{team.name}</h4>
                          <Badge variant="outline">{teamClass?.code}</Badge>
                        </div>
                        <p className="text-sm text-gray-600 mb-2">
                          Tiến độ: {team.progress}% - Cần hỗ trợ
                        </p>
                        <Button size="sm" variant="outline" className="w-full">
                          Liên hệ nhóm
                        </Button>
                      </div>
                    );
                  })}
                </div>
              </CardContent>
            </Card>
          )}

          {/* My Classes */}
          <Card>
            <CardHeader>
              <CardTitle>Lớp học của tôi</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {lecturerClasses.map((classItem) => {
                  const classTeams = allTeams.filter(t => t.classId === classItem.id);
                  return (
                    <div key={classItem.id} className="p-3 border rounded-lg">
                      <h4 className="font-medium">{classItem.name}</h4>
                      <div className="flex items-center gap-4 text-sm text-gray-500 mt-2">
                        <span>{classItem.studentIds.length} sinh viên</span>
                        <span>•</span>
                        <span>{classTeams.length} nhóm</span>
                      </div>
                      <Button size="sm" variant="outline" className="w-full mt-3">
                        Quản lý lớp
                      </Button>
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>

          {/* Pending Projects */}
          {pendingProjects.length > 0 && (
            <Card>
              <CardHeader>
                <CardTitle className="flex items-center gap-2">
                  <Clock className="w-5 h-5 text-blue-600" />
                  Dự án chờ duyệt
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="space-y-3">
                  {pendingProjects.map((project) => (
                    <div key={project.id} className="p-3 bg-blue-50 rounded-lg border border-blue-200">
                      <h4 className="font-medium text-sm">{project.title}</h4>
                      <p className="text-xs text-gray-500 mt-1">
                        Đã gửi: {project.createdAt}
                      </p>
                      <Badge variant="secondary" className="mt-2">
                        Chờ trưởng khoa phê duyệt
                      </Badge>
                    </div>
                  ))}
                </div>
              </CardContent>
            </Card>
          )}

          {/* Quick Actions */}
          <Card>
            <CardHeader>
              <CardTitle>Hành động nhanh</CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <Button variant="outline" className="w-full justify-start">
                <Plus className="w-4 h-4 mr-2" />
                Tạo nhóm mới
              </Button>
              <Button variant="outline" className="w-full justify-start">
                <FileText className="w-4 h-4 mr-2" />
                Tải tài nguyên
              </Button>
              <Button variant="outline" className="w-full justify-start">
                <BarChart3 className="w-4 h-4 mr-2" />
                Xem báo cáo
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
