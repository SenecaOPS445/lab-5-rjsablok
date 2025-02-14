#!/usr/bin/env python3
# Author ID: [seneca_id]

def read_file_string(file_name):
    """
    Takes file_name as a string and returns its entire contents as a string.
    """
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {file_name} not found."

def read_file_list(file_name):
    """
    Takes file_name as a string and returns its entire contents as a list of lines without new-line characters.
    """
    try:
        with open(file_name, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return [f"Error: {file_name} not found."]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
