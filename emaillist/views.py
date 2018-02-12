from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import University, UniversityOwner, UniversityStaff
from .forms import UniversityForm
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
	context["has_associated_unis"] = True if len(associated_unis)>0 else False

	return render(request, "emaillist/home.html", context)

@login_required
def add_organization(request):
	"""
	Simple form with just the name of the university.
	Univeristy Owner is automatically assigned to the current owner. 
	This person has delete access to the University. 
	Can add other owners. 
	"""
	if request.method == "POST":
		form = UniversityForm(request.POST)
		if form.is_valid():
			uni = form.save()
			#Create Uni owner as well. 
			print(uni)
			owner = UniversityOwner.objects.create(university = uni, user = request.user)
			staff = UniversityStaff.objects.create(university = uni, user = request.user)

			return redirect("emaillist_home")
	else:
		form = UniversityForm()

	context = {}
	context["form"] = form

	return render(request, "emaillist/create_organization.html", context)


@login_required
def organization_detail(request, organization_pk):
	"""
	Details of the Organization.

	Name , created, modified

	Owners

	Staffs

	related emails


	Buttons
	--------
	Add Owner. Owners can delete the organization....
	Add Staff. 
	"""
	organization = get_object_or_404(University, pk = organization_pk)
	context = {}
	
	owners = UniversityOwner.objects.filter(university = organization)
	staffs = UniversityStaff.objects.filter(university = organization)
	
	context["organization"] = organization
	context["owners"] = owners
	context["staffs"] = staffs

	return render(request, "emaillist/organization_detail.html", context)
	


@login_required
def edit_organization(request, org_id):
	"""
	Simple form with just the name of the university.
	Univeristy Owner is automatically assigned to the current owner. 
	This person has delete access to the University. 
	Can add other owners. 
	"""
	org = get_object_or_404(University, pk = org_id)
	# Only owner has rights to make changes to the organization.
	org_owners = UniversityOwner.objects.filter(organization = org, user = request.user)
	if len(org_owners) > 1:
		pass
	if request.method == "POST":
		form = UniversityForm(request.POST)
		if form.is_valid():
			uni = form.save()
			#Create Uni owner as well. 
			owner = UniversityOwner.objects.create(university = uni, user = request.user)
			staff = UniversityStaff.objects.create(university = uni, user = request.user)

			return redirect("emaillist_home")
	else:
		form = UniversityForm()

	context = {}
	context["form"] = form

	return render(request, "emaillist/create_university.html", context)
