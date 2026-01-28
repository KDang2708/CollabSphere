import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '../ui/card';
import { Button } from '../ui/button';
import { Badge } from '../ui/badge';
import { Input } from '../ui/input';
import { Textarea } from '../ui/textarea';
import { Avatar, AvatarFallback } from '../ui/avatar';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../ui/tabs';
import {
  Video,
  VideoOff,
  Mic,
  MicOff,
  PhoneOff,
  ScreenShare,
  MessageSquare,
  Users,
  Settings,
  MoreVertical,
  Send,
  Maximize2,
  Volume2,
  Camera,
  User,
} from 'lucide-react';
import { mockUsers, mockMessages } from '../../data/mockData';
import { useAuth } from '../../contexts/AuthContext';

export const VideoMeeting: React.FC = () => {
  const { currentUser } = useAuth();
  const [isVideoOn, setIsVideoOn] = useState(true);
  const [isAudioOn, setIsAudioOn] = useState(true);
  const [isSharingScreen, setIsSharingScreen] = useState(false);
  const [showChat, setShowChat] = useState(true);
  const [chatMessage, setChatMessage] = useState('');
  const [messages, setMessages] = useState(mockMessages);

  // Mock participants in the call
  const participants = mockUsers.filter(u => 
    ['stu1', 'stu2', 'stu3', 'lec1'].includes(u.id)
  );

  const handleSendMessage = () => {
    if (chatMessage.trim()) {
      const newMessage = {
        id: `msg${messages.length + 1}`,
        senderId: currentUser?.id || '',
        content: chatMessage,
        timestamp: new Date().toLocaleString('vi-VN'),
        type: 'text' as const,
      };
      setMessages([...messages, newMessage]);
      setChatMessage('');
    }
  };

  const getInitials = (name: string) => {
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase()
      .slice(0, 2);
  };

  return (
    <div className="h-[calc(100vh-200px)] flex gap-4">
      {/* Main Video Area */}
      <div className="flex-1 flex flex-col gap-4">
        {/* Main Speaker View */}
        <Card className="flex-1 relative overflow-hidden bg-gray-900">
          <div className="absolute inset-0 flex items-center justify-center">
            {isSharingScreen ? (
              <div className="text-center text-white">
                <ScreenShare className="w-16 h-16 mx-auto mb-4" />
                <p className="text-xl">Đang chia sẻ màn hình</p>
                <p className="text-sm text-gray-400 mt-2">
                  Screen sharing simulation
                </p>
              </div>
            ) : (
              <div className="text-center">
                <div className="w-32 h-32 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-full flex items-center justify-center mx-auto mb-4">
                  {isVideoOn ? (
                    <Camera className="w-16 h-16 text-white" />
                  ) : (
                    <VideoOff className="w-16 h-16 text-white" />
                  )}
                </div>
                <p className="text-white text-xl">{currentUser?.name}</p>
                <Badge variant="secondary" className="mt-2">
                  {isVideoOn ? 'Camera bật' : 'Camera tắt'}
                </Badge>
              </div>
            )}
          </div>

          {/* Video Controls Overlay */}
          <div className="absolute bottom-0 left-0 right-0 p-6 bg-gradient-to-t from-black/80 to-transparent">
            <div className="flex items-center justify-center gap-3">
              <Button
                size="lg"
                variant={isAudioOn ? 'secondary' : 'destructive'}
                className="rounded-full w-14 h-14"
                onClick={() => setIsAudioOn(!isAudioOn)}
              >
                {isAudioOn ? <Mic className="w-6 h-6" /> : <MicOff className="w-6 h-6" />}
              </Button>

              <Button
                size="lg"
                variant={isVideoOn ? 'secondary' : 'destructive'}
                className="rounded-full w-14 h-14"
                onClick={() => setIsVideoOn(!isVideoOn)}
              >
                {isVideoOn ? <Video className="w-6 h-6" /> : <VideoOff className="w-6 h-6" />}
              </Button>

              <Button
                size="lg"
                variant="destructive"
                className="rounded-full w-16 h-16"
              >
                <PhoneOff className="w-7 h-7" />
              </Button>

              <Button
                size="lg"
                variant={isSharingScreen ? 'default' : 'secondary'}
                className="rounded-full w-14 h-14"
                onClick={() => setIsSharingScreen(!isSharingScreen)}
              >
                <ScreenShare className="w-6 h-6" />
              </Button>

              <Button
                size="lg"
                variant={showChat ? 'default' : 'secondary'}
                className="rounded-full w-14 h-14"
                onClick={() => setShowChat(!showChat)}
              >
                <MessageSquare className="w-6 h-6" />
              </Button>

              <Button
                size="lg"
                variant="secondary"
                className="rounded-full w-14 h-14"
              >
                <Settings className="w-6 h-6" />
              </Button>
            </div>
          </div>

          {/* Meeting Info */}
          <div className="absolute top-4 left-4 bg-black/60 backdrop-blur-sm rounded-lg px-4 py-2 text-white">
            <p className="text-sm font-medium">Sprint Planning Meeting</p>
            <p className="text-xs text-gray-300">00:23:45</p>
          </div>
        </Card>

        {/* Participant Grid */}
        <div className="grid grid-cols-4 gap-3 h-32">
          {participants.map((participant) => (
            <Card key={participant.id} className="relative overflow-hidden bg-gray-800 border-gray-700">
              <div className="h-full flex items-center justify-center">
                <div className="text-center">
                  <div className="w-12 h-12 bg-gradient-to-br from-purple-600 to-pink-600 rounded-full flex items-center justify-center mx-auto mb-2">
                    <span className="text-white font-semibold">
                      {getInitials(participant.name)}
                    </span>
                  </div>
                  <p className="text-white text-xs">{participant.name.split(' ').slice(-2).join(' ')}</p>
                </div>
              </div>
              <div className="absolute bottom-2 left-2 flex items-center gap-1">
                <div className="w-5 h-5 bg-green-500 rounded-full flex items-center justify-center">
                  <Mic className="w-3 h-3 text-white" />
                </div>
              </div>
            </Card>
          ))}
        </div>
      </div>

      {/* Chat Sidebar */}
      {showChat && (
        <Card className="w-96 flex flex-col">
          <CardHeader className="border-b">
            <div className="flex items-center justify-between">
              <CardTitle className="text-lg">Trò chuyện</CardTitle>
              <div className="flex items-center gap-2">
                <Badge variant="outline">{participants.length} người</Badge>
                <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
                  <MoreVertical className="w-4 h-4" />
                </Button>
              </div>
            </div>
          </CardHeader>

          <Tabs defaultValue="chat" className="flex-1 flex flex-col">
            <TabsList className="w-full">
              <TabsTrigger value="chat" className="flex-1">
                <MessageSquare className="w-4 h-4 mr-2" />
                Chat
              </TabsTrigger>
              <TabsTrigger value="participants" className="flex-1">
                <Users className="w-4 h-4 mr-2" />
                Người tham gia
              </TabsTrigger>
            </TabsList>

            <TabsContent value="chat" className="flex-1 flex flex-col m-0">
              <CardContent className="flex-1 overflow-y-auto p-4 space-y-3">
                {messages.map((msg) => {
                  const sender = mockUsers.find(u => u.id === msg.senderId);
                  const isCurrentUser = msg.senderId === currentUser?.id;

                  return (
                    <div
                      key={msg.id}
                      className={`flex gap-2 ${isCurrentUser ? 'flex-row-reverse' : ''}`}
                    >
                      <Avatar className="w-8 h-8 flex-shrink-0">
                        <AvatarFallback className="bg-blue-600 text-white text-xs">
                          {getInitials(sender?.name || 'U')}
                        </AvatarFallback>
                      </Avatar>
                      <div className={`flex-1 ${isCurrentUser ? 'text-right' : ''}`}>
                        <div className="flex items-center gap-2 mb-1">
                          <p className="text-xs font-medium text-gray-900">
                            {sender?.name}
                          </p>
                          <p className="text-xs text-gray-500">{msg.timestamp}</p>
                        </div>
                        <div
                          className={`inline-block px-3 py-2 rounded-lg text-sm ${
                            isCurrentUser
                              ? 'bg-blue-600 text-white'
                              : 'bg-gray-100 text-gray-900'
                          }`}
                        >
                          {msg.content}
                        </div>
                      </div>
                    </div>
                  );
                })}
              </CardContent>

              <div className="p-4 border-t">
                <div className="flex gap-2">
                  <Input
                    placeholder="Nhập tin nhắn..."
                    value={chatMessage}
                    onChange={(e) => setChatMessage(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter' && !e.shiftKey) {
                        e.preventDefault();
                        handleSendMessage();
                      }
                    }}
                  />
                  <Button onClick={handleSendMessage}>
                    <Send className="w-4 h-4" />
                  </Button>
                </div>
              </div>
            </TabsContent>

            <TabsContent value="participants" className="flex-1 m-0">
              <CardContent className="p-4">
                <div className="space-y-3">
                  {participants.map((participant) => (
                    <div
                      key={participant.id}
                      className="flex items-center justify-between p-2 hover:bg-gray-50 rounded-lg"
                    >
                      <div className="flex items-center gap-3">
                        <Avatar>
                          <AvatarFallback className="bg-purple-600 text-white">
                            {getInitials(participant.name)}
                          </AvatarFallback>
                        </Avatar>
                        <div>
                          <p className="font-medium text-sm">{participant.name}</p>
                          <p className="text-xs text-gray-500">
                            {participant.role === 'lecturer' ? 'Giảng viên' : 'Sinh viên'}
                          </p>
                        </div>
                      </div>
                      <div className="flex items-center gap-2">
                        <div className="w-2 h-2 bg-green-500 rounded-full" />
                        <Button variant="ghost" size="sm" className="h-8 w-8 p-0">
                          <MoreVertical className="w-4 h-4" />
                        </Button>
                      </div>
                    </div>
                  ))}
                </div>
              </CardContent>
            </TabsContent>
          </Tabs>
        </Card>
      )}
    </div>
  );
};
