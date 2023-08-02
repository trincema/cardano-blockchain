import requests
import json
import time
import subprocess
from block import Block
from blockchain import Blockchain
from flask import Flask, request

app =  Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data}) + '\n'

app.run(debug=True, port=5000)