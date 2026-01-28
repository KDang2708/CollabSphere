import React, { useState, useRef, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Input } from '@/app/components/ui/input';
import { Avatar, AvatarFallback } from '@/app/components/ui/avatar';
import { Badge } from '@/app/components/ui/badge';
import { ScrollArea } from '@/app/components/ui/scroll-area';
import {
  Send,
  Paperclip,
  Smile,
  MoreVertical,
  Phone,
  Video,
  Search,
  Pin,
} from 'lucide-react';
import { useAuth } from '@/app/contexts/AuthContext';
import { mockMessages, mockUsers } from '@/app/data/mockData';
import { Message } from '@/app/types';
import { toast } from 'sonner';

interface ChatSystemProps {
  teamId?: string;
  participants?: string[];
}

export const ChatSystem: React.FC<ChatSystemProps> = ({ teamId, participants = [] }) => {
  const { currentUser } = useAuth();
  const [messages, setMessages] = useState<Message[]>(mockMessages);
  const [newMessage, setNewMessage] = useState('');
  const [typing, setTyping] = useState<string[]>([]);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  // Simulate typing indicator
  useEffect(() => {
    const interval = setInterval(() => {
      if (Math.random() > 0.8) {
        const randomUser = mockUsers.filter(u => u.id !== currentUser?.id)[
          Math.floor(Math.random() * mockUsers.length)
        ];
        setTyping([randomUser.name]);
        setTimeout(() => setTyping([]), 2000);
      }
    }, 5000);

    return () => clearInterval(interval);
  }, [currentUser]);

  const handleSendMessage = () => {
    if (!newMessage.trim()) return;

    const message: Message = {
      id: `msg-${Date.now()}`,
      senderId: currentUser?.id || 'unknown',
      content: newMessage,
      timestamp: new Date().toISOString(),
      type: 'text',
    };

    setMessages([...messages, message]);
    setNewMessage('');
    toast.success('Đã gửi tin nhắn');

    // Simulate response
    setTimeout(() => {
      const responseUser = mockUsers.find(u => u.id !== currentUser?.id);
      if (responseUser) {
        const response: Message = {
          id: `msg-${Date.now()}-response`,
          senderId: responseUser.id,
          content: 'Đã nhận được tin nhắn của bạn!',
          timestamp: new Date().toISOString(),
          type: 'text',
        };
        setMessages(prev => [...prev, response]);
      }
    }, 2000);
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const files = e.target.files;
    if (!files || files.length === 0) return;

    const file = files[0];
    const message: Message = {
      id: `msg-${Date.now()}`,
      senderId: currentUser?.id || 'unknown',
      content: `📎 ${file.name}`,
      timestamp: new Date().toISOString(),
      type: 'file',
    };

    setMessages([...messages, message]);
    toast.success('Đã gửi tệp đính kèm');
  };

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const formatTime = (timestamp: string) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffInHours = (now.getTime() - date.getTime()) / (1000 * 60 * 60);

    if (diffInHours < 24) {
      return date.toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' });
    }
    return date.toLocaleDateString('vi-VN', { day: '2-digit', month: '2-digit' });
  };

  return (
    <Card className="flex flex-col h-[600px]">
      <CardHeader className="border-b">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-3">
            <Avatar>
              <AvatarFallback>T</AvatarFallback>
            </Avatar>
            <div>
              <CardTitle className="text-base">Team Alpha</CardTitle>
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <div className="w-2 h-2 bg-green-500 rounded-full"></div>
                <span>{mockUsers.length} thành viên</span>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <Button size="sm" variant="ghost">
              <Phone className="w-4 h-4" />
            </Button>
            <Button size="sm" variant="ghost">
              <Video className="w-4 h-4" />
            </Button>
            <Button size="sm" variant="ghost">
              <Search className="w-4 h-4" />
            </Button>
            <Button size="sm" variant="ghost">
              <MoreVertical className="w-4 h-4" />
            </Button>
          </div>
        </div>
      </CardHeader>

      <CardContent className="flex-1 p-0 overflow-hidden">
        <ScrollArea className="h-full p-4">
          <div className="space-y-4">
            {messages.map((message) => {
              const sender = mockUsers.find(u => u.id === message.senderId);
              const isCurrentUser = message.senderId === currentUser?.id;

              return (
                <div
                  key={message.id}
                  className={`flex gap-3 ${isCurrentUser ? 'flex-row-reverse' : ''}`}
                >
                  {!isCurrentUser && (
                    <Avatar className="w-8 h-8">
                      <AvatarFallback>{sender?.name.charAt(0)}</AvatarFallback>
                    </Avatar>
                  )}

                  <div className={`flex flex-col ${isCurrentUser ? 'items-end' : 'items-start'}`}>
                    {!isCurrentUser && (
                      <span className="text-xs text-gray-600 mb-1">{sender?.name}</span>
                    )}
                    <div
                      className={`px-4 py-2 rounded-lg max-w-md ${
                        isCurrentUser
                          ? 'bg-blue-600 text-white'
                          : 'bg-gray-100 text-gray-900'
                      }`}
                    >
                      {message.type === 'file' ? (
                        <div className="flex items-center gap-2">
                          <Paperclip className="w-4 h-4" />
                          <span>{message.content}</span>
                        </div>
                      ) : (
                        <p className="text-sm">{message.content}</p>
                      )}
                    </div>
                    <span className="text-xs text-gray-500 mt-1">
                      {formatTime(message.timestamp)}
                    </span>
                  </div>
                </div>
              );
            })}

            {typing.length > 0 && (
              <div className="flex items-center gap-2 text-sm text-gray-500">
                <div className="flex gap-1">
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '150ms' }}></div>
                  <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '300ms' }}></div>
                </div>
                <span>{typing[0]} đang nhập...</span>
              </div>
            )}

            <div ref={messagesEndRef} />
          </div>
        </ScrollArea>
      </CardContent>

      <div className="border-t p-4">
        <div className="flex items-center gap-2">
          <input
            type="file"
            ref={fileInputRef}
            className="hidden"
            onChange={handleFileUpload}
          />
          <Button
            size="sm"
            variant="ghost"
            onClick={() => fileInputRef.current?.click()}
          >
            <Paperclip className="w-4 h-4" />
          </Button>

          <div className="flex-1">
            <Input
              placeholder="Nhập tin nhắn..."
              value={newMessage}
              onChange={(e) => setNewMessage(e.target.value)}
              onKeyPress={handleKeyPress}
            />
          </div>

          <Button
            size="sm"
            variant="ghost"
            onClick={() => toast.info('Chọn emoji')}
          >
            <Smile className="w-4 h-4" />
          </Button>

          <Button size="sm" onClick={handleSendMessage} disabled={!newMessage.trim()}>
            <Send className="w-4 h-4" />
          </Button>
        </div>
      </div>
    </Card>
  );
};
