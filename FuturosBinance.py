import pprint
import ccxt
binance = ccxt.binance()
markets = binance.load_markets()
pares = [i["symbol"] for i in markets.values()] ## tem q colcoar o symbol
def info():
    pprint.pprint(f"available coins are {pares}")
    print("roll up to see available pairs")
    print("\nthis script calculates the ideal leverage for binance futures")
    print("\n it follows the Gannn's rules and some interpretations presented in C. Miner's High Probability Trading book")
    print("\nIt takes a maximum exposure for each trade as 3% of capital exposure")
    print("Works for both long and short position,\nShort positions will have negative sign, though")
    return info

def get_pair(a=None):
    a = str(input("What coin are u trading? ")).upper()
    return a


def get_quote(a):
    pair = binance.fetch_ticker(a)
    preco = round(pair["last"], 6)
    print(f"{a} is {preco}")
    return preco


def leverage(b=None):
    b = int(input("What's your leverage? "))
    print(f"U are trading at {b}X leverage")
    return b


def total_capital():
    capital = float(input("What's is your total capital? "))
    maximum_contract = capital*b
    print(f"total capital is {maximum_contract}")
    return maximum_contract


def coin_contract():
    coinc = maximum_contract / cointicker
    print(f"The max contract/coin leverage is {coinc} {a}")    
    return coinc

def operation_size(size=None):
    size1 = maximum_contract * 0.03
    print(f"maximum recomended order size is {size1}")
    size = float(input("Order size: "))
    size_percentual = (size/maximum_contract) * 100
    while (size>maximum_contract):
        
            print("the ammount excceds ur total capital\nenter a valid value: ")
            size = float(input("Order size: "))
    
    print(f"u open order is {size_percentual:.2f}%, of ur max capital {maximum_contract}")

    return size




def get_order():
    entry = float(input("Entry price: "))
    return entry


def stoploss(entry,size, stop=None):
    stop = float(input("StopLoss: "))
    stop_percentualDecimal = (entry-stop)/entry 
    stop_percentual1 = stop_percentualDecimal * 100
    margin = maximum_contract
    dolar_loss = size * stop_percentualDecimal
    liquidation_point = entry - (margin/size)
    ##print(f"DEBUG: dolar_loss = {dolar_loss}, margin = {margin}, size = {size}, stopdecimal= {stop_percentualDecimal}")
    if(dolar_loss>size):
        print(f"your max loss is liquidation")
        print(f"your liquidation point was {liquidation_point}")
    else:
        print(f"your max loss is {dolar_loss:.2f}$, \nin %leveraged: {b*stop_percentual1:.2f}%")
    return stop_percentualDecimal




def takeprofit(entry, tp=None):
    selec = str(input("want to set a TP ORDER?(S/N): ")).upper()
    if(selec!="S"):
        print("\nContinuing with no TP")
    else:
        tp = float(input("your tp: "))
        coin_purchasable = size / cointicker
        gain_per_coin = tp  - entry
        tp_dolar = coin_purchasable * gain_per_coin
        tp_percentual = (tp - entry)/entry
        
        print(f"ur max gain in usd is {tp_dolar:.2f}\nIn leveraged %gain: {b*tp_percentual*100:.2f}%")
        print("To quit the script ctrl+c")
        return tp_dolar
        
info()
while True:
    a = get_pair()
    cointicker = get_quote(a)
    b = leverage()
    maximum_contract = total_capital()
    coinc = coin_contract()
    size = operation_size()
    entry = get_order()
    dolar_loss = stoploss(entry, size)
    tp_dolar = takeprofit(entry)
    z = str(input("would u like to pick other crypto pair?(y/n): ")).upper()
    if(z!="Y"):
            cointicker = get_quote(a)
            b = leverage()
            maximum_contract = total_capital()
            coinc = coin_contract()
            size = operation_size()
            entry = get_order()
            dolar_loss = stoploss(entry, size)
            tp_dolar = takeprofit(entry)

    else:
         a = get_pair()
         cointicker = get_quote(a)
         b = leverage()
         maximum_contract = total_capital()
         coinc = coin_contract()
         size = operation_size()
         entry = get_order()
         dolar_loss = stoploss(entry, size)
         tp_dolar = takeprofit(entry)
         




    



    



