from django.db import models
from django.contrib.auth.models import User 
from organizations.models import Organization, OrganizationUser, OrganizationOwner
from django_extensions.db.models import TimeStampedModel


# Create your models here.
class University(TimeStampedModel):
    university_name = models.TextField()#Name of the university

class UniversityOwner(TimeStampedModel):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)

class UniversityStaff(TimeStampedModel):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)  

class Alumni(TimeStampedModel):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    email_address =  models.EmailField() #primary email address.
    phone_number = models.TextField()
    graduation_year = models.IntegerField()
    graduation_month = models.TextField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)

class WorkHistory(TimeStampedModel):
    company_name = models.TextField()
    work_email = models.EmailField()
    position = models.TextField()
    alumni = models.ForeignKey(Alumni, on_delete=models.CASCADE)




class OrganizationSecret(TimeStampedModel):

    def randStr():
        N = int(random.uniform(8,24))
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))


    secret = models.CharField(max_length=24, default=randStr, unique=True) #Must be unique
    organization = models.ForeignKey(University,  on_delete=models.CASCADE)
    active = models.BooleanField(default = True)

"""

Auth Model.
Phase 1:
User signs up. Creates a University. 
Invites other users to signup with a email link. [Email link is generated on the site.]
Email link can be hash of the id of the organization. Signup will look like 
- blah.com/signup/hash/



Each authorized User is associated with a univeristy. 

User can be staff   -    can add other staffs and student leaders. 
student leader     -    can add email addresses. Cannot add staff. Can add student leaders. Cannot delete. 

Staff can add student leaders.
Student leader can add email addresses. 


User Story
A)
1. User signs up. 
2. They create a organization - Use Django Organization for ease of APIs. 
3. They invite others to join. Invitation can be for staff or for student leader. 

try:
/Users/krishnaregmi/workdir/alumni-email-list/emaillist/templates/emailist/org_signup.html

/Users/krishnaregmi/workdir/alumni-email-list/emaillist/templates/emaillist/org_signup.html
/Users/krishnaregmi/workdir/alumni-email-list/emaillist/templates/emailist/org_signup.html
"""