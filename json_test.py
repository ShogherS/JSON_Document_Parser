import random
import string
from json_parser import delete_key, update_key

def generate_random_txt_file(file_path):
    def generate_random_key(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_random_data(depth):
        if depth <= 0:
            return random.randint(1, 100)

        data = {}
        num_keys = random.randint(1, 5)
        for _ in range(num_keys):
            key_length = random.randint(3, 8)
            key = generate_random_key(key_length)
            data[key] = generate_random_data(depth - 1)

        return data

    data = generate_random_data(3)

    # Write data to text file
    with open(file_path, 'w') as file:
        file.write(str(data))

def select_random_key(data):
    """Selects a random key from the given data."""
    if not data or not isinstance(data, dict):
        return None

    keys = list(data.keys())

    if not keys:
        return None

    random_key = random.choice(keys)
    return random_key

def is_deleted(current_data):
    tmp_data = eval(current_data)
    random_key = select_random_key(tmp_data)
    final_data = delete_key(current_data, random_key)

    if random_key in final_data:
        print("deleting is failed!")
    else:
        print("Deleting is complete!")

def is_updated(current_data):
    tmp_data = eval(current_data)
    random_key = select_random_key(tmp_data)
    final_data = update_key(current_data, "vvj", 1111)

    if random_key in final_data :
        print("Updating is complete!")
    else:
        print("Updating was failed!")