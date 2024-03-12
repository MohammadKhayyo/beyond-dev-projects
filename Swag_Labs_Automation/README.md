# Swag Labs Automation

## Overview
This project is an automated testing suite for the Swag Labs demo website, designed to validate functionality across various aspects of the site including login, inventory management, and checkout processes. It leverages Selenium WebDriver for browser automation to simulate user actions and verify correct application behavior.

## Project Structure
The project is organized into several directories and files, each serving a specific purpose:

- `dsl/`: Contains the Domain Specific Language (DSL) class which abstracts common Selenium WebDriver commands for easier test script development.
  - `dsl.py`: Defines the `DSL` class with methods to interact with web elements.
- `page_objects/`: Implements the Page Object Model (POM) pattern to encapsulate the structure and behaviors of pages within the Swag Labs website.
  - `login_page.py`: Defines the `Login_Page` class for interactions with the login page.
  - `inventory_page.py`: Defines the `Inventory_Page` class for interactions with the inventory listing page.
  - `checkout_page.py`: Defines the `Checkout_Page` class for interactions during the checkout process.
- `test_objects/`: Contains unittest test cases that use the page objects to interact with the Swag Labs website.
  - `test_login.py`: Contains tests for verifying login functionality.
  - `test_checkout.py`: Contains tests for the checkout process.
  - `test_product_sort.py`: Contains tests for product sorting functionality.

## Prerequisites
Before running the tests, ensure you have the following installed:
- Python 3.6 or higher
- Selenium WebDriver
- Google Chrome and ChromeDriver

## Setup
1. Clone the repository to your local machine.
2. Install the required Python packages:  
   ```bash
   pip install selenium
3. Download ChromeDriver and ensure it's in your PATH.

## Running the Tests
To run the tests, navigate to the `test_objects/` directory and execute the desired test file using Python. For example:

```bash
cd Swag_Labs_Automation/test_objects/
python test_login.py
```

## Contributing
Contributions are welcome. Please open an issue first to discuss what you would like to change, or directly submit a pull request.

## License
This project is open-source and available under the MIT License.