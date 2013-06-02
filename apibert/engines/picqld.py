import data.picqld.models as picqld


def _to_keywords(text):
    keywords = set()
    l = text.split(' ');
    for s in l:
        if len(s) > 4:
            keywords.add(s)
    return keywords


class PictureQueenslandEngine(object):
    """ picture queensland engine, returns a engine wrapping the pictures queensland data
    """

    def keyword(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with keyword as a 
        keyword in the dict.
        """
        return self._items(picqld.get_items_by_keywords(value, num))

    def date(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with all dict 
        objects matching the date passed
        """
        return self._items(picqld.get_items_by_date(value, num))

    def id(self, value, num, request):
        """ Returns at most 1 dict objects, as an iterable, specified by its id 
        of value
        """
        item = picqld.get_item_by_id(value)
        return self._items([item])

    def _items(self, items):
        results = []
        for item in items:
            results.append(self._format_result(item))
        return results

    def _format_result(self, item):        
        return {
            'id':item.id, 
            'keyword': self._format_keywords(item),
            'text': item.description,
            'date': item.year,
            'url' : item.small_url,
            'url_link' : item.large_url,
        }

    def _format_keywords(self, item):
        keywords = set()
        keywords |= _to_keywords(item.description)
        keywords |= _to_keywords(item.subjects)
        return list(keywords)

    def _format_text(self, item):
        return item.description

    def _format_date(self, item):
        return item.year

    def _format_photo(self, item):
        url = ''
        if item.photo_id is not None:
            url = '/assets/myouseum/%s.jpg' % item.photo_id
        return url
