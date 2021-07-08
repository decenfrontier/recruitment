from django.contrib import admin
from jobs.models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('type', 'name', 'city', 'creator', 'created_date', 'modified_date')


admin.site.register(Job, JobAdmin)