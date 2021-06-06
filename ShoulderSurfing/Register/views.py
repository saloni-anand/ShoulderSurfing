from django.shortcuts import render
from .forms import SignUpForm
from .LogicFiles.addUser import register
from django.conf import settings
from django.core.mail import send_mail

def RegisterUser(request):

	context = {}

	data = SignUpForm(request.POST or None)
	if(data.is_valid()):
		email = data.cleaned_data.get("email")
		userdata = data.cleaned_data
		register(userdata)
		subject = 'welcome to GFG world'
		message = f'Hi, thank you. your otp is 1234.'
		email_from = settings.EMAIL_HOST_USER
		recipient_list = [email, ]
		send_mail( subject, message, email_from, recipient_list )

	context['form'] = SignUpForm()

	return render(request, "Register/Register.html", context)

