from django.contrib import admin

# Register your models here.
from models import Meeting


class MeetingAdmin(admin.ModelAdmin):
    list_display = ('user',
                    'mentor_name',
                    'mentee_name',
                    'date',
                    'subject',
                    'status',
                    'comments',
                    )


admin.site.register(Meeting, MeetingAdmin)
