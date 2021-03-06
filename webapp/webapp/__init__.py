from pyramid.config import Configurator

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('assets', 'assets', cache_max_age=3600)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('about', '/about')
    config.add_route('speak', '/speak/{id}/{cmd}/{kw}')
    config.add_route('item', '/{db}/{id}')
    config.include('pyramid_jinja2')
    config.scan('.views')
    return config.make_wsgi_app()
