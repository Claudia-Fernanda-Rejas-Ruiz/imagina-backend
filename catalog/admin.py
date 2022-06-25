from django.contrib import admin

# Register your models here.
from .models import Cliente, CotizaInstance


admin.site.register(Cliente)
admin.site.register(CotizaInstance)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    fields = ['first_name', 'last_name']




class CotizaInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )