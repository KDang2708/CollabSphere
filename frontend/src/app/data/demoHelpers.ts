// Demo helper data and utility functions for CollabSphere

export const demoAccounts = [
  {
    role: 'Admin',
    email: 'admin@cosre.edu',
    description: 'Quản trị viên hệ thống - Quản lý tài khoản, xem báo cáo',
    features: [
      'Xem tất cả tài khoản người dùng',
      'Vô hiệu hóa tài khoản',
      'Xem báo cáo hệ thống',
      'Quản lý bảo mật',
    ],
  },
  {
    role: 'Staff',
    email: 'staff@cosre.edu',
    description: 'Nhân viên học vụ - Quản lý môn học, lớp học, tài khoản',
    features: [
      'Import môn học và đề cương',
      'Tạo và quản lý lớp học',
      'Tạo tài khoản giảng viên/sinh viên',
      'Phân công giảng viên cho lớp',
    ],
  },
  {
    role: 'Head Department',
    email: 'head@cosre.edu',
    description: 'Trưởng khoa - Phê duyệt dự án và giám sát hoạt động',
    features: [
      'Phê duyệt/từ chối dự án',
      'Giao dự án cho lớp học',
      'Xem tổng quan các lớp học',
      'Quản lý môn học và đề cương',
    ],
  },
  {
    role: 'Lecturer',
    email: 'lecturer1@cosre.edu',
    description: 'Giảng viên - Tạo dự án, quản lý lớp học và nhóm sinh viên',
    features: [
      'Tạo dự án với hỗ trợ AI',
      'Quản lý lớp học và nhóm',
      'Theo dõi tiến độ nhóm',
      'Đánh giá sinh viên',
      'Video meeting & Chat',
      'AI Assistant',
    ],
  },
  {
    role: 'Student',
    email: 'student1@cosre.edu',
    description: 'Sinh viên - Tham gia nhóm, làm việc trên dự án',
    features: [
      'Xem dự án và cột mốc',
      'Workspace với Kanban board',
      'Nộp checkpoint và bài tập',
      'Đánh giá đồng đẳng',
      'Video meeting & Chat',
      'AI Assistant',
    ],
  },
];

export const systemFeatures = [
  {
    category: 'Quản lý Dự án',
    features: [
      'Tạo dự án với AI support',
      'Phê duyệt workflow',
      'Milestone tracking',
      'Checkpoint management',
    ],
  },
  {
    category: 'Cộng tác Nhóm',
    features: [
      'Kanban board (drag & drop)',
      'Video conferencing',
      'Real-time chat',
      'Screen sharing',
      'Whiteboard (mô phỏng)',
    ],
  },
  {
    category: 'Đánh giá & Phản hồi',
    features: [
      'Lecturer evaluation',
      'Peer review system',
      'Contribution tracking',
      'Progress analytics',
    ],
  },
  {
    category: 'AI Assistant',
    features: [
      'Idea brainstorming',
      'Progress analysis',
      'Milestone generation',
      'Tech stack suggestions',
    ],
  },
  {
    category: 'Thông báo',
    features: [
      'Email notifications',
      'Real-time notifications',
      'Meeting reminders',
      'Milestone updates',
    ],
  },
];

export const techStack = {
  frontend: ['React', 'TypeScript', 'Tailwind CSS', 'Shadcn/ui'],
  backend: ['Python Web API', 'PostgreSQL', 'Redis (Upstash)'],
  cloud: ['Azure (hosting)', 'AWS (frontend)', 'Cloudinary (media)'],
  realtime: ['WebRTC', 'Signal', 'Socket.IO'],
  ai: ['AWS Bedrock'],
};
