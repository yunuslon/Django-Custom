from django.contrib import admin
from orm.models import TesOlimpiade

class TesOlimpiadeAdmin(admin.ModelAdmin):
    pass
admin.site.register(TesOlimpiade, TesOlimpiadeAdmin)
