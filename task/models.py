from django.db import models

# Create your models here.
class Task(models.Model):
    
    TASK_STATUS = {
        ('Completed','Completed'),
        ('InComplete','InComplete'),
        ('InProgress','InProgress')
    }
    
    
    title = models.CharField(max_length=250)
    description = models.TextField()
    task_status = models.CharField(max_length=20,choices=TASK_STATUS,default='InProgress')
    created_at = models.DateField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']