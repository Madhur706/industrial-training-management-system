

from django.contrib import admin

from .models import (
    Register,
    Training,
    Attendance,
    Report,
    Certificate
)

admin.site.register(Register)
admin.site.register(Training)
admin.site.register(Attendance)
admin.site.register(Report)
admin.site.register(Certificate)