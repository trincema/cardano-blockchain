## What is a Blockchain?
The system that Bitcoin relies upon — a growing list of records (i.e. blocks) that are linked to one another — is known as a blockchain. Bitcoin was the first successful application of this system, and shortly after its rise in popularity, other cryptocurrencies were founded on the same principles. This system, however, is not restricted to storing financial information. Rather, the type of data being stored is inconsequential to and independent of the blockchain network.

Fundamentally, the data stored in a blockchain must have the following characteristics:
- `Immutable`
- `Unhackable`
- `Persistent (no loss of data)`
- `Distributed`

These qualities are necessary to maintain the integrity of the blockchain and the security of the network within which the transactions occur. We will assume that the data stored in the block is transactional data, as cryptocurrencies are currently the dominant use case for blockchain.

## Creating the First Block
I will use the standard JSON format to store data in each block. The data for each block looks something like:
{
    "author": "author_name",
    "timestamp": "transaction_time", 
    "data": "transaction_data"
}

To implement this in Python, we first create a block class with the aforementioned attributes. We also want to make each block unique in order to ensure that duplications do not occur.
one of the characteristics of the data in each block is immutability, which can be implemented using a cryptographic hash function. This is a one-way algorithm that takes arbitrarily-sized input data (known as a key) and maps it onto values of fixed sizes (hash value). To illustrate why a hash function is useful for us, consider the following example:
 
1. Alice and Bob are racing to solve a difficult math problem
2. Alice wants to prove to Bob she correctly solved it first without sharing the solution, so she runs her answer through a hash function and shares the resulting hash value with Bob
3. Bob finally solves the problem correctly, but did Alice get the right answer first?
4. Alice now shares her answer with Bob so he can put it through the hash function and check to see if the resulting hash value matches the one that Alice initially provided him.
5. The hash values match, meaning that Alice did indeed solve the problem correctly before Bob.

Python can use any standard cryptographic hash function, such as those in the US National Security Agency’s (NSA) set of SHA-2 functions. For example, SHA-256 can be implemented by adding a compute_hash method within the class block.
Hashing each block ensures the security of each one individually, making it extremely difficult to tamper with the data within the blocks. Now that we’ve established a single block, we need a way to chain them together.

## Coding the Blockchain
Let’s create a new class for the blockchain. In order to ensure the immutability of the entire blockchain, we will use the clever approach of including a hash of the previous block within the current block. The awareness of all data within each block establishes a mechanism for protecting the entire chain’s integrity (partially, at least). This is why we included the previous_hash variable in the block class. We also need a way to initialize the blockchain, so we define the `create_genesis_block` method. This creates an initial block with an index of 0 and a previous hash of 0. We then add this to the list chain that keeps track of each block.

## A Proof-of-Work System for Blockchain
The hashing that we’ve described so far only gets us part of the way there. As it stands, it is feasible for someone to modify a previous block in the chain and then recompute each of the following blocks to create another valid chain. We would also like to implement a way for users to come to a consensus on a single chronological history of the chain in the correct order in which the transactions were made. To solve this, Satoshi Nakamoto established a proof-of-work system.

The proof-of-work system makes it progressively more difficult to perform the work required to create a new block. This means that someone who modifies a previous block would have to redo the work of the block and all of the blocks that follow it. The proof-of-work system requires scanning for a value that starts with a certain number of zero bits when hashed. This value is known as a nonce value. The number of leading zero bits is known as the difficulty. The average work required to create a block increases exponentially with the number of leading zero bits, and therefore, by increasing the difficulty with each new block, we can sufficiently prevent users from modifying previous blocks, since it is practically impossible to redo the following blocks and catch up to others.
To implement this system, we can add a proof_of_work method in the blockchain class.

Now that we have a system that ensures the security of the entire chain in place, we add a few more methods to the blockchain class in order to put everything together so that we can actually construct a chain. We will initially store the data of each transaction in unconfirmed_transactions. Once we confirm that the new block is a valid proof that satisfies the difficulty criteria we can add it to the chain. The process of performing the computational work within this system is commonly known as mining.

## References
https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/
