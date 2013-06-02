from pyramid.view import view_config
import requests

@view_config(route_name='speak', renderer='templates/speak/speak.jinja2')
def speak(request):
    cmd = request.matchdict['cmd']
    url = 'http://127.0.0.1:8080/speak/%s' % cmd
    r = requests.get(url)
    search_results = r.json()
    return {
        'speak': search_results
    }
