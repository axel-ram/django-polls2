from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('question', 'author', 'text')
    
    def __init__(self, question_pk=None, *args, **kwargs):
        
        super(CommentForm, self).__init__(*args, **kwargs)
        if question_pk:
            self.fields['question'].initial = question_pk