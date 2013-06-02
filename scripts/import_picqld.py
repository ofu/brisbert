import sys
sys.path.append('./')

from datetime import datetime
import transaction
import xml.dom.minidom as dom
import data.common as common
import data.picqld.models as models
import re


year_search_ = re.compile(r'^[^0-9]*([0-9][0-9][0-9][0-9])[^0-9]*')

small_image_search_ = re.compile(r'^150 pixel jpg: (.*)$')

large_image_search_ = re.compile(r'^1000 pixel jpg: (.*)$')

def _to_unicode(s):
    try:
        return u'%s' % s
    except:
        print s

        
def _read_dom(filename):
    with open(filename, 'rb') as xmlfile:
        d = dom.parse(xmlfile)
        return d
    raise Exception()

    
def _get_text_node(el):
    retval = '';
    for node in el.childNodes:
        if node.nodeType == node.TEXT_NODE:
            retval += node.data
    return retval
    
    
def _get_string(dom, element, joiner=' '):
    retval = ''
    for el in dom.getElementsByTagName(element):
        str = _get_text_node(el)
        if len(str):
            if len(retval):
                retval += joiner + str
            else:
                retval += str

    return retval


def _get_year(dom):
    # Most of the year stuff is contained in the coverage tag, along with the
    # positional data. 
    for el in dom.getElementsByTagName('dc:coverage'):
        str = _get_text_node(el)
        match = year_search_.search(str)
        if match:
            return int(match.group(1))
    return None

    
def _get_url(dom, search):
    for el in dom.getElementsByTagName('dc:identifier'):
        str = _get_text_node(el)
        match = search.search(str)
        if match:
            return match.group(1)
    return None

common.init('sqlite:///bert.sqlite')

with transaction.manager:
    dom = _read_dom('NASLA_non_ATSI_copyright_expired.xml')
    for dc in dom.getElementsByTagName('oai_dc:dc'):
        # Check this is an image type (not sure there is any other type, but 
        # it pays to be careful
        if _get_string(dc, 'dc:type') != 'image':
            continue
            
        picture = models.Picture()
        picture.title = _get_string(dc, 'dc:title')
        picture.description = _get_string(dc, 'dc:description')
        picture.subjects = _get_string(dc, 'dc:subject')
        picture.year = _get_year(dc)
        picture.small_url = _get_url(dc, small_image_search_)
        picture.large_url = _get_url(dc, large_image_search_)
        models.add_picture(picture)