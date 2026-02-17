import os

def count_words(filename):

    src_folder = os.path.dirname(os.path.abspath(__file__))
    homework_folder = os.path.dirname(src_folder)
    file_path = os.path.join(homework_folder, filename)
    
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            return len(text.split())
    except FileNotFoundError:
        return 0