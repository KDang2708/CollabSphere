import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Input } from '../ui/input';
import { Badge } from '../ui/badge';
import { Avatar, AvatarFallback } from '../ui/avatar';
import { Bot, Send, Sparkles, Lightbulb, Target, TrendingUp, Users, FileText } from 'lucide-react';

interface Message {
  id: string;
  type: 'user' | 'ai';
  content: string;
  timestamp: string;
  suggestions?: string[];
}

export const AIAssistant: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: '1',
      type: 'ai',
      content: 'Xin chào! Tôi là AI Assistant của CollabSphere. Tôi có thể giúp bạn với:\n\n• Động não ý tưởng cho dự án\n• Gợi ý giải pháp kỹ thuật\n• Phân tích tiến độ nhóm\n• Tạo nội dung dự án\n\nBạn cần tôi hỗ trợ gì?',
      timestamp: new Date().toLocaleTimeString('vi-VN'),
      suggestions: [
        'Gợi ý ý tưởng cho hệ thống quản lý thư viện',
        'Phân tích tiến độ nhóm hiện tại',
        'Tạo mốc quan trọng cho dự án',
        'Gợi ý công nghệ phù hợp',
      ],
    },
  ]);
  const [inputMessage, setInputMessage] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  const aiResponses: Record<string, { content: string; suggestions?: string[] }> = {
    'tiến độ': {
      content: 'Dựa trên dữ liệu workspace của nhóm bạn:\n\n📊 **Phân tích tiến độ:**\n• Tổng số nhiệm vụ: 15 tasks\n• Hoàn thành: 6 tasks (40%)\n• Đang thực hiện: 5 tasks\n• Chưa bắt đầu: 4 tasks\n\n⚠️ **Cảnh báo:**\n- Task "Xây dựng API Authentication" đang trễ 2 ngày\n- Thành viên Võ Thị F chưa được giao nhiệm vụ nào trong sprint này\n\n💡 **Gợi ý:**\n1. Tổ chức daily standup để đồng bộ tiến độ\n2. Phân bổ lại công việc cho cân bằng\n3. Review lại deadline của các tasks quan trọng',
      suggestions: [
        'Làm thế nào để cải thiện tiến độ?',
        'Phân tích đóng góp của từng thành viên',
        'Tạo kế hoạch sprint tiếp theo',
      ],
    },
    'ý tưởng': {
      content: '💡 **Ý tưởng cho Hệ thống Quản lý Thư viện:**\n\n**Core Features:**\n1. **Quản lý sách:**\n   - Catalog với search & filter nâng cao\n   - QR code scanning\n   - Đề xuất sách dựa trên lịch sử\n\n2. **Mượn/Trả:**\n   - Self-checkout kiosk\n   - Auto-reminder qua email/SMS\n   - Fine management\n\n3. **Member Portal:**\n   - Đặt sách trước\n   - Lịch sử mượn\n   - Đánh giá & review\n\n4. **Analytics:**\n   - Popular books dashboard\n   - Member activity tracking\n   - Inventory reports\n\n**Tech Stack gợi ý:**\n• Frontend: React + TypeScript\n• Backend: Node.js + Express\n• Database: PostgreSQL\n• Cloud: AWS/Azure',
      suggestions: [
        'Chi tiết về tính năng AI recommendation',
        'Cách thiết kế database schema',
        'Security best practices',
      ],
    },
    'mốc quan trọng': {
      content: '🎯 **Mốc quan trọng cho dự án 4 tháng:**\n\n**Tháng 1: Nghiên cứu & Thiết kế (25%)**\n• Tuần 1-2: Requirements gathering & analysis\n• Tuần 3-4: System design & architecture\n• Deliverable: SRS Document, Use Case Diagrams\n\n**Tháng 2: Phát triển Core (50%)**\n• Tuần 5-6: Database setup & Backend API\n• Tuần 7-8: Frontend UI development\n• Deliverable: Working prototype\n\n**Tháng 3: Tính năng nâng cao (75%)**\n• Tuần 9-10: Advanced features implementation\n• Tuần 11-12: Integration & testing\n• Deliverable: Beta version\n\n**Tháng 4: Hoàn thiện (100%)**\n• Tuần 13-14: Bug fixes & optimization\n• Tuần 15-16: Documentation & presentation\n• Deliverable: Final product + Documentation',
      suggestions: [
        'Break down chi tiết từng tuần',
        'Phân công nhiệm vụ cho team',
        'Risk management plan',
      ],
    },
    'công nghệ': {
      content: '🔧 **Gợi ý Tech Stack cho dự án của bạn:**\n\n**Frontend:**\n• **React** - UI library phổ biến, component-based\n• **TypeScript** - Type safety, better DX\n• **Tailwind CSS** - Utility-first styling\n• **React Query** - Server state management\n\n**Backend:**\n• **Node.js + Express** - Fast, scalable\n• **Python + FastAPI** - Great for AI/ML features\n• **PostgreSQL** - Robust relational DB\n• **Redis** - Caching & real-time features\n\n**DevOps:**\n• **Docker** - Containerization\n• **GitHub Actions** - CI/CD\n• **AWS/Azure** - Cloud hosting\n\n**Tools:**\n• **Figma** - UI/UX design\n• **Postman** - API testing\n• **Jest** - Unit testing',
      suggestions: [
        'So sánh React vs Vue',
        'MongoDB vs PostgreSQL cho dự án này',
        'Best practices cho REST API',
      ],
    },
  };

  const handleSendMessage = async () => {
    if (!inputMessage.trim()) return;

    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: inputMessage,
      timestamp: new Date().toLocaleTimeString('vi-VN'),
    };

    setMessages([...messages, userMessage]);
    setInputMessage('');
    setIsTyping(true);

    // Simulate AI thinking
    setTimeout(() => {
      const lowercaseInput = inputMessage.toLowerCase();
      let aiResponse: { content: string; suggestions?: string[] };

      if (lowercaseInput.includes('tiến độ') || lowercaseInput.includes('progress')) {
        aiResponse = aiResponses['tiến độ'];
      } else if (lowercaseInput.includes('ý tưởng') || lowercaseInput.includes('idea')) {
        aiResponse = aiResponses['ý tưởng'];
      } else if (lowercaseInput.includes('mốc') || lowercaseInput.includes('milestone')) {
        aiResponse = aiResponses['mốc quan trọng'];
      } else if (lowercaseInput.includes('công nghệ') || lowercaseInput.includes('tech')) {
        aiResponse = aiResponses['công nghệ'];
      } else {
        aiResponse = {
          content: 'Tôi hiểu bạn đang quan tâm về: "' + inputMessage + '"\n\nĐể tôi có thể hỗ trợ tốt hơn, bạn có thể hỏi cụ thể hơn về:\n\n• Tiến độ và phân tích dự án\n• Ý tưởng và giải pháp kỹ thuật\n• Mốc quan trọng và lập kế hoạch\n• Lựa chọn công nghệ phù hợp\n• Quản lý nhóm và phân công công việc',
          suggestions: [
            'Phân tích tiến độ nhóm',
            'Gợi ý ý tưởng dự án',
            'Tạo timeline cho dự án',
          ],
        };
      }

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'ai',
        content: aiResponse.content,
        timestamp: new Date().toLocaleTimeString('vi-VN'),
        suggestions: aiResponse.suggestions,
      };

      setMessages(prev => [...prev, aiMessage]);
      setIsTyping(false);
    }, 1500);
  };

  const handleSuggestionClick = (suggestion: string) => {
    setInputMessage(suggestion);
  };

  const quickActions = [
    { icon: Lightbulb, label: 'Động não ý tưởng', query: 'Gợi ý ý tưởng cho dự án của tôi' },
    { icon: TrendingUp, label: 'Phân tích tiến độ', query: 'Phân tích tiến độ nhóm hiện tại' },
    { icon: Target, label: 'Tạo mốc quan trọng', query: 'Tạo mốc quan trọng cho dự án' },
    { icon: FileText, label: 'Viết tài liệu', query: 'Hướng dẫn viết tài liệu SRS' },
  ];

  return (
    <div className="h-[calc(100vh-200px)] flex gap-6">
      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        <Card className="flex-1 flex flex-col">
          <CardHeader className="border-b">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-3">
                <div className="w-12 h-12 bg-gradient-to-br from-purple-600 to-pink-600 rounded-full flex items-center justify-center">
                  <Bot className="w-7 h-7 text-white" />
                </div>
                <div>
                  <CardTitle className="flex items-center gap-2">
                    AI Assistant
                    <Sparkles className="w-4 h-4 text-yellow-500" />
                  </CardTitle>
                  <p className="text-sm text-gray-500">Luôn sẵn sàng hỗ trợ bạn</p>
                </div>
              </div>
              <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200">
                Online
              </Badge>
            </div>
          </CardHeader>

          <CardContent className="flex-1 overflow-y-auto p-6 space-y-4">
            {messages.map((message) => (
              <div key={message.id} className={`flex gap-3 ${message.type === 'user' ? 'flex-row-reverse' : ''}`}>
                <Avatar className="w-10 h-10 flex-shrink-0">
                  <AvatarFallback className={message.type === 'ai' ? 'bg-gradient-to-br from-purple-600 to-pink-600' : 'bg-blue-600'}>
                    {message.type === 'ai' ? <Bot className="w-6 h-6 text-white" /> : <Users className="w-6 h-6 text-white" />}
                  </AvatarFallback>
                </Avatar>
                
                <div className={`flex-1 max-w-2xl ${message.type === 'user' ? 'text-right' : ''}`}>
                  <div className="flex items-center gap-2 mb-1">
                    <span className="text-sm font-medium">
                      {message.type === 'ai' ? 'AI Assistant' : 'Bạn'}
                    </span>
                    <span className="text-xs text-gray-500">{message.timestamp}</span>
                  </div>
                  
                  <div
                    className={`inline-block px-4 py-3 rounded-2xl ${
                      message.type === 'user'
                        ? 'bg-blue-600 text-white'
                        : 'bg-gray-100 text-gray-900'
                    }`}
                  >
                    <div className="whitespace-pre-wrap text-sm">{message.content}</div>
                  </div>

                  {message.suggestions && message.suggestions.length > 0 && (
                    <div className="mt-3 flex flex-wrap gap-2">
                      {message.suggestions.map((suggestion, idx) => (
                        <Button
                          key={idx}
                          variant="outline"
                          size="sm"
                          onClick={() => handleSuggestionClick(suggestion)}
                          className="text-sm"
                        >
                          {suggestion}
                        </Button>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {isTyping && (
              <div className="flex gap-3">
                <Avatar className="w-10 h-10">
                  <AvatarFallback className="bg-gradient-to-br from-purple-600 to-pink-600">
                    <Bot className="w-6 h-6 text-white" />
                  </AvatarFallback>
                </Avatar>
                <div className="bg-gray-100 px-4 py-3 rounded-2xl">
                  <div className="flex gap-1">
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }} />
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }} />
                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }} />
                  </div>
                </div>
              </div>
            )}
          </CardContent>

          <div className="p-4 border-t">
            <div className="flex gap-2">
              <Input
                placeholder="Nhập câu hỏi hoặc yêu cầu của bạn..."
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSendMessage();
                  }
                }}
                className="flex-1"
              />
              <Button onClick={handleSendMessage} disabled={!inputMessage.trim() || isTyping}>
                <Send className="w-4 h-4" />
              </Button>
            </div>
          </div>
        </Card>
      </div>

      {/* Sidebar - Quick Actions */}
      <div className="w-80 space-y-4">
        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Hành động nhanh</CardTitle>
          </CardHeader>
          <CardContent className="space-y-2">
            {quickActions.map((action) => {
              const Icon = action.icon;
              return (
                <Button
                  key={action.label}
                  variant="outline"
                  className="w-full justify-start"
                  onClick={() => handleSuggestionClick(action.query)}
                >
                  <Icon className="w-4 h-4 mr-2" />
                  {action.label}
                </Button>
              );
            })}
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle className="text-lg">Khả năng</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-3 text-sm text-gray-600">
              <div className="flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-purple-600 mt-0.5" />
                <p>Phân tích tiến độ và đóng góp của nhóm</p>
              </div>
              <div className="flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-purple-600 mt-0.5" />
                <p>Gợi ý ý tưởng và giải pháp sáng tạo</p>
              </div>
              <div className="flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-purple-600 mt-0.5" />
                <p>Tạo mốc quan trọng và timeline</p>
              </div>
              <div className="flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-purple-600 mt-0.5" />
                <p>Tư vấn công nghệ và kiến trúc</p>
              </div>
              <div className="flex items-start gap-2">
                <Sparkles className="w-4 h-4 text-purple-600 mt-0.5" />
                <p>Hỗ trợ viết tài liệu kỹ thuật</p>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
          <CardContent className="p-4">
            <div className="flex items-start gap-3">
              <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center flex-shrink-0">
                <Lightbulb className="w-5 h-5 text-white" />
              </div>
              <div>
                <p className="font-medium text-blue-900 mb-1">Mẹo sử dụng</p>
                <p className="text-sm text-blue-700">
                  Hãy đặt câu hỏi cụ thể để nhận được câu trả lời chi tiết và hữu ích nhất!
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};
