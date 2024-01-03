from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def scraping_options(request):
    return render(request, 'scraping/scraping_options.html')

def get_quaid_speech(request):

    quaid_quote = scraper('https://www.goodreads.com/quotes/457259-you-are-free-you-are-free-to-go-to-your')

    context = {
        'quote': quaid_quote
    }

    return render(request, 'scraping/quaid_speech.html', context=context)

def get_abraham_speech(request):

    abraham_quote = scraper('https://www.goodreads.com/quotes/114791-four-score-and-seven-years-ago-our-fathers-brought-forth')

    context = {
        'quote': abraham_quote
    }

    return render(request, 'scraping/abraham_speech.html', context=context)

# https://www.goodreads.com/quotes/4417-you-re-not-to-be-so-blind-with-patriotism-that-you

def scraper(url):
    req = requests.get(url)

    soup = BeautifulSoup(req.content, "html.parser")

    res = soup.find('div', class_='quoteText')

    quote = res.get_text().split('\n')[2]

    return quote
    