import React, { useRef, useState, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/app/components/ui/card';
import { Button } from '@/app/components/ui/button';
import { Badge } from '@/app/components/ui/badge';
import { Slider } from '@/app/components/ui/slider';
import {
  Pencil,
  Eraser,
  Square,
  Circle,
  Minus,
  Type,
  Trash2,
  Download,
  Undo,
  Redo,
  Users,
  Save,
} from 'lucide-react';
import { toast } from 'sonner';

type Tool = 'pen' | 'eraser' | 'rectangle' | 'circle' | 'line' | 'text';

interface WhiteboardProps {
  teamId?: string;
  readOnly?: boolean;
}

export const Whiteboard: React.FC<WhiteboardProps> = ({ teamId, readOnly = false }) => {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const [isDrawing, setIsDrawing] = useState(false);
  const [currentTool, setCurrentTool] = useState<Tool>('pen');
  const [currentColor, setCurrentColor] = useState('#000000');
  const [lineWidth, setLineWidth] = useState([3]);
  const [activeUsers, setActiveUsers] = useState(3);
  const [history, setHistory] = useState<ImageData[]>([]);
  const [historyStep, setHistoryStep] = useState(-1);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    // Set canvas size
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    // Set white background
    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Save initial state
    saveState();

    // Simulate real-time collaboration
    const interval = setInterval(() => {
      setActiveUsers(Math.floor(Math.random() * 5) + 1);
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const saveState = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    const imageData = ctx.getImageData(0, 0, canvas.width, canvas.height);
    const newHistory = history.slice(0, historyStep + 1);
    newHistory.push(imageData);
    setHistory(newHistory);
    setHistoryStep(newHistory.length - 1);
  };

  const undo = () => {
    if (historyStep > 0) {
      const canvas = canvasRef.current;
      if (!canvas) return;

      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      const newStep = historyStep - 1;
      ctx.putImageData(history[newStep], 0, 0);
      setHistoryStep(newStep);
    }
  };

  const redo = () => {
    if (historyStep < history.length - 1) {
      const canvas = canvasRef.current;
      if (!canvas) return;

      const ctx = canvas.getContext('2d');
      if (!ctx) return;

      const newStep = historyStep + 1;
      ctx.putImageData(history[newStep], 0, 0);
      setHistoryStep(newStep);
    }
  };

  const clearCanvas = () => {
    if (!confirm('Bạn có chắc muốn xóa toàn bộ bảng vẽ?')) return;

    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.fillStyle = '#ffffff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    saveState();
    toast.success('Đã xóa bảng vẽ');
  };

  const downloadCanvas = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const link = document.createElement('a');
    link.download = `whiteboard-${Date.now()}.png`;
    link.href = canvas.toDataURL();
    link.click();
    toast.success('Đã tải xuống bảng vẽ');
  };

  const handleMouseDown = (e: React.MouseEvent<HTMLCanvasElement>) => {
    if (readOnly) return;
    setIsDrawing(true);

    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    ctx.strokeStyle = currentColor;
    ctx.lineWidth = lineWidth[0];
    ctx.lineCap = 'round';
    ctx.lineJoin = 'round';

    if (currentTool === 'pen' || currentTool === 'eraser') {
      ctx.beginPath();
      ctx.moveTo(x, y);
    }
  };

  const handleMouseMove = (e: React.MouseEvent<HTMLCanvasElement>) => {
    if (!isDrawing || readOnly) return;

    const canvas = canvasRef.current;
    if (!canvas) return;

    const rect = canvas.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    if (currentTool === 'pen') {
      ctx.strokeStyle = currentColor;
      ctx.lineTo(x, y);
      ctx.stroke();
    } else if (currentTool === 'eraser') {
      ctx.strokeStyle = '#ffffff';
      ctx.lineTo(x, y);
      ctx.stroke();
    }
  };

  const handleMouseUp = () => {
    if (readOnly) return;
    setIsDrawing(false);
    saveState();
  };

  const tools: { icon: React.ReactNode; tool: Tool; label: string }[] = [
    { icon: <Pencil className="w-4 h-4" />, tool: 'pen', label: 'Bút vẽ' },
    { icon: <Eraser className="w-4 h-4" />, tool: 'eraser', label: 'Tẩy' },
    { icon: <Square className="w-4 h-4" />, tool: 'rectangle', label: 'Hình chữ nhật' },
    { icon: <Circle className="w-4 h-4" />, tool: 'circle', label: 'Hình tròn' },
    { icon: <Minus className="w-4 h-4" />, tool: 'line', label: 'Đường thẳng' },
    { icon: <Type className="w-4 h-4" />, tool: 'text', label: 'Chữ' },
  ];

  const colors = [
    '#000000', // Black
    '#FF0000', // Red
    '#0000FF', // Blue
    '#00FF00', // Green
    '#FFFF00', // Yellow
    '#FF00FF', // Magenta
    '#00FFFF', // Cyan
    '#FFA500', // Orange
  ];

  return (
    <Card className="w-full">
      <CardHeader>
        <div className="flex items-center justify-between">
          <div>
            <CardTitle className="flex items-center gap-2">
              Whiteboard
              <Badge variant="outline" className="flex items-center gap-1">
                <Users className="w-3 h-3" />
                {activeUsers} đang xem
              </Badge>
            </CardTitle>
          </div>
          <div className="flex items-center gap-2">
            <Button size="sm" variant="outline" onClick={() => toast.success('Đã lưu')}>
              <Save className="w-4 h-4 mr-1" />
              Lưu
            </Button>
            <Button size="sm" variant="outline" onClick={downloadCanvas}>
              <Download className="w-4 h-4 mr-1" />
              Tải xuống
            </Button>
          </div>
        </div>
      </CardHeader>
      <CardContent>
        <div className="space-y-4">
          {/* Toolbar */}
          <div className="flex items-center gap-4 p-4 bg-gray-50 rounded-lg">
            {/* Tools */}
            <div className="flex items-center gap-1 border-r pr-4">
              {tools.map(({ icon, tool, label }) => (
                <Button
                  key={tool}
                  size="sm"
                  variant={currentTool === tool ? 'default' : 'ghost'}
                  onClick={() => setCurrentTool(tool)}
                  title={label}
                  disabled={readOnly}
                >
                  {icon}
                </Button>
              ))}
            </div>

            {/* Colors */}
            <div className="flex items-center gap-1 border-r pr-4">
              {colors.map((color) => (
                <button
                  key={color}
                  className={`w-8 h-8 rounded-md border-2 transition-all ${
                    currentColor === color ? 'border-blue-500 scale-110' : 'border-gray-300'
                  }`}
                  style={{ backgroundColor: color }}
                  onClick={() => setCurrentColor(color)}
                  disabled={readOnly}
                />
              ))}
            </div>

            {/* Line Width */}
            <div className="flex items-center gap-2 border-r pr-4 min-w-[150px]">
              <span className="text-sm text-gray-600">Độ dày:</span>
              <Slider
                value={lineWidth}
                onValueChange={setLineWidth}
                min={1}
                max={20}
                step={1}
                className="w-20"
                disabled={readOnly}
              />
              <span className="text-sm font-medium w-6">{lineWidth[0]}</span>
            </div>

            {/* Actions */}
            <div className="flex items-center gap-1 ml-auto">
              <Button
                size="sm"
                variant="ghost"
                onClick={undo}
                disabled={readOnly || historyStep <= 0}
                title="Hoàn tác"
              >
                <Undo className="w-4 h-4" />
              </Button>
              <Button
                size="sm"
                variant="ghost"
                onClick={redo}
                disabled={readOnly || historyStep >= history.length - 1}
                title="Làm lại"
              >
                <Redo className="w-4 h-4" />
              </Button>
              <Button
                size="sm"
                variant="ghost"
                onClick={clearCanvas}
                disabled={readOnly}
                title="Xóa tất cả"
              >
                <Trash2 className="w-4 h-4" />
              </Button>
            </div>
          </div>

          {/* Canvas */}
          <div className="border-2 border-gray-300 rounded-lg overflow-hidden bg-white">
            <canvas
              ref={canvasRef}
              onMouseDown={handleMouseDown}
              onMouseMove={handleMouseMove}
              onMouseUp={handleMouseUp}
              onMouseLeave={handleMouseUp}
              className="w-full cursor-crosshair"
              style={{ height: '500px' }}
            />
          </div>

          {readOnly && (
            <div className="text-center text-sm text-gray-500">
              Bạn đang xem ở chế độ chỉ đọc
            </div>
          )}
        </div>
      </CardContent>
    </Card>
  );
};
