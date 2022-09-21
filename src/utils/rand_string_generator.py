import random, string

def get_random_string(length):
    letters = f"{string.ascii_letters}{string.digits}{string.ascii_lowercase}{string.ascii_uppercase}"
    result = ''.join(random.choice(letters) for i in range(length))
    return result