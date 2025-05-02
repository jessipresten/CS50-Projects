#propmt for greeting as a string output an int
#hello returns 0
#starts with h returns 20
#100 else
#use return for int in value

def main():
    greeting = input("Greeting: ")
    value_to_print = value(greeting)
    print(f"${value_to_print}")


    ...


def value(greeting):
    greeting = greeting.lower().strip()
    if 'hello' in greeting:
        return 0
    elif 'h' == greeting[0]:
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
