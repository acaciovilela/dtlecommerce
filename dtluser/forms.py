from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(
		required=True,
		widget=forms.TextInput(
			attrs={'class': 'form-control'}
		)
	)
	username = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	first_name = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	last_name = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	password1 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))
	password2 = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control'
		}
	))

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)

	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class ChangeForm(UserChangeForm):
	first_name = forms.CharField()
	first_name.widget.attrs.update({'class': 'form-control'})
	first_name.label = 'Nome'

	last_name = forms.CharField()
	last_name.widget.attrs.update({'class': 'form-control'})
	last_name.label = 'Sobrenome'

	email = forms.EmailField()
	email.widget.attrs.update({'class': 'form-control'})
	email.label = 'E-mail'

	class Meta:
		model = User
		fields = (
			'first_name',
			'last_name',
			'email',
		)

	def save(self, commit=True):
		user = super(ChangeForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user
