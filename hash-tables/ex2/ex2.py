#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = [None] * length
    hashtable = HashTable(length)
    
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    key = "NONE"

    for i in range(length):
        current_ticket = hash_table_retrieve(hashtable, key)
        key = current_ticket
        route[i] = current_ticket
         

    return route
