import struct
import hashlib
import base64

#RE: public static string CalcHNameString(SHA1CryptoServiceProvider sha1, ulong checksum, ulong size, byte[] name)
def CalcHNameString(checksum: int, size: int, name: str) -> str:
    """The hash name calculation process in uma(args & return exist in the meta db).

    Args:
        checksum(int) : column 'c'
        size(int) : column 'l'
        name(str) : column 'n'
    Return: 
        hname(str) : column 'h': 
    """
    bhash = (struct.pack(">qq", checksum, size) + name.encode("utf-8"))
    hname = base64.b32encode(hashlib.sha1(bhash).digest()).decode('ascii')
    return hname

if __name__ == '__main__':
    #test
    print(CalcHNameString(-2990107160765535323, 1733387, 'master.mdb.lz4'))
    