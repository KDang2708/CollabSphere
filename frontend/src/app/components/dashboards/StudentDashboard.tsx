import React from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Progress } from '../ui/progress';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs';
import {
  Calendar,
  Clock,
  Users,
  CheckCircle2,
  AlertCircle,
  TrendingUp,
  MessageSquare,
  Video,
  FileText,
  Target,
} from 'lucide-react';
import { mockTeams, mockClasses, mockProjects, mockMeetings, mockNotifications } from '../../data/mockData';
import { useAuth } from '../../contexts/AuthContext';

export const StudentDashboard: React.FC = () => {
  const { currentUser } = useAuth();

  // Get student's team
  const studentTeam = mockTeams.find(t => t.memberIds.includes(currentUser?.id || ''));
  const studentClass = mockClasses.find(c => c.id === studentTeam?.classId);
  const teamProject = mockProjects.find(p => p.id === studentTeam?.projectId);

  // Calculate stats
  const completedMilestones = studentTeam?.milestones.filter(m => m.completed).length || 0;
  const totalMilestones = studentTeam?.milestones.length || 0;
  const upcomingMeetings = mockMeetings.filter(m => 
    m.participants.includes(currentUser?.id || '') && m.status === 'scheduled'
  );

  const recentNotifications = mockNotifications
    .filter(n => n.userId === currentUser?.id)
    .slice(0, 3);

  return (
    <div className="space-y-6">
      {/* Welcome Section */}
      <div className="bg-gradient-to-r from-blue-600 to-indigo-600 rounded-xl p-6 text-white">
        <h1 className="text-3xl font-bold mb-2">Chào mừng trở lại! 👋</h1>
        <p className="text-blue-100">
          Hãy cùng nhóm tiếp tục phát triển dự án của bạn
        </p>
      </div>

      {/* Quick Stats */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Tiến độ dự án</p>
                <p className="text-2xl font-bold">{studentTeam?.progress || 0}%</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <TrendingUp className="w-6 h-6 text-blue-600" />
              </div>
            </div>
            <Progress value={studentTeam?.progress || 0} className="mt-3" />
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Cột mốc hoàn thành</p>
                <p className="text-2xl font-bold">{completedMilestones}/{totalMilestones}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <CheckCircle2 className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Thành viên nhóm</p>
                <p className="text-2xl font-bold">{studentTeam?.memberIds.length || 0}</p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                <Users className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Cuộc họp sắp tới</p>
                <p className="text-2xl font-bold">{upcomingMeetings.length}</p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                <Calendar className="w-6 h-6 text-orange-600" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Main Content */}
        <div className="lg:col-span-2 space-y-6">
          {/* Project Overview */}
          <Card>
            <CardHeader>
              <div className="flex items-center justify-between">
                <div>
                  <CardTitle>Dự án hiện tại</CardTitle>
                  <CardDescription>{studentClass?.name}</CardDescription>
                </div>
                <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200">
                  {studentTeam?.name}
                </Badge>
              </div>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                <div>
                  <div className="flex items-start justify-between mb-2">
                    <div className="flex items-center gap-2">
                      <Target className="w-5 h-5 text-blue-600" />
                      <h3 className="font-semibold">{teamProject?.title}</h3>
                    </div>
                  </div>
                  <p className="text-sm text-gray-600">{teamProject?.description}</p>
                </div>

                <div>
                  <div className="flex items-center justify-between mb-3">
                    <h4 className="font-medium">Các cột mốc quan trọng</h4>
                    <span className="text-sm text-gray-500">
                      {completedMilestones}/{totalMilestones} hoàn thành
                    </span>
                  </div>
                  <div className="space-y-3">
                    {studentTeam?.milestones.map((milestone) => (
                      <div
                        key={milestone.id}
                        className="flex items-start gap-3 p-3 bg-gray-50 rounded-lg"
                      >
                        <div className="mt-0.5">
                          {milestone.completed ? (
                            <CheckCircle2 className="w-5 h-5 text-green-600" />
                          ) : (
                            <div className="w-5 h-5 border-2 border-gray-300 rounded-full" />
                          )}
                        </div>
                        <div className="flex-1">
                          <div className="flex items-start justify-between">
                            <div>
                              <p className={`font-medium ${milestone.completed ? 'text-gray-500 line-through' : ''}`}>
                                {milestone.title}
                              </p>
                              <p className="text-sm text-gray-500 mt-1">{milestone.description}</p>
                            </div>
                            <Badge variant={milestone.completed ? 'secondary' : 'outline'}>
                              {milestone.completed ? 'Hoàn thành' : 'Đang thực hiện'}
                            </Badge>
                          </div>
                          <div className="flex items-center gap-2 mt-2 text-sm text-gray-500">
                            <Clock className="w-4 h-4" />
                            <span>Hạn: {milestone.dueDate}</span>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="flex gap-2 pt-4">
                  <Button className="flex-1">
                    <MessageSquare className="w-4 h-4 mr-2" />
                    Trò chuyện nhóm
                  </Button>
                  <Button variant="outline" className="flex-1">
                    <Video className="w-4 h-4 mr-2" />
                    Tạo cuộc họp
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>

          {/* Checkpoints */}
          <Card>
            <CardHeader>
              <CardTitle>Điểm kiểm tra (Checkpoints)</CardTitle>
              <CardDescription>Các Sprint và nhiệm vụ cần hoàn thành</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {studentTeam?.checkpoints.map((checkpoint) => (
                  <div key={checkpoint.id} className="border rounded-lg p-4">
                    <div className="flex items-start justify-between mb-2">
                      <div className="flex-1">
                        <h4 className="font-medium">{checkpoint.title}</h4>
                        <p className="text-sm text-gray-600 mt-1">{checkpoint.description}</p>
                      </div>
                      <Badge variant={checkpoint.completed ? 'default' : 'secondary'}>
                        {checkpoint.completed ? 'Hoàn thành' : 'Chưa hoàn thành'}
                      </Badge>
                    </div>
                    <div className="flex items-center gap-4 text-sm text-gray-500 mt-3">
                      <div className="flex items-center gap-1">
                        <Users className="w-4 h-4" />
                        <span>{checkpoint.assignedMembers.length} thành viên</span>
                      </div>
                      <div className="flex items-center gap-1">
                        <Clock className="w-4 h-4" />
                        <span>Hạn: {checkpoint.dueDate}</span>
                      </div>
                    </div>
                    {!checkpoint.completed && (
                      <Button size="sm" className="mt-3">
                        Nộp bài
                      </Button>
                    )}
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </div>

        {/* Sidebar */}
        <div className="space-y-6">
          {/* Upcoming Meetings */}
          <Card>
            <CardHeader>
              <CardTitle>Cuộc họp sắp tới</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {upcomingMeetings.length > 0 ? (
                  upcomingMeetings.map((meeting) => (
                    <div key={meeting.id} className="p-3 bg-blue-50 rounded-lg border border-blue-200">
                      <div className="flex items-start justify-between mb-2">
                        <h4 className="font-medium text-sm">{meeting.title}</h4>
                        <Video className="w-4 h-4 text-blue-600" />
                      </div>
                      <p className="text-sm text-gray-600">{meeting.scheduledAt}</p>
                      <p className="text-xs text-gray-500 mt-1">Thời lượng: {meeting.duration} phút</p>
                      <Button size="sm" className="w-full mt-3">
                        Tham gia
                      </Button>
                    </div>
                  ))
                ) : (
                  <div className="text-center py-6 text-gray-500">
                    <Calendar className="w-8 h-8 mx-auto mb-2 text-gray-400" />
                    <p className="text-sm">Chưa có cuộc họp nào</p>
                  </div>
                )}
                <Button variant="outline" className="w-full">
                  Lên lịch cuộc họp
                </Button>
              </div>
            </CardContent>
          </Card>

          {/* Recent Notifications */}
          <Card>
            <CardHeader>
              <CardTitle>Thông báo gần đây</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-3">
                {recentNotifications.map((notif) => (
                  <div key={notif.id} className="p-3 border rounded-lg">
                    <div className="flex items-start gap-2">
                      {!notif.read && (
                        <div className="w-2 h-2 bg-blue-600 rounded-full mt-2" />
                      )}
                      <div className="flex-1">
                        <p className="font-medium text-sm">{notif.title}</p>
                        <p className="text-xs text-gray-600 mt-1">{notif.message}</p>
                        <p className="text-xs text-gray-400 mt-1">{notif.createdAt}</p>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          {/* Quick Actions */}
          <Card>
            <CardHeader>
              <CardTitle>Hành động nhanh</CardTitle>
            </CardHeader>
            <CardContent className="space-y-2">
              <Button variant="outline" className="w-full justify-start">
                <FileText className="w-4 h-4 mr-2" />
                Xem tài nguyên
              </Button>
              <Button variant="outline" className="w-full justify-start">
                <Users className="w-4 h-4 mr-2" />
                Đánh giá thành viên
              </Button>
              <Button variant="outline" className="w-full justify-start">
                <AlertCircle className="w-4 h-4 mr-2" />
                Báo cáo vấn đề
              </Button>
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
};
