from django.forms import ModelForm
from django.forms import Textarea, TextInput, Select
from .models import University, UniversityOwner, UniversityStaff
from .models import Alumni
from django.utils import timezone



class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = "__all__"


class AlumniForm(ModelForm):
	class Meta:
		model = Alumni
		#fields = "__all__"
		exclude = ["university"]

		grad_semester_choices = [(sem,sem) for sem in ["Fall","Summer","Spring","other"]]

		current_year = timezone.now().year
		years = [(year, year) for year in range(current_year+2, 1900 , -1) ]


		widgets={
			"phone_number": TextInput(),
			"graduation_year":Select(choices=years),
			"graduation_month": Select(choices=grad_semester_choices),
		}