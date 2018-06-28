# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

# clear the terminal
for i in range(0,40):
    print '\n'

# Welcome Message
print('Python Scraper. Returnerar en lista på de senaste auktionerna från http://tradera.se')
#specify the search query

def main():
        query = raw_input('Sökord:  ')
        query = query.replace(' ', '%20') # Removes blankspaces and replaces them with %20

        # specify the url
        quote_page = 'https://www.tradera.com/search?q=' + query

        # query the website and return the html to the variable ‘page’
        page = urllib2.urlopen(quote_page)

        ##############
        items = {}
        prices = {}
        times = {}
        bids = {}
        ind = 0
        ##############
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')

        # Take out the <div> of name and get its value
        name_box = soup.find('h3', attrs={'class': 'item-card-details-header'})
        price_box = soup.find('span', attrs={'class': 'item-card-details-price-amount'})
        time_box = soup.find('span', attrs={'class': 'item-card-details-time-left'})
        bid_box = card_box = soup.find('span', attrs={'class': 'item-card-details-bids'})

        #Print Column Names
        print '%0s  %14s %18s  %12s  %24s' % ('#', 'Tid Kvar', 'Antal Bud', 'Pris', 'Artikelnamn')
        print('------------------------------------------------------------------------------------------------------------------------------------')
        # Get all the items
        for name_box in soup.find_all('h3', attrs={'class': 'item-card-details-header'}):
            items[ind] = name_box.text.strip()
            ind += 1

        ind = 0
        # Get all the item prices
        for price_box in soup.find_all('span', attrs={'class': 'item-card-details-price-amount'}):
            prices[ind] = price_box.text.strip()
            ind += 1
        ind = 0

        # Get number of bids
        for bid_box in soup.find_all('span', attrs={'class': 'item-card-details-bids'}):
            bids[ind] = bid_box.text.strip()
            ind += 1
        ind = 0

        # Get time remaining (FINALLY WORKS)
        for card_box in soup.find_all('span', attrs={'class': 'item-card-details-time-left'}):
            times[ind] = card_box.text.strip()
            ind += 1

        #Output everything in a table
        for i in range(0,15):
            try:
                    line_new = '%0s  %14s %16s  %16s  %5s' % (str(i+1) + '.', times[i], bids[i], prices[i], items[i])
                    print line_new
            except:
                pass
        # Funkar 100 % men då visas ej de andra artiklarna ex "21 Jul 12:22"
        print('------------------------------------------------------------------------------------------------------------------------------------')
        pass

while(True):
    main()
