from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # user = models.OneToOneField(User, unique=True, null=True)
    user = models.OneToOneField(User)
    profile_photo = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user.username)

    def getProfilePicture(self):
        return self.profile_photo