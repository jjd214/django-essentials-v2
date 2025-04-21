from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'title', 'created_at')

