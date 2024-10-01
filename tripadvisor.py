from flask import Flask, request, render_template
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

# Function to create the WebDriver
def create_driver():
    chromedriver_path = r'C:\Users\fabio\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Your specific path
    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--lang=en')  # Set WebDriver language to English
    
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to search for the element with the attribute 'data-test-target'
def search_for_element_with_test_target(query):
    driver = create_driver()
    info = {}

    try:
        # Perform the search on Google
        google_search_url = f"https://www.google.com/search?q={query}+tripadvisor"
        driver.get(google_search_url)
        logging.debug("Google search page loaded")

        # Accept the cookie popup, if present
        try:
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[text()='Accept all']"))
            )
            accept_button.click()
            logging.debug("Cookies accepted")
        except Exception as e:
            logging.debug(f"No cookie banner found or unable to click: {e}")

        # Click on the first result
        first_result = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'h3'))
        )
        first_result.click()
        logging.debug("First search result clicked and page opened")

        # Search for the element with the attribute 'data-test-target="restaurants-detail"'
        try:
            element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@data-test-target="restaurants-detail"]'))
            )
            logging.debug("Element with 'data-test-target=restaurants-detail' found!")
            info['found'] = True
            info['name'] = element.text  # Get the text from the element
        except Exception as e:
            logging.debug(f"Element with 'data-test-target' not found: {e}")
            info['found'] = False

        return info

    except Exception as e:
        logging.debug(f"Error during search or click: {e}")
        return {'error': 'An error occurred during the search'}

    finally:
        driver.quit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query'].strip()  # Sanitize input
    if not query:
        return render_template('index.html', error='The search field cannot be empty')

    search_result = search_for_element_with_test_target(query)

    # If there is an error during the search, return a message
    if 'error' in search_result:
        return render_template('index.html', error=search_result['error'])

    # Return the search result on the same page
    return render_template('index.html', result=search_result)

if __name__ == '__main__':
    app.run(debug=True)
