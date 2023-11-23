def main():
    path_to_file = "books/frankenstein.txt"
    #get word count
    with open(path_to_file) as f:
        #read file into string variable
        file_contents = f.read()
        #split string into words and store into a list
        words = file_contents.split()
    
    count = word_count(words)

    #store dictionary of charecters and counts
    result = count_letters(file_contents)

    #sort dictionary
    result = dict(sorted(result.items(),key=lambda item: item[1], reverse=True))

    #print book report
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count} words found in the document")
    print("")
    for letter, count in result.items():
        print(f"The \'{letter}\' charecter was was found {count} times")
    print(f"--- End report ---")


#return count of words in list
def word_count(string):
    return len(string)

#return count of letters in book(list of words)
def count_letters(book):
    letter_count = {}

    for char in book:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1

    return letter_count




main()