from django import forms

class ContactoForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super(ContactoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'] = forms.CharField(required = True)
		self.fields['telefono'] = forms.CharField(required = True)
		self.fields['mensaje'] = forms.CharField(widget=forms.Textarea, required=True)
