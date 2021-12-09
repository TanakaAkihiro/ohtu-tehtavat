from matchers import *

class QueryBuilder:
    def __init__(self, query=all):
        self._query = query
    
    def build(self):
        return self._query
    
    def playsIn(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))
    
    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))
    
    def oneOf(self, *matchers):
        return QueryBuilder(Or(*matchers))

query_builder = QueryBuilder()
