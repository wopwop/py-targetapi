from errors import NotFoundError

class Person:
    def __init__(self, Api):
        self.api = Api

    def list(self):
        '''Return list of persons
        '''
        return self.api.call('persons')

    def get(self, person_id):
        '''Return Person with given id
        '''
        try:
            item = self.api.call('person/' + person_id)[0]
        except NotFoundError, ex:
            print "Person " + person_id + ' does not exist'
            return
        return item

    def modify(self, person_id, dict):
        ''' add or modify a person with given id
        '''
        self.api.call('person/' + person_id, dict)

    def delete(self, person_id):
        ''' delete person with given id
        '''
        self.api.delete('person/' + person_id)

    def recommendations(self, person_id):
        ''' request recommendations for person
        '''
        return self.api.call('person/' + person_id + '/recommendations')


