import data.myouseum.models as myouseum
import data.common as common

class CollectionItemEngine(object):
    """ myouseum engine class, returns a dict object for the myouseum150 collections
    """

    def __init__(self):
        common.init('sqlite:///bert.sqlite')

    def keyword(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with keyword as a 
        keyword in the dict.
        """
        return self._items(myouseum.get_items_by_keywords(value, num))

    def date(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with all dict 
        objects matching the date passed
        """
        return self._items(myouseum.get_items_by_date(value, num))

    def id(self, value, num, request):
        """ Returns at most 1 dict objects, as an iterable, specified by its id 
        of value
        """
        item = myouseum.get_item_by_id(value, num)
        return self._items([collection])

    def _items(self, items):
        results = []
        for item in items:
            results.append(self._format_item(item))
        return results

    def _format_item(self, item):        
        return {
            'id':item.id, 
            'keyword': self._format_keywords(item),
            'text': self._format_text(item),
            'date': self._format_date(item),
            'url' : self._format_photo(item),
        }

    def _format_keywords(self, item):
        keywords = set()
        keywords |= self._to_keywords(item.collection.title)
        keywords |= self._to_keywords(item.collection.description)
        keywords |= self._to_keywords(item.object_name)
        keywords |= self._to_keywords(item.scientific_name)
        keywords |= self._to_keywords(item.story)
        keywords |= self._to_keywords(item.credit)
        keywords |= self._to_keywords(item.comment)
        return list(keywords)

    def _format_text(self, item):
        return '%s %s %s' % (item.collection.title, item.collection.description, item.story)

    def _to_keywords(self, text):
        keywords = set()
        l = text.split(' ');
        for s in l:
            if len(s) > 4:
                keywords.add(s)
        return keywords

    def _format_date(self, item):
        return item.collection.year

    def _format_photo(self, item):
        url = ''
        if item.photo_id is not None:
            url = '/assets/myouseum/%s.jpg' % item.photo_id
        return url
