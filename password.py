import  random
import string
a="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
b="1234567890"
c="!@~#$%^&*()_+`/.,';][?><:}{\|}"
d=a +b +c
print("".join(random.sample(d,8)))