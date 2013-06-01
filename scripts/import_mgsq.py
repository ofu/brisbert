import sys
from datetime import datetime
sys.path.append('./')

import transaction
import csv
import data.common as common
import data.mgsq.models as models

def to_unicode(s):
    try:
        return u'%s' % s
    except:
        print s

common.init('sqlite:///bert.sqlite')

with transaction.manager:
    with open('external_data/MuseumGalleryFinder-May2013.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:        
            museum = models.Museum()
            museum.organisation_name = to_unicode(row[0])
            museum.postal_address_1 = to_unicode(row[1])
            museum.postal_address_2 = to_unicode(row[2])
            museum.town = to_unicode(row[3])
            museum.state = to_unicode(row[4])
            museum.pcode = to_unicode(row[5])
            museum.physical_address_1 = to_unicode(row[6])
            museum.physical_address_2 = to_unicode(row[7])
            museum.physical_town = to_unicode(row[8])        
            museum.physical_state = to_unicode(row[9])       
            museum.physical_pcode = to_unicode(row[10])
            museum.phone = to_unicode(row[11])          
            museum.email = to_unicode(row[12])          
            museum.website = to_unicode(row[13])        
            museum.opening_times = to_unicode(row[14])           
            museum.admission_cost = to_unicode(row[15])          
            museum.wheelchair_access = to_unicode(row[16])           
            museum.toilets = to_unicode(row[17])        
            museum.guided_tours = to_unicode(row[18])        
            museum.merchandise_for_sale = to_unicode(row[19])
            museum.cafe = to_unicode(row[20])           
            museum.collection_specification = to_unicode(row[21])                   
            models.add_museum(museum)
