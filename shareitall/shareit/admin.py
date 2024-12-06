from django.contrib import admin
from .models import Listing, Service, Category, ForumPost


admin.site.register(Listing)
admin.site.register(Service)
admin.site.register(Category)
admin.site.register(ForumPost)