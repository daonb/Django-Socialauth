from django.conf import settings

def socialauth (request):
    return {'fb_api_key':settings.FACEBOOK_API_KEY,}
