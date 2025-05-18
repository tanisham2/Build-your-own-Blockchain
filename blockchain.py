import hashlib
import time

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = str(self.index) + str(self.timestamp) + str(self.data) + self.previous_hash
        return hashlib.sha256(value.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        last = self.get_last_block()
        new_block = Block(len(self.chain), data, last.hash)
        self.chain.append(new_block)
my_chain = Blockchain()

while True:
    user_input = input("\nEnter transaction data (or type 'exit' to finish): ")
    if user_input.lower() == 'exit':
        break
    my_chain.add_block(user_input)

# --- Display the Blockchain ---
print("\nBlockchain contents:")
for block in my_chain.chain:
    print(f"\nIndex: {block.index}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
