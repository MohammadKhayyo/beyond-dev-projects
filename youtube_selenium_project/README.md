# YouTube Selenium Automation

This project is a Selenium-based testing framework designed to automate various interactions with YouTube, such as
searching for videos, toggling mute, entering/exiting full screen and miniplayer modes, and switching between light and
dark themes. The framework utilizes the Page Object Model (POM) design pattern for enhanced maintainability and
readability.

## Structure

The project is organized into three main directories:

- `infra/`: Contains foundational classes for browser interaction. Includes `browser_wrapper.py` for managing browser
  sessions.
- `logic/`: Contains the `YouTubePage` class that extends the base page functionality from `page_base.py` in the `infra`
  directory. This class provides methods for specific YouTube interactions.
- `tests/`: Includes `youtube_test.py`, which contains unit tests that demonstrate how to use the `YouTubePage` class
  methods to interact with YouTube.

## Setup

To run this project, you will need Python 3.x and Selenium. You can install Selenium using pip:

```bash
pip install selenium
```

Ensure you have the appropriate WebDriver for the browser you plan to use (Chrome, Firefox, etc.). Place the WebDriver
in a directory that is on your system's PATH, or modify the `browser_wrapper.py` file to include the path to your
WebDriver.

## Usage

To execute the tests, navigate to the `tests/` directory and run:

```bash
python youtube_test.py
```

This command will run all the test methods in the `YouTubePageTest` class.

## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Implement your changes.
4. Write or update tests as necessary.
5. Submit a pull request.

Please ensure your code follows the project's coding standards and includes adequate test coverage.

## License

[MIT License](LICENSE.md)


