from matchers import *

class QueryBuilder:
    def __init__(self, query=all):
        self._query = query
    
    def build(self):
        return self._query

query_builder = QueryBuilder()
