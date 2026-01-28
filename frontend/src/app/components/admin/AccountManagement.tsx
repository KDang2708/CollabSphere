import React, { useState } from 'react';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Badge } from '@/app/components/ui/badge';
import { Avatar, AvatarFallback } from '@/app/components/ui/avatar';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/app/components/ui/tabs';
import {
  Search,
  UserX,
  UserCheck,
  Mail,
  Shield,
  GraduationCap,
  Users,
  MoreVertical,
  Upload,
} from 'lucide-react';
import { mockUsers } from '@/app/data/mockData';
import { User, UserRole } from '@/app/types';
import { toast } from 'sonner';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/app/components/ui/dropdown-menu';

interface AccountManagementProps {
  canDeactivate?: boolean;
  canImport?: boolean;
  filterRoles?: UserRole[];
}

export const AccountManagement: React.FC<AccountManagementProps> = ({
  canDeactivate = false,
  canImport = false,
  filterRoles,
}) => {
  const [users, setUsers] = useState<User[]>(mockUsers);
  const [searchQuery, setSearchQuery] = useState('');

  const handleToggleActive = (userId: string) => {
    const user = users.find(u => u.id === userId);
    if (!user) return;

    if (confirm(`Bạn có chắc muốn ${user.isActive ? 'vô hiệu hóa' : 'kích hoạt'} tài khoản ${user.name}?`)) {
      setUsers(users.map(u =>
        u.id === userId ? { ...u, isActive: !u.isActive } : u
      ));
      toast.success(`Đã ${user.isActive ? 'vô hiệu hóa' : 'kích hoạt'} tài khoản ${user.name}`);
    }
  };

  const handleSendEmail = (user: User) => {
    toast.success(`Đã gửi email đến ${user.email}`);
  };

  const handleImport = () => {
    toast.info('Chức năng import file đang được phát triển');
  };

  const getRoleIcon = (role: UserRole) => {
    switch (role) {
      case 'admin':
        return <Shield className="w-4 h-4" />;
      case 'staff':
        return <Users className="w-4 h-4" />;
      case 'head_department':
        return <Shield className="w-4 h-4" />;
      case 'lecturer':
        return <GraduationCap className="w-4 h-4" />;
      case 'student':
        return <Users className="w-4 h-4" />;
    }
  };

  const getRoleLabel = (role: UserRole) => {
    const labels: Record<UserRole, string> = {
      admin: 'Quản trị viên',
      staff: 'Nhân viên',
      head_department: 'Trưởng khoa',
      lecturer: 'Giảng viên',
      student: 'Sinh viên',
    };
    return labels[role];
  };

  const getRoleBadgeColor = (role: UserRole) => {
    const colors: Record<UserRole, string> = {
      admin: 'bg-red-100 text-red-700',
      staff: 'bg-green-100 text-green-700',
      head_department: 'bg-purple-100 text-purple-700',
      lecturer: 'bg-blue-100 text-blue-700',
      student: 'bg-orange-100 text-orange-700',
    };
    return colors[role];
  };

  const filteredUsers = users.filter(user => {
    const matchesSearch = user.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
                         user.email.toLowerCase().includes(searchQuery.toLowerCase());
    const matchesRole = !filterRoles || filterRoles.includes(user.role);
    return matchesSearch && matchesRole;
  });

  const groupedByRole = filteredUsers.reduce((acc, user) => {
    if (!acc[user.role]) acc[user.role] = [];
    acc[user.role].push(user);
    return acc;
  }, {} as Record<UserRole, User[]>);

  const UserCard: React.FC<{ user: User }> = ({ user }) => (
    <Card className="hover:shadow-md transition-shadow">
      <CardContent className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3 flex-1">
            <Avatar className="w-10 h-10">
              <AvatarFallback>{user.name.charAt(0)}</AvatarFallback>
            </Avatar>
            <div className="flex-1 min-w-0">
              <div className="flex items-center gap-2">
                <h4 className="font-medium truncate">{user.name}</h4>
                {!user.isActive && (
                  <Badge variant="destructive" className="text-xs">
                    Vô hiệu hóa
                  </Badge>
                )}
              </div>
              <p className="text-sm text-gray-600 truncate">{user.email}</p>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Badge className={getRoleBadgeColor(user.role)}>
              <span className="flex items-center gap-1">
                {getRoleIcon(user.role)}
                {getRoleLabel(user.role)}
              </span>
            </Badge>

            <DropdownMenu>
              <DropdownMenuTrigger asChild>
                <Button size="sm" variant="ghost">
                  <MoreVertical className="w-4 h-4" />
                </Button>
              </DropdownMenuTrigger>
              <DropdownMenuContent align="end">
                <DropdownMenuItem onClick={() => handleSendEmail(user)}>
                  <Mail className="w-4 h-4 mr-2" />
                  Gửi email
                </DropdownMenuItem>
                {canDeactivate && (
                  <DropdownMenuItem
                    onClick={() => handleToggleActive(user.id)}
                    className={user.isActive ? 'text-red-600' : 'text-green-600'}
                  >
                    {user.isActive ? (
                      <>
                        <UserX className="w-4 h-4 mr-2" />
                        Vô hiệu hóa
                      </>
                    ) : (
                      <>
                        <UserCheck className="w-4 h-4 mr-2" />
                        Kích hoạt
                      </>
                    )}
                  </DropdownMenuItem>
                )}
              </DropdownMenuContent>
            </DropdownMenu>
          </div>
        </div>
      </CardContent>
    </Card>
  );

  return (
    <Card>
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle>Quản lý Tài khoản</CardTitle>
            <CardDescription>
              Quản lý người dùng trong hệ thống
            </CardDescription>
          </div>
          {canImport && (
            <Button onClick={handleImport}>
              <Upload className="w-4 h-4 mr-2" />
              Import tài khoản
            </Button>
          )}
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {/* Search */}
          <div className="relative">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
            <Input
              placeholder="Tìm kiếm theo tên hoặc email..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="pl-9"
            />
          </div>

          {/* Stats */}
          <div className="grid grid-cols-2 md:grid-cols-5 gap-4">
            {(['admin', 'staff', 'head_department', 'lecturer', 'student'] as UserRole[]).map(role => {
              const count = users.filter(u => u.role === role).length;
              if (filterRoles && !filterRoles.includes(role)) return null;
              
              return (
                <Card key={role} className="p-3">
                  <div className="flex items-center gap-2">
                    {getRoleIcon(role)}
                    <div>
                      <p className="text-xs text-gray-600">{getRoleLabel(role)}</p>
                      <p className="text-xl font-bold">{count}</p>
                    </div>
                  </div>
                </Card>
              );
            })}
          </div>

          {/* Users List */}
          <Tabs defaultValue="all">
            <TabsList>
              <TabsTrigger value="all">
                Tất cả ({filteredUsers.length})
              </TabsTrigger>
              <TabsTrigger value="active">
                Hoạt động ({filteredUsers.filter(u => u.isActive).length})
              </TabsTrigger>
              <TabsTrigger value="inactive">
                Vô hiệu hóa ({filteredUsers.filter(u => !u.isActive).length})
              </TabsTrigger>
            </TabsList>

            <TabsContent value="all" className="space-y-4 mt-4">
              {Object.entries(groupedByRole).map(([role, roleUsers]) => (
                <div key={role}>
                  <h3 className="font-medium text-sm text-gray-600 mb-3">
                    {getRoleLabel(role as UserRole)} ({roleUsers.length})
                  </h3>
                  <div className="grid gap-3">
                    {roleUsers.map(user => (
                      <UserCard key={user.id} user={user} />
                    ))}
                  </div>
                </div>
              ))}
              {filteredUsers.length === 0 && (
                <div className="text-center py-12 text-gray-400">
                  <Users className="w-12 h-12 mx-auto mb-3" />
                  <p>Không tìm thấy người dùng</p>
                </div>
              )}
            </TabsContent>

            <TabsContent value="active" className="space-y-3 mt-4">
              {filteredUsers.filter(u => u.isActive).map(user => (
                <UserCard key={user.id} user={user} />
              ))}
            </TabsContent>

            <TabsContent value="inactive" className="space-y-3 mt-4">
              {filteredUsers.filter(u => !u.isActive).map(user => (
                <UserCard key={user.id} user={user} />
              ))}
            </TabsContent>
          </Tabs>
        </div>
      </CardContent>
    </Card>
  );
};
