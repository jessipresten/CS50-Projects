#prompt user for fraction x/y
#outputs percentage to nearest int
#1% or less return E
#99%  return F
#if x or Y is not int prompt again
#if y is bigger than x prompt again
#y = 0 prompt again

def main():
    fraction = input("Fraction: ")
    fraction_converted = convert(fraction)
    output = gauge(fraction_converted)
    print(output)

def convert(fraction):
    while True:
        try:
            numerator, denominator = fraction.split("/")
            x = int(numerator)
            y = int(denominator)
            if y == 0:
                raise ZeroDivisionError
            f = x / y
            if f <= 1:
                p = round(f * 100)  # Use round to avoid rounding down
                return p
            else:
                fraction = input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return str(p) + "%"

if __name__ == "__main__":
    main()



























