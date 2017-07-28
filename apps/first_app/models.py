from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []

        if not postData['name'] or len(postData['name']) < 3:
            results['status'] = False
            results['errors'].append('Name needs to be longer than 2 characters.')

        if not postData['alias'] or len(postData['alias']) < 3:
            results['status'] = False
            results['errors'].append('Alias name needs to be longer than 2 characters.')

        if not postData['email'] or len(postData['email']) < 5 or not re.match(r'[^@]+@[^@]+\.[^@]+', postData['email']):
            results['status'] = False
            results['errors'].append('Email is invalid.')

        if not postData['password'] or len(postData['password']) < 8 != postData['con_password']:
            results['status'] = False
            results['errors'].append('Password does not match. Please try again.')

        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])

        if len(user) != 0:
            results['status'] = False
            results['errors'].append('User already exists. Please try another email.')

        print results['status']
        print results['errors']
        return results


    def loginVal(self, postData):
        results = {'status':True, 'errors': [], 'user': None}
        if len(postData['email']) < 3:
            results['status'] = False
            results['errors'].append('Something went wrong. Double check everything.')

        else:
            user = User.objects.filter(email = postData['email'])

            if len(user) <= 0:
                results['status'] = False
                results['errors'].append('Something went wrong. Double check everything.')

            elif len(postData['password']) < 8 or postData['password'] != user[0].password:
                results['status'] = False
                results['errors'].append('Something went wrong. Double check everything.')

            else:
                results['user'] = user[0]

        print results['status']
        print results['errors']
        return results

    def createUser(self, postData):
        p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = User.objects. create(name = postData['name'], alias = postData['alias'], email = postData['email'], password = postData['password'])
        return user


class User(models.Model):
    name = models.CharField(max_length = 100)
    alias = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    birth_date = models.DateField(max_length = 8, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
