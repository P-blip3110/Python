import random

def str_builder(str):
    '''returns strings consisting of non-duplicate elements'''
    random.shuffle(str)
    return ''.join(str)
    pass

print(str_builder(['a','e','i','o','u']))
