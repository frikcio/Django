from django.contrib import admin
from .models import *

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookTable)
admin.site.register(SomeUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Grant)

# Register your models here.
