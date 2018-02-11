from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import University, UniversityOwner, UniversityStaff
from organizations.forms import OrganizationAddForm
# Create your views here.
# Step 1 - Signup with a username password. 

@login_required
def home(request):
	"""
	1. Check if the user is associated with a university. If yes, show the email list for this university.
	If no, ask them to
	-- Create 
	-- Join
	"""
	context = {}
	universities = University.objects.all()
	print(universities)
	associated_unis = UniversityStaff.objects.filter(user = request.user)

	context["universities"] = universities
	context["associated_unis"] = associated_unis

	return render(request, "emaillist/home.html", context)

