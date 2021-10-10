from django.db import models
from django.db.models.fields import CharField

class user(models.Model) :
    id = models.IntegerField(auto_created=True, primary_key=True) 
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    id_identification_type = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    number_id = models.CharField(max_length=15)
    id_city = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class session (models.Model) :
    id = models.IntegerField(auto_created=True, primary_key=True)
    id_user = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    ip = models.CharField((""), max_length=200)
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class identification_type (models.Model):
    id =models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE), models.AutoField((""))
    type = models.CharField((""), max_length=150)
    abrev = models.CharField((""), max_length=4)
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class city (models.Model):
    id = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    code = models.CharField((""), max_length=10)
    name = models.CharField((""), max_length=150)
    abrev = models.CharField((""), max_length=4)
    id_country = models.IntegerField((""))
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class country (models.Model):
    id = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    code = models.CharField((""), max_length=10)
    name = models.CharField((""), max_length=150)
    abrev = models.CharField((""), max_length=4)
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class pet (models.Model):
    id = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    code = models.CharField((""), max_length=10)
    name = models.CharField((""), max_length=150)
    status = models.BooleanField((""))
    id_user = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    id_type = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    id_race = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class type (models.Model):
    id = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    code = models.CharField((""), max_length=10)
    name = models.CharField((""), max_length=150)
    abrev = models.CharField((""), max_length=4)
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)

class race (models.Model):
    id = models.IntegerField(("")), models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)
    code = models.CharField((""), max_length=10)
    name = models.CharField((""), max_length=150)
    abrev = models.CharField((""), max_length=4)
    status = models.BooleanField((""))
    created_at = models.DateTimeField( (""), auto_now=False, auto_now_add=False)
    updated_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)
    deleted_at = models.DateTimeField((""), auto_now=False, auto_now_add=False)


