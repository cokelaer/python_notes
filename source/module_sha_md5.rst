The md5 and sha modules
########################

:Status: in progress

Python provides two secure built-in algorithms that you can use for password generation. These are passwords that can’t be reversed; they’re useful for authenticating users to an application that could contain sensitive information.


In order to store passwords in an encrypted form, you will need under Unix the standard encryption protocol called DES or hashing using md5 (or sha-1). Windows systems usually keep passwords in an entirely different format in the registry.

Here is an example that works with the sha or md5 module::


    import sha # or import md5, which is considered less stronger
    import random
    import base64 # allow to turn binary data into text data

    def _gen_salt():
        salt = [chr(random.randint(0,255)) for i in range(4) ]
        return ''.join(salt)

    def make_pass(cleartext):
        salt = _gen_salt()
        text = salt + cleartext
        hash = sha.new(text).digest()
        data = salt + hash
        return base64.encodestring(data)

    def check_pass(cipher, cleartext):
        cipher = base64.decodestring(cipher)
        salt, hash = cipher[:4], cipher[4:]
        hash2 = sha.new(salt + cleartext).digest()
        return hash2 == hash

    if __name__ == '__main__':
        cipher = make_pass('TEST')
        for word in 'spam', 'test, 'Test', 'dummy':
            passwd = check_pass(cipher, word)
            print '%s: %d'% (word, passwd)

The same code could be used with md5 as the core encryption mechanism, although sha is usually considered stronger.
