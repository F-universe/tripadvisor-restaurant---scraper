Google Search with Flask and Selenium
This project contains a simple web application built using Flask and Selenium to automate Google searches. The application retrieves specific information from Tripadvisor pages by searching for elements with a certain class attribute (data-test-target="restaurants-detail"). The code can be easily modified to search for other elements or information by adjusting the class or search query.

Features
Flask Web Application: The frontend is built with HTML and allows users to input search queries through a simple form.
Selenium Web Scraping: The backend automates a Google search and navigates to Tripadvisor pages, searching for a specific element.
Results Display: The search results (if the element is found) are displayed in a table format on the webpage.
Error Handling: If no results are found or if an error occurs during the search process, the app provides feedback to the user.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/your-repo-name.git
Install the necessary Python dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure you have the Chrome WebDriver installed and update the chromedriver_path in the Python code to match the path on your machine:

python
Copy code 
chromedriver_path = r'path_to_your_chromedriver'
Run the Flask application:

bash
Copy code 
python app.py
Open your browser and navigate to http://127.0.0.1:5000/ to use the web interface.

Usage
Enter a search term (such as the name of a restaurant or place) in the input field.
The application will search Google for Tripadvisor results related to that term and try to locate the element with data-test-target="restaurants-detail".
The result, if found, will be displayed on the page in table format.
Customization
You are free to copy and modify this code to suit your needs. For example, you can:

Modify the XPATH or class attribute in the Selenium code to extract different data.
Reorganize the results or display additional details.
Adapt the front-end HTML as per your project's needs.
Contributing
Feel free to contribute by opening a pull request or submitting an issue if you find any bugs or have suggestions for improvement.

This README provides a good overview of the project and helps other developers understand how they can use or modify the code.
