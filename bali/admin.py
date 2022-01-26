from django.contrib import admin

# Register your models here.
from bali.models import CheckList, CheckListItem

admin.site.register(CheckList)
admin.site.register(CheckListItem)