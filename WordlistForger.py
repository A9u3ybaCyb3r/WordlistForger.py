import random
import itertools

# Parse number input: either a range (e.g., '1-9') or specific numbers (e.g., '2 4 7')
def parse_number_input(number_input):
    numbers = []
    if '-' in number_input:
        start, end = map(int, number_input.split('-'))
        numbers = [str(num) for num in range(start, end + 1)]
    else:
        numbers = number_input.split()
    return numbers

# Generate all possible combinations of words and numbers
def generate_possible_passwords(words, numbers):
    all_elements = words + numbers  # Combine words and numbers
    # Generate all possible permutations of the combined list
    possible_passwords = [''.join(perm) for perm in itertools.permutations(all_elements)]
    return possible_passwords

# Shuffle passwords for randomness
def shuffle_passwords(passwords):
    random.shuffle(passwords)
    return passwords

# Main function to gather user input and create the password file
def main():
    # Input: words to use in the password (can be empty)
    words = input("Enter a word to use (leave empty if none): ").split()

    # Input: numbers to use (e.g., '2 0 1 9' or '1-9')
    number_input = input("Enter numbers to use, separated by spaces (or a range like '1-9'): ")
    numbers = parse_number_input(number_input)

    # Input: whether to shuffle the passwords
    shuffle_option = input("Do you want to shuffle the generated passwords? (yes/no): ").lower()

    # Generate all possible passwords
    possible_passwords = generate_possible_passwords(words, numbers)

    # Shuffle passwords if the user requested
    if shuffle_option == 'yes':
        possible_passwords = shuffle_passwords(possible_passwords)

    # Write all generated passwords to a file
    with open("passwords.txt", "w") as f:
        for password in possible_passwords:
            f.write(password + "\n")

    # Display total number of passwords generated
    print(f"Total passwords generated: {len(possible_passwords)}")
    print(f"{len(possible_passwords)} possible passwords have been generated and saved to passwords.txt")

# Entry point
if __name__ == "__main__":
    main()
