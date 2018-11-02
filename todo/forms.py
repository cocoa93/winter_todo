from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    class Meta:
        widgets = {
            'dueDate': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        model = Todo
        fields = ('title', 'content','importance','dueDate')