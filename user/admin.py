from django.contrib import admin
from .models import ProfessionalName, Service, PersonalInformation, Skill, GalleryImage, UserInformation

admin.site.register(ProfessionalName)
admin.site.register(Service)
admin.site.register(PersonalInformation)
admin.site.register(Skill)
admin.site.register(GalleryImage)
admin.site.register(UserInformation)
