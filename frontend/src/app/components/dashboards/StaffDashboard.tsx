import React from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { BookOpen, Users, Upload, FileText, GraduationCap, CheckCircle } from 'lucide-react';
import { mockSubjects, mockSyllabi, mockClasses, mockUsers } from '../../data/mockData';

export const StaffDashboard: React.FC = () => {
  const totalSubjects = mockSubjects.length;
  const totalSyllabi = mockSyllabi.length;
  const totalClasses = mockClasses.length;
  const lecturers = mockUsers.filter(u => u.role === 'lecturer');
  const students = mockUsers.filter(u => u.role === 'student');

  return (
    <div className="space-y-6">
      <div className="bg-gradient-to-r from-green-600 to-teal-600 rounded-xl p-6 text-white">
        <h1 className="text-3xl font-bold mb-2">Quản lý Học vụ</h1>
        <p className="text-green-100">
          Quản lý môn học, đề cương, lớp học và tài khoản
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Môn học</p>
                <p className="text-2xl font-bold">{totalSubjects}</p>
              </div>
              <div className="w-12 h-12 bg-blue-100 rounded-full flex items-center justify-center">
                <BookOpen className="w-6 h-6 text-blue-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Đề cương</p>
                <p className="text-2xl font-bold">{totalSyllabi}</p>
              </div>
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center">
                <FileText className="w-6 h-6 text-green-600" />
              </div>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardContent className="p-6">
            <div className="flex items-center justify-between">
              <div>
                <p className="text-sm text-gray-500">Lớp học</p>
                <p className="text-2xl font-bold">{totalClasses}</p>
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
                <p className="text-sm text-gray-500">Giảng viên</p>
                <p className="text-2xl font-bold">{lecturers.length}</p>
              </div>
              <div className="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                <GraduationCap className="w-6 h-6 text-orange-600" />
              </div>
            </div>
          </CardContent>
        </Card>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle>Quản lý Môn học & Đề cương</CardTitle>
              <Button size="sm">
                <Upload className="w-4 h-4 mr-2" />
                Import
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {mockSubjects.map((subject) => (
                <div key={subject.id} className="border rounded-lg p-4">
                  <div className="flex items-start justify-between mb-2">
                    <div className="flex-1">
                      <h4 className="font-medium">{subject.name}</h4>
                      <p className="text-sm text-gray-600 mt-1">{subject.description}</p>
                    </div>
                    <Badge variant="outline">{subject.code}</Badge>
                  </div>
                  <div className="flex items-center gap-2 text-sm text-gray-500">
                    <CheckCircle className="w-4 h-4 text-green-600" />
                    <span>Có đề cương</span>
                  </div>
                  <div className="flex gap-2 mt-3">
                    <Button size="sm" variant="outline">Chi tiết</Button>
                    <Button size="sm" variant="outline">Sửa</Button>
                  </div>
                </div>
              ))}
              <Button variant="outline" className="w-full">
                Xem tất cả môn học
              </Button>
            </div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <div className="flex items-center justify-between">
              <CardTitle>Quản lý Lớp học</CardTitle>
              <Button size="sm">
                <Upload className="w-4 h-4 mr-2" />
                Import
              </Button>
            </div>
          </CardHeader>
          <CardContent>
            <div className="space-y-3">
              {mockClasses.map((classItem) => {
                const lecturer = lecturers.find(l => l.id === classItem.lecturerId);
                return (
                  <div key={classItem.id} className="border rounded-lg p-4">
                    <div className="flex items-start justify-between mb-2">
                      <div className="flex-1">
                        <h4 className="font-medium">{classItem.name}</h4>
                        <p className="text-sm text-gray-600 mt-1">
                          Giảng viên: {lecturer?.name}
                        </p>
                      </div>
                      <Badge variant="outline">{classItem.code}</Badge>
                    </div>
                    <div className="flex items-center gap-4 text-sm text-gray-500">
                      <span>{classItem.studentIds.length} sinh viên</span>
                      <span>•</span>
                      <span>{classItem.semester} {classItem.year}</span>
                    </div>
                    <div className="flex gap-2 mt-3">
                      <Button size="sm" variant="outline">Quản lý</Button>
                      <Button size="sm" variant="outline">Thành viên</Button>
                    </div>
                  </div>
                );
              })}
              <Button variant="outline" className="w-full">
                Xem tất cả lớp học
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card>
        <CardHeader>
          <CardTitle>Hành động nhanh</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
            <Button variant="outline" className="h-24 flex-col gap-2">
              <Upload className="w-6 h-6" />
              <span>Import Môn học</span>
            </Button>
            <Button variant="outline" className="h-24 flex-col gap-2">
              <Upload className="w-6 h-6" />
              <span>Import Lớp học</span>
            </Button>
            <Button variant="outline" className="h-24 flex-col gap-2">
              <Upload className="w-6 h-6" />
              <span>Import Tài khoản</span>
            </Button>
            <Button variant="outline" className="h-24 flex-col gap-2">
              <Users className="w-6 h-6" />
              <span>Phân công GV</span>
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
