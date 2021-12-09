from matchers import *

class QueryBuilder:
    def __init__(self, query=all):
        self._query = query
    
    def build(self):
        return self._query
    
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(team))

query_builder = QueryBuilder()
