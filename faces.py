def main():
    #get user input
    msg = input()
    #call convert function
    result = convert(msg)
    #print the result
    print(result)

def convert(msg):
    #replace :) for happy emoji
    msg1 = msg.replace(":)", '🙂')
    #replace :( for sad emoji
    msg2 = msg1.replace(":(", '🙁')
    #return string
    return msg2
main()
