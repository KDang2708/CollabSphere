import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs';
import {
  FolderKanban,
  CheckCircle2,
  Clock,
  XCircle,
  Users,
  BookOpen,
  Eye,
  Check,
  X,
} from 'lucide-react';
import { mockProjects, mockClasses } from '../../data/mockData';

export const HeadDepartmentDashboard: React.FC = () => {
  const [projects] = useState(mockProjects);

  const approvedProjects = projects.filter(p => p.status === 'approved');
  const pendingProjects = projects.filter(p => p.status === 'pending');
  const rejectedProjects = projects.filter(p => p.status === 'rejected');

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-purple-600 to-indigo-600 rounded-xl p-6 text-white">
        <h1 className="text-3xl font-bold mb-2">Bảng điều khiển Trưởng khoa</h1>
        <p className="text-purple-100">
          Quản lý và phê duyệt dự án, giám sát hoạt động của khoa
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Tổng dự án</p>
                <p className="text-2xl font-bold">{projects.length}</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <FolderKanban className="w-6 h-6 text-blue-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Đã duyệt</p>
                <p className="text-2xl font-bold text-green-600">{approvedProjects.length}</p>
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
                <p className="text-sm text-gray-500">Chờ duyệt</p>
                <p className="text-2xl font-bold text-orange-600">{pendingProjects.length}</p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                <Clock className="w-6 h-6 text-orange-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Lớp học</p>
                <p className="text-2xl font-bold">{mockClasses.length}</p>
              </div>
              <div className="w-12 h-12 bg-purple-100 rounded-full flex items-center justify-center">
                <Users className="w-6 h-6 text-purple-600" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <Tabs defaultValue="pending" className="space-y-6">
        <TabsList>
          <TabsTrigger value="pending" className="flex items-center gap-2">
            <Clock className="w-4 h-4" />
            Chờ duyệt ({pendingProjects.length})
          </TabsTrigger>
          <TabsTrigger value="approved" className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4" />
            Đã duyệt ({approvedProjects.length})
          </TabsTrigger>
          <TabsTrigger value="all" className="flex items-center gap-2">
            <FolderKanban className="w-4 h-4" />
            Tất cả ({projects.length})
          </TabsTrigger>
        </TabsList>

        <TabsContent value="pending">
          <Card>
            <CardHeader>
              <CardTitle>Dự án chờ phê duyệt</CardTitle>
              <CardDescription>Xem xét và phê duyệt các dự án mới được tạo bởi giảng viên</CardDescription>
            </CardHeader>
            <CardContent>
              {pendingProjects.length > 0 ? (
                <div className="space-y-4">
                  {pendingProjects.map((project) => (
                    <div key={project.id} className="border rounded-lg p-4">
                      <div className="flex items-start justify-between mb-3">
                        <div className="flex-1">
                          <h4 className="font-medium text-lg">{project.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">{project.description}</p>
                        </div>
                        <Badge variant="secondary">Chờ duyệt</Badge>
                      </div>

                      <div className="space-y-2 mb-4">
                        <div className="text-sm">
                          <span className="font-medium">Mục tiêu:</span>
                          <ul className="list-disc list-inside ml-2 mt-1 text-gray-600">
                            {project.objectives.slice(0, 3).map((obj, idx) => (
                              <li key={idx}>{obj}</li>
                            ))}
                          </ul>
                        </div>
                        <div className="flex items-center gap-4 text-sm text-gray-500">
                          <span>{project.milestones.length} cột mốc</span>
                          <span>•</span>
                          <span>Ngày tạo: {project.createdAt}</span>
                        </div>
                      </div>

                      <div className="flex gap-2">
                        <Button size="sm" variant="outline">
                          <Eye className="w-4 h-4 mr-2" />
                          Chi tiết
                        </Button>
                        <Button size="sm" variant="default">
                          <Check className="w-4 h-4 mr-2" />
                          Phê duyệt
                        </Button>
                        <Button size="sm" variant="destructive">
                          <X className="w-4 h-4 mr-2" />
                          Từ chối
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-12 text-gray-500">
                  <Clock className="w-12 h-12 mx-auto mb-3 text-gray-400" />
                  <p>Không có dự án chờ duyệt</p>
                </div>
              )}
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="approved">
          <Card>
            <CardHeader>
              <CardTitle>Dự án đã duyệt</CardTitle>
              <CardDescription>Các dự án đã được phê duyệt và sẵn sàng giao cho lớp học</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {approvedProjects.map((project) => (
                  <div key={project.id} className="border rounded-lg p-4">
                    <div className="flex items-start justify-between mb-3">
                      <div className="flex-1">
                        <h4 className="font-medium text-lg">{project.title}</h4>
                        <p className="text-sm text-gray-600 mt-1">{project.description}</p>
                      </div>
                      <Badge className="bg-green-600">Đã duyệt</Badge>
                    </div>

                    <div className="flex items-center gap-4 text-sm text-gray-500 mb-4">
                      <span>{project.milestones.length} cột mốc</span>
                      <span>•</span>
                      <span>{project.objectives.length} mục tiêu</span>
                    </div>

                    <div className="flex gap-2">
                      <Button size="sm" variant="outline">
                        <Eye className="w-4 h-4 mr-2" />
                        Chi tiết
                      </Button>
                      <Button size="sm">
                        Giao cho lớp
                      </Button>
                      <Button size="sm" variant="outline">
                        Chỉnh sửa
                      </Button>
                    </div>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        <TabsContent value="all">
          <Card>
            <CardHeader>
              <CardTitle>Tất cả dự án</CardTitle>
              <CardDescription>Xem tổng quan tất cả các dự án trong hệ thống</CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {projects.map((project) => {
                  const statusColors = {
                    approved: 'bg-green-600',
                    pending: 'bg-orange-500',
                    rejected: 'bg-red-600',
                  };
                  const statusLabels = {
                    approved: 'Đã duyệt',
                    pending: 'Chờ duyệt',
                    rejected: 'Bị từ chối',
                  };

                  return (
                    <div key={project.id} className="border rounded-lg p-4">
                      <div className="flex items-start justify-between mb-2">
                        <div className="flex-1">
                          <h4 className="font-medium">{project.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">{project.description}</p>
                        </div>
                        <Badge className={statusColors[project.status]}>
                          {statusLabels[project.status]}
                        </Badge>
                      </div>
                      <div className="flex items-center gap-4 text-sm text-gray-500 mt-3">
                        <span>{project.milestones.length} cột mốc</span>
                        <span>•</span>
                        <span>Ngày tạo: {project.createdAt}</span>
                      </div>
                    </div>
                  );
                })}
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Lớp học</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {mockClasses.map((classItem) => (
                <div key={classItem.id} className="border rounded-lg p-4">
                  <div className="flex items-start justify-between">
                    <div className="flex-1">
                      <h4 className="font-medium">{classItem.name}</h4>
                      <div className="flex items-center gap-4 text-sm text-gray-500 mt-2">
                        <span>{classItem.studentIds.length} sinh viên</span>
                        <span>•</span>
                        <span>{classItem.semester} {classItem.year}</span>
                      </div>
                    </div>
                    <Badge variant="outline">{classItem.code}</Badge>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Môn học & Đề cương</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {mockProjects.slice(0, 3).map((project) => (
                <div key={project.id} className="flex items-center gap-3 p-3 border rounded-lg">
                  <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                    <BookOpen className="w-5 h-5 text-blue-600" />
                  </div>
                  <div className="flex-1">
                    <p className="font-medium text-sm">{project.title}</p>
                    <p className="text-xs text-gray-500">{project.milestones.length} milestones</p>
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};
