from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import make_password, check_password

from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User, UserFavourite

from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
# Create your views here.

@csrf_exempt
def userRegistration(request):
	data = JSONParser().parse(request)

	if "email" in data and len(data) == 1:
		email = data["email"]
		try:
			user = User.objects.get(email = email)
			user_id = user.user_id

			return JsonResponse({"user_id": user_id, "login_type": "signin"}, status = 200)

		except ObjectDoesNotExist:

			return JsonResponse({"user_id": "not registered", "login_type": "signup"}, status = 400)
	elif "user_id" in data:
		user_id = data["user_id"]
		password = data["password"]
		try:
			user = User.objects.get(user_id = user_id)
			if check_password(password, user.password):
				return JsonResponse({"message": "login successfull"}, status = 202)
			else:
				return JsonResponse({"message": "failed"}, status = 400)
		except ObjectDoesNotExist:
			return JsonResponse({"message": "user_id is invalid"}, status = 400)

	elif "email" in data and len(data) == 4:
		email = data["email"]
		first_name = data["first_name"]
		last_name = data["last_name"]
		password = data["password"]
		hashed_pwd = make_password(password)

		try:
			user = User.objects.create(email = email, first_name = first_name, last_name = last_name, password = hashed_pwd)
			return JsonResponse({"message": "registration success", "user_id": user.user_id}, status = 201)
		except:
			return JsonResponse({"message": "invalid credentials"}, status = 201)

@csrf_exempt
def userDetails(request):
	data = JSONParser().parse(request)
	user_id = data["user_id"]

	try:
		user_data = User.objects.values("email", "first_name", "last_name").get(user_id = user_id)
		user = User.objects.get(user_id = user_id)

		favoutites_list = UserFavourite.objects.values_list('favourite').filter(user = user)
		favourites = []
		for fav in favoutites_list:
			favourites.append(fav[0])
		print(favourites)

		user_data["favourite"] = favourites

		return JsonResponse(user_data, status = 200)

	except ObjectDoesNotExist:
		return JsonResponse({"message": "invalid credentials"}, status = 400)

@csrf_exempt
def addFavourite(request):
	data = JSONParser().parse(request)
	user_id = data["user_id"]
	fav = data["favourite"]

	try:
		user = User.objects.get(user_id = user_id)
		UserFavourite.objects.create(user = user, favourite = fav)

		return JsonResponse({"message": "favourite list updated"}, status = 200)

	except:
		return JsonResponse({"message": "invalid credentials"}, status = 400)



@csrf_exempt
def removeFavourite(request):
	data = JSONParser().parse(request)
	user_id = data["user_id"]
	fav = data["favourite"]

	try:
		user = User.objects.get(user_id = user_id)
		UserFavourite.objects.get(user = user, favourite = fav).delete()

		return JsonResponse({"message": "deletion success"}, status = 200)

	except:
		return JsonResponse({"message": "invalid credentials"}, status = 400)









