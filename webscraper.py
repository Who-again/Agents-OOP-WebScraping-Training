import yfinance as yf


# I'm sorry if this is a bit unreadable and chaotic
def fetch_stock(ticker):

    data = None  # Just incase if they don't put anything in the input, it might break the entire file
    userinput = ticker
    if userinput.isalpha():
        data = yf.Ticker(userinput)
        data = data.history(
            period="7d"
        )  #   Fetches the history of inputted ticker symbol and its period
        data = data.reset_index()  #   Resets the dataframe's index which makes it use the default one, so when you get the finished data, the Date (or first column) column will still exist
        data["Date"] = data["Date"].astype(str)
        data = data.to_dict(orient="records")
        print(data)
    else:
        print("Input must be Alphanumeric")

    return data
