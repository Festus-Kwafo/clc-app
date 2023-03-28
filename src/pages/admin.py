from django.contrib import admin
from pages.models import Sermon, Announcement, Gallery

admin.site.admin_header = "CLC ADMINISTRATION"  # default: "Django Administration"
# Register your models here.
admin.site.register(Sermon)
admin.site.register(Announcement)
admin.site.register(Gallery)