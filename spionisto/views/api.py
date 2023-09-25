from cornice import Service
from spionisto import models
_VALUES = {}

settings_api = Service(name='settings_api',
                 path='/api/v1/settings',
                 description="Spionisto Settings API")


users_api = Service(name='users_api',
                 path='/api/v1/users',
                 description="Spionisto Users API")


@settings_api.get(context='..models.SpionistoRoot')
def get_settings(request):
    """Returns the settings
    """
    return request.context['settings'].as_dict()


# @settings.api.get(context='..models.Users')