from django.contrib import admin
from .models import Letter


class LetterAdmin(admin.ModelAdmin):
    list_display = ('title', 'send_date', 'number_of_readers')


admin.site.register(Letter, LetterAdmin)