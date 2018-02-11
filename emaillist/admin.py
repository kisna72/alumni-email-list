from django.contrib import admin
from .models import University, UniversityOwner, UniversityStaff, Alumni, WorkHistory, Invite
# Register your models here.
admin.site.register(University)
admin.site.register(UniversityOwner)
admin.site.register(UniversityStaff)
admin.site.register(Alumni)
admin.site.register(WorkHistory)
admin.site.register(Invite)
