from django.contrib import admin
from .models import Tag, Standings, Post, Comment

# Register your models here.

class StandingsAdmin(admin.ModelAdmin):
    list_display = ("club", "MP", "GD", "pts",)
    list_filter = ("pts",)
    prepopulated_fields = {"standings_slug": ("club",)}



class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}

class CommentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")



admin.site.register(Standings, StandingsAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)


#username: tea
#pass: teatea
