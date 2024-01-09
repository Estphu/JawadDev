import platform
import subprocess
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.
def elections_result(request):
    url = 'https://interactive.aljazeera.com/aje/2018/live-results-pakistan-election-day-2018/index.html'

    # Specify the path to the Chrome binary
    # Get the Chrome binary path
    chrome_binary_path = get_chrome_binary_path()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.binary_location = webdriver_path
    chrome_options.add_argument('--headless')

    chrome_driver_path = ChromeDriverManager(chrome_type='google-chrome').install()

    chrome_options.binary_location = chrome_binary_path

    driver = webdriver.Chrome(service=ChromeService(chrome_driver_path),options=chrome_options)

    try:
    # Load the page
        driver.get(url)

        # Wait for the tab content to be present (adjust the timeout as needed)
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'provincial-tab-content'))
        )

        # Get the page source after JavaScript execution
        page_source = driver.page_source

        # Use BeautifulSoup to parse the page source
        soup = BeautifulSoup(page_source, 'html.parser')

        
        election_dict = {}
        
        for content in soup.find_all('div', class_='constituency-card'):

            constituency_id = content.find('h2', class_ = 'constituency-card__id').get_text()

            election_dict[constituency_id] = {
                'id': constituency_id,
                'name': content.find('h3', class_ = 'constituency-card__name').get_text(),
                'voters': content.find('div', class_ = 'constituency-card__reg-voters').get_text().replace(' VOTERS',''),
                'winner': content.find('div', class_ = 'constituency-card__candidate-name').get_text(),
            }

            for value in content.find_all('div', class_ = 'constituency-card__label'):
                if 'TURNOUT' in value.get_text():
                    election_dict[constituency_id]['turnout'] = value.get_text().replace('TURNOUT','')
                if 'POLLED' in value.get_text():
                    election_dict[constituency_id]['polled_votes'] = value.get_text().replace('VOTES POLLED','')
                elif 'VOTES' in value.get_text():
                    election_dict[constituency_id]['votes'] = value.get_text().replace('VOTES','')

            # Extract box shadow from the style attribute
            box_shadow_match = re.search(r'box-shadow:[^;]+(\b\w+)', content['style'])
            
            if box_shadow_match:
                election_dict[constituency_id]['box_shadow_color'] = box_shadow_match.group(1)        

        context = {
            'kpk_results': election_dict
        }

        return render(request, 'scraping/elections_result.html', context=context)

    finally:
        # Close the browser window
        driver.quit()
    return render(request, 'scraping/elections_result.html')

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
    
def get_chrome_binary_path():
    if platform.system() == 'Windows':
        # Default installation path on Windows
        return r"C:/Program Files/Google/Chrome/Application/chrome.exe"
    elif platform.system() == 'Linux':
        # Try to find the path on Linux
        try:
            return subprocess.check_output(['which', 'google-chrome'], text=True).strip()
        except subprocess.CalledProcessError:
            return None
    elif platform.system() == 'Darwin':
        # Default installation path on macOS
        return "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    else:
        return None    