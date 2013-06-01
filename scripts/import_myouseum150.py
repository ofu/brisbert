import sys
from datetime import datetime
sys.path.append('./')

import transaction
import csv
import data.common as common
import data.myouseum150.models as models

common.init('sqlite:///bert.sqlite')

with transaction.manager:
    with open('external_data/myouseum150-collections.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:        
            collection = models.Collection()
            collection.id = u'%s' % row[0]
            collection.title = u'%s' % row[1]
            collection.description = u'%s' % row[2]
            collection.date = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
            models.add_collection(collection)

            item = models.CollectionItem()
            item.photo_id = row[4]
            item.object_name = u'%s' % row[5]
            item.scientific_name = u'%s' % row[6]
            item.story = u'%s' % row[7]
            item.vernon_id = u'%s' % row[8]
            item.qm_filename = u'%s' % row[9]
            item.credit = u'%s' % row[10]
            item.comment = u'%s' % row[11]
            models.add_collection_item(collection, item)
