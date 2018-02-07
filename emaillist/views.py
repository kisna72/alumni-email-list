from django.shortcuts import render
from organizations.forms import OrganizationAddForm
# Create your views here.
def organization_signup(request):
	form = OrganizationAddForm(request)

	return render(request, "emaillist/org_signup.html", {"form":form})