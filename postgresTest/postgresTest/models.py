from django.db import models
"""
class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    class_id = models.IntegerField()
    login_user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user' """

class photo(models.Model):
    photo_id = models.IntegerField(primary_key=True)
    date = models.CharField(max_length=11)
    time = models.CharField(max_length = 20)
    location = models.CharField(max_length = 100)
    size = models.IntegerField()
    tag_color = models.CharField(max_length = 10)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'photo'