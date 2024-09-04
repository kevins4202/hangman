def filter_words(file_path):
        # Read the content of the file
    with open(file_path, 'r') as file:
        words = file.read().split()
        
        # Filter words to keep only those that are four letters or longer
    filtered_words = [word for word in words if len(word) >= 4]
        
        # Write the filtered words back into the file
    with open('filtered_words.txt', 'w') as file:
        file.write('\n'.join(filtered_words))
            
    print("Words have been filtered and written back to the file successfully.")

# Define the path to the text file
file_path = 'words.txt'

# Call the function
filter_words(file_path)