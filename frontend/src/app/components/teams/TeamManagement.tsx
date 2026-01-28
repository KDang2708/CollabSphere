import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Badge } from '@/app/components/ui/badge';
import { Progress } from '@/app/components/ui/progress';
import { Avatar, AvatarFallback } from '@/app/components/ui/avatar';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import {
  Users,
  Plus,
  Edit,
  Trash2,
  UserPlus,
  TrendingUp,
  CheckCircle2,
  AlertCircle,
  PieChart,
  Search,
} from 'lucide-react';
import { mockTeams, mockUsers, mockClasses } from '@/app/data/mockData';
import { Team, MemberContribution } from '@/app/types';
import { toast } from 'sonner';

interface TeamManagementProps {
  classId?: string;
  canEdit?: boolean;
}

export const TeamManagement: React.FC<TeamManagementProps> = ({
  classId,
  canEdit = false,
}) => {
  const [teams, setTeams] = useState<Team[]>(
    classId ? mockTeams.filter(t => t.classId === classId) : mockTeams
  );
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedTeam, setSelectedTeam] = useState<Team | null>(null);

  const getMemberContribution = (teamId: string, memberId: string): MemberContribution => {
    const member = mockUsers.find(u => u.id === memberId);
    // Mock contribution data
    return {
      memberId,
      name: member?.name || 'Unknown',
      tasksCompleted: Math.floor(Math.random() * 20) + 5,
      contributionPercentage: Math.floor(Math.random() * 30) + 10,
      lastActive: new Date(Date.now() - Math.random() * 7 * 24 * 60 * 60 * 1000).toISOString().split('T')[0],
    };
  };

  const handleCreateTeam = () => {
    toast.info('Chức năng tạo nhóm mới');
  };

  const handleDeleteTeam = (teamId: string) => {
    if (confirm('Bạn có chắc muốn xóa nhóm này?')) {
      setTeams(teams.filter(t => t.id !== teamId));
      toast.success('Đã xóa nhóm');
    }
  };

  const filteredTeams = teams.filter(team =>
    team.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const TeamCard: React.FC<{ team: Team }> = ({ team }) => {
    const teamClass = mockClasses.find(c => c.id === team.classId);
    const leader = mockUsers.find(u => u.id === team.leaderId);
    const completedMilestones = team.milestones.filter(m => m.completed).length;
    const completedCheckpoints = team.checkpoints.filter(c => c.completed).length;

    return (
      <Card className="hover:shadow-md transition-shadow">
        <CardContent className="p-6">
          <div className="space-y-4">
            {/* Header */}
            <div className="flex items-start justify-between">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <h3 className="font-semibold text-lg">{team.name}</h3>
                  {team.progress < 40 && (
                    <Badge variant="destructive" className="text-xs">
                      <AlertCircle className="w-3 h-3 mr-1" />
                      Cần chú ý
                    </Badge>
                  )}
                </div>
                <div className="flex items-center gap-2 text-sm text-gray-500">
                  <span>Lớp: {teamClass?.code}</span>
                  <span>•</span>
                  <span>Trưởng nhóm: {leader?.name}</span>
                </div>
              </div>
              <Badge variant="outline" className="text-lg px-3 py-1">
                {team.progress}%
              </Badge>
            </div>

            {/* Progress */}
            <div>
              <div className="flex items-center justify-between text-sm mb-2">
                <span className="text-gray-600">Tiến độ dự án</span>
                <span className="font-medium">{team.progress}%</span>
              </div>
              <Progress value={team.progress} />
            </div>

            {/* Stats */}
            <div className="grid grid-cols-3 gap-4">
              <div className="text-center p-2 bg-gray-50 rounded-lg">
                <Users className="w-4 h-4 mx-auto mb-1 text-gray-600" />
                <p className="text-xs text-gray-500">Thành viên</p>
                <p className="font-semibold">{team.memberIds.length}</p>
              </div>
              <div className="text-center p-2 bg-gray-50 rounded-lg">
                <CheckCircle2 className="w-4 h-4 mx-auto mb-1 text-green-600" />
                <p className="text-xs text-gray-500">Milestones</p>
                <p className="font-semibold">{completedMilestones}/{team.milestones.length}</p>
              </div>
              <div className="text-center p-2 bg-gray-50 rounded-lg">
                <CheckCircle2 className="w-4 h-4 mx-auto mb-1 text-blue-600" />
                <p className="text-xs text-gray-500">Checkpoints</p>
                <p className="font-semibold">{completedCheckpoints}/{team.checkpoints.length}</p>
              </div>
            </div>

            {/* Actions */}
            <div className="flex gap-2 pt-2">
              <Button
                size="sm"
                variant="outline"
                className="flex-1"
                onClick={() => setSelectedTeam(team)}
              >
                <Users className="w-4 h-4 mr-1" />
                Chi tiết
              </Button>
              {canEdit && (
                <>
                  <Button size="sm" variant="outline">
                    <Edit className="w-4 h-4" />
                  </Button>
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={() => handleDeleteTeam(team.id)}
                  >
                    <Trash2 className="w-4 h-4 text-red-500" />
                  </Button>
                </>
              )}
            </div>
          </div>
        </CardContent>
      </Card>
    );
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <Card>
        <CardHeader>
          <div className="flex items-center justify-between">
            <div>
              <CardTitle>Quản lý Nhóm</CardTitle>
              <CardDescription>
                Quản lý và theo dõi tiến độ các nhóm dự án
              </CardDescription>
            </div>
            {canEdit && (
              <Button onClick={handleCreateTeam}>
                <Plus className="w-4 h-4 mr-2" />
                Tạo nhóm mới
              </Button>
            )}
          </div>
        </CardHeader>
        <CardContent>
          {/* Search and Stats */}
          <div className="space-y-4">
            <div className="relative">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
              <Input
                placeholder="Tìm kiếm nhóm..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="pl-9"
              />
            </div>

            {/* Quick Stats */}
            <div className="grid grid-cols-4 gap-4">
              <div className="p-3 border rounded-lg">
                <p className="text-sm text-gray-600">Tổng nhóm</p>
                <p className="text-2xl font-bold">{teams.length}</p>
              </div>
              <div className="p-3 border rounded-lg">
                <p className="text-sm text-gray-600">Tiến độ TB</p>
                <p className="text-2xl font-bold">
                  {Math.round(teams.reduce((sum, t) => sum + t.progress, 0) / teams.length || 0)}%
                </p>
              </div>
              <div className="p-3 border rounded-lg">
                <p className="text-sm text-gray-600">Hoàn thành tốt</p>
                <p className="text-2xl font-bold text-green-600">
                  {teams.filter(t => t.progress >= 70).length}
                </p>
              </div>
              <div className="p-3 border rounded-lg">
                <p className="text-sm text-gray-600">Cần chú ý</p>
                <p className="text-2xl font-bold text-red-600">
                  {teams.filter(t => t.progress < 40).length}
                </p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Teams Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {filteredTeams.map(team => (
          <TeamCard key={team.id} team={team} />
        ))}
      </div>

      {filteredTeams.length === 0 && (
        <Card>
          <CardContent className="py-12 text-center text-gray-400">
            <Users className="w-12 h-12 mx-auto mb-3" />
            <p>Không tìm thấy nhóm nào</p>
          </CardContent>
        </Card>
      )}

      {/* Team Detail Modal */}
      {selectedTeam && (
        <Card className="fixed inset-4 z-50 overflow-auto">
          <CardHeader className="border-b">
            <div className="flex items-center justify-between">
              <div>
                <CardTitle>{selectedTeam.name}</CardTitle>
                <CardDescription>Chi tiết nhóm và đóng góp của thành viên</CardDescription>
              </div>
              <Button variant="ghost" onClick={() => setSelectedTeam(null)}>
                ✕
              </Button>
            </div>
          </CardHeader>
          <CardContent className="p-6">
            <Tabs defaultValue="members">
              <TabsList>
                <TabsTrigger value="members">Thành viên</TabsTrigger>
                <TabsTrigger value="milestones">Milestones</TabsTrigger>
                <TabsTrigger value="checkpoints">Checkpoints</TabsTrigger>
              </TabsList>

              <TabsContent value="members" className="space-y-4 mt-4">
                <div className="grid gap-4">
                  {selectedTeam.memberIds.map(memberId => {
                    const member = mockUsers.find(u => u.id === memberId);
                    const contribution = getMemberContribution(selectedTeam.id, memberId);
                    const isLeader = memberId === selectedTeam.leaderId;

                    return (
                      <Card key={memberId}>
                        <CardContent className="p-4">
                          <div className="flex items-center gap-4">
                            <Avatar className="w-12 h-12">
                              <AvatarFallback>{member?.name.charAt(0)}</AvatarFallback>
                            </Avatar>
                            <div className="flex-1">
                              <div className="flex items-center gap-2">
                                <h4 className="font-medium">{member?.name}</h4>
                                {isLeader && (
                                  <Badge variant="default">Trưởng nhóm</Badge>
                                )}
                              </div>
                              <p className="text-sm text-gray-600">{member?.email}</p>
                              <div className="mt-2 grid grid-cols-3 gap-4 text-sm">
                                <div>
                                  <p className="text-gray-500">Đóng góp</p>
                                  <p className="font-semibold">{contribution.contributionPercentage}%</p>
                                </div>
                                <div>
                                  <p className="text-gray-500">Tasks</p>
                                  <p className="font-semibold">{contribution.tasksCompleted}</p>
                                </div>
                                <div>
                                  <p className="text-gray-500">Hoạt động</p>
                                  <p className="font-semibold">{contribution.lastActive}</p>
                                </div>
                              </div>
                            </div>
                            {canEdit && (
                              <Button size="sm" variant="outline">
                                <Edit className="w-4 h-4" />
                              </Button>
                            )}
                          </div>
                        </CardContent>
                      </Card>
                    );
                  })}
                </div>
              </TabsContent>

              <TabsContent value="milestones">
                <div className="space-y-3">
                  {selectedTeam.milestones.map(milestone => (
                    <Card key={milestone.id}>
                      <CardContent className="p-4">
                        <div className="flex items-center gap-3">
                          {milestone.completed ? (
                            <CheckCircle2 className="w-5 h-5 text-green-600" />
                          ) : (
                            <div className="w-5 h-5 border-2 border-gray-300 rounded-full" />
                          )}
                          <div className="flex-1">
                            <h4 className="font-medium">{milestone.title}</h4>
                            <p className="text-sm text-gray-600">{milestone.description}</p>
                          </div>
                          <Badge variant={milestone.completed ? 'default' : 'secondary'}>
                            {milestone.completed ? 'Hoàn thành' : 'Đang thực hiện'}
                          </Badge>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </TabsContent>

              <TabsContent value="checkpoints">
                <div className="space-y-3">
                  {selectedTeam.checkpoints.map(checkpoint => (
                    <Card key={checkpoint.id}>
                      <CardContent className="p-4">
                        <h4 className="font-medium">{checkpoint.title}</h4>
                        <p className="text-sm text-gray-600 mt-1">{checkpoint.description}</p>
                        <div className="flex items-center gap-4 mt-3 text-sm">
                          <span className="text-gray-500">
                            Phân công: {checkpoint.assignedMembers.length} người
                          </span>
                          <span>•</span>
                          <span className="text-gray-500">Hạn: {checkpoint.dueDate}</span>
                        </div>
                      </CardContent>
                    </Card>
                  ))}
                </div>
              </TabsContent>
            </Tabs>
          </CardContent>
        </Card>
      )}
    </div>
  );
};
