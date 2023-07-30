#! /bin/bash

mkdir ~/preview
cd ~/preview

echo "Download the configuration files for Preview Testnet"
wget https://book.world.dev.cardano.org/environments/preview/config.json
wget https://book.world.dev.cardano.org/environments/preview/topology.json
wget https://book.world.dev.cardano.org/environments/preview/byron-genesis.json
wget https://book.world.dev.cardano.org/environments/preview/shelley-genesis.json
wget https://book.world.dev.cardano.org/environments/preview/alonzo-genesis.json
wget https://book.world.dev.cardano.org/environments/preview/conway-genesis.json

export PATH="~/.local/bin:$PATH"

cardano-node run --help

cardano-node run --topology topology.json \
--database-path db \
--socket-path node.socket \
--port 3001 \
--config config.json 

export CARDANO_NODE_SOCKET_PATH="$HOME/preview/node.socket"

cardano-cli query tip --testnet-magic 2