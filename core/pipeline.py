#coding: utf8
from profiles.models import UserProfile

# def create_UserProfile(sender, details, response, user, *args, **kwargs):
def teste_de_pipeline(response, user, **kwargs):
    try:
        profile_picture = response.get('image')['url']

        # username = response['username']
        # user_object = User.objects.get(username=username)
        user_object = user
        if UserProfile.objects.filter(user=user_object).exists():
            print "Usuário Existente"
            pass
        else:
            print "Salvando foto"
            new_profile = UserProfile(user=user_object, profile_photo=profile_picture)
            new_profile.save()
    except NameError:
        print "ERRO"
        raise

    return kwargs