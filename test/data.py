import random
import string
from model.partner import Partner

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

PHONE = str(random.randint(70000000000, 79999999999))
test_question = random_string("name", 20) + ' ' + random_string("name", 20)
testdata = [
        Partner(phone=PHONE, email=random_string("email", 2) + "@test.ru", name=random_string("name", 10), question=test_question),
        Partner(phone=PHONE, email=random_string("email", 2) + "@test.com", name=random_string("name", 10), question=test_question)
]
