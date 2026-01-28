import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Badge } from '@/app/components/ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import {
  Upload,
  File,
  FileText,
  Image,
  Video,
  Link as LinkIcon,
  Download,
  Trash2,
  Eye,
  Search,
  Folder,
  Calendar,
  User,
} from 'lucide-react';
import { toast } from 'sonner';
import { mockResources, mockUsers } from '@/app/data/mockData';
import { Resource } from '@/app/types';

interface ResourceManagerProps {
  context: 'class' | 'team' | 'milestone' | 'checkpoint';
  contextId: string;
  canUpload?: boolean;
}

export const ResourceManager: React.FC<ResourceManagerProps> = ({
  context,
  contextId,
  canUpload = true,
}) => {
  const [resources, setResources] = useState<Resource[]>(mockResources);
  const [searchQuery, setSearchQuery] = useState('');
  const [uploading, setUploading] = useState(false);

  const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const files = event.target.files;
    if (!files || files.length === 0) return;

    setUploading(true);
    
    // Simulate file upload
    setTimeout(() => {
      const newResources: Resource[] = Array.from(files).map((file, index) => ({
        id: `res-${Date.now()}-${index}`,
        name: file.name,
        type: getFileType(file.name),
        url: URL.createObjectURL(file),
        uploadedBy: 'current-user',
        uploadedAt: new Date().toISOString().split('T')[0],
        size: formatFileSize(file.size),
      }));

      setResources([...newResources, ...resources]);
      toast.success(`Đã tải lên ${files.length} tệp thành công`);
      setUploading(false);
    }, 1500);
  };

  const getFileType = (filename: string): 'file' | 'document' | 'link' => {
    const ext = filename.split('.').pop()?.toLowerCase();
    if (['pdf', 'doc', 'docx', 'txt'].includes(ext || '')) return 'document';
    return 'file';
  };

  const formatFileSize = (bytes: number): string => {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
  };

  const getFileIcon = (type: string, name: string) => {
    const ext = name.split('.').pop()?.toLowerCase();
    
    if (['jpg', 'jpeg', 'png', 'gif', 'svg'].includes(ext || '')) {
      return <Image className="w-5 h-5 text-blue-600" />;
    }
    if (['mp4', 'avi', 'mov', 'wmv'].includes(ext || '')) {
      return <Video className="w-5 h-5 text-purple-600" />;
    }
    if (['pdf', 'doc', 'docx'].includes(ext || '')) {
      return <FileText className="w-5 h-5 text-red-600" />;
    }
    if (type === 'link') {
      return <LinkIcon className="w-5 h-5 text-green-600" />;
    }
    return <File className="w-5 h-5 text-gray-600" />;
  };

  const handleDelete = (resourceId: string) => {
    if (confirm('Bạn có chắc muốn xóa tài nguyên này?')) {
      setResources(resources.filter(r => r.id !== resourceId));
      toast.success('Đã xóa tài nguyên');
    }
  };

  const handleDownload = (resource: Resource) => {
    toast.success(`Đang tải xuống ${resource.name}`);
    // Simulate download
  };

  const filteredResources = resources.filter(r =>
    r.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const groupedByDate = filteredResources.reduce((acc, resource) => {
    const date = resource.uploadedAt;
    if (!acc[date]) acc[date] = [];
    acc[date].push(resource);
    return acc;
  }, {} as Record<string, Resource[]>);

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle>Quản lý Tài nguyên</CardTitle>
            <CardDescription>
              Quản lý tệp, tài liệu và liên kết cho {context === 'class' ? 'lớp học' : context === 'team' ? 'nhóm' : 'milestone'}
            </CardDescription>
          </div>
          {canUpload && (
            <div>
              <input
                type="file"
                id="file-upload"
                multiple
                className="hidden"
                onChange={handleFileUpload}
                disabled={uploading}
              />
              <Button asChild disabled={uploading}>
                <label htmlFor="file-upload" className="cursor-pointer">
                  <Upload className="w-4 h-4 mr-2" />
                  {uploading ? 'Đang tải lên...' : 'Tải lên'}
                </label>
              </Button>
            </div>
          )}
        </div>
      </CardHeader>
      <CardContent>
        <Tabs defaultValue="all" className="space-y-4">
          <div className="flex items-center justify-between">
            <TabsList>
              <TabsTrigger value="all">
                Tất cả ({filteredResources.length})
              </TabsTrigger>
              <TabsTrigger value="documents">
                <FileText className="w-4 h-4 mr-1" />
                Tài liệu
              </TabsTrigger>
              <TabsTrigger value="media">
                <Image className="w-4 h-4 mr-1" />
                Hình ảnh & Video
              </TabsTrigger>
              <TabsTrigger value="links">
                <LinkIcon className="w-4 h-4 mr-1" />
                Liên kết
              </TabsTrigger>
            </TabsList>

            <div className="relative w-64">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
              <Input
                placeholder="Tìm kiếm tài nguyên..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-9"
              />
            </div>
          </div>

          <TabsContent value="all" className="space-y-4">
            {Object.keys(groupedByDate).length > 0 ? (
              Object.entries(groupedByDate).map(([date, items]) => (
                <div key={date}>
                  <div className="flex items-center gap-2 mb-3">
                    <Calendar className="w-4 h-4 text-gray-400" />
                    <h4 className="text-sm font-medium text-gray-600">{date}</h4>
                  </div>
                  <div className="grid grid-cols-1 gap-2">
                    {items.map((resource) => {
                      const uploader = mockUsers.find(u => u.id === resource.uploadedBy);
                      return (
                        <Card key={resource.id} className="p-3 hover:shadow-md transition-shadow">
                          <div className="flex items-center gap-3">
                            <div className="w-10 h-10 bg-gray-100 rounded-lg flex items-center justify-center">
                              {getFileIcon(resource.type, resource.name)}
                            </div>
                            <div className="flex-1 min-w-0">
                              <h4 className="font-medium text-sm truncate">{resource.name}</h4>
                              <div className="flex items-center gap-2 text-xs text-gray-500 mt-1">
                                <User className="w-3 h-3" />
                                <span>{uploader?.name || 'Unknown'}</span>
                                <span>•</span>
                                <span>{resource.size}</span>
                              </div>
                            </div>
                            <div className="flex items-center gap-1">
                              <Button
                                size="sm"
                                variant="ghost"
                                onClick={() => handleDownload(resource)}
                              >
                                <Download className="w-4 h-4" />
                              </Button>
                              <Button
                                size="sm"
                                variant="ghost"
                                onClick={() => window.open(resource.url, '_blank')}
                              >
                                <Eye className="w-4 h-4" />
                              </Button>
                              {canUpload && (
                                <Button
                                  size="sm"
                                  variant="ghost"
                                  onClick={() => handleDelete(resource.id)}
                                >
                                  <Trash2 className="w-4 h-4 text-red-500" />
                                </Button>
                              )}
                            </div>
                          </div>
                        </Card>
                      );
                    })}
                  </div>
                </div>
              ))
            ) : (
              <div className="text-center py-12 text-gray-400">
                <Folder className="w-12 h-12 mx-auto mb-3" />
                <p>Chưa có tài nguyên nào</p>
                {canUpload && (
                  <p className="text-sm mt-1">Nhấn nút "Tải lên" để thêm tệp</p>
                )}
              </div>
            )}
          </TabsContent>

          <TabsContent value="documents">
            <div className="text-center py-8 text-gray-400">
              <FileText className="w-12 h-12 mx-auto mb-3" />
              <p>Tính năng lọc tài liệu</p>
            </div>
          </TabsContent>

          <TabsContent value="media">
            <div className="text-center py-8 text-gray-400">
              <Image className="w-12 h-12 mx-auto mb-3" />
              <p>Tính năng lọc media</p>
            </div>
          </TabsContent>

          <TabsContent value="links">
            <div className="text-center py-8 text-gray-400">
              <LinkIcon className="w-12 h-12 mx-auto mb-3" />
              <p>Tính năng lọc liên kết</p>
            </div>
          </TabsContent>
        </Tabs>
      </CardContent>
    </Card>
  );
};
