#Q5.
#Write a python program that accepts a text
#and displays a string which contains the word with the largest frequency in the text
#and the frequency itself separated by a space.

#Rules: The word should have the largest frequency.

#In case multiple words have the same frequency, then choose the word that has the maximum length.

#Assumptions:
#The text has no special characters other than space. The text would begin with a word and there will be only a single space between the words.
#Perform case insensitive string comparisons wherever necessary.

def find_word_with_largest_frequency(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Split text into words
    words = text.split()
    
    # Create a dictionary to store word frequency
    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    
    # Find the word with the largest frequency
    max_freq = 0
    max_word = ""
    for word, freq in freq_dict.items():
        if freq > max_freq:
            max_freq = freq
            max_word = word
        elif freq == max_freq:
            if len(word) > len(max_word):
                max_word = word
    
    # Return the word with its frequency
    return max_word + " " + str(max_freq)

text = "This is a sample text with sample words to test the program"
result = find_word_with_largest_frequency(text)
print(result)  # Output: sample 2
