from tkinter import *
import requests
import json

pycrypto = Tk()
pycrypto.title("my crypto portfolio")
name = Label(pycrypto, text = 'Bitcone', bg = 'black', fg = "white")
name.grid(row = 0,  column = 0, sticky= N+S+E+W)

def font_color(amount):
    if amount >= 0:
        return 'green'

    else:
        return 'red'

def my_portfolio():
    api_request = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?CMC_PRO_API_KEY=d34e2cbd-43ca-435c-9a56-fcfcd8e364cb')
    api = json.loads(api_request.content)
    coins = [
        {
            "symbol": 'BTC',
            "amount_owned": 2,
            "price_per_coin": 3200

        },
        {
            "symbol": "XRP",
            "amount_owned": 3,
            "price_per_coin": 2.05

        },
        {
            "symbol": "EOS",
            "amount_owned":9 ,
            "price_per_coin": 2.81
  
        },
        {
            "symbol": "XTZ",
            "amount_owned": 10,
            "price_per_coin":2.78 

        }
    ]
    total_pl = 0
    coin_row = 1
    total_current_value = 0
    for i in range(0,10):
        for coin in coins:
            if api['data'][i]['symbol'] == coin['symbol']:
                total_paid = coin['price_per_coin']* coin['amount_owned']
                currant_value = coin["amount_owned"] * api['data'][i]['quote']["USD"]["price"]
                pl_percoin = api['data'][i]['quote']["USD"]["price"] - coin["price_per_coin"]
                total_pl_coin = pl_percoin * coin["amount_owned"]
                total_pl = total_pl + total_pl_coin
                total_current_value = total_current_value + currant_value


                print(f"{api['data'][i]['name']}-{api['data'][i]['symbol']}")
                print("price - ${0:.2f}".format(api['data'][i]['quote']["USD"]["price"]))
                print('number_of_coin:', coin["amount_owned"])
                print('total_paid:', "${0:.2f}".format(total_paid))
                print('currant_value:', "${0:.2f}".format(currant_value))
                print('p/l per_coin:',"${0:.2f}".format(pl_percoin))
                print("total p/l with coin:","${0:.2f}".format(total_pl_coin))
                print("..............")


                bg_color = '#ffffff'
                if coin_row % 2 == 0:
                    bg_color = '#C2DFFF'
                name = Label(pycrypto, text = api['data'][i]['symbol'], bg = bg_color, fg = "black",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                name.grid(row = coin_row,  column = 0, sticky= N+S+E+W)

                price = Label(pycrypto, text = "${0:.2f}".format(api['data'][i]['quote']["USD"]["price"]), bg = bg_color, fg = "black",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                price.grid(row = coin_row,  column = 1, sticky= N+S+E+W)


                no_coin = Label(pycrypto, text = coin["amount_owned"], bg = bg_color, fg = "black",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                no_coin.grid(row = coin_row,  column = 2, sticky= N+S+E+W)


                amount_paid= Label(pycrypto, text = "${0:.2f}".format(total_paid), bg = bg_color, fg = "black",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                amount_paid.grid(row = coin_row,  column = 3, sticky= N+S+E+W)


                current_value= Label(pycrypto, text = "${0:.2f}".format(currant_value), bg = bg_color, fg =font_color(float("{0:.2f}".format(currant_value))),font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                current_value.grid(row = coin_row,  column = 4, sticky= N+S+E+W)

                pl_coin = Label(pycrypto, text = "${0:.2f}".format(pl_percoin), bg=bg_color , fg =font_color(float("{0:.2f}".format(pl_percoin))) ,font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                pl_coin.grid(row = coin_row,  column = 5, sticky= N+S+E+W)


                totalpl = Label(pycrypto, text = "${0:.2f}".format(total_pl_coin), bg = bg_color, fg =font_color(float("{0:.2f}".format(total_pl_coin))) ,font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
                totalpl.grid(row = coin_row,  column = 6, sticky= N+S+E+W)
                coin_row = coin_row + 1



    totalpl = Label(pycrypto, text = "${0:.2f}".format(total_current_value), bg = 'black', fg = "white",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
    totalpl.grid(row = coin_row,  column = 4, sticky= N+S+E+W)
    

    totalpl = Label(pycrypto, text = "${0:.2f}".format(total_pl), bg = 'black', fg = "white",font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
    totalpl.grid(row = coin_row,  column = 6, sticky= N+S+E+W)

    api = ""

    update = Button(pycrypto, text = 'update', bg = 'white', fg = "black",command = my_portfolio,font = 'Lato 12 bold', padx = '5',pady = '5',borderwidth ='2', relief = 'groove')
    update.grid(row = coin_row + 1,  column = 6, sticky= N+S+E+W)

    
header_bg_color = '#157DEC'
name = Label(pycrypto, text = 'coin name', bg = header_bg_color, fg = "white")
name.grid(row = 0,  column = 0, sticky= N+S+E+W)

price = Label(pycrypto, text = 'price', bg = header_bg_color, fg = "white")
price.grid(row = 0,  column = 1, sticky= N+S+E+W)


no_coin = Label(pycrypto, text = 'coin owned', bg = header_bg_color, fg = "white")
no_coin.grid(row = 0,  column = 2, sticky= N+S+E+W)


amount_paid= Label(pycrypto, text = 'total amount paid', bg = header_bg_color, fg = "white")
amount_paid.grid(row = 0,  column = 3, sticky= N+S+E+W)


current_value= Label(pycrypto, text = 'current value', bg = header_bg_color, fg = "white")
current_value.grid(row = 0,  column = 4, sticky= N+S+E+W)

pl_coin = Label(pycrypto, text = 'p/l per coin', bg = header_bg_color, fg = "white")
pl_coin.grid(row = 0,  column = 5, sticky= N+S+E+W)


totalpl = Label(pycrypto, text = 'total p/l with coin', bg = header_bg_color, fg = "white")
totalpl.grid(row = 0,  column = 6, sticky= N+S+E+W)

name = Label(pycrypto, text = 'Bitcoin', bg = header_bg_color, fg = "white")
name.grid(row = 0,  column = 0, sticky= N+S+E+W)





my_portfolio()
pycrypto.mainloop()
print('my programm completed')