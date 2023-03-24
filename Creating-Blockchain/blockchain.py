import hashlib
import json
import datetime
from flask import Flask, jsonify 

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(1,'0')
        
    def create_block(self, proof, previousHash):
        block = {"index" : len(self.chain) + 1,
                 "timestamp" : str(datetime.datetime.now()),
                 "proof" : proof,
                 "previousHash" : previousHash}
        self.chain.append(block)
        return block
    def getPriviousBlock(self):
        return self.chain[-1]
    def proofOfWork(self, previousProof):
        newProof = 1
        checkProof = False
        while checkProof is False:
            hashOperation = hashlib.sha256(str(newProof ** 2 - previousProof ** 2 ).encode()).hexdigest()
            if hashOperation[ : 4] == "0000":
                checkProof = True
            else:
                newProof += 1
        return newProof
    def hash(self, block):
        encodedBlock = json.dumps(block, sort_keys= True).encode()
        return hashlib.sha256(encodedBlock).hexdigest()
    def chainVAlidation(self, chain):
        previousBlock = chain[0]
        blockIndex = 1
        while blockIndex < len(chain):
            block = chain[blockIndex]
            if block["priviousHash"] != self.hash(previousBlock):
                return False
            previousProof = previousBlock['proof']
            proof = block['proof']
            hashOperation = hashlib.sha256(str(proof ** 2 - previousProof ** 2 ).encode()).hexdigest()
            if hashOperation[ : 4] != "0000":
                return False
            previousBlock = block
            blockIndex += 1
        return True 

app = Flask(__name__)

blockchain = Blockchain()

@app.route("/mining", methods = ["GET"])
def mining():
    previousBlock = blockchain.getPriviousBlock()
    previousProof = previousBlock['proof']
    proof = blockchain.proofOfWork(previousProof)
    previousHash = blockchain.hash(previousBlock)
    block = blockchain.create_block(proof, previousHash)
    response = {"Message" : "Congratulations you are mined a block!",
                "index" : block["index"],
                 "timestamp" : block["timestamp"],
                 "proof" : block['proof'],
                 "previousHash" : block["previousHash"]}
    return jsonify(response), 200

@app.route("/getchain", methods = ["GET"])
def getchain():
    response = {"chain" : blockchain.chain,
                "length": len(blockchain.chain)}
    return jsonify(response), 200

app.run(host = "0.0.0.0", port = 5000)
    
    