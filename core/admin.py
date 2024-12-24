from django.contrib import admin
from .models import User, Skill, UserSkill, Reference, WorkExperience, Contact, Education

admin.site.register(User)
admin.site.register(Skill)
admin.site.register(UserSkill)
admin.site.register(Reference)
admin.site.register(WorkExperience)
admin.site.register(Contact)
admin.site.register(Education)

