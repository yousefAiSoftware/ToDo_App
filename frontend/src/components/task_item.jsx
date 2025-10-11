import React, { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Card, CardContent } from './ui/card';
import { Badge } from './ui/badge';
import { Check, Edit2, Trash2, Clock } from 'lucide-react';

const TaskItem = ({ task, onUpdate, onDelete, priorityColor }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editTitle, setEditTitle] = useState(task.title);

  const handleToggleComplete = () => {
    onUpdate(task.id, { is_completed: !task.is_completed });
  };

  const handleSaveEdit = () => {
    onUpdate(task.id, { title: editTitle });
    setIsEditing(false);
  };

  const getPriorityBorder = (priority) => {
    switch (priority) {
      case 'Important AND Urgent': return 'border-l-red-500';
      case 'Important AND Not Urgent': return 'border-l-yellow-500';
      case 'Not Important AND Urgent': return 'border-l-blue-500'; 
      case 'Not Important AND Not Urgent': return 'border-l-gray-400';
      default: return 'border-l-gray-400';
    }
  };

  return (
    <Card className={`border-l-4 ${getPriorityBorder(task.priority)} transition-all hover:shadow-md`}>
      <CardContent className="p-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-3 flex-1">
            <Button
              variant="ghost"
              size="sm"
              className={`h-6 w-6 p-0 rounded-full border-2 ${
                task.is_completed 
                  ? 'bg-primary text-primary-foreground border-primary' 
                  : 'border-muted-foreground hover:border-primary'
              }`}
              onClick={handleToggleComplete}
            >
              {task.is_completed && <Check className="h-3 w-3" />}
            </Button>
            {isEditing ? (
              <Input
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                onBlur={handleSaveEdit}
                onKeyPress={(e) => e.key === 'Enter' && handleSaveEdit()}
                className="flex-1"
                autoFocus
              />
            ) : (
              <div
                className={`flex-1 cursor-pointer ${
                  task.is_completed 
                    ? 'line-through text-muted-foreground' 
                    : 'text-foreground'
                }`}
                onDoubleClick={() => setIsEditing(true)}
              >
                <h3 className="font-medium">{task.title}</h3>
                {task.task_description && (
                  <p className="text-sm text-muted-foreground mt-1">{task.task_description}</p>
                )}
                {task.due_date && (
                  <div className="flex items-center gap-1 text-xs text-muted-foreground mt-2">
                    <Clock className="h-3 w-3" />
                    Due: {new Date(task.due_date).toLocaleString()}
                  </div>
                )}
              </div>
            )}
          </div>
          <div className="flex items-center gap-2">
            <Badge variant="outline" className="text-xs">
              {task.priority.replace(' AND ', ' & ')}
            </Badge>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setIsEditing(!isEditing)}
              className="h-8 w-8 p-0"
            >
              <Edit2 className="h-4 w-4" />
            </Button>
            <Button
              variant="ghost"
              size="sm"
              onClick={() => onDelete(task.id)}
              className="h-8 w-8 p-0 text-destructive hover:text-destructive hover:bg-destructive/10"
            >
              <Trash2 className="h-4 w-4" />
            </Button>
          </div>
        </div>
      </CardContent>
    </Card>
  );
};

export default TaskItem;