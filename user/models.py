from django.db import models

# Create your models here.


class User(models.Model):
	user_id = models.AutoField(primary_key = True, db_column = "User Id")
	email = models.EmailField(max_length = 128, unique = True, db_column = "Email")
	first_name = models.CharField(max_length = 25, db_column = "First Name")
	last_name = models.CharField(max_length = 25, db_column = "Last Name")
	password = models.CharField(max_length = 256, db_column = "Password")
	created_at = models.DateTimeField(auto_now_add = True, db_column = "Created At")


class UserFavourite(models.Model):
	user = models.ForeignKey(User, db_column = "User", on_delete = models.CASCADE)
	favourite = models.CharField(max_length = 100, db_column = "Favourite")