from django.contrib import admin
from .models import Award, Movie, Viewer


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'plot', 'runtime', 'released', 'awards', 'genres')
    search_fields = ('title', 'plot')


@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
