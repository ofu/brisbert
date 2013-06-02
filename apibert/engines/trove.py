import requests

def _to_keywords(text):
    keywords = set()
    l = text.split(' ');
    for s in l:
        if len(s) > 4:
            keywords.add(s)
    return keywords

    
class TroveBaseEngine(object):
    """ Trove engine, returns a engine wrapping the pictures queensland data
    """
    trove_key_ = 'jveqr2nb1rqgn1mp'
    trove_uri_ = 'http://api.trove.nla.gov.au/result'
    trove_zones_ = 'picture'

    def keyword(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with keyword as a 
        keyword in the dict.
        """
                                             
        try:
            r = requests.get(TroveBaseEngine.trove_uri_, 
                             params={'key': TroveBaseEngine.trove_key_, 
                                     'zone': TroveBaseEngine.trove_zones_, 
                                     'q': value,
                                     'l-australian': 'y',
                                     'encoding': 'json',
                                     'n': num})
            return self._items(r.json())
        except Exception as e:
            print(str(e))
            return []


    def date(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with all dict 
        objects matching the date passed
        """
        try:
            r = requests.get(TroveBaseEngine.trove_uri_, 
                             params={'key': TroveBaseEngine.trove_key_, 
                                     'zone': TroveBaseEngine.trove_zones_, 
                                     'q': ' ',
                                     'l-australian': 'y',
                                     'l-year': value,
                                     'encoding': 'json',
                                     'n': num})
            return self._items(r.json())
        except Exception as e:
            return []
        return []

    def id(self, value, num, request):
        """ Returns at most 1 dict objects, as an iterable, specified by its id 
        of value
        """
        try:
            r = requests.get(TroveBaseEngine.trove_uri_, 
                             params={'key': TroveBaseEngine.trove_key_, 
                                     'zone': TroveBaseEngine.trove_zones_, 
                                     'q': 'id:' + str(value),
                                     'l-australian': 'y',
                                     'encoding': 'json'})
            return self._items(r.json())
        except Exception as e:
            return []

    def _items(self, items):
        print(str(items))
        results = []
        for item in items['response']['zone'][0]['records']['work']:
            results.append({'id': item['id'],
                            'keyword': self._format_keywords(item),
                            'text': self._format_text(item),
                            'date': self._format_date(item),
                            'url': self._format_url(item)})
                            
        return results

    def _format_keywords(self, item):
        keywords = set()
        if 'title' in item:
            keywords |= _to_keywords(item['title'])
        if 'snippet' in item:
            keywords |= _to_keywords(item['snippet'])
        return list(keywords)
        
    def _format_text(self, item):
        text = ''
        for key in ('title', 'snippet'):
            if key in item:
                text = text + item[key] + '\n'
        return text                

    def _format_date(self, item):
        return '' if 'issued' not in item else item['issued']
        
    def _format_url(self, item):
        for pic in item['identifier']:
            if pic['type'] == 'url' and (pic['linktype'] == 'unknown' or
                                         pic['linktype'] == 'thumbnail'):
                return pic['value']
        return ''
