from django.contrib import admin
from .models import Clients, Tasks, Deals

# admin.site.register(Clients)

@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone','company')
    search_fields = ('name', 'email', 'phone','company')
    list_filter = ('company',)


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'status', 'client')
    search_fields = ('name','price', 'status', 'client__name')
    list_filter = ('company',)


@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('description', 'deadline', 'comleted', 'client')
    search_fields = ('description', 'client__name')
    list_filter = ('comleted',)


