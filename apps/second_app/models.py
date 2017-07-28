from __future__ import unicode_literals
from django.db import models
from ..first_app.models import User
from django.contrib import messages

# Create your models here.
class PokeManager(models.Manager):
    def createPoker(self, postData):
        results = {'status': True, 'poke': None}
        poke = []
        if results['status'] == True:
            print postData(['user_id']), '***********'
            userInt = int(postData['user_id'])
            user = User.objects.get(id = userInt)
            results['poke'] = Poke.objects.create(name = postData['name'], alias = postData['alias'], email = postData['email'], poker = user)
        return results

class Poke(models.Model):
    poke = models.ManyToManyField(User, related_name = 'poke')
    number_of_pokes = models.IntegerField(default = 0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = PokeManager()
