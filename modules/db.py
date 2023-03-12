import tinydb
import random
import string

db = tinydb.TinyDB('/var/www/bjarne.io/data/db.json', indent=4)
qr_codes = db.table('qr_codes')

def get_qr_url(code:str) -> str:
    ''' Returns the url for a given QR code'''
    return qr_codes.get(tinydb.Query().code == code)['url']

def add_qr(url:str, code:str = None) -> str:
    ''' Adds a new QR code to the database and returns the code'''
    if url in [qr['url'] for qr in qr_codes.all()]: # If the url already exists, return the code
        return qr_codes.get(tinydb.Query().url == url)['code']

    code_chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    code = ''.join( random.choice(code_chars) for _ in range(3)) if code is None else code

    qr_codes.insert({'code': code, 'url': url})

    return code

def validate_qr_code(code:str) -> bool:
    ''' Validates a QR code'''
    return code in [qr['code'] for qr in qr_codes.all()]
