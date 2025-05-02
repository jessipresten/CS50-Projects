
import csv
import sys


def main():
    # Ensure correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python dna.py database.csv sequence.txt")
        sys.exit(1)

    # Read the DNA database file into a variable
    with open(sys.argv[1], "r") as database_file:
        reader = csv.DictReader(database_file)
        database = [row for row in reader]
        

    # Read the DNA sequence file into a variable
    with open(sys.argv[2], "r") as sequence_file:
        sequence = sequence_file.read()

    # Find the longest match of each STR in the DNA sequence
    str_count = {}
    for key in database[0].keys():
        if key == "name":
            continue
        str_count[key] = longest_match(sequence, key)

    # Check database for matching profiles
    for row in database:
        match = True
        for key in str_count:
            if int(row[key]) != str_count[key]:
                match = False
                break
        if match:
            print(row["name"])
            return

    print("No match")
    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters within the sequence)
        while True:
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        # Update the longest consecutive match found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()





























































































