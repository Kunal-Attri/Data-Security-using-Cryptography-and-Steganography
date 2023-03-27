from Crypto.PublicKey import RSA


class Rsa:
    def __init__(self):
        pass

    @staticmethod
    def generate_keys():
        keypair = RSA.generate(2048)
        pubkey = keypair.publickey()
        public_key_pem = pubkey.exportKey('PEM')
        private_key_pem = keypair.exportKey('PEM')

        with open('lib/output/public.pem', 'wb') as file:
            file.write(public_key_pem)
        with open('lib/output/private.pem', 'wb') as file:
            file.write(private_key_pem)

        print("Public key available at: lib/output/public.pem")
        print("Private key available at: lib/output/private.pem")
