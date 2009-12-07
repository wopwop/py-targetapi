import JsonRest
import Item
import Person
from errors import NotFoundError

class Api:
    def __init__(self, base_url, api_key):
        api = JsonRest.JsonRest(base_url, api_key)
        self.Item = Item.Item(api)
        self.Person = Person.Person(api)



