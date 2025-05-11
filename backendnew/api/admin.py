from django.contrib import admin
from .models import student,teacher,course,course_category,Common_user,video
# Register your models here.
admin.site.register(student)
admin.site.register(teacher)
admin.site.register(course_category)
admin.site.register(course)
admin.site.register(video)
admin.site.register(Common_user)




