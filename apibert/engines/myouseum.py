import data.myouseum.models as myouseum


def _to_keywords(text):
    keywords = set()
    l = text.split(' ');
    for s in l:
        if len(s) > 4:
            keywords.add(s)
    return keywords


class CollectionItemEngine(object):
    """ myouseum engine class, returns a dict object for the myouseum150 collections
    """

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
        item = myouseum.get_item_by_id(value)
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
            'text': self._format_text(item),
            'date': self._format_date(item),
            'url' : self._format_photo(item),
        }

    def _format_keywords(self, item):
        keywords = set()
        keywords |= _to_keywords(item.collection.title)
        keywords |= _to_keywords(item.collection.description)
        return list(keywords)

    def _format_text(self, item):
        return '%s %s' % (item.collection.title, item.collection.description)

    def _format_date(self, item):
        return item.collection.year

    def _format_photo(self, item):
        url = ''
        if item.photo_id is not None:
            url = '/assets/myouseum/%s.jpg' % item.photo_id
        return url


class CollectionPhotoEngine(object):
    """ myouseum engine class, returns a dict object for the 
    myouseum150 photos
    """        

    def keyword(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with keyword as a 
        keyword in the dict.
        """
        return self._photos(myouseum.get_photos_by_keywords(value, num))

    def date(self, value, num, request):
        """ Returns at most num dict objects, as an iterable, with all dict 
        objects matching the date passed
        """
        photos = []
        ids = set()
        items = myouseum.get_items_by_date(value, num)
        for item in items:
            ids.add(item.photo_id)
        for id in ids:
            photos.append(myouseum.get_photos_by_id(id))
        return self._photos(photos)

    def id(self, value, num, request):
        """ Returns at most 1 dict objects, as an iterable, specified by its id 
        of value
        """
        photo = myouseum.get_photos_by_id(id)
        return self._photos([photo])

    def _photos(self, photos):
        results = []
        for photo in photos:
            results.append(self._format_result(photo))
        return results

    def _format_result(self, photo):        
        return {
            'id':photo.id, 
            'keyword': self._format_keywords(photo),
            'text': self._format_text(photo),
            'date': self._format_date(photo),
            'url' : self._format_photo(photo),
        }

    def _format_keywords(self, photo):
        keywords = set()
        keywords |= _to_keywords(photo.object_name)
        keywords |= _to_keywords(photo.story)
        return list(keywords)

    def _format_text(self, photo):
        return '%s %s' % (photo.object_name, photo.story)

    def _format_date(self, photo):        
        return ''

    def _format_photo(self, photo):
        return '/assets/myouseum/%s.jpg' % photo.id
