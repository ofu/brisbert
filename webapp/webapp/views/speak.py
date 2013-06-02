from pyramid.view import view_config
import requests

@view_config(route_name='speak', renderer='templates/speak/speak.jinja2', http_cache=0)
def speak(request):
    cmd = request.matchdict['cmd']
    kw = request.matchdict['kw']
    url = 'http://127.0.0.1:8080/speak/%s' % cmd
    r = requests.get(url)
    search_results = r.json()
    url = '<a href="/?search_query=%s">%s</a>' % (kw, kw)
    search_results['bert'] = search_results['bert'].replace('{{SUBJECT}}', url)
    return {
        'speak': search_results,        
    }
