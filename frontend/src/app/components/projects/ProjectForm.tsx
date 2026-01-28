import React, { useState } from 'react';
import { Dialog, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle } from '@/app/components/ui/dialog';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Label } from '@/app/components/ui/label';
import { Textarea } from '@/app/components/ui/textarea';
import { Badge } from '@/app/components/ui/badge';
import { Card } from '@/app/components/ui/card';
import { Plus, X, Sparkles, Calendar, Loader2 } from 'lucide-react';
import { toast } from 'sonner';

interface Milestone {
  id: string;
  title: string;
  description: string;
  dueDate: string;
}

interface ProjectFormProps {
  open: boolean;
  onClose: () => void;
  onSubmit: (project: any) => void;
  initialData?: any;
  syllabusId?: string;
}

export const ProjectForm: React.FC<ProjectFormProps> = ({ 
  open, 
  onClose, 
  onSubmit, 
  initialData,
  syllabusId 
}) => {
  const [loading, setLoading] = useState(false);
  const [aiGenerating, setAiGenerating] = useState(false);
  const [formData, setFormData] = useState({
    title: initialData?.title || '',
    description: initialData?.description || '',
    objectives: initialData?.objectives || [''],
    milestones: initialData?.milestones || [] as Milestone[],
  });

  const handleAddObjective = () => {
    setFormData({
      ...formData,
      objectives: [...formData.objectives, ''],
    });
  };

  const handleRemoveObjective = (index: number) => {
    setFormData({
      ...formData,
      objectives: formData.objectives.filter((_, i) => i !== index),
    });
  };

  const handleObjectiveChange = (index: number, value: string) => {
    const newObjectives = [...formData.objectives];
    newObjectives[index] = value;
    setFormData({ ...formData, objectives: newObjectives });
  };

  const handleAddMilestone = () => {
    setFormData({
      ...formData,
      milestones: [
        ...formData.milestones,
        {
          id: `m-${Date.now()}`,
          title: '',
          description: '',
          dueDate: '',
        },
      ],
    });
  };

  const handleRemoveMilestone = (index: number) => {
    setFormData({
      ...formData,
      milestones: formData.milestones.filter((_, i) => i !== index),
    });
  };

  const handleMilestoneChange = (index: number, field: string, value: string) => {
    const newMilestones = [...formData.milestones];
    newMilestones[index] = { ...newMilestones[index], [field]: value };
    setFormData({ ...formData, milestones: newMilestones });
  };

  const handleAIGenerate = async () => {
    if (!formData.title || !formData.description) {
      toast.error('Vui lòng nhập tên và mô tả dự án trước');
      return;
    }

    setAiGenerating(true);
    
    // Simulate AI generation
    setTimeout(() => {
      const aiSuggestions = {
        objectives: [
          'Phân tích và thiết lập yêu cầu hệ thống chi tiết',
          'Thiết kế kiến trúc hệ thống và cơ sở dữ liệu',
          'Phát triển các tính năng chính của ứng dụng',
          'Kiểm thử và tối ưu hóa hiệu năng',
          'Triển khai và bàn giao sản phẩm',
        ],
        milestones: [
          {
            id: `m-${Date.now()}-1`,
            title: 'Giai đoạn 1: Phân tích yêu cầu',
            description: 'Thu thập và phân tích yêu cầu, xác định scope dự án',
            dueDate: new Date(Date.now() + 14 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
          },
          {
            id: `m-${Date.now()}-2`,
            title: 'Giai đoạn 2: Thiết kế hệ thống',
            description: 'Thiết kế kiến trúc, database schema và UI/UX',
            dueDate: new Date(Date.now() + 28 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
          },
          {
            id: `m-${Date.now()}-3`,
            title: 'Giai đoạn 3: Phát triển',
            description: 'Xây dựng các tính năng chính của hệ thống',
            dueDate: new Date(Date.now() + 56 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
          },
          {
            id: `m-${Date.now()}-4`,
            title: 'Giai đoạn 4: Kiểm thử',
            description: 'Thực hiện unit test, integration test và user acceptance test',
            dueDate: new Date(Date.now() + 70 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
          },
        ],
      };

      setFormData({
        ...formData,
        objectives: aiSuggestions.objectives,
        milestones: aiSuggestions.milestones,
      });

      toast.success('AI đã tạo mục tiêu và cột mốc thành công!');
      setAiGenerating(false);
    }, 2000);
  };

  const handleSubmit = () => {
    if (!formData.title || !formData.description) {
      toast.error('Vui lòng điền đầy đủ thông tin');
      return;
    }

    const filteredObjectives = formData.objectives.filter(obj => obj.trim() !== '');
    if (filteredObjectives.length === 0) {
      toast.error('Vui lòng thêm ít nhất một mục tiêu');
      return;
    }

    setLoading(true);
    setTimeout(() => {
      const project = {
        id: initialData?.id || `proj-${Date.now()}`,
        ...formData,
        objectives: filteredObjectives,
        syllabusId: syllabusId || 'syl1',
        status: 'pending',
        createdAt: new Date().toISOString().split('T')[0],
      };

      onSubmit(project);
      toast.success(initialData ? 'Cập nhật dự án thành công' : 'Tạo dự án thành công');
      setLoading(false);
      onClose();
    }, 1000);
  };

  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto">
        <DialogHeader>
          <DialogTitle>
            {initialData ? 'Chỉnh sửa dự án' : 'Tạo dự án mới'}
          </DialogTitle>
          <DialogDescription>
            Điền thông tin dự án. Bạn có thể sử dụng AI để tự động tạo mục tiêu và cột mốc.
          </DialogDescription>
        </DialogHeader>

        <div className="space-y-6 py-4">
          {/* Basic Info */}
          <div className="space-y-4">
            <div>
              <Label htmlFor="title">Tên dự án *</Label>
              <Input
                id="title"
                value={formData.title}
                onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                placeholder="VD: Hệ thống Quản lý Thư viện"
              />
            </div>

            <div>
              <Label htmlFor="description">Mô tả *</Label>
              <Textarea
                id="description"
                value={formData.description}
                onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                placeholder="Mô tả chi tiết về dự án..."
                rows={3}
              />
            </div>
          </div>

          {/* AI Generate Button */}
          <Card className="p-4 bg-gradient-to-r from-purple-50 to-blue-50 border-purple-200">
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <h4 className="font-medium flex items-center gap-2 mb-1">
                  <Sparkles className="w-4 h-4 text-purple-600" />
                  Hỗ trợ AI
                </h4>
                <p className="text-sm text-gray-600">
                  Để AI tự động tạo mục tiêu và cột mốc dựa trên thông tin dự án của bạn
                </p>
              </div>
              <Button
                type="button"
                onClick={handleAIGenerate}
                disabled={aiGenerating || !formData.title}
                className="ml-4"
              >
                {aiGenerating ? (
                  <>
                    <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                    Đang tạo...
                  </>
                ) : (
                  <>
                    <Sparkles className="w-4 h-4 mr-2" />
                    Tạo bằng AI
                  </>
                )}
              </Button>
            </div>
          </Card>

          {/* Objectives */}
          <div>
            <div className="flex items-center justify-between mb-3">
              <Label>Mục tiêu dự án *</Label>
              <Button type="button" size="sm" onClick={handleAddObjective}>
                <Plus className="w-4 h-4 mr-1" />
                Thêm mục tiêu
              </Button>
            </div>
            <div className="space-y-2">
              {formData.objectives.map((objective, index) => (
                <div key={index} className="flex gap-2">
                  <Input
                    value={objective}
                    onChange={(e) => handleObjectiveChange(index, e.target.value)}
                    placeholder={`Mục tiêu ${index + 1}`}
                  />
                  {formData.objectives.length > 1 && (
                    <Button
                      type="button"
                      variant="ghost"
                      size="icon"
                      onClick={() => handleRemoveObjective(index)}
                    >
                      <X className="w-4 h-4" />
                    </Button>
                  )}
                </div>
              ))}
            </div>
          </div>

          {/* Milestones */}
          <div>
            <div className="flex items-center justify-between mb-3">
              <Label>Cột mốc dự án</Label>
              <Button type="button" size="sm" onClick={handleAddMilestone}>
                <Plus className="w-4 h-4 mr-1" />
                Thêm cột mốc
              </Button>
            </div>
            <div className="space-y-3">
              {formData.milestones.map((milestone, index) => (
                <Card key={milestone.id} className="p-4">
                  <div className="space-y-3">
                    <div className="flex items-start justify-between">
                      <Badge variant="outline">Cột mốc {index + 1}</Badge>
                      <Button
                        type="button"
                        variant="ghost"
                        size="icon"
                        onClick={() => handleRemoveMilestone(index)}
                      >
                        <X className="w-4 h-4" />
                      </Button>
                    </div>
                    <Input
                      value={milestone.title}
                      onChange={(e) => handleMilestoneChange(index, 'title', e.target.value)}
                      placeholder="Tên cột mốc"
                    />
                    <Textarea
                      value={milestone.description}
                      onChange={(e) => handleMilestoneChange(index, 'description', e.target.value)}
                      placeholder="Mô tả cột mốc"
                      rows={2}
                    />
                    <div>
                      <Label className="text-sm">Deadline</Label>
                      <div className="flex items-center gap-2 mt-1">
                        <Calendar className="w-4 h-4 text-gray-400" />
                        <Input
                          type="date"
                          value={milestone.dueDate}
                          onChange={(e) => handleMilestoneChange(index, 'dueDate', e.target.value)}
                        />
                      </div>
                    </div>
                  </div>
                </Card>
              ))}
              {formData.milestones.length === 0 && (
                <div className="text-center py-8 text-gray-400 border-2 border-dashed rounded-lg">
                  <p>Chưa có cột mốc nào</p>
                  <p className="text-sm mt-1">Nhấn "Thêm cột mốc" hoặc dùng AI để tạo</p>
                </div>
              )}
            </div>
          </div>
        </div>

        <DialogFooter>
          <Button variant="outline" onClick={onClose} disabled={loading}>
            Hủy
          </Button>
          <Button onClick={handleSubmit} disabled={loading}>
            {loading ? (
              <>
                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                Đang xử lý...
              </>
            ) : (
              initialData ? 'Cập nhật' : 'Tạo dự án'
            )}
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
