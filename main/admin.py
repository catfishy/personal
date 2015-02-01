from django.contrib import admin
from main.models import WritingSample, MusicSample


# Register your models here.
class WritingSampleAdmin(admin.ModelAdmin):
    fields = ['title','text', 'static_img_location', 'archived', 'writing_type']
    list_display = ('title', 'text','static_img_location', 'archived', 'writing_type')

class MusicSampleAdmin(admin.ModelAdmin):
    fields = ['title','text', 'embed_html', 'archived']
    list_display = ('title', 'text', 'archived')

admin.site.register(WritingSample, WritingSampleAdmin)
admin.site.register(MusicSample, MusicSampleAdmin)