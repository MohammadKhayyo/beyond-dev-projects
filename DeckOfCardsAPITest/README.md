# DeckOfCardsAPITest

DeckOfCardsAPITest is a Python-based testing suite designed to interact with the [Deck of Cards API](https://deckofcardsapi.com/). It provides a comprehensive set of functions to manage decks of cards, including creating new decks, shuffling, drawing cards, managing piles, and shuffling piles. This suite is aimed at developers who need to test or integrate Deck of Cards API functionalities within their projects.

## Features

- **API Wrapper:** A simple interface for GET and POST requests to the Deck of Cards API.
- **Config Reader:** A utility to read configuration settings from a JSON file.
- **Deck API:** An interface to interact with the Deck of Cards API, offering functionalities such as creating new decks, shuffling, drawing cards, and managing card piles.
- **Test Suite:** A set of unit tests to validate the functionality of the DeckAPI class.

## Installation

To get started with DeckOfCardsAPITest, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python 3.6 or higher installed.
3. Install the required dependencies by running `pip install -r requirements.txt` in your terminal. This project requires the `requests` library for making HTTP requests.

## Configuration

Before running the tests or using the DeckAPI, you need to set up the configuration file:

1. Navigate to the `DeckOfCardsAPITest` directory.
2. Locate the `config.json` file and ensure it contains the URL to the Deck of Cards API. The default configuration should look like this:

```json
{
    "url": "https://deckofcardsapi.com/api/deck/"
}
```

## Usage

### Using the DeckAPI

The `DeckAPI` class provides methods to interact with the Deck of Cards API. Here's a simple example to create a new shuffled deck with jokers:

```python
from DeckOfCardsAPITest.logic.deck_api import DeckAPI

deck_api = DeckAPI()
deck = deck_api.new_deck(shuffle=True, jokers_enabled=True)
print(deck)
```

### Running Tests

To run the provided tests, execute the following command from the root directory of the project:

```bash
python -m unittest discover -s tests
```

This command will discover and run all tests within the `tests` directory, providing a summary of the test results.

## Contributing

Contributions to DeckOfCardsAPITest are welcome. Please ensure that your code adheres to the project's coding standards and include unit tests for new features or bug fixes.

## License

DeckOfCardsAPITest is open-sourced software licensed under the MIT license.