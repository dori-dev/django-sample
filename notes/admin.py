from django.contrib import admin
from .models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'author', 'created')
    list_filter = ('author',)
    search_fields = ('title', 'body', 'author__username')


admin.site.register(Note, NoteAdmin)
