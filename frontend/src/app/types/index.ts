// Type definitions for CollabSphere

export type UserRole = 'admin' | 'staff' | 'head_department' | 'lecturer' | 'student';

export interface User {
  id: string;
  email: string;
  name: string;
  role: UserRole;
  avatar?: string;
  isActive: boolean;
}

export interface Subject {
  id: string;
  name: string;
  code: string;
  description: string;
}

export interface Syllabus {
  id: string;
  subjectId: string;
  title: string;
  description: string;
  objectives: string[];
  content: string;
}

export interface Class {
  id: string;
  name: string;
  code: string;
  subjectId: string;
  lecturerId: string;
  studentIds: string[];
  projectId?: string;
  semester: string;
  year: number;
}

export interface Milestone {
  id: string;
  title: string;
  description: string;
  dueDate: string;
  completed: boolean;
  questions?: MilestoneQuestion[];
}

export interface MilestoneQuestion {
  id: string;
  question: string;
  createdBy: string;
}

export interface Project {
  id: string;
  title: string;
  description: string;
  objectives: string[];
  milestones: Milestone[];
  syllabusId: string;
  createdBy: string;
  status: 'pending' | 'approved' | 'rejected';
  createdAt: string;
}

export interface Team {
  id: string;
  name: string;
  classId: string;
  projectId: string;
  leaderId: string;
  memberIds: string[];
  progress: number;
  milestones: Milestone[];
  checkpoints: Checkpoint[];
}

export interface Checkpoint {
  id: string;
  title: string;
  description: string;
  assignedMembers: string[];
  dueDate: string;
  completed: boolean;
  submissions: CheckpointSubmission[];
}

export interface CheckpointSubmission {
  id: string;
  checkpointId: string;
  memberId: string;
  content: string;
  submittedAt: string;
  feedback?: Feedback;
}

export interface Task {
  id: string;
  title: string;
  description: string;
  assignedTo: string[];
  status: 'todo' | 'in-progress' | 'review' | 'done';
  priority: 'low' | 'medium' | 'high';
  dueDate: string;
  subtasks: Subtask[];
  createdBy: string;
}

export interface Subtask {
  id: string;
  title: string;
  completed: boolean;
}

export interface Feedback {
  id: string;
  fromUserId: string;
  toUserId: string;
  rating: number;
  comment: string;
  createdAt: string;
}

export interface Resource {
  id: string;
  name: string;
  type: 'file' | 'document' | 'link';
  url: string;
  uploadedBy: string;
  uploadedAt: string;
  size?: string;
}

export interface Message {
  id: string;
  senderId: string;
  content: string;
  timestamp: string;
  type: 'text' | 'file' | 'meeting';
}

export interface Meeting {
  id: string;
  title: string;
  scheduledAt: string;
  duration: number;
  participants: string[];
  organizer: string;
  status: 'scheduled' | 'ongoing' | 'completed';
}

export interface Notification {
  id: string;
  userId: string;
  type: 'email' | 'realtime';
  title: string;
  message: string;
  read: boolean;
  createdAt: string;
}

export interface MemberContribution {
  memberId: string;
  name: string;
  tasksCompleted: number;
  contributionPercentage: number;
  lastActive: string;
}
