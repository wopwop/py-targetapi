from errors import NotFoundError

class Item:
    def __init__(self, Api):
        self.api = Api

    def list(self):
        '''Return list of content items
        '''
        return self.api.call('items')

    def get(self, item_id):
        '''Return Item with given id
        '''
        try:
            item = self.api.call('item/' + item_id)[0]
        except NotFoundError, ex:
            print "Item " + item_id + ' does not exist'
            return
        return item

    def modify(self, item_id, dict):
        ''' add or modify an item with given id
        '''
        self.api.call('item/' + item_id, dict)

    def delete(self, item_id):
        ''' delete item with given id
        '''
        self.api.delete('item/' + item_id)

