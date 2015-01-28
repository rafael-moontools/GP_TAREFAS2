# This is models.py for a new user profile that you would like to create.

"""
this gist gets an id from django-social-auth and based on that saves the photo from social networks into your model. This is one of the best ways to extend User model because this way, you don't need to redefine a CustomUser as explained in the doc for django-social-auth. this is a new implementation based on https://gist.github.com/1248728
"""

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db import models
from social.backends import google
# from social_auth.signals import socialauth_registered

from urllib2 import urlopen, HTTPError
from django.template.defaultfilters import slugify
from django.core.files.base import ContentFile

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    pass
#
# class UserProfile(models.Model):
#
#     user = models.OneToOneField(User)
#     profile_photo = models.ImageField(upload_to='profiles')
#
#     def __str__(self):
#         return "%s's profile" % self.user
#
#
#
# def new_users_handler(sender, user, response, details, **kwargs):
#     user.is_new = True
#     if user.is_new:
#         if "id" in response:
#
#             try:
#                 url = None
#                 # if sender == FacebookBackend:
#                 #     url = "http://graph.facebook.com/%s/picture?type=large" \
#                 #                 % response["id"]
#                 if sender == google.GoogleOAuth2Backend and "picture" in response:
#                     url = response["picture"]
#
#                 if url:
#                     avatar = urlopen(url)
#                     profile = UserProfile(user=user)
#
#                     profile.profile_photo.save(slugify(user.username + " social") + '.jpg', ContentFile(avatar.read()))
#                     profile.save()
#
#             except HTTPError:
#                 pass
#
#     return False
#
# socialauth_registered.connect(new_users_handler, sender=None)
