from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = contact
		fields = ['primeiro_nome', 'segundo_nome', 'email', 'mensagem'] 