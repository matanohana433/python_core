# Project 1:

import os
import re

# Part 1:
# Create text file containing the encrypted message:
file = open("./file.txt", "w+")
file.write(''''Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'
J.U.U.U Kmltin. 
mmps iks nmk eio; ---> hkmu''')
file.seek(0)
enc_text = file.read()
file.close()


# print(enc_text)


# Count letters and check what is the 4 most common
def count_char_dict(enc_string):
    top4_dict = {}
    enc_text_low = enc_string.lower()
    for char in enc_text_low:
        if char.isalpha():
            top4_dict[char] = top4_dict.get(char, 0) + 1

    top4_dict = dict(sorted(top4_dict.items(), key=lambda item: item[1], reverse=True)[:4])
    return top4_dict


# top4 = count_char_dict(enc_text)
# print(top4)


# expand connection between letters and create a new dictionary:
def key_to_value(dictionary: dict, word: str):
    index = 0
    for key in dictionary:
        dictionary[key] = word[index]
        index += 1
    new_dict = dictionary.copy()

    for key, value in dictionary.items():
        new_key = value
        new_value = key
        new_dict[new_key] = new_value

    return new_dict


# dicteight = key_to_value(top4, "etor")
# print(dicteight)


# Part 2:
# Replace characters inside the encrypted text to decrypt it
def replace_chars(d8: dict, input_string: str):
    decrypted_string = ""
    input_string = input_string.lower()
    for char in input_string:
        if char in d8.keys():
            decrypted_string += d8.get(char)
        else:
            decrypted_string += char
    return decrypted_string.title()


# print(replace_chars(dicteight, enc_text))

# Part 3:
# get file path:
enc_file_path = os.path.abspath("./file.txt")


#  change original file and create a new results file:
def create_file(file_path):
    txt = open(file_path, "r+")
    data = txt.read()
    d_4 = count_char_dict(data)
    d_8 = key_to_value(d_4, "etor")
    dec_txt = replace_chars(d_8, data)
    txt.write("\n")
    txt.write("The encryption for the above text is:\n")
    txt.write(dec_txt + "\n")
    txt.close()
    results = open("./results.txt", "w")
    results.write(dec_txt + "\n")
    results.close()


# create_file(enc_file_path)

# Part 4:
# results path:
results_path = os.path.abspath("./results.txt")


# first function:
# count only alphabetic words and return the list with the max length words
def count_letters(file_path):
    results_file = open(file_path, "r")
    data = results_file.read()
    all_words = []
    longest_chars = []
    max_len = -1

    for word in data.split():
        regex = re.compile('[^a-zA-Z]')
        cleaned_word = regex.sub('', word)
        all_words.append(cleaned_word)

        if len(cleaned_word) > max_len:
            max_len = len(cleaned_word)

    for word in all_words:
        if len(word) == max_len:
            longest_chars.append(word)

    results_file.close()
    return longest_chars[0]


# print(count_letters(results_path))


# second function:
# count lines in results.txt:
def count_lines(file_path):
    results_file = open(file_path, "r")
    num_of_lines = len(results_file.readlines())
    results_file.close()
    return num_of_lines


# print(count_lines(results_path))


# Main function:

def main():
    top4 = count_char_dict(enc_text)
    dicteight = key_to_value(top4, "etor")
    print(replace_chars(dicteight, enc_text))
    create_file(enc_file_path)
    l_word = count_letters(results_path)
    c_lines = count_lines(results_path)
    print(f"Your longest word is {l_word}")
    print(f"The number of lines is {c_lines}")
    rows = 8
    k = "*"
    space = " "
    orig_file = open(enc_file_path, "a")
    orig_file.write((l_word + " ") * c_lines + "\n")
    for i in range(1, rows):
        for j in range(1, 3):
            if i == 1 or i == 2 or i == 6 or i == 7:
                orig_file.write(k + space * 5)
            elif i == 3 or i == 5:
                orig_file.write(space + k + space * 2)
            elif i == 4 and j == 1:
                orig_file.write(space * 3 + k + space * 2)
        orig_file.write('\n')
    orig_file.close()


if __name__ == "__main__":
    main()
