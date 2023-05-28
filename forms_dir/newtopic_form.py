from django import forms
from boards.models import Topic
from mdeditor.fields import MDTextFormField

class NewTopic_Form(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea, label='Treść')
	class Meta:
		model = Topic
		fields = ['subject', 'message']
		help_texts = {'subject':'Dopuszczalna długość to 300 znaków.'}
		widgets = {'subject': forms.TextInput}
		labels = {'subject': 'Temat'}