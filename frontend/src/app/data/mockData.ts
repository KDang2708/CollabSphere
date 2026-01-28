import { User, Project, Class, Team, Subject, Syllabus, Resource, Message, Meeting, Notification } from '../types';

// Mock Users
export const mockUsers: User[] = [
  { id: 'admin1', email: 'admin@cosre.edu', name: 'Admin System', role: 'admin', isActive: true },
  { id: 'staff1', email: 'staff@cosre.edu', name: 'Nguyễn Văn A', role: 'staff', isActive: true },
  { id: 'head1', email: 'head@cosre.edu', name: 'Trần Thị B', role: 'head_department', isActive: true },
  { id: 'lec1', email: 'lecturer1@cosre.edu', name: 'GV Phạm Văn C', role: 'lecturer', isActive: true },
  { id: 'lec2', email: 'lecturer2@cosre.edu', name: 'GV Lê Thị D', role: 'lecturer', isActive: true },
  { id: 'stu1', email: 'student1@cosre.edu', name: 'SV Hoàng Văn E', role: 'student', isActive: true },
  { id: 'stu2', email: 'student2@cosre.edu', name: 'SV Võ Thị F', role: 'student', isActive: true },
  { id: 'stu3', email: 'student3@cosre.edu', name: 'SV Đỗ Văn G', role: 'student', isActive: true },
  { id: 'stu4', email: 'student4@cosre.edu', name: 'SV Bùi Thị H', role: 'student', isActive: true },
];

// Mock Subjects
export const mockSubjects: Subject[] = [
  {
    id: 'sub1',
    name: 'Công nghệ Phần mềm',
    code: 'CS301',
    description: 'Môn học về quy trình phát triển phần mềm và các phương pháp quản lý dự án',
  },
  {
    id: 'sub2',
    name: 'Phát triển Ứng dụng Web',
    code: 'CS401',
    description: 'Học cách xây dựng ứng dụng web hiện đại với React và Node.js',
  },
];

// Mock Syllabi
export const mockSyllabi: Syllabus[] = [
  {
    id: 'syl1',
    subjectId: 'sub1',
    title: 'Đề cương Công nghệ Phần mềm',
    description: 'Đề cương chi tiết cho môn Công nghệ Phần mềm',
    objectives: [
      'Hiểu các quy trình phát triển phần mềm',
      'Áp dụng UML trong thiết kế hệ thống',
      'Làm việc nhóm hiệu quả trong dự án phần mềm',
    ],
    content: 'Nội dung bao gồm: Requirements Analysis, System Design, Implementation, Testing...',
  },
];

// Mock Projects
export const mockProjects: Project[] = [
  {
    id: 'proj1',
    title: 'Hệ thống Quản lý Thư viện',
    description: 'Xây dựng hệ thống quản lý thư viện số với đầy đủ tính năng',
    objectives: [
      'Phân tích yêu cầu hệ thống',
      'Thiết kế cơ sở dữ liệu',
      'Xây dựng giao diện người dùng',
      'Triển khai và kiểm thử',
    ],
    milestones: [
      {
        id: 'm1',
        title: 'Phân tích yêu cầu',
        description: 'Hoàn thành tài liệu phân tích yêu cầu',
        dueDate: '2025-02-15',
        completed: true,
      },
      {
        id: 'm2',
        title: 'Thiết kế hệ thống',
        description: 'Hoàn thành sơ đồ UML và thiết kế cơ sở dữ liệu',
        dueDate: '2025-03-15',
        completed: false,
      },
      {
        id: 'm3',
        title: 'Phát triển',
        description: 'Xây dựng các tính năng chính',
        dueDate: '2025-04-30',
        completed: false,
      },
    ],
    syllabusId: 'syl1',
    createdBy: 'lec1',
    status: 'approved',
    createdAt: '2025-01-01',
  },
  {
    id: 'proj2',
    title: 'Ứng dụng Quản lý Tài chính Cá nhân',
    description: 'Phát triển app mobile quản lý chi tiêu cá nhân',
    objectives: [
      'Thiết kế giao diện UX/UI',
      'Xây dựng backend API',
      'Tích hợp với ngân hàng',
    ],
    milestones: [
      {
        id: 'm4',
        title: 'Nghiên cứu & Thiết kế',
        description: 'Research và thiết kế mockup',
        dueDate: '2025-02-20',
        completed: false,
      },
    ],
    syllabusId: 'syl1',
    createdBy: 'lec2',
    status: 'pending',
    createdAt: '2025-01-10',
  },
];

// Mock Classes
export const mockClasses: Class[] = [
  {
    id: 'class1',
    name: 'Công nghệ Phần mềm - Lớp 01',
    code: 'CS301-01',
    subjectId: 'sub1',
    lecturerId: 'lec1',
    studentIds: ['stu1', 'stu2', 'stu3', 'stu4'],
    projectId: 'proj1',
    semester: 'Spring',
    year: 2025,
  },
];

// Mock Teams
export const mockTeams: Team[] = [
  {
    id: 'team1',
    name: 'Team Alpha',
    classId: 'class1',
    projectId: 'proj1',
    leaderId: 'stu1',
    memberIds: ['stu1', 'stu2', 'stu3'],
    progress: 45,
    milestones: [
      {
        id: 'm1',
        title: 'Phân tích yêu cầu',
        description: 'Hoàn thành tài liệu phân tích yêu cầu',
        dueDate: '2025-02-15',
        completed: true,
        questions: [
          {
            id: 'q1',
            question: 'Những stakeholder chính của dự án là ai?',
            createdBy: 'lec1',
          },
          {
            id: 'q2',
            question: 'Hệ thống cần giải quyết vấn đề gì?',
            createdBy: 'lec1',
          },
        ],
      },
      {
        id: 'm2',
        title: 'Thiết kế hệ thống',
        description: 'Hoàn thành sơ đồ UML và thiết kế cơ sở dữ liệu',
        dueDate: '2025-03-15',
        completed: false,
      },
    ],
    checkpoints: [
      {
        id: 'cp1',
        title: 'Sprint 1: User Authentication',
        description: 'Xây dựng tính năng đăng nhập và đăng ký',
        assignedMembers: ['stu1', 'stu2'],
        dueDate: '2025-02-28',
        completed: true,
        submissions: [],
      },
      {
        id: 'cp2',
        title: 'Sprint 2: Database Design',
        description: 'Thiết kế và triển khai cơ sở dữ liệu',
        assignedMembers: ['stu3'],
        dueDate: '2025-03-15',
        completed: false,
        submissions: [],
      },
    ],
  },
];

// Mock Resources
export const mockResources: Resource[] = [
  {
    id: 'res1',
    name: 'Tài liệu Yêu cầu Hệ thống.pdf',
    type: 'file',
    url: '#',
    uploadedBy: 'lec1',
    uploadedAt: '2025-01-15',
    size: '2.5 MB',
  },
  {
    id: 'res2',
    name: 'UML Diagrams.pdf',
    type: 'document',
    url: '#',
    uploadedBy: 'stu1',
    uploadedAt: '2025-02-10',
    size: '1.8 MB',
  },
];

// Mock Messages
export const mockMessages: Message[] = [
  {
    id: 'msg1',
    senderId: 'lec1',
    content: 'Chào các em, hôm nay chúng ta sẽ review milestone đầu tiên.',
    timestamp: '2025-01-29 09:00',
    type: 'text',
  },
  {
    id: 'msg2',
    senderId: 'stu1',
    content: 'Dạ, em đã hoàn thành phần phân tích yêu cầu ạ.',
    timestamp: '2025-01-29 09:15',
    type: 'text',
  },
];

// Mock Meetings
export const mockMeetings: Meeting[] = [
  {
    id: 'meet1',
    title: 'Sprint Planning Meeting',
    scheduledAt: '2025-01-30 14:00',
    duration: 60,
    participants: ['lec1', 'stu1', 'stu2', 'stu3'],
    organizer: 'lec1',
    status: 'scheduled',
  },
];

// Mock Notifications
export const mockNotifications: Notification[] = [
  // Student notifications
  {
    id: 'notif1',
    userId: 'stu1',
    type: 'realtime',
    title: 'Milestone hoàn thành',
    message: 'Giảng viên đã đánh giá milestone "Phân tích yêu cầu"',
    read: false,
    createdAt: '2025-01-29T10:00:00',
  },
  {
    id: 'notif2',
    userId: 'stu1',
    type: 'realtime',
    title: 'Cuộc họp sắp diễn ra',
    message: 'Sprint Planning Meeting sẽ bắt đầu vào 14:00 ngày mai',
    read: false,
    createdAt: '2025-01-29T15:00:00',
  },
  {
    id: 'notif3',
    userId: 'stu1',
    type: 'email',
    title: 'Tài nguyên mới được tải lên',
    message: 'GV Phạm Văn C đã tải lên tài liệu mới cho lớp học',
    read: true,
    createdAt: '2025-01-28T09:00:00',
  },
  {
    id: 'notif4',
    userId: 'stu1',
    type: 'realtime',
    title: 'Đánh giá từ giảng viên',
    message: 'Bạn đã nhận được đánh giá cho checkpoint "User Authentication"',
    read: false,
    createdAt: '2025-01-29T16:30:00',
  },
  // Lecturer notifications
  {
    id: 'notif5',
    userId: 'lec1',
    type: 'realtime',
    title: 'Nhóm đã nộp checkpoint',
    message: 'Team Alpha đã nộp checkpoint "Sprint 1: User Authentication"',
    read: false,
    createdAt: '2025-01-29T11:00:00',
  },
  {
    id: 'notif6',
    userId: 'lec1',
    type: 'email',
    title: 'Dự án được phê duyệt',
    message: 'Dự án "Hệ thống Quản lý Thư viện" đã được trưởng khoa phê duyệt',
    read: true,
    createdAt: '2025-01-28T14:00:00',
  },
  {
    id: 'notif7',
    userId: 'lec1',
    type: 'realtime',
    title: 'Team leader đánh dấu milestone hoàn thành',
    message: 'SV Hoàng Văn E đã đánh dấu milestone "Phân tích yêu cầu" là hoàn thành',
    read: false,
    createdAt: '2025-01-29T10:30:00',
  },
  // Admin notifications
  {
    id: 'notif8',
    userId: 'admin1',
    type: 'email',
    title: 'Báo cáo hệ thống',
    message: 'Người dùng đã gửi báo cáo về lỗi trong hệ thống',
    read: false,
    createdAt: '2025-01-29T08:00:00',
  },
  {
    id: 'notif9',
    userId: 'admin1',
    type: 'realtime',
    title: 'Tài khoản mới được tạo',
    message: '5 tài khoản sinh viên mới đã được tạo trong hệ thống',
    read: false,
    createdAt: '2025-01-29T09:00:00',
  },
  // Staff notifications
  {
    id: 'notif10',
    userId: 'staff1',
    type: 'realtime',
    title: 'Import dữ liệu thành công',
    message: 'Đã import thành công 30 tài khoản sinh viên từ file Excel',
    read: false,
    createdAt: '2025-01-29T10:00:00',
  },
  {
    id: 'notif11',
    userId: 'staff1',
    type: 'email',
    title: 'Môn học mới cần phê duyệt',
    message: 'Có 2 môn học mới cần được xem xét và phê duyệt',
    read: true,
    createdAt: '2025-01-28T13:00:00',
  },
  // Head Department notifications
  {
    id: 'notif12',
    userId: 'head1',
    type: 'realtime',
    title: 'Dự án chờ phê duyệt',
    message: 'GV Lê Thị D đã nộp dự án "Ứng dụng Quản lý Tài chính Cá nhân" chờ phê duyệt',
    read: false,
    createdAt: '2025-01-29T11:30:00',
  },
  {
    id: 'notif13',
    userId: 'head1',
    type: 'email',
    title: 'Báo cáo tiến độ các lớp',
    message: 'Báo cáo tiến độ học tập của các lớp trong tháng 1 đã sẵn sàng',
    read: false,
    createdAt: '2025-01-29T15:30:00',
  },
];