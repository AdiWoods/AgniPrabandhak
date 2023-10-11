from django.contrib import admin
from .models import ForestDepartmentData,ReportData

# Register your models here.


@admin.register(ForestDepartmentData)
class ShowForestData(admin.ModelAdmin):
    list_display=("id",'location','phone_no','longitude','lattitude')


@admin.register(ReportData)
class ShowReportData(admin.ModelAdmin):
    list_display=("id","longitude","lattitude","fireimage",'date')