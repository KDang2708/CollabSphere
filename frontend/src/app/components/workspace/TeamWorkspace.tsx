import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Input } from '../ui/input';
import { Textarea } from '../ui/textarea';
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '../ui/dialog';
import { Label } from '../ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../ui/select';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs';
import { DndProvider, useDrag, useDrop } from 'react-dnd';
import { HTML5Backend } from 'react-dnd-html5-backend';
import {
  Plus,
  MoreVertical,
  User,
  Calendar,
  Flag,
  MessageSquare,
  Paperclip,
  CheckSquare,
} from 'lucide-react';
import { Task } from '../../types';
import { mockUsers } from '../../data/mockData';

interface TaskCardProps {
  task: Task;
  onMove: (taskId: string, newStatus: Task['status']) => void;
}

const TaskCard: React.FC<TaskCardProps> = ({ task, onMove }) => {
  const [{ isDragging }, drag] = useDrag({
    type: 'TASK',
    item: { id: task.id, status: task.status },
    collect: (monitor) => ({
      isDragging: monitor.isDragging(),
    }),
  });

  const getPriorityColor = (priority: string) => {
    switch (priority) {
      case 'high':
        return 'bg-red-100 text-red-700 border-red-200';
      case 'medium':
        return 'bg-yellow-100 text-yellow-700 border-yellow-200';
      case 'low':
        return 'bg-green-100 text-green-700 border-green-200';
      default:
        return 'bg-gray-100 text-gray-700 border-gray-200';
    }
  };

  const assignedUsers = mockUsers.filter(u => task.assignedTo.includes(u.id));

  return (
    <div
      ref={drag}
      className={`bg-white border rounded-lg p-3 cursor-move hover:shadow-md transition-shadow ${
        isDragging ? 'opacity-50' : ''
      }`}
    >
      <div className="flex items-start justify-between mb-2">
        <h4 className="font-medium text-sm">{task.title}</h4>
        <Button variant="ghost" size="sm" className="h-6 w-6 p-0">
          <MoreVertical className="w-4 h-4" />
        </Button>
      </div>

      <p className="text-sm text-gray-600 mb-3">{task.description}</p>

      {task.subtasks.length > 0 && (
        <div className="flex items-center gap-2 mb-3 text-sm text-gray-500">
          <CheckSquare className="w-4 h-4" />
          <span>
            {task.subtasks.filter(st => st.completed).length}/{task.subtasks.length}
          </span>
        </div>
      )}

      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <Badge variant="outline" className={getPriorityColor(task.priority)}>
            {task.priority === 'high' && 'Cao'}
            {task.priority === 'medium' && 'Trung bình'}
            {task.priority === 'low' && 'Thấp'}
          </Badge>
          <div className="flex items-center gap-1 text-xs text-gray-500">
            <Calendar className="w-3 h-3" />
            <span>{task.dueDate}</span>
          </div>
        </div>

        <div className="flex -space-x-2">
          {assignedUsers.slice(0, 3).map((user) => {
            const initials = user.name
              .split(' ')
              .map(n => n[0])
              .join('')
              .toUpperCase()
              .slice(0, 2);
            return (
              <div
                key={user.id}
                className="w-6 h-6 rounded-full bg-blue-600 text-white text-xs flex items-center justify-center border-2 border-white"
                title={user.name}
              >
                {initials}
              </div>
            );
          })}
          {assignedUsers.length > 3 && (
            <div className="w-6 h-6 rounded-full bg-gray-200 text-gray-600 text-xs flex items-center justify-center border-2 border-white">
              +{assignedUsers.length - 3}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

interface ColumnProps {
  title: string;
  status: Task['status'];
  tasks: Task[];
  onMove: (taskId: string, newStatus: Task['status']) => void;
}

const Column: React.FC<ColumnProps> = ({ title, status, tasks, onMove }) => {
  const [{ isOver }, drop] = useDrop({
    accept: 'TASK',
    drop: (item: { id: string; status: Task['status'] }) => {
      if (item.status !== status) {
        onMove(item.id, status);
      }
    },
    collect: (monitor) => ({
      isOver: monitor.isOver(),
    }),
  });

  const getColumnColor = () => {
    switch (status) {
      case 'todo':
        return 'border-gray-300 bg-gray-50';
      case 'in-progress':
        return 'border-blue-300 bg-blue-50';
      case 'review':
        return 'border-yellow-300 bg-yellow-50';
      case 'done':
        return 'border-green-300 bg-green-50';
      default:
        return 'border-gray-300 bg-gray-50';
    }
  };

  return (
    <div className="flex-1 min-w-[280px]">
      <div className={`border-2 rounded-lg p-4 h-full ${getColumnColor()} ${isOver ? 'ring-2 ring-blue-500' : ''}`} ref={drop}>
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <h3 className="font-semibold">{title}</h3>
            <Badge variant="secondary">{tasks.length}</Badge>
          </div>
          <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
            <Plus className="w-4 h-4" />
          </Button>
        </div>

        <div className="space-y-3">
          {tasks.map((task) => (
            <TaskCard key={task.id} task={task} onMove={onMove} />
          ))}
        </div>
      </div>
    </div>
  );
};

export const TeamWorkspace: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([
    {
      id: 'task1',
      title: 'Thiết kế giao diện đăng nhập',
      description: 'Tạo mockup và prototype cho màn hình đăng nhập',
      assignedTo: ['stu1', 'stu2'],
      status: 'done',
      priority: 'high',
      dueDate: '2025-02-05',
      subtasks: [
        { id: 'st1', title: 'Wireframe', completed: true },
        { id: 'st2', title: 'Hi-fi design', completed: true },
      ],
      createdBy: 'stu1',
    },
    {
      id: 'task2',
      title: 'Xây dựng API Authentication',
      description: 'Phát triển endpoints cho đăng nhập, đăng ký, và quản lý session',
      assignedTo: ['stu3'],
      status: 'in-progress',
      priority: 'high',
      dueDate: '2025-02-10',
      subtasks: [
        { id: 'st3', title: 'Login endpoint', completed: true },
        { id: 'st4', title: 'Register endpoint', completed: false },
        { id: 'st5', title: 'Session management', completed: false },
      ],
      createdBy: 'stu1',
    },
    {
      id: 'task3',
      title: 'Thiết kế cơ sở dữ liệu',
      description: 'Tạo ERD và schema cho database',
      assignedTo: ['stu2', 'stu3'],
      status: 'review',
      priority: 'medium',
      dueDate: '2025-02-08',
      subtasks: [],
      createdBy: 'stu1',
    },
    {
      id: 'task4',
      title: 'Viết tài liệu API',
      description: 'Tạo documentation cho các API endpoints',
      assignedTo: ['stu1'],
      status: 'todo',
      priority: 'low',
      dueDate: '2025-02-15',
      subtasks: [],
      createdBy: 'stu2',
    },
    {
      id: 'task5',
      title: 'Unit Testing',
      description: 'Viết test cases cho authentication module',
      assignedTo: ['stu2'],
      status: 'todo',
      priority: 'medium',
      dueDate: '2025-02-12',
      subtasks: [],
      createdBy: 'stu1',
    },
  ]);

  const [isCreateDialogOpen, setIsCreateDialogOpen] = useState(false);

  const handleMoveTask = (taskId: string, newStatus: Task['status']) => {
    setTasks(prevTasks =>
      prevTasks.map(task =>
        task.id === taskId ? { ...task, status: newStatus } : task
      )
    );
  };

  const todoTasks = tasks.filter(t => t.status === 'todo');
  const inProgressTasks = tasks.filter(t => t.status === 'in-progress');
  const reviewTasks = tasks.filter(t => t.status === 'review');
  const doneTasks = tasks.filter(t => t.status === 'done');

  return (
    <DndProvider backend={HTML5Backend}>
      <div className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold">Không gian làm việc nhóm</h1>
            <p className="text-gray-600">Quản lý nhiệm vụ và theo dõi tiến độ</p>
          </div>
          <Dialog open={isCreateDialogOpen} onOpenChange={setIsCreateDialogOpen}>
            <DialogTrigger asChild>
              <Button>
                <Plus className="w-4 h-4 mr-2" />
                Tạo nhiệm vụ
              </Button>
            </DialogTrigger>
            <DialogContent className="max-w-2xl">
              <DialogHeader>
                <DialogTitle>Tạo nhiệm vụ mới</DialogTitle>
                <DialogDescription>
                  Thêm nhiệm vụ mới vào workspace của nhóm
                </DialogDescription>
              </DialogHeader>
              <div className="space-y-4">
                <div className="space-y-2">
                  <Label htmlFor="title">Tiêu đề</Label>
                  <Input id="title" placeholder="Nhập tiêu đề nhiệm vụ" />
                </div>
                <div className="space-y-2">
                  <Label htmlFor="description">Mô tả</Label>
                  <Textarea id="description" placeholder="Mô tả chi tiết nhiệm vụ" rows={3} />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div className="space-y-2">
                    <Label htmlFor="priority">Độ ưu tiên</Label>
                    <Select defaultValue="medium">
                      <SelectTrigger>
                        <SelectValue />
                      </SelectTrigger>
                      <SelectContent>
                        <SelectItem value="low">Thấp</SelectItem>
                        <SelectItem value="medium">Trung bình</SelectItem>
                        <SelectItem value="high">Cao</SelectItem>
                      </SelectContent>
                    </Select>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="dueDate">Hạn hoàn thành</Label>
                    <Input id="dueDate" type="date" />
                  </div>
                </div>
                <div className="space-y-2">
                  <Label>Phân công cho</Label>
                  <Select>
                    <SelectTrigger>
                      <SelectValue placeholder="Chọn thành viên" />
                    </SelectTrigger>
                    <SelectContent>
                      {mockUsers.filter(u => u.role === 'student').map(user => (
                        <SelectItem key={user.id} value={user.id}>
                          {user.name}
                        </SelectItem>
                      ))}
                    </SelectContent>
                  </Select>
                </div>
                <div className="flex justify-end gap-2">
                  <Button variant="outline" onClick={() => setIsCreateDialogOpen(false)}>
                    Hủy
                  </Button>
                  <Button onClick={() => setIsCreateDialogOpen(false)}>
                    Tạo nhiệm vụ
                  </Button>
                </div>
              </div>
            </DialogContent>
          </Dialog>
        </div>

        <Tabs defaultValue="kanban">
          <TabsList>
            <TabsTrigger value="kanban">Kanban Board</TabsTrigger>
            <TabsTrigger value="list">Danh sách</TabsTrigger>
            <TabsTrigger value="timeline">Timeline</TabsTrigger>
          </TabsList>

          <TabsContent value="kanban" className="mt-6">
            <div className="flex gap-4 overflow-x-auto pb-4">
              <Column
                title="Cần làm"
                status="todo"
                tasks={todoTasks}
                onMove={handleMoveTask}
              />
              <Column
                title="Đang thực hiện"
                status="in-progress"
                tasks={inProgressTasks}
                onMove={handleMoveTask}
              />
              <Column
                title="Đang review"
                status="review"
                tasks={reviewTasks}
                onMove={handleMoveTask}
              />
              <Column
                title="Hoàn thành"
                status="done"
                tasks={doneTasks}
                onMove={handleMoveTask}
              />
            </div>
          </TabsContent>

          <TabsContent value="list" className="mt-6">
            <Card>
              <CardContent className="p-6">
                <div className="space-y-3">
                  {tasks.map(task => {
                    const assignedUsers = mockUsers.filter(u => task.assignedTo.includes(u.id));
                    return (
                      <div key={task.id} className="border rounded-lg p-4">
                        <div className="flex items-start justify-between">
                          <div className="flex-1">
                            <h4 className="font-medium">{task.title}</h4>
                            <p className="text-sm text-gray-600 mt-1">{task.description}</p>
                            <div className="flex items-center gap-4 mt-3">
                              <Badge variant="outline">{task.status}</Badge>
                              <Badge variant="outline" className={
                                task.priority === 'high' ? 'bg-red-50 text-red-700' :
                                task.priority === 'medium' ? 'bg-yellow-50 text-yellow-700' :
                                'bg-green-50 text-green-700'
                              }>
                                {task.priority}
                              </Badge>
                              <span className="text-sm text-gray-500">{task.dueDate}</span>
                            </div>
                          </div>
                          <div className="flex -space-x-2">
                            {assignedUsers.map(user => {
                              const initials = user.name.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2);
                              return (
                                <div
                                  key={user.id}
                                  className="w-8 h-8 rounded-full bg-blue-600 text-white text-xs flex items-center justify-center border-2 border-white"
                                  title={user.name}
                                >
                                  {initials}
                                </div>
                              );
                            })}
                          </div>
                        </div>
                      </div>
                    );
                  })}
                </div>
              </CardContent>
            </Card>
          </TabsContent>

          <TabsContent value="timeline" className="mt-6">
            <Card>
              <CardContent className="p-6">
                <div className="text-center py-12 text-gray-500">
                  <Calendar className="w-12 h-12 mx-auto mb-3 text-gray-400" />
                  <p>Timeline view sẽ hiển thị lịch trình các nhiệm vụ</p>
                </div>
              </CardContent>
            </Card>
          </TabsContent>
        </Tabs>
      </div>
    </DndProvider>
  );
};
