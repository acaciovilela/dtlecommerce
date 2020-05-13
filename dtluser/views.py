from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegistrationForm, ChangeForm
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required
def profile(request):
	print(settings.MEDIA_ROOT)
	args = {'user': request.user}
	return render(request, 'user/profile.html', args)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/user')
	else:
		form = RegistrationForm()

	return render(request, 'user/register.html', {'form': form})

@login_required
def edit(request):
	if request.method == 'POST':
		form = ChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/user')
	else:
		form = ChangeForm(instance=request.user)

	return render(request, 'user/edit.html', {'form': form})
