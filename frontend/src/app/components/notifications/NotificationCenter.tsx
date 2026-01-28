import React, { useState } from 'react';
import { Popover, PopoverContent, PopoverTrigger } from '@/app/components/ui/popover';
import { Button } from '@/app/components/ui/button';
import { Badge } from '@/app/components/ui/badge';
import { ScrollArea } from '@/app/components/ui/scroll-area';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import {
  Bell,
  Check,
  CheckCheck,
  Trash2,
  Mail,
  Users,
  FileText,
  Calendar,
  AlertCircle,
  Info,
} from 'lucide-react';
import { mockNotifications } from '@/app/data/mockData';
import { Notification } from '@/app/types';
import { toast } from 'sonner';
import { useAuth } from '@/app/contexts/AuthContext';

interface NotificationCenterProps {
  onViewAll?: () => void;
}

export const NotificationCenter: React.FC<NotificationCenterProps> = ({ onViewAll }) => {
  const { currentUser } = useAuth();
  const [notifications, setNotifications] = useState<Notification[]>(mockNotifications);
  const [open, setOpen] = useState(false);

  // Filter notifications for current user
  const userNotifications = notifications.filter(n => n.userId === currentUser?.id);
  const unreadCount = userNotifications.filter(n => !n.read).length;

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
    const now = new Date();
    const diffInHours = (now.getTime() - date.getTime()) / (1000 * 60 * 60);

    if (diffInHours < 1) {
      const minutes = Math.floor(diffInHours * 60);
      return `${minutes} phút trước`;
    }
    if (diffInHours < 24) {
      const hours = Math.floor(diffInHours);
      return `${hours} giờ trước`;
    }
    const days = Math.floor(diffInHours / 24);
    return `${days} ngày trước`;
  };

  const realtimeNotifications = userNotifications.filter(n => n.type === 'realtime');
  const emailNotifications = userNotifications.filter(n => n.type === 'email');

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button variant="ghost" size="icon" className="relative">
          <Bell className="w-5 h-5" />
          {unreadCount > 0 && (
            <Badge
              variant="destructive"
              className="absolute -top-1 -right-1 w-5 h-5 p-0 flex items-center justify-center text-xs"
            >
              {unreadCount > 9 ? '9+' : unreadCount}
            </Badge>
          )}
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-96 p-0" align="end">
        <div className="p-4 border-b">
          <div className="flex items-center justify-between">
            <h3 className="font-semibold">Thông báo</h3>
            <div className="flex items-center gap-1">
              {unreadCount > 0 && (
                <Button size="sm" variant="ghost" onClick={markAllAsRead}>
                  <CheckCheck className="w-4 h-4 mr-1" />
                  Đọc tất cả
                </Button>
              )}
              {userNotifications.length > 0 && (
                <Button size="sm" variant="ghost" onClick={deleteAll}>
                  <Trash2 className="w-4 h-4" />
                </Button>
              )}
            </div>
          </div>
        </div>

        <Tabs defaultValue="all" className="w-full">
          <div className="px-4 pt-2">
            <TabsList className="w-full">
              <TabsTrigger value="all" className="flex-1">
                Tất cả
                {unreadCount > 0 && (
                  <Badge variant="secondary" className="ml-2">
                    {unreadCount}
                  </Badge>
                )}
              </TabsTrigger>
              <TabsTrigger value="realtime" className="flex-1">
                Realtime
              </TabsTrigger>
              <TabsTrigger value="email" className="flex-1">
                Email
              </TabsTrigger>
            </TabsList>
          </div>

          <TabsContent value="all" className="m-0">
            <ScrollArea className="h-[400px]">
              {userNotifications.length > 0 ? (
                <div className="divide-y">
                  {userNotifications.map((notification) => (
                    <div
                      key={notification.id}
                      className={`p-4 hover:bg-gray-50 cursor-pointer transition-colors ${
                        !notification.read ? 'bg-blue-50' : ''
                      }`}
                      onClick={() => markAsRead(notification.id)}
                    >
                      <div className="flex items-start gap-3">
                        <div className="mt-0.5">
                          {getNotificationIcon(notification)}
                        </div>
                        <div className="flex-1 min-w-0">
                          <div className="flex items-start justify-between gap-2">
                            <h4 className="font-medium text-sm">{notification.title}</h4>
                            {!notification.read && (
                              <div className="w-2 h-2 bg-blue-600 rounded-full mt-1.5"></div>
                            )}
                          </div>
                          <p className="text-sm text-gray-600 mt-1">{notification.message}</p>
                          <div className="flex items-center justify-between mt-2">
                            <span className="text-xs text-gray-500">
                              {formatTime(notification.createdAt)}
                            </span>
                            <Button
                              size="sm"
                              variant="ghost"
                              onClick={(e) => {
                                e.stopPropagation();
                                deleteNotification(notification.id);
                              }}
                            >
                              <Trash2 className="w-3 h-3" />
                            </Button>
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-12 text-gray-400">
                  <Bell className="w-12 h-12 mx-auto mb-3" />
                  <p>Không có thông báo nào</p>
                </div>
              )}
            </ScrollArea>
            {userNotifications.length > 0 && (
              <div className="border-t p-2">
                <button
                  className="w-full text-center text-sm text-blue-600 hover:bg-blue-50 py-2 rounded transition-colors"
                  onClick={() => {
                    setOpen(false);
                    if (onViewAll) {
                      onViewAll();
                    }
                  }}
                >
                  Xem tất cả thông báo
                </button>
              </div>
            )}
          </TabsContent>

          <TabsContent value="realtime" className="m-0">
            <ScrollArea className="h-[400px]">
              {realtimeNotifications.length > 0 ? (
                <div className="divide-y">
                  {realtimeNotifications.map((notification) => (
                    <div
                      key={notification.id}
                      className={`p-4 hover:bg-gray-50 cursor-pointer ${
                        !notification.read ? 'bg-blue-50' : ''
                      }`}
                      onClick={() => markAsRead(notification.id)}
                    >
                      <div className="flex items-start gap-3">
                        <div className="mt-0.5">
                          {getNotificationIcon(notification)}
                        </div>
                        <div className="flex-1">
                          <h4 className="font-medium text-sm">{notification.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">{notification.message}</p>
                          <span className="text-xs text-gray-500 mt-2 block">
                            {formatTime(notification.createdAt)}
                          </span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-12 text-gray-400">
                  <AlertCircle className="w-12 h-12 mx-auto mb-3" />
                  <p>Không có thông báo realtime</p>
                </div>
              )}
            </ScrollArea>
          </TabsContent>

          <TabsContent value="email" className="m-0">
            <ScrollArea className="h-[400px]">
              {emailNotifications.length > 0 ? (
                <div className="divide-y">
                  {emailNotifications.map((notification) => (
                    <div
                      key={notification.id}
                      className="p-4 hover:bg-gray-50 cursor-pointer"
                      onClick={() => markAsRead(notification.id)}
                    >
                      <div className="flex items-start gap-3">
                        <Mail className="w-5 h-5 text-blue-600 mt-0.5" />
                        <div className="flex-1">
                          <h4 className="font-medium text-sm">{notification.title}</h4>
                          <p className="text-sm text-gray-600 mt-1">{notification.message}</p>
                          <span className="text-xs text-gray-500 mt-2 block">
                            {formatTime(notification.createdAt)}
                          </span>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-12 text-gray-400">
                  <Mail className="w-12 h-12 mx-auto mb-3" />
                  <p>Không có thông báo email</p>
                </div>
              )}
            </ScrollArea>
          </TabsContent>
        </Tabs>
      </PopoverContent>
    </Popover>
  );
};