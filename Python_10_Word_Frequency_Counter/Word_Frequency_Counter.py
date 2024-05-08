def count_word_frequency(text):
    # Base case: empty input
    if not text:
        return {}
    
    # Remove punctuation and convert to lowercase
    text = text.lower().replace(",", "").replace(".", "").replace("!", "").replace("?", "")
    
    # Split the text into words
    words = text.split()
    
    # Initialize the word frequency dictionary
    frequency = {}
    
    # Recursive helper function to process the words
    def process_words(words, index):
        # Base case: all words processed
        if index == len(words):
            return
        
        # Get the current word
        word = words[index]
        
        # Update the word frequency dictionary
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
        
        # Recursive call to process the next word
        process_words(words, index + 1)
    
    # Call the recursive helper function
    process_words(words, 0)
    
    return frequency

# Test the word frequency counter
text = "This is a sample text. It contains some words. Some words are repeated, like 'is' and 'words'."
frequency_dict = count_word_frequency(text)

# Print the word frequency dictionary
for word, count in frequency_dict.items():
    print(f"{word}: {count}")