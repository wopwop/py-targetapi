import simplejson
import urllib2
import urllib
from errors import NotFoundError

class JsonRest:
    def __init__(self, base_url, api_key):
        self._baseurl = base_url + '/' + api_key + '/'

    def call(self, action, values = None):
        ''' Perform either GET or POST based on values
        '''
        url = self._baseurl + action
        data = None

        if (values):
            data = urllib.urlencode(values)

        req = urllib2.Request(url, data)

        try:
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            raise NotFoundError(url + ' returned nothing')

        return simplejson.load(response)
    
    
    def delete(self, action):
        ''' Perform HTTP DELETE
        '''
        url = self._baseurl + action
        req = urllib2.Request(url)
        req.get_method = lambda: 'DELETE'
        response = urllib2.urlopen(req)


