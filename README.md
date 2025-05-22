# Build Your Own Blockchain 🔗

A beginner-friendly Python project that demonstrates how a simple blockchain works — from creating blocks to linking them using cryptographic hashes. Ideal for learning the fundamentals behind blockchain technology without the complexity of distributed networks or mining.

## 🚀 Features
- Create a blockchain from scratch using Python
- Add custom transaction data interactively
- Auto-link blocks via `previous_hash`
- Calculate block hashes using SHA-256
- View the entire blockchain in readable format

## 🧠 Concepts Covered
- Hashing with SHA-256
- Timestamps and block creation
- Linking blocks via hash chains
- Python classes and object-oriented programming
- Basic command-line user input

## 🛠️ Technologies Used
- Python 3
- `hashlib` for hashing
- `time` module for timestamps

## 📦 How to Run
1. Clone the repository:
   git clone https://github.com/your-username/build-your-own-blockchain.git
   cd build-your-own-blockchain

2. Run the Python script:
python blockchain.py

3. Follow the prompts to enter transaction data:
Enter transaction data (or type 'exit' to finish): A pays B 10
Enter transaction data (or type 'exit' to finish): B pays C 5
Enter transaction data (or type 'exit' to finish): exit

4. View the final blockchain printed on the console.

## 📄 Sample Output:
Blockchain contents:

Index: 0
Data: Genesis Block
Previous Hash: 0
Hash: c301e36b05847db88b9950b847603b8705b1f3b4030aa8432c017c1ecfcac52b

Index: 1
Data: GIVE MONEY TO A
Previous Hash: c301e36b05847db88b9950b847603b8705b1f3b4030aa8432c017c1ecfcac52b
Hash: 78a1bcf0dc01083b3e845d34a32093fe8b9463471d5ca12fa2d082cd2d98bc7c

Index: 2
Data: A GIVES MONEY TO B
Previous Hash: 78a1bcf0dc01083b3e845d34a32093fe8b9463471d5ca12fa2d082cd2d98bc7c
Hash: db35e7380251c0faf7158e87720c43aa475a36c5ac2e4003638c4db95584c903

Index: 3
Data: B GIVES MONEY TO C
Previous Hash: db35e7380251c0faf7158e87720c43aa475a36c5ac2e4003638c4db95584c903
Hash: 9cfe7995b667322afbcb0b76d77cf8dd15b3960a3199a779ae5abfa26b4241c2

## 🔧 Future Improvements
- ✅ Add blockchain integrity verification
- ⛏️ Implement simple proof-of-work
- 💾 Save/load blockchain from file
- 🖼️ Visualize blockchain with a GUI
- ⚙️ Experiment with smart contract logic
