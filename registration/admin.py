from django.contrib import admin
from registration.models import *

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class ChocolateAdmin(admin.ModelAdmin):
    pass
admin.site.register(Chocolate, ChocolateAdmin)
