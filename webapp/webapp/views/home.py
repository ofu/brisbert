from pyramid.view import view_config
from webhelpers import paginate
from webhelpers.paginate import Page

@view_config(route_name='home', renderer='templates/home/home.jinja2')
def home(request):
    return {'subject': "robots"}
