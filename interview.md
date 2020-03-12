## Interview Questions:

### (1) Explain in detail the workings of a dynamic array:

- What is the runtime complexity to access an array, 
    - O(1) because you can access via index
- add or remove from the front
    - O(n) because all other elements of the array must be shifted over
- add or remove from the back?
    - O(1) on avg, but (next question about worst case) 

- What is the worse case scenario if you try to extend the storage size of a dynamic array?
    -worst case O(n) if adding one element exceeds the capacity in memory allocated to the array, and a new array (doubled in size) must be created

### (2) Explain how a blockchain is structured. 
    - A blockchain is structured kind of like a linked list. It consists of a chain of blocks- the head or root of the chain is called the genesis block. Unlike a typical singly linked list, instead of pointing from the head to the tail, each node in the chain points backward to previous block, all the way to the genesis block.

- What are the blocks
    The blocks are basically like nodes, or containers, that store information such as the index of the block in the chain, the timestamp it was created (added to the chain), a list of transactions (or otehr timestamped data), the proof used to mine the block, and the cryptographic hash of the previous block

- What is the chain? 
    The chain is the link between blocks, that traces from the most recently created block all the way back to the genesis block

- How is the data organized? Explained above: Each block contains a reference, which is the hash of the preceding block. This serves as a link to the preceding block and establishes the order throughout the chain of blocks.

### (3) Explain how proof of work functions. 
- How does it operate?
    Proof of work is an arbitrarily difficult problem to solve that requires a large amount of computational resources. In our mock blockchain example used in class, the proof required was the cryptographic hash of the previous block in the chain plus a new value (the new proof), must result in leading series of 6 zeros. (in the case of bitcoin, the proof required is something around 70 leading zeros).

- How does this protect the chain from attack?
    It protects the chain by making it very difficult to mine a new block. In order to edit/alter a previous block in the chain, that modification will change the cryptographic hash of the next block, and also all other blocks throughout the rest of the chain, so a new proof must be computed for each subsequent block throughout the chain (cascading effect). 

- What kind of attack is possible?
    A 51% attack, where an attacker controls more than 50% of computing resources used to mining new blocks. That way they can sort of outpace all other miners and end up with the longest valid chain (which is what the network consensus uses to essentially establish as what is the valid chain)


### Bash output from mining the Lambda Test Server:

'''
ID is Josh-Mancuso
Searching for next proof
Proof found: 21536348.845357925 in 60.28998231998412
Total coins mined: 1
Searching for next proof
Proof found: 10886205.11362053 in 28.167239352012984
Total coins mined: 2
Searching for next proof
Proof found: 27268542.20016242 in 75.8041621579905
Total coins mined: 3
Searching for next proof
Proof found: 44400404.19171439 in 169.03676401794655
Total coins mined: 4
Searching for next proof
Proof found: 4155954.0147444597 in 15.208587859990075
Total coins mined: 5
Searching for next proof
Proof found: 5419931.716254644 in 20.794430792040657
Total coins mined: 6
'''