#two command line arguments
#ouput new file with first,last and house
#spliting the names into first and last
#sys.exit if there are two command line arguments or first cant be read

import sys
import csv

def main():
    check_length()
    output = []
    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            for row in reader:
                split_name=row["name"].split(",")
                output.append({"first": split_name[1].lstrip(), "last":split_name[0], "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Couldn't read {sys.argv[1]}")
    except KeyError as e:
        sys.exit(f"Missing key in CSV file: {e}")

    with open(sys.argv[2], "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writerow({"first":"first","last":"last","house":"house"})
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


def check_length():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")






if __name__ == "__main__":
    main()






