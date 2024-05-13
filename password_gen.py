import random
import string

selected_characters =[]
for i in range(12):
    selected_array =random.choice([list(range(10)), list(string.ascii_letters), string.punctuation])
    selected_characters.append(str(random.choice(selected_array)))

print(''.join(selected_characters))
