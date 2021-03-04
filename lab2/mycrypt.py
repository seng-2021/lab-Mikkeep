import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    illegalmapping = ["å", "ä", "ö", "+"]
    if len(s) > 1000:
        raise ValueError
    padded_val = s.ljust(1000, "z")
    for c in padded_val:
        if c in illegalmapping:
            raise ValueError
        elif c.isalpha():
            if c.islower():
                c=c.upper()
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
    return crypted[:origlen]

def decode(s):
    decrypted = encode(s).lower()
    return decrypted
