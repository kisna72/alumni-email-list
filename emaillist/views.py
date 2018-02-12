from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
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
	Details of the Organization. Only visible to members or the owners. 

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
	
	if request.user in [i.user for i in owners] or request.user in [x.user for x in staffs]:
		context["organization"] = organization
		context["owners"] = owners
		context["staffs"] = staffs

		return render(request, "emaillist/organization_detail.html", context)
	
	return HttpRequest("You are not allowed to be here.")


@login_required
def edit_organization(request, organization_pk):
	"""
	Simple form with just the name of the university.
	Univeristy Owner is automatically assigned to the current owner. 
	This person has delete access to the University. 
	Can add other owners. 
	"""
	print("Got here")
	org = get_object_or_404(University, pk = organization_pk)
	# Only owner has rights to make changes to the organization.
	owners = UniversityOwner.objects.filter(university = org)
	if not request.user in [i.user for i in owners]:
		return HttpRequest("You most be a owner to edit the name of the organization.")

	if request.method == "POST":
		form = UniversityForm(request.POST, instance = org)
		if form.is_valid():
			uni = form.save()
			return redirect("organization_detail", organization_pk=uni.id)
	else:
		form = UniversityForm(instance = org)

	context = {}
	context["form"] = form
	return render(request, "emaillist/organization_edit.html", context)


@login_required
def delete_organization(request, organization_pk):
	"""Code to Delete Organization. 
	"""
	org = get_object_or_404(University, pk=organization_pk)
	owners = UniversityOwner.objects.filter(university = org)
	if not  request.user in [i.user for i in owners]:
		return HttpRequest("You do not have the permission to delete. Must be owner")
	if request.method == "POST":
		org.delete()
		return redirect("emaillist_home")

	else:
		print("Show Confirmation")

	return render(request, "emaillist/organization_delete.html")



def add_organization_owner(request):
	pass

def remove_organization_owner(request):
	pass

def add_organization_staff(request):
	pass

def remove_organization_staff(request):
	pass











