## RSA Digital Signature Scheme
RSA algorithm is an asymmetric cryptography algorithm. Asymmetric actually means that it works on two different keys i.e. Public Key and Private Key. As the name describes that the Public Key is given to everyone and the Private key is kept private.
An example of asymmetric cryptography :
- A client (for example browser) sends its public key to the server and requests for some data. 
- The server encrypts the data using the client’s public key and sends the encrypted data. 
- Client receives this data and decrypts it. 
Since this is asymmetric, nobody else except the browser can decrypt the data even if a third party has the public key of browser.
Digital signatures are used to verify the authenticity of the message sent electronically. A digital signature algorithm uses a public key system. The intended transmitter signs his/her message with his/her private key and the intended receiver verifies it with the transmitter’s public key. A digital signature can provide message authentication, message integrity and non-repudiation services.
