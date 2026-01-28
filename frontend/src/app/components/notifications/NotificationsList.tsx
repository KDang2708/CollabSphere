import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Badge } from '@/app/components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import { Input } from '@/app/components/ui/input';
import {
  Bell,
  CheckCheck,
  Trash2,
  Mail,
  Users,
  FileText,
  Calendar,
  Info,
  Search,
  Filter,
} from 'lucide-react';
import { mockNotifications } from '@/app/data/mockData';
import { Notification } from '@/app/types';
import { useAuth } from '@/app/contexts/AuthContext';
import { toast } from 'sonner';

export const NotificationsList: React.FC = () => {
  const { currentUser } = useAuth();
  const [notifications, setNotifications] = useState<Notification[]>(mockNotifications);
  const [searchQuery, setSearchQuery] = useState('');
  const [filterType, setFilterType] = useState<'all' | 'realtime' | 'email'>('all');
  const [filterRead, setFilterRead] = useState<'all' | 'read' | 'unread'>('all');

  // Filter notifications for current user
  const userNotifications = notifications
    .filter(n => n.userId === currentUser?.id)
    .filter(n => {
      if (filterType !== 'all' && n.type !== filterType) return false;
      if (filterRead === 'read' && !n.read) return false;
      if (filterRead === 'unread' && n.read) return false;
      if (searchQuery && !n.title.toLowerCase().includes(searchQuery.toLowerCase()) && 
          !n.message.toLowerCase().includes(searchQuery.toLowerCase())) return false;
      return true;
    })
    .sort((a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime());

  const unreadCount = notifications.filter(n => n.userId === currentUser?.id && !n.read).length;

  const markAsRead = (notificationId: string) => {
    setNotifications(notifications.map(n =>
      n.id === notificationId ? { ...n, read: true } : n
    ));
  };

  const markAllAsRead = () => {
    setNotifications(notifications.map(n => 
      n.userId === currentUser?.id ? { ...n, read: true } : n
    ));
    toast.success('Đã đánh dấu tất cả là đã đọc');
  };

  const deleteNotification = (notificationId: string) => {
    setNotifications(notifications.filter(n => n.id !== notificationId));
    toast.success('Đã xóa thông báo');
  };

  const deleteAll = () => {
    if (confirm('Bạn có chắc muốn xóa tất cả thông báo?')) {
      setNotifications(notifications.filter(n => n.userId !== currentUser?.id));
      toast.success('Đã xóa tất cả thông báo');
    }
  };

  const getNotificationIcon = (notification: Notification) => {
    if (notification.title.includes('Milestone')) {
      return <CheckCheck className="w-5 h-5 text-green-600" />;
    }
    if (notification.title.includes('Cuộc họp')) {
      return <Calendar className="w-5 h-5 text-blue-600" />;
    }
    if (notification.title.includes('Tài nguyên')) {
      return <FileText className="w-5 h-5 text-purple-600" />;
    }
    if (notification.title.includes('Đánh giá')) {
      return <Users className="w-5 h-5 text-orange-600" />;
    }
    if (notification.type === 'email') {
      return <Mail className="w-5 h-5 text-blue-600" />;
    }
    return <Info className="w-5 h-5 text-gray-600" />;
  };

  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString('vi-VN', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    });
  };

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-3xl font-bold">Trung tâm Thông báo</h1>
        <p className="text-gray-500 mt-1">Quản lý tất cả thông báo của bạn</p>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-medium text-gray-500">Tổng số thông báo</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold">{userNotifications.length}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-medium text-gray-500">Chưa đọc</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-blue-600">{unreadCount}</div>
          </CardContent>
        </Card>
        <Card>
          <CardHeader className="pb-3">
            <CardTitle className="text-sm font-medium text-gray-500">Đã đọc</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="text-2xl font-bold text-gray-600">{userNotifications.length - unreadCount}</div>
          </CardContent>
        </Card>
      </div>

      {/* Filters and Actions */}
      <Card>
        <CardHeader>
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div className="flex-1 flex items-center gap-2">
              <div className="relative flex-1 max-w-md">
                <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 w-4 h-4 text-gray-400" />
                <Input
                  placeholder="Tìm kiếm thông báo..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="pl-10"
                />
              </div>
            </div>
            <div className="flex items-center gap-2">
              <Button size="sm" variant="outline" onClick={markAllAsRead} disabled={unreadCount === 0}>
                <CheckCheck className="w-4 h-4 mr-2" />
                Đọc tất cả
              </Button>
              <Button size="sm" variant="outline" onClick={deleteAll} disabled={userNotifications.length === 0}>
                <Trash2 className="w-4 h-4 mr-2" />
                Xóa tất cả
              </Button>
            </div>
          </div>
        </CardHeader>
        <CardContent>
          {/* Filter Buttons */}
          <div className="flex flex-wrap gap-2 mb-4">
            <div className="flex items-center gap-2 pr-4 border-r">
              <Filter className="w-4 h-4 text-gray-500" />
              <span className="text-sm font-medium text-gray-500">Loại:</span>
            </div>
            <Button
              size="sm"
              variant={filterType === 'all' ? 'default' : 'outline'}
              onClick={() => setFilterType('all')}
            >
              Tất cả
            </Button>
            <Button
              size="sm"
              variant={filterType === 'realtime' ? 'default' : 'outline'}
              onClick={() => setFilterType('realtime')}
            >
              Realtime
            </Button>
            <Button
              size="sm"
              variant={filterType === 'email' ? 'default' : 'outline'}
              onClick={() => setFilterType('email')}
            >
              Email
            </Button>

            <div className="flex items-center gap-2 pl-4 ml-4 border-l">
              <span className="text-sm font-medium text-gray-500">Trạng thái:</span>
            </div>
            <Button
              size="sm"
              variant={filterRead === 'all' ? 'default' : 'outline'}
              onClick={() => setFilterRead('all')}
            >
              Tất cả
            </Button>
            <Button
              size="sm"
              variant={filterRead === 'unread' ? 'default' : 'outline'}
              onClick={() => setFilterRead('unread')}
            >
              Chưa đọc
            </Button>
            <Button
              size="sm"
              variant={filterRead === 'read' ? 'default' : 'outline'}
              onClick={() => setFilterRead('read')}
            >
              Đã đọc
            </Button>
          </div>

          {/* Notifications List */}
          <div className="space-y-2">
            {userNotifications.length > 0 ? (
              userNotifications.map((notification) => (
                <div
                  key={notification.id}
                  className={`p-4 border rounded-lg transition-colors ${
                    !notification.read ? 'bg-blue-50 border-blue-200' : 'bg-white hover:bg-gray-50'
                  }`}
                >
                  <div className="flex items-start gap-4">
                    <div className="mt-1">
                      {getNotificationIcon(notification)}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="flex items-start justify-between gap-2">
                        <div className="flex items-center gap-2">
                          <h4 className="font-semibold">{notification.title}</h4>
                          {!notification.read && (
                            <Badge variant="default" className="text-xs">Mới</Badge>
                          )}
                          <Badge variant="outline" className="text-xs">
                            {notification.type === 'realtime' ? 'Realtime' : 'Email'}
                          </Badge>
                        </div>
                        <div className="flex items-center gap-1">
                          {!notification.read && (
                            <Button
                              size="sm"
                              variant="ghost"
                              onClick={() => markAsRead(notification.id)}
                            >
                              <CheckCheck className="w-4 h-4" />
                            </Button>
                          )}
                          <Button
                            size="sm"
                            variant="ghost"
                            onClick={() => deleteNotification(notification.id)}
                          >
                            <Trash2 className="w-4 h-4 text-red-600" />
                          </Button>
                        </div>
                      </div>
                      <p className="text-gray-600 mt-1">{notification.message}</p>
                      <p className="text-sm text-gray-400 mt-2">{formatTime(notification.createdAt)}</p>
                    </div>
                  </div>
                </div>
              ))
            ) : (
              <div className="text-center py-12">
                <Bell className="w-16 h-16 mx-auto text-gray-300 mb-4" />
                <h3 className="text-lg font-medium text-gray-900 mb-1">Không có thông báo nào</h3>
                <p className="text-gray-500">
                  {searchQuery
                    ? 'Không tìm thấy thông báo phù hợp với tìm kiếm của bạn'
                    : 'Bạn không có thông báo nào với bộ lọc hiện tại'}
                </p>
              </div>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
