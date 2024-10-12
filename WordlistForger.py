import random
import itertools

# Function to insert numbers based on the specified format
def format_password(word, numbers, format_option):
    if format_option == 'start':  # Numbers at the start
        return ''.join(numbers) + word
    elif format_option == 'end':  # Numbers at the end
        return word + ''.join(numbers)
    elif format_option == 'middle':  # Numbers in the middle
        mid_point = len(word) // 2
        return word[:mid_point] + ''.join(numbers) + word[mid_point:]
    elif format_option == 'random':  # Numbers inserted randomly
        return insert_numbers_randomly(word, numbers)
    else:
        raise ValueError("Invalid format option provided.")

# Function to insert numbers at random positions within the word
def insert_numbers_randomly(word, numbers):
    word_list = list(word)  # Convert the word to a list of characters
    all_positions = list(range(len(word_list) + 1))  # Get positions including before, between, and after characters
    random.shuffle(all_positions)  # Shuffle positions for random insertion
    
    # Insert numbers into random positions
    for num in numbers:
        pos = all_positions.pop(0)  # Get the next available position and insert the number
        word_list.insert(pos, num)
    
    return ''.join(word_list)

# Function to generate all combinations of words and numbers
def generate_possible_passwords(words, numbers, format_option):
    possible_passwords = []
    
    if not words:  # If no words, just use permutations of numbers
        possible_passwords = [''.join(num_comb) for num_comb in itertools.permutations(numbers)]
    else:
        # For each word, generate different ways of inserting the numbers based on the format option
        for word in words:
            for num_comb in itertools.permutations(numbers):  # Generate all permutations of the numbers
                formatted_password = format_password(word, num_comb, format_option)
                possible_passwords.append(formatted_password)

    return possible_passwords

# Function to shuffle the generated passwords for randomness
def shuffle_passwords(passwords):
    random.shuffle(passwords)
    return passwords

# Main function to gather user inputs and create the password file
def main():
    # Input: words to use in the password (can be empty)
    words = input("Enter a word to use (e.g. cat)(leave empty if none): ").split()

    # Input: numbers to use (e.g., '2 0 1 9')
    numbers = input("Enter numbers to use, separated by spaces (e.g., '2 0 1 9'): ").split()

    # Input: preferred format for inserting numbers
    print("Choose a format for the numbers in the password:")
    print("1. Start (e.g., '2019cat')")
    print("2. End (e.g., 'cat2019')")
    print("3. Middle (e.g., 'ca2019t')")
    print("4. Random (e.g., 'c2a9t1')")
    format_option_input = input("Enter your choice (start/end/middle/random): ").lower()

    # Input: whether to shuffle the passwords
    shuffle_option = input("Do you want to shuffle the generated passwords? (yes/no): ").lower()

    # Generate all possible passwords
    possible_passwords = generate_possible_passwords(words, numbers, format_option_input)

    # Shuffle passwords if the user requested
    if shuffle_option == 'yes':
        possible_passwords = shuffle_passwords(possible_passwords)

    # Write all generated passwords to a file
    with open("passwords.txt", "w") as f:
        for password in possible_passwords:
            f.write(password + "\n")

    print(f"{len(possible_passwords)} possible passwords have been generated and saved to passwords.txt")

# Entry point
if __name__ == "__main__":
    main()
