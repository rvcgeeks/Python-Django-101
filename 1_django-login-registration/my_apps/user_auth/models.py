
# created by rvcgeeks <github.com/rvcgeeks> (linkedin.com/in/rvchavadekar) @ Pune, India

from django.db import models
from re import fullmatch

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        name_regx = r"^[a-zA-Z ,.'-]{2,}$" # name should be greater than 2 chars
        if not fullmatch(name_regx, postData['first_name']):
            errors['first_name'] = "First name invalid"

        if not fullmatch(name_regx, postData['last_name']):
            errors['last_name'] = "Last name invalid"

        if not fullmatch(r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$", postData['email']):
            errors['email'] = "Enter a valid email"

        if not fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$", postData['password']):
            errors['password'] = "Password must be 6 chars long, must have atleast one numeral, one uppercase, one lowercase, and any special characher from @$!%*#?&"
            
        if postData['password'] != postData['confirm_password']:
            errors['confirm'] = "No Password match in confirmation"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
