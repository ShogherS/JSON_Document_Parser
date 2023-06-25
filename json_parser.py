def load_json_file(file_path):
    with open(file_path, 'r') as file:
        json_text = file.read()
    return json_text

def save_json_file(file_path, json_text):
    with open(file_path, 'w') as file:
        file.write(json_text)

def delete_key(json_text, key):
    json_dict = eval(json_text)
    keys = key.split('.')
    current_dict = json_dict

    for k in keys[:-1]:
        if k in current_dict:
            current_dict = current_dict[k]
        else:
            return str(json_dict)

    last_key = keys[-1]
    if last_key in current_dict:
        del current_dict[last_key]

    return str(json_dict)

def update_key(json_text, key, value):
    json_dict = eval(json_text)
    keys = key.split('.')
    current_dict = json_dict

    for k in keys[:-1]:
        if k in current_dict:
            current_dict = current_dict[k]
        else:
            current_dict[k] = {}
            current_dict = current_dict[k]

    last_key = keys[-1]
    current_dict[last_key] = value

    return str(json_dict)

def format_json(json_text):
    formatted_json = ""
    indentation_level = 0

    for char in json_text:
        if char == '{':
            indentation_level += 1
            formatted_json += char + '\n' + '\t' * indentation_level
        elif char == '}':
            formatted_json += '\n' + '\t' * indentation_level + char
            indentation_level -= 1
        elif char == ',':
            
            formatted_json += char + '\n' + '\t' * indentation_level
        elif char == ' ':
            continue
        else:
            formatted_json += char

    return formatted_json

#Example usage:
# file_path = 'random.txt'
# user_command = input('Enter a command del/upd: ')

# json_text = load_json_file(file_path)
# if user_command.startswith('del '):
#     command_parts = user_command.split(' ')
#     if len(command_parts) == 2:
#         key = command_parts[1]
#         json_text = delete_key(json_text, key)
#     elif len(command_parts) == 3:
#         key, attribute = command_parts[1:]
#         json_text = delete_key(json_text, f'{key}.{attribute}')
#     else:
#         print('Invalid command.')
# elif user_command.startswith('upd '):
#     command_parts = user_command.split(' ')
#     if len(command_parts) == 3:
#         key, value = command_parts[1:]
#         json_text = update_key(json_text, key, value)
#     else:
#         print('Invalid command.')
# else:
#     print('Invalid command.')

# json_text = format_json(json_text)
# save_json_file(file_path, json_text)
# print('File updated successfully.')