from django.contrib import admin

from main_app.models import Sister, Pnm, Nickname_Request, Chapter

# Register your models here.

admin.site.register(Sister)
admin.site.register(Pnm)
admin.site.register(Nickname_Request)
admin.site.register(Chapter)
