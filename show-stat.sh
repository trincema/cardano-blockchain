#! /bin/bash

export PATH="~/.local/bin:$PATH"
export CARDANO_NODE_SOCKET_PATH="$HOME/preview/node.socket"

counter=1
while [ $counter -gt 0 ]
do
    cardano-cli query tip --testnet-magic 2
    time sleep 5
done