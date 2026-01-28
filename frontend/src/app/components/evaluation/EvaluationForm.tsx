import React, { useState } from 'react';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/app/components/ui/dialog';
import { Button } from '@/app/components/ui/button';
import { Label } from '@/app/components/ui/label';
import { Textarea } from '@/app/components/ui/textarea';
import { Slider } from '@/app/components/ui/slider';
import { Avatar, AvatarFallback } from '@/app/components/ui/avatar';
import { Card } from '@/app/components/ui/card';
import { Badge } from '@/app/components/ui/badge';
import { Star, Loader2, ThumbsUp } from 'lucide-react';
import { toast } from 'sonner';

interface EvaluationFormProps {
  open: boolean;
  onClose: () => void;
  onSubmit: (evaluation: any) => void;
  targetUser?: any;
  targetTeam?: any;
  type: 'team' | 'member' | 'milestone' | 'checkpoint';
  title?: string;
}

export const EvaluationForm: React.FC<EvaluationFormProps> = ({
  open,
  onClose,
  onSubmit,
  targetUser,
  targetTeam,
  type,
  title,
}) => {
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    rating: [7.5],
    comment: '',
    criteria: {
      quality: [7],
      teamwork: [8],
      communication: [7],
      technical: [7],
      creativity: [8],
    },
  });

  const handleSubmit = () => {
    if (!formData.comment.trim()) {
      toast.error('Vui lòng nhập nhận xét');
      return;
    }

    setLoading(true);
    setTimeout(() => {
      const evaluation = {
        id: `eval-${Date.now()}`,
        type,
        rating: formData.rating[0],
        comment: formData.comment,
        criteria: type === 'member' || type === 'team' ? {
          quality: formData.criteria.quality[0],
          teamwork: formData.criteria.teamwork[0],
          communication: formData.criteria.communication[0],
          technical: formData.criteria.technical[0],
          creativity: formData.criteria.creativity[0],
        } : undefined,
        targetUserId: targetUser?.id,
        targetTeamId: targetTeam?.id,
        createdAt: new Date().toISOString(),
      };

      onSubmit(evaluation);
      toast.success('Đánh giá đã được gửi thành công');
      setLoading(false);
      onClose();
    }, 1000);
  };

  const getRatingLabel = (value: number) => {
    if (value >= 9) return 'Xuất sắc';
    if (value >= 8) return 'Tốt';
    if (value >= 6.5) return 'Khá';
    if (value >= 5) return 'Trung bình';
    return 'Cần cải thiện';
  };

  const getRatingColor = (value: number) => {
    if (value >= 9) return 'text-green-600';
    if (value >= 8) return 'text-blue-600';
    if (value >= 6.5) return 'text-yellow-600';
    if (value >= 5) return 'text-orange-600';
    return 'text-red-600';
  };

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-2xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-2">
            <Star className="w-5 h-5 text-yellow-500" />
            {title || 'Đánh giá & Phản hồi'}
          </DialogTitle>
          <DialogDescription>
            {type === 'team' && 'Đánh giá hiệu suất và đóng góp của nhóm'}
            {type === 'member' && 'Đánh giá đóng góp của thành viên'}
            {type === 'milestone' && 'Đánh giá câu trả lời milestone'}
            {type === 'checkpoint' && 'Đánh giá bài nộp checkpoint'}
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-6 py-4">
          {/* Target Info */}
          {targetUser && (
            <Card className="p-4 bg-gray-50">
              <div className="flex items-center gap-3">
                <Avatar>
                  <AvatarFallback>{targetUser.name.charAt(0)}</AvatarFallback>
                </Avatar>
                <div>
                  <h4 className="font-medium">{targetUser.name}</h4>
                  <p className="text-sm text-gray-600">{targetUser.email}</p>
                </div>
              </div>
            </Card>
          )}

          {targetTeam && (
            <Card className="p-4 bg-gray-50">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="font-medium">{targetTeam.name}</h4>
                  <p className="text-sm text-gray-600">{targetTeam.memberIds.length} thành viên</p>
                </div>
                <Badge>Tiến độ: {targetTeam.progress}%</Badge>
              </div>
            </Card>
          )}

          {/* Overall Rating */}
          <div>
            <div className="flex items-center justify-between mb-3">
              <Label>Điểm đánh giá tổng thể</Label>
              <div className="flex items-center gap-2">
                <span className={`text-2xl font-bold ${getRatingColor(formData.rating[0])}`}>
                  {formData.rating[0].toFixed(1)}
                </span>
                <span className="text-sm text-gray-500">/ 10</span>
              </div>
            </div>
            <Slider
              value={formData.rating}
              onValueChange={(value) => setFormData({ ...formData, rating: value })}
              min={0}
              max={10}
              step={0.5}
              className="mb-2"
            />
            <div className="flex items-center justify-between text-sm">
              <span className="text-gray-500">Kéo để chấm điểm</span>
              <Badge variant="outline" className={getRatingColor(formData.rating[0])}>
                {getRatingLabel(formData.rating[0])}
              </Badge>
            </div>
          </div>

          {/* Detailed Criteria (for team/member evaluation) */}
          {(type === 'team' || type === 'member') && (
            <div className="space-y-4">
              <h4 className="font-medium">Tiêu chí chi tiết</h4>
              
              <div>
                <div className="flex items-center justify-between mb-2">
                  <Label className="text-sm">Chất lượng công việc</Label>
                  <span className="text-sm font-medium">{formData.criteria.quality[0]}/10</span>
                </div>
                <Slider
                  value={formData.criteria.quality}
                  onValueChange={(value) => setFormData({
                    ...formData,
                    criteria: { ...formData.criteria, quality: value }
                  })}
                  min={0}
                  max={10}
                  step={0.5}
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <Label className="text-sm">Kỹ năng làm việc nhóm</Label>
                  <span className="text-sm font-medium">{formData.criteria.teamwork[0]}/10</span>
                </div>
                <Slider
                  value={formData.criteria.teamwork}
                  onValueChange={(value) => setFormData({
                    ...formData,
                    criteria: { ...formData.criteria, teamwork: value }
                  })}
                  min={0}
                  max={10}
                  step={0.5}
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <Label className="text-sm">Kỹ năng giao tiếp</Label>
                  <span className="text-sm font-medium">{formData.criteria.communication[0]}/10</span>
                </div>
                <Slider
                  value={formData.criteria.communication}
                  onValueChange={(value) => setFormData({
                    ...formData,
                    criteria: { ...formData.criteria, communication: value }
                  })}
                  min={0}
                  max={10}
                  step={0.5}
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <Label className="text-sm">Kỹ năng kỹ thuật</Label>
                  <span className="text-sm font-medium">{formData.criteria.technical[0]}/10</span>
                </div>
                <Slider
                  value={formData.criteria.technical}
                  onValueChange={(value) => setFormData({
                    ...formData,
                    criteria: { ...formData.criteria, technical: value }
                  })}
                  min={0}
                  max={10}
                  step={0.5}
                />
              </div>

              <div>
                <div className="flex items-center justify-between mb-2">
                  <Label className="text-sm">Sáng tạo & Đổi mới</Label>
                  <span className="text-sm font-medium">{formData.criteria.creativity[0]}/10</span>
                </div>
                <Slider
                  value={formData.criteria.creativity}
                  onValueChange={(value) => setFormData({
                    ...formData,
                    criteria: { ...formData.criteria, creativity: value }
                  })}
                  min={0}
                  max={10}
                  step={0.5}
                />
              </div>
            </div>
          )}

          {/* Comment */}
          <div>
            <Label htmlFor="comment">Nhận xét chi tiết *</Label>
            <Textarea
              id="comment"
              value={formData.comment}
              onChange={(e) => setFormData({ ...formData, comment: e.target.value })}
              placeholder="Nhập nhận xét chi tiết về điểm mạnh, điểm cần cải thiện..."
              rows={6}
              className="mt-2"
            />
            <p className="text-sm text-gray-500 mt-1">
              {formData.comment.length} ký tự
            </p>
          </div>

          {/* Tips */}
          <Card className="p-4 bg-blue-50 border-blue-200">
            <div className="flex items-start gap-3">
              <ThumbsUp className="w-5 h-5 text-blue-600 mt-0.5" />
              <div>
                <h4 className="font-medium text-sm mb-1">Gợi ý đánh giá hiệu quả</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                  <li>• Đưa ra nhận xét cụ thể, có ví dụ minh họa</li>
                  <li>• Nêu rõ điểm mạnh và điểm cần cải thiện</li>
                  <li>• Đề xuất hướng phát triển trong tương lai</li>
                  <li>• Giữ thái độ khách quan và mang tính xây dựng</li>
                </ul>
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
                Đang gửi...
              </>
            ) : (
              <>
                <Star className="w-4 h-4 mr-2" />
                Gửi đánh giá
              </>
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
