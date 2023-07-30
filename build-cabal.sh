
#! /bin/bash
# Give permission: chmod +x build-cabal.sh

taggedVersion=$1
start=`date +%s`

echo "Cleanup..."
rm -rf ~/src

echo "================== Installing dependencies =================="
sudo apt-get update -y
sudo apt-get install curl -y
sudo apt-get install automake build-essential pkg-config libffi-dev libgmp-dev libssl-dev libtinfo-dev libsystemd-dev zlib1g-dev make g++ tmux git jq wget libncursesw5 libtool autoconf liblmdb-dev -y

echo "================== Installing Haskell environment =================="
curl --proto '=https' --tlsv1.2 -sSf https://get-ghcup.haskell.org | sh -y
ghcup install ghc 8.10.7
ghcup install cabal 3.6.2.0
ghcup set ghc 8.10.7
ghcup set cabal 3.6.2.0
cabal --version
ghc --version

echo "================== Installing Libsodium =================="
mkdir -p ~/src
cd ~/src
git clone https://github.com/input-output-hk/libsodium
cd libsodium
git checkout dbb48cc
./autogen.sh
./configure
make
make check
sudo make install
export LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig:$PKG_CONFIG_PATH"

echo "================== Installing Secp256k1 =================="
mkdir -p ~/src
cd ~/src
git clone https://github.com/bitcoin-core/secp256k1
cd secp256k1
git checkout ac83be33
./autogen.sh
./configure --enable-module-schnorrsig --enable-experimental
make
make check
sudo make install

echo "================== Downloading the source code for cardano-node =================="
mkdir -p ~/src
cd ~/src
git clone https://github.com/input-output-hk/cardano-node.git
cd cardano-node
git fetch --all --recurse-submodules --tags
git tag | sort -V
git checkout tags/$taggedVersion
echo "with-compiler: ghc-8.10.7" >> cabal.project.local
cabal update

echo "================== Building cardano-node and cardano-cli =================="
cabal build cardano-node cardano-cli
mkdir -p ~/.local/bin
cp -p "$(./scripts/bin-path.sh cardano-node)" ~/.local/bin/
cp -p "$(./scripts/bin-path.sh cardano-cli)" ~/.local/bin/
export PATH="~/.local/bin:$PATH"
echo $PATH
cardano-node --version
cardano-cli --version

end=`date +%s%N`
echo Execution time: $end nanoseconds
time=$end - $start
time=$time/60000000000
echo Execution time: $time minutes