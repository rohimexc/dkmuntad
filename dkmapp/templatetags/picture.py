from django import template
from django.contrib.auth.models import User
from dkmapp.models import DKM

register = template.Library()
@register.simple_tag(takes_context=True)
def get_user_profil(context):
    request = context['request']
    user=User.objects.get(username=request.user)
    try:
        profile = DKM.objects.get(id_dkm=user)
        photo=f'.././media/{profile.photo}'
    except:
        photo='.././static/img_2/profile-img.jpg'
    return photo