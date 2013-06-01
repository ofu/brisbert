import sys
from datetime import datetime
sys.path.append('./')

import transaction
import csv
import data.common as common
import data.myouseum150.models as models

def to_unicode(s):
    try:
        return u'%s' % s
    except:
        print s

common.init('sqlite:///bert.sqlite')

with transaction.manager:
    with open('external_data/myouseum150-collections.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:        
            collection = models.Collection()
            collection.id = to_unicode(row[0])
            collection.title = to_unicode(row[1])
            collection.description = to_unicode(row[2])
            collection.date = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            models.add_collection(collection)

            item = models.CollectionItem()
            item.photo_id = row[4]
            item.object_name = to_unicode(row[5])
            item.scientific_name = to_unicode(row[6])
            item.story = to_unicode(row[7])
            item.vernon_id = to_unicode(row[8])
            item.qm_filename = to_unicode(row[9])
            item.credit = to_unicode(row[10])
            item.comment = to_unicode(row[11])
            models.add_collection_item(collection, item)

with transaction.manager:
    with open('external_data/myouseum150-photos.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:        
            photo = models.Photo()
            photo.id = to_unicode(row[0])
            photo.object_name = to_unicode(row[1])
            photo.scientific_name = to_unicode(row[2])
            photo.story = to_unicode(row[3])
            photo.vernon_id = to_unicode(row[4])
            photo.qm_filename = to_unicode(row[5])
            photo.credit = to_unicode(row[6])
            models.add_photo(photo)
