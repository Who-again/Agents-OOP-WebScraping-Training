def ticker_input():

    ticker = None
    i = None
    data = None

    ticker = input("Enter ticker    $:  ")

    if ticker.isalpha():
        pass
    else:
        print("Must be Alphanumeric")

    i = input("Enter Index (int, 0 - inf)   :   ")

    if i.isnumeric():
        i = int(i)
    else:
        print("Must be an integer")

    data = input("Which data would you like to retrieve?    :   ")

    if data.isalpha():
        pass
    else:
        print("Must be a Alphanumeric")

    return ticker, i, data
