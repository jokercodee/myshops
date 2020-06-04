from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'john'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'carter'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'john@gmail.com'}))
	address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Street Name'}))
	postal_code = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': '63xxx1'}))
	city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control','placeholder': 'Coimbatore'}))

	class Meta:
		model = Order
		fields = ['first_name','last_name','email','address',
				  'postal_code','city']
		