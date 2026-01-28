import React, { useState } from 'react';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/app/components/ui/dialog';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Label } from '@/app/components/ui/label';
import { Textarea } from '@/app/components/ui/textarea';
import { Card } from '@/app/components/ui/card';
import { Badge } from '@/app/components/ui/badge';
import { Avatar, AvatarFallback } from '@/app/components/ui/avatar';
import { Checkbox } from '@/app/components/ui/checkbox';
import { Calendar, Clock, Users, Video, Loader2, Bell } from 'lucide-react';
import { toast } from 'sonner';
import { mockUsers, mockMeetings } from '@/app/data/mockData';
import { Meeting } from '@/app/types';

interface MeetingSchedulerProps {
  open: boolean;
  onClose: () => void;
  onSchedule: (meeting: Meeting) => void;
  teamMembers?: string[];
}

export const MeetingScheduler: React.FC<MeetingSchedulerProps> = ({
  open,
  onClose,
  onSchedule,
  teamMembers = [],
}) => {
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    title: '',
    description: '',
    date: '',
    time: '',
    duration: '60',
    participants: teamMembers,
    sendNotification: true,
    sendReminder: true,
  });

  const availableMembers = mockUsers.filter(u => 
    u.role === 'student' || u.role === 'lecturer'
  );

  const handleToggleParticipant = (userId: string) => {
    if (formData.participants.includes(userId)) {
      setFormData({
        ...formData,
        participants: formData.participants.filter(id => id !== userId),
      });
    } else {
      setFormData({
        ...formData,
        participants: [...formData.participants, userId],
      });
    }
  };

  const handleSubmit = () => {
    if (!formData.title || !formData.date || !formData.time) {
      toast.error('Vui lòng điền đầy đủ thông tin');
      return;
    }

    if (formData.participants.length === 0) {
      toast.error('Vui lòng chọn ít nhất một người tham gia');
      return;
    }

    setLoading(true);

    setTimeout(() => {
      const meeting: Meeting = {
        id: `meet-${Date.now()}`,
        title: formData.title,
        scheduledAt: `${formData.date} ${formData.time}`,
        duration: parseInt(formData.duration),
        participants: formData.participants,
        organizer: 'current-user',
        status: 'scheduled',
      };

      onSchedule(meeting);
      toast.success('Đã lên lịch cuộc họp thành công');
      
      if (formData.sendNotification) {
        toast.info('Thông báo đã được gửi đến người tham gia');
      }

      setLoading(false);
      onClose();
    }, 1000);
  };

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Video className="w-5 h-5 text-blue-600" />
            Lên lịch cuộc họp
          </DialogTitle>
          <DialogDescription>
            Tạo cuộc họp mới và mời thành viên tham gia
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-6 py-4">
          {/* Basic Info */}
          <div className="space-y-4">
            <div>
              <Label htmlFor="title">Tiêu đề cuộc họp *</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                placeholder="VD: Sprint Planning Meeting"
              />
            </div>

            <div>
              <Label htmlFor="description">Mô tả</Label>
              <Textarea
                id="description"
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                placeholder="Nội dung và mục đích cuộc họp..."
                rows={3}
              />
            </div>
          </div>

          {/* Date & Time */}
          <div className="grid grid-cols-2 gap-4">
            <div>
              <Label htmlFor="date">Ngày họp *</Label>
              <div className="flex items-center gap-2 mt-1">
                <Calendar className="w-4 h-4 text-gray-400" />
                <Input
                  type="date"
                  id="date"
                  value={formData.date}
                  onChange={(e) => setFormData({ ...formData, date: e.target.value })}
                  min={new Date().toISOString().split('T')[0]}
                />
              </div>
            </div>

            <div>
              <Label htmlFor="time">Giờ họp *</Label>
              <div className="flex items-center gap-2 mt-1">
                <Clock className="w-4 h-4 text-gray-400" />
                <Input
                  type="time"
                  id="time"
                  value={formData.time}
                  onChange={(e) => setFormData({ ...formData, time: e.target.value })}
                />
              </div>
            </div>
          </div>

          {/* Duration */}
          <div>
            <Label htmlFor="duration">Thời lượng (phút)</Label>
            <select
              id="duration"
              value={formData.duration}
              onChange={(e) => setFormData({ ...formData, duration: e.target.value })}
              className="w-full px-3 py-2 border rounded-md mt-1"
            >
              <option value="15">15 phút</option>
              <option value="30">30 phút</option>
              <option value="45">45 phút</option>
              <option value="60">1 giờ</option>
              <option value="90">1.5 giờ</option>
              <option value="120">2 giờ</option>
            </select>
          </div>

          {/* Participants */}
          <div>
            <Label className="mb-3 block">
              Người tham gia * ({formData.participants.length})
            </Label>
            <Card className="p-4 max-h-60 overflow-y-auto">
              <div className="space-y-3">
                {availableMembers.map((member) => (
                  <div
                    key={member.id}
                    className="flex items-center justify-between p-2 hover:bg-gray-50 rounded-lg"
                  >
                    <div className="flex items-center gap-3">
                      <Checkbox
                        checked={formData.participants.includes(member.id)}
                        onCheckedChange={() => handleToggleParticipant(member.id)}
                      />
                      <Avatar className="w-8 h-8">
                        <AvatarFallback>{member.name.charAt(0)}</AvatarFallback>
                      </Avatar>
                      <div>
                        <p className="font-medium text-sm">{member.name}</p>
                        <p className="text-xs text-gray-500">{member.email}</p>
                      </div>
                    </div>
                    <Badge variant="outline">
                      {member.role === 'lecturer' ? 'Giảng viên' : 'Sinh viên'}
                    </Badge>
                  </div>
                ))}
              </div>
            </Card>
          </div>

          {/* Notification Options */}
          <Card className="p-4 bg-gray-50">
            <h4 className="font-medium mb-3 flex items-center gap-2">
              <Bell className="w-4 h-4" />
              Tùy chọn thông báo
            </h4>
            <div className="space-y-3">
              <div className="flex items-center gap-2">
                <Checkbox
                  checked={formData.sendNotification}
                  onCheckedChange={(checked) =>
                    setFormData({ ...formData, sendNotification: !!checked })
                  }
                />
                <Label className="cursor-pointer">
                  Gửi email thông báo cho người tham gia
                </Label>
              </div>
              <div className="flex items-center gap-2">
                <Checkbox
                  checked={formData.sendReminder}
                  onCheckedChange={(checked) =>
                    setFormData({ ...formData, sendReminder: !!checked })
                  }
                />
                <Label className="cursor-pointer">
                  Gửi nhắc nhở trước cuộc họp 15 phút
                </Label>
              </div>
            </div>
          </Card>

          {/* Meeting Link Info */}
          <Card className="p-4 bg-blue-50 border-blue-200">
            <div className="flex items-start gap-3">
              <Video className="w-5 h-5 text-blue-600 mt-0.5" />
              <div>
                <h4 className="font-medium text-sm mb-1">Liên kết cuộc họp</h4>
                <p className="text-sm text-gray-600">
                  Liên kết video meeting sẽ được tự động tạo và gửi đến người tham gia khi lên lịch thành công.
                </p>
              </div>
            </div>
          </Card>
        </div>

        <DialogFooter>
          <Button variant="outline" onClick={onClose} disabled={loading}>
            Hủy
          </Button>
          <Button onClick={handleSubmit} disabled={loading}>
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                Đang lên lịch...
              </>
            ) : (
              <>
                <Calendar className="w-4 h-4 mr-2" />
                Lên lịch
              </>
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
