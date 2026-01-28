import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Label } from '@/app/components/ui/label';
import { Switch } from '@/app/components/ui/switch';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/app/components/ui/select';
import { Separator } from '@/app/components/ui/separator';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import {
  Bell,
  Globe,
  Palette,
  Volume2,
  Monitor,
  Smartphone,
  Moon,
  Sun,
  Languages,
  Save,
} from 'lucide-react';
import { toast } from 'sonner';

export const Settings: React.FC = () => {
  const [settings, setSettings] = useState({
    // Notifications
    emailNotifications: true,
    pushNotifications: true,
    meetingReminders: true,
    projectUpdates: true,
    teamMessages: true,
    
    // Appearance
    theme: 'light',
    language: 'vi',
    fontSize: 'medium',
    
    // Sound
    soundEnabled: true,
    notificationSound: true,
    messageTone: true,
  });

  const handleSave = () => {
    toast.success('Cài đặt đã được lưu');
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div>
        <h1 className="text-3xl font-bold">Cài đặt</h1>
        <p className="text-gray-500 mt-1">Quản lý các tùy chọn và cài đặt của bạn</p>
      </div>

      <Tabs defaultValue="notifications" className="w-full">
        <TabsList className="grid w-full grid-cols-3">
          <TabsTrigger value="notifications">
            <Bell className="w-4 h-4 mr-2" />
            Thông báo
          </TabsTrigger>
          <TabsTrigger value="appearance">
            <Palette className="w-4 h-4 mr-2" />
            Giao diện
          </TabsTrigger>
          <TabsTrigger value="sound">
            <Volume2 className="w-4 h-4 mr-2" />
            Âm thanh
          </TabsTrigger>
        </TabsList>

        {/* Notifications Tab */}
        <TabsContent value="notifications">
          <Card>
            <CardHeader>
              <CardTitle>Cài đặt Thông báo</CardTitle>
              <CardDescription>
                Quản lý cách bạn nhận thông báo từ hệ thống
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              {/* Email Notifications */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Thông báo Email</Label>
                  <p className="text-sm text-gray-500">
                    Nhận thông báo qua email
                  </p>
                </div>
                <Switch
                  checked={settings.emailNotifications}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, emailNotifications: checked })
                  }
                />
              </div>

              <Separator />

              {/* Push Notifications */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Thông báo đẩy</Label>
                  <p className="text-sm text-gray-500">
                    Nhận thông báo đẩy trên trình duyệt
                  </p>
                </div>
                <Switch
                  checked={settings.pushNotifications}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, pushNotifications: checked })
                  }
                />
              </div>

              <Separator />

              {/* Meeting Reminders */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Nhắc nhở cuộc họp</Label>
                  <p className="text-sm text-gray-500">
                    Nhận thông báo trước khi cuộc họp bắt đầu
                  </p>
                </div>
                <Switch
                  checked={settings.meetingReminders}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, meetingReminders: checked })
                  }
                />
              </div>

              <Separator />

              {/* Project Updates */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Cập nhật dự án</Label>
                  <p className="text-sm text-gray-500">
                    Nhận thông báo về tiến độ và milestone của dự án
                  </p>
                </div>
                <Switch
                  checked={settings.projectUpdates}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, projectUpdates: checked })
                  }
                />
              </div>

              <Separator />

              {/* Team Messages */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Tin nhắn nhóm</Label>
                  <p className="text-sm text-gray-500">
                    Nhận thông báo khi có tin nhắn mới trong nhóm
                  </p>
                </div>
                <Switch
                  checked={settings.teamMessages}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, teamMessages: checked })
                  }
                />
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Appearance Tab */}
        <TabsContent value="appearance">
          <Card>
            <CardHeader>
              <CardTitle>Cài đặt Giao diện</CardTitle>
              <CardDescription>
                Tùy chỉnh giao diện và ngôn ngữ hiển thị
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              {/* Theme */}
              <div className="space-y-2">
                <Label>Chủ đề</Label>
                <div className="grid grid-cols-3 gap-3">
                  <button
                    onClick={() => setSettings({ ...settings, theme: 'light' })}
                    className={`flex flex-col items-center gap-2 p-4 border-2 rounded-lg transition-colors ${
                      settings.theme === 'light'
                        ? 'border-blue-600 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <Sun className="w-6 h-6" />
                    <span className="text-sm font-medium">Sáng</span>
                  </button>
                  <button
                    onClick={() => setSettings({ ...settings, theme: 'dark' })}
                    className={`flex flex-col items-center gap-2 p-4 border-2 rounded-lg transition-colors ${
                      settings.theme === 'dark'
                        ? 'border-blue-600 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <Moon className="w-6 h-6" />
                    <span className="text-sm font-medium">Tối</span>
                  </button>
                  <button
                    onClick={() => setSettings({ ...settings, theme: 'system' })}
                    className={`flex flex-col items-center gap-2 p-4 border-2 rounded-lg transition-colors ${
                      settings.theme === 'system'
                        ? 'border-blue-600 bg-blue-50'
                        : 'border-gray-200 hover:border-gray-300'
                    }`}
                  >
                    <Monitor className="w-6 h-6" />
                    <span className="text-sm font-medium">Hệ thống</span>
                  </button>
                </div>
              </div>

              <Separator />

              {/* Language */}
              <div className="space-y-2">
                <Label htmlFor="language">Ngôn ngữ</Label>
                <Select
                  value={settings.language}
                  onValueChange={(value) => setSettings({ ...settings, language: value })}
                >
                  <SelectTrigger id="language">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="vi">
                      <div className="flex items-center gap-2">
                        <Languages className="w-4 h-4" />
                        Tiếng Việt
                      </div>
                    </SelectItem>
                    <SelectItem value="en">
                      <div className="flex items-center gap-2">
                        <Globe className="w-4 h-4" />
                        English
                      </div>
                    </SelectItem>
                  </SelectContent>
                </Select>
              </div>

              <Separator />

              {/* Font Size */}
              <div className="space-y-2">
                <Label htmlFor="fontSize">Kích thước chữ</Label>
                <Select
                  value={settings.fontSize}
                  onValueChange={(value) => setSettings({ ...settings, fontSize: value })}
                >
                  <SelectTrigger id="fontSize">
                    <SelectValue />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="small">Nhỏ</SelectItem>
                    <SelectItem value="medium">Trung bình</SelectItem>
                    <SelectItem value="large">Lớn</SelectItem>
                  </SelectContent>
                </Select>
              </div>
            </CardContent>
          </Card>
        </TabsContent>

        {/* Sound Tab */}
        <TabsContent value="sound">
          <Card>
            <CardHeader>
              <CardTitle>Cài đặt Âm thanh</CardTitle>
              <CardDescription>
                Quản lý âm thanh và nhạc chuông thông báo
              </CardDescription>
            </CardHeader>
            <CardContent className="space-y-6">
              {/* Sound Enabled */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Bật âm thanh</Label>
                  <p className="text-sm text-gray-500">
                    Bật/tắt tất cả âm thanh trong ứng dụng
                  </p>
                </div>
                <Switch
                  checked={settings.soundEnabled}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, soundEnabled: checked })
                  }
                />
              </div>

              <Separator />

              {/* Notification Sound */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Âm thanh thông báo</Label>
                  <p className="text-sm text-gray-500">
                    Phát âm thanh khi có thông báo mới
                  </p>
                </div>
                <Switch
                  checked={settings.notificationSound}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, notificationSound: checked })
                  }
                  disabled={!settings.soundEnabled}
                />
              </div>

              <Separator />

              {/* Message Tone */}
              <div className="flex items-center justify-between">
                <div className="space-y-0.5">
                  <Label>Âm báo tin nhắn</Label>
                  <p className="text-sm text-gray-500">
                    Phát âm thanh khi nhận tin nhắn mới
                  </p>
                </div>
                <Switch
                  checked={settings.messageTone}
                  onCheckedChange={(checked) =>
                    setSettings({ ...settings, messageTone: checked })
                  }
                  disabled={!settings.soundEnabled}
                />
              </div>
            </CardContent>
          </Card>
        </TabsContent>
      </Tabs>

      {/* Save Button */}
      <div className="flex justify-end">
        <Button onClick={handleSave} size="lg">
          <Save className="w-4 h-4 mr-2" />
          Lưu thay đổi
        </Button>
      </div>
    </div>
  );
};
