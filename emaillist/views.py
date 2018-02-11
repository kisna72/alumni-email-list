from django.shortcuts import render
from organizations.forms import OrganizationAddForm
# Create your views here.
# Step 1 - Signup with a username password. 

def home(request):
	return render(request, "emaillist/home.html")


def organization_signup(request):
	form = OrganizationAddForm(request)
	return render(request, "emaillist/org_signup.html", {"form":form})