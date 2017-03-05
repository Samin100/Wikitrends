import csv
import matplotlib.pyplot as pyplot
import requests
from _datetime import date, timedelta, datetime
import _json
from pprint import pprint as print
from yahoo_finance import Share
import os
import time


def build_wiki_URL(article, granularity, start, end):
    """
    Builds the wikipedia pageview request URL.
    :param article: wiki article
    :param granularity: 'monthly' or 'daily'
    :param start: datetime date object
    :param end: datetime date object
    :return: request URL as a string
    """
    # GET /metrics/pageviews/per-article/{project}/{access}/{agent}/{article}/{granularity}/{start}/{end}
    wiki_base = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents"

    # YYYYMMDD format
    d_start = '%02d' % start.day
    m_start = '%02d' % start.month
    y_start = start.year
    str_start = str(y_start) + str(m_start) + str(d_start)

    d_end = '%02d' % end.day
    m_end = '%02d' % end.month
    y_end = '%02d' % end.year
    str_end = str(y_end) + str(m_end) + str(d_end)

    return wiki_base + '/' + article + '/' + granularity + '/' + str_start + '/' + str_end


def visualize_wiki(company, start, end):
    wikiurl = build_wiki_URL(company, 'daily', start, end)
    wikidata = requests.get(wikiurl).json()

    fb_views = []
    prev = (int(wikidata['items'][0]['views']))

    for item in wikidata['items']:

        # calculates percentage change
        curr = (int(item['views']))
        change = ((curr - prev) / prev) * 100
        fb_views.append(change / 10)
        prev = (int(item['views']))

    pyplot.plot(fb_views, 'b')


def visualize_stock(symbol, start, end):
    stock = Share(symbol)
    stockdata = stock.get_historical(str(start), str(end + timedelta(days=7)))
    closing_prices = {}

    for item in stockdata:
        closing_prices[item['Date']] = float(item['Close'])

    for x in range((end - start).days):

        curr = start + timedelta(days=x)

        if str(curr) not in closing_prices.keys():
            replacement = curr + timedelta(days=1)
            while str(replacement) not in closing_prices.keys():  # loops until a replacement price is found
                replacement = replacement + timedelta(days=1)

            closing_prices[str(curr)] = closing_prices[str(replacement)]

    stocklist = []

    prev = closing_prices[str(start)]
    for x in range((end - start).days):
        curr = start + timedelta(days=x)

        curr_price = closing_prices[str(curr)]

        change = ((curr_price - prev) / prev) * 1000
        prev = closing_prices[str(curr)]
        stocklist.append(change)

    pyplot.plot(stocklist, 'g')


def show_plot():
    axes = pyplot.gca()
    axes.set_ylim([-100, 100])
    pyplot.legend(['Stock price (' + symbol + ')', 'Wikipedia page views'])
    pyplot.title(company + ' (' + symbol + ')' + ' Wikipedia page views and stock price')
    pyplot.ylabel('Percentage change')
    pyplot.xlabel("# of days after March 1st, 2016")
    #pyplot.show()  # uncomment this to view instead of save the plot
    pyplot.savefig(company + '.png')
    pyplot.close()

start = datetime(2016, 3, 1).date()
end = start + timedelta(days=60)
os.chdir('Plots')

timeA = time.time()

with open('../SP500.csv') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    error_list = []
    for row in reader:
        count += 1
        try:
            symbol = str(row[0])
            company = row[1]
            print(str(count) + ': ' + 'Processing ' + company)
            visualize_stock(symbol, start, end)  # processes stock data
            visualize_wiki(company, start, end)  # processes Wikipedia page view data
            show_plot()  # formats and saves plot
        except Exception as e:
            error_list.append(company)
            print('--Error in processing ' + company)
            print(e)

timeB = time.time()
print('Errors occurred while processing: ')
for c in error_list:
    print(c)
print('\nCompleted in ' + str(timeB - timeA) + 'seconds')
print('Min: ' + str((timeB - timeA) // 60) + ' sec: ' + str((timeB - timeA) % 60))