from django.contrib import admin
from lib_sys.models import BookInfo, AuthorInfo, BorrowerInfo, LenderInfo
# Register your models here.

admin.site.register(BookInfo)
admin.site.register(AuthorInfo)
admin.site.register(BorrowerInfo)
admin.site.register(LenderInfo)