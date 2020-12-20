from django.contrib import admin

# Register your models here.

from .models import User, UserFavourite

class UserInfoAdmin(admin.ModelAdmin):
	list_display = ["user_id", "email", "password", "first_name", "last_name", "created_at"]

admin.site.register(User, UserInfoAdmin)

class UserFavouriteAdmin(admin.ModelAdmin):
	list_display = ["id", "user", "favourite"]

admin.site.register(UserFavourite, UserFavouriteAdmin)