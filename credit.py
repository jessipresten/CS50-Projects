#get user credit card
#output card type
# Amex 15 digits starts with 37 or 34
# Mastercard starts with 51, 52, 53, 54, 55 16 digits
# Visa starts with a 4 and 13 or 16 digits
#check if card is valid
#start = length -2
# stop = -1
# step = -2

def main():
    user = input("Number: ")
    sum = 0
    x=sum_every_other(user)
    y=sum_other(user)
    sum=x+y
    sum= display_card(sum, user)


def sum_every_other(user):
    sum = 0
    for i in range (len(user)-2, -1, -2):
        digit = int(user[i])
        mult =  digit*2
        if mult < 10:
            sum = sum + mult
        else:
            sum = sum + mult % 10 + mult // 10
    return sum
def sum_other(user):
    sum = 0
    for i in range(len(user)-1,-1, -2):
        digit = int(user[i])
        sum = sum + digit
    return sum
def display_card(sum, user):
    if sum % 10 != 0:
        print("Invalid")
    else:
        if len(user)==15 and(user[0:2] =="37" or user[0:2] == "34"):
            print("Amex")
        if len(user) == 16 and (user[0:2] =="51" or user[0:2] == "52" or user[0:2] == "53"or user[0:2] == "54" or user[0:2] == "55"):
            print("Mastercard")
        if len(user) == 13 or len(user) == 16 and user[0:1] == "4":
            print("Visa")


if __name__ == "__main__":
    main()
