
import string
import random
total= string.ascii_letters + string.digits + string.punctuation
length=random.randint(8,13)
password="".join(random.sample(total,length))
print(password)