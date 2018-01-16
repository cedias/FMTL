from FMTL import FMTL
import random


def new_tuple(nf,alphabet):
    return tuple([random.choice(alphabet) for x in range(nf)])



print("creating tuple list")

alphabet = set("aazertyuiopqsdfghjklwxcvbn")
alphabet.update(set(range(25)))
alphabet = list(alphabet)
print(alphabet)




lt = [ new_tuple(5,alphabet) for _ in range(25)]
print(lt)

