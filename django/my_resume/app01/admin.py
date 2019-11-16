from django.contrib import admin
from . import models

# Register your models here.


#定制下模板
class  ResumeAdmin(admin.ModelAdmin):
    #展示出来的
    list_display = ("resume_name","resume_type")
    #可以编辑的
    list_display_links = ("resume_type",)

admin.site.register(models.Type)
admin.site.register(models.Username)
admin.site.register(models.Resume,ResumeAdmin)