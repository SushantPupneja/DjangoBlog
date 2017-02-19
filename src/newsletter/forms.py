from django import forms

from .models import SignUp


class ContactForm(forms.Form):
	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()



class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ["full_name", "email"]

		## we can use exclude as well
		## exclude = ["email"]

		#Lets start with validation of the form fields
		# Get the instance of the form using self
		# make sure to add cleaned_data use any custom validator.

	def clean_email(self):
		email = self.cleaned_data.get('email')
		#validation code starts here

		#This should not consider as a good practise if a particular extension is required 
		#if not "edu" in email:
		#	raise forms.ValidationError("Please enter valid edu extension address")

		base_name, provider = email.split('@')
		domain, extension = provider.split('.')
		if not extension == "edu":
			raise forms.ValidationError("Please enter valid edu extension address")
		return email
		

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#validation code starts here
		return full_name