from django.urls import path, include

from .views import userRegistration, userDetails, addFavourite, removeFavourite

urlpatterns = [
	path('login_signup/', userRegistration),
	path('get_details/', userDetails),
	path('add_favourite/', addFavourite),
	path('remove_favourite/', removeFavourite)
]
