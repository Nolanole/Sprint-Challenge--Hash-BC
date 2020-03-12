#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #iterate thru each weight
    for i, weight in enumerate(weights):
        diff = limit - weight
        #check to see if the weight remainder (the diff) is already stored in the hashtable:
        if hash_table_retrieve(ht, diff) is not None:
            #if found, return tuple of current index and the index where the difference is located
            return i, hash_table_retrieve(ht, diff)[1]
        #if the diff is not already in the hashtable, store key,val pair of weight : (limit minus weight, current index) 
        hash_table_insert(ht, weight, (diff, i))
    
    #if no solution is found, return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")