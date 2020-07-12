from django.contrib import admin


from newsapp.models import mainnews

# Register your models here.


class mainnewsAdmin(admin.ModelAdmin):
    list_display = ['news1', 'news2', 'news3', 'news4', 'news5', 'news6']


admin.site.register(mainnews, mainnewsAdmin)
