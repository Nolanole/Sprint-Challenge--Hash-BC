#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #iterate thru the tickets
    for ticket in tickets:
        #insert each ticket into the hashtable, key = source, value = destination
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    
    route = []
    current = 'NONE' #start where source = NONE
    #assign the first destination to variable 
    destination = hash_table_retrieve(hashtable, current)

    #iterate until we reach the final destination of 'NONE'
    while destination != 'NONE':
        route.append(destination) #add the next destination to the list
        current = destination #update the current with the next destination
        destination = hash_table_retrieve(hashtable, current) #update the new destination
    
    #return the list of destinations
    return route