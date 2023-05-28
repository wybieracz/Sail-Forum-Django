from django import forms
from boards.models import Post
from mdeditor.fields import MDTextFormField

class TopicReply_Form(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea, label='Treść')
	class Meta:
		model = Post
		fields = ['message']
		
		
	