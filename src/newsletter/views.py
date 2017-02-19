from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from .forms import ContactForm, SignUpForm
from .models import SignUp
# Create your views here.

#contact url hit

def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)

	if form.is_valid():
		full_name = form.cleaned_data.get("full_name")
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		
		# print email, message, full_name
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email, 'sushant_pupneja@yahoo.com']
		contact_message = '%s: %s via %s' %(full_name, message, email)
		send_mail(
				subject, 
				contact_message, 
				from_email, 
				to_email, 
				fail_silently=False)
	
	context = {
		'form': form,
		 'title': title,

	}

	return render(request, "forms.html", context)


#home url hit



def home(request):
	title = "Welcome %s start purchasing product's" %(request.user)
	if not request.user.is_authenticated():
		title = "Welcome!"

	form = SignUpForm(request.POST or None)

	context = {

		"template_title": title,
		"form": form

	}




	if form.is_valid():
		print request.POST['email']
		instance = form.save(commit=False)
		instance.save()
		context = {
			'template_title': 'Thank You for Sign Up',

		}

	if request.user.is_authenticated() and request.user.is_staff:
		instance = SignUp.objects.all()
		for f in instance:
			print f
		context = {

			'instance':instance,
		}
	
	


	return render(request, "home.html" , context)




def signuplist(request):
	instance = SignUp.objects.all().order_by('-timestamp')
	context = {
		'instance':instance,
	}
		
	return render(request, "signuplist.html", context)