from django.shortcuts import render
from yahoo_fin.stock_info import *
from .serializers import TradeSerializer


# Create your views here.
def home(request):
    stock_list = tickers_nifty50()
    return render(request, 'stocks/index.html', {'stock_list':stock_list})

# def stocksInfo(request):
#     stock_list = request.GET.getlist('stock_list')
#     request.session.create()
#     stock_details = {}
#     for stock in stock_list:
#         stock_detail = get_quote_table(stock)
#         stock_details.update({stock:stock_detail})
#     return render(request, 'stocks/selectedstocks.html', {'stock_details':stock_details})


from django.shortcuts import render
import yfinance as yf

def stocksInfo(request):
    stock_list = request.GET.getlist('stock_list')
    stock_details = {}

    for stock in stock_list:
        try:
            stock_data = yf.Ticker(stock).info
            if 'currentPrice' in stock_data:
                stock_details[stock] = {
                    "Quote Price": stock_data.get('currentPrice', 'N/A'),
                    "Open": stock_data.get('open', 'N/A'),
                    "Previous Close": stock_data.get('previousClose', 'N/A'),
                    "Market Cap": stock_data.get('marketCap', 'N/A'),
                    "Change": round((stock_data.get('currentPrice', 0) - stock_data.get('previousClose', 0)), 2)
                }
            else:
                stock_details[stock] = {"Error": "Stock data unavailable"}
        except IndexError:
            stock_details[stock] = {"Error": "Stock not found"}
        except Exception as e:
            stock_details[stock] = {"Error": str(e)}

    return render(request, 'stocks/selectedstocks.html', {'stock_details': stock_details})
