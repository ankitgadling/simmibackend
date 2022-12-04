from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Blog)
admin.site.register(Quote)
admin.site.register(Timeline)
admin.site.register(Story)