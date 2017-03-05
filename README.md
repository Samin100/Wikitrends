# Introduction
For my data visualization assignment, I decided to see if there was any correlation between stock prices for companies in the S&P 500 and how much traffic
its Wikipedia page gets. The logic behind it being a sudden increases of visitors to a company's Wikipedia page may be cause for concern and allow us to
predict stock price fluctuations ahead of time.

# The Data
I needed access to both a Wikipedia page view dataset for individual articles and
stock datasets for the S&P 500 companies. The Wikipedia data was cumbersome at first since it was looking like I had to download about 30 gigs of data just to get the
pages I wanted, but luckily
I discovered an experimental API Wikipedia has that would allow me to view page data
for any time period for the article I specify. You can check that out <a href= "https://wikimedia.org/api/rest_v1/#/href">here</a>.

In addition, I would also need stock data for a the list of S&P 500 companies. Luckily
I was able to use the <a href="https://finance.yahoo.com/lookup?s=API">Yahoo Finance API</a> and only pull the data I needed.

Finally, I would need a list of the S&P 500 companies which I found at this <a href="https://github.com/datasets/s-and-p-500-companies">GitHub
repository</a>.

# Processing the data
After getting access to all the data I needed, I had to parse it. The Wikipedia page viewdata was loading just fine, however there were some hiccups with the stock data.
It turns out there's no closing price for weekends and holidays and that would leave
some pretty bad discontinuities in my plots. I decided to just carry over the previous working day's prices which solved that problem just fine.

Another hiccup was that the Wikipedia page view count would be in the thousands while
the stock prices were only about a hundred dollars. This made for an extremely uneven
plot so I decided to plot percentage change per day instead of the actual amount. This made it much easier to view change in data relative to itself across relatively
different scales.

# Plots and conclusion
For my range, I tried scales as large as 3 years, and as small as 2 weeks. I decided to focus on 2 months since it provided enough data to be able to analyze easily yet not be overly crowded. The date range is 60 days beginning at March 1st, 2016.
After plotting all 500 companies and outputting it to a folder, I was able to notice
a common trend simply by looking at a few of the plots. An increase in Wikipedia
page traffic can either mean a stock is about to go up or down. This makes sense
because if people notice a drastically changing stock, they're going to want to
investigate and learn more about the company, regardless if the stock is rising or
falling quickly.

Here's a plot of Alphabet (Google's parent company):

![Alphabet](/Plots/Alphabet%20Inc%20Class%20C.png)

Around the 53 day mark we can see a sharp increase in Wikipedia traffic, and a
sharp decrease in stock price. I decided to look up the day which was March 23rd, 2016, and one of the top stories was Alphabet released it's first quarter earnings
and it didn't live up to investors' expectations.

Here are a few more plots, most of them being large banks, that I found fairly interesting. You can view another 40+ plots in the Plots folder above.

![3M](/Plots/3M%20Company.png)
</br>
![Abbott](Plots/Abbott%20Laboratories.png)
</br>
![BBT](Plots/BB%26T%20Corporation.png)
</br>
![Bank of America](Plots/Bank%20of%20America%20Corp.png)
</br>
![GAP](Plots/Gap%20\(The).png)
</br>
