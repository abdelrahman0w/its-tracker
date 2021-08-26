from django.contrib import admin
from .models import *


class CarAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('car_id',)

        return self.readonly_fields


class ViolationAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('car',)

        return self.readonly_fields


class TrafficAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('street', 'additional',)

        return self.readonly_fields

admin.site.register(Car, CarAdmin)
admin.site.register(Violation, ViolationAdmin)
admin.site.register(Traffic, TrafficAdmin)
