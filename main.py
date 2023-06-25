import random
import string
from json_parser import load_json_file, save_json_file, format_json
from json_test import generate_random_txt_file, is_deleted, is_updated

txt_file = 'random.txt'
generate_random_txt_file(txt_file)
current_data =load_json_file(txt_file)


is_updated(current_data)
is_updated(current_data)
is_deleted(current_data)
is_deleted(current_data)

current_data = format_json(current_data)
save_json_file(txt_file, current_data)

