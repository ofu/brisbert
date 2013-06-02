from pyramid.view import view_config

@view_config(route_name='about', renderer='templates/about/about.jinja2')
def about(request):
    return {}
