from pyramid.view import view_config

from ..models import SpionistoRoot


@view_config(context=SpionistoRoot, renderer='spionisto:templates/mytemplate.jinja2')
def my_view(request):
    return {'project': 'Spionisto'}
