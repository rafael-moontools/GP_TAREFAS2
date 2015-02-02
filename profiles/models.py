#coding: UTF8
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class UserProfile(models.Model):

    GENERO = (
        ('M', _('Masculino')),
        ('F', _('Feminino')),
    )

    user = models.OneToOneField(User)

    profile_photo = models.CharField(_('Profile Picture'), max_length=255, blank=True, null=True)
    cover_photo = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=150, blank=True, null=True)
    language = models.CharField(max_length=6, blank=True, null=True)
    gender = models.CharField(_(u'Gênero'), max_length=1, choices=GENERO, default='M')

    def __unicode__(self):
        return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user.username)

    def getProfilePicture(self):
        return self.profile_photo

    def getDisplayName(self):
        if self.display_name:
            return self.display_name
        else:
            return "%s %s (%s)" % (self.user.first_name, self.user.last_name, self.user.username)