from django.forms import ModelForm
from .models import University, UniversityOwner, UniversityStaff


class UniversityForm(ModelForm):
	class Meta:
		model = University
		fields = "__all__"

