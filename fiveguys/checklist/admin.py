from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Checklist)
admin.site.register(Checklistitem)
admin.site.register(Completedchecklists)
admin.site.register(Item)
admin.site.register(Store)
admin.site.register(Template)
admin.site.register(Managers)