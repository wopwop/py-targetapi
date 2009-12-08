import JsonRest
import Item
import Person
from errors import NotFoundError

class Api:
    def __init__(self, base_url, api_key):
        self.api = JsonRest.JsonRest(base_url, api_key)

    def person_load(self, person_id):
        ''' Initiate/load person for future operations on it
        '''
        self._person_id = person_id
    
    def person_get(self, person_id):
        '''Return Person with given id
        '''
        try:
            item = self.api.call('person/' + person_id)[0]
        except NotFoundError, ex:
            print "Person " + person_id + ' does not exist'
            return
        return item

    def person_list(self):
        ''' List all persons known to the system
        '''
        return self.api.call('persons')
    
    def person_modify(self, dict):
        ''' Add or modify loaded person
        '''
        self.api.call('person/' + self._person_id, dict)
    
    def person_delete(self):
        ''' Delete loaded person. Nonreversible operation!
        '''
        self.api.delete('person/' + self._person_id)

    def item_list(self):
        '''Return list of content items
        '''
        return self.api.call('items')

    def item_get(self, item_id):
        '''Return Item with given id
        '''
        try:
            item = self.api.call('item/' + item_id)[0]
        except NotFoundError, ex:
            print "Item " + item_id + ' does not exist'
            return
        return item
    
    def item_modify(self, item_id, dict):
        ''' Add or modify an item with given id
        '''
        self.api.call('item/' + item_id, dict)

    def item_delete(self, item_id):
        ''' Delete item with given id
        '''
        self.api.delete('item/' + item_id)

    def recommendations(self):
        ''' Request recommendations for loaded person
        '''
        return self.api.call('person/' + self._person_id + '/recommendations')

    def like(self, item_id):
        ''' Upvotes an item with given id for current person
        '''
        params = {'rating_value' : 1}
        return self.api.call('person/' + self._person_id + '/rating/' + item_id, params)

    def dislike(self, item_id):
        ''' Downvotes an item with given id for current person
        '''
        params = {'rating_value' : -11}
        return self.api.call('person/' + self._person_id + '/rating/' + item_id, params)

    def ratings(self):
        ''' List all ratings given by current person
        '''
        return self.api.call('person/' + self._person_id + '/ratings')





