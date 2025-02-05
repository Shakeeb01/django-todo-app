from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','task_status','created_at']
        
        # widgets for form fields
        widgets = {
            
            'title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Task Title'
                    }),
            'description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Task Description'
                    }),
            
            'created_at': forms.DateInput(
                attrs={'type': 'date',
                       'class': 'form-control',
                    }),
        }
        
        #  Labels for form fields
        labels = {
            'title': '',
            'description': '',
            'task_status': 'Task Status',
            'created_at': '',
        }
