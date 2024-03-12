# Appium Automation Suite for TaskAgenda

Welcome to the Appium Automation Suite for TaskAgenda, a comprehensive testing framework designed to automate and validate the functionality of the TaskAgenda mobile application. This suite employs Appium and Selenium to interact with the application on Android devices, ensuring that every aspect of TaskAgenda, from event management to UI responsiveness, operates as intended.

## Features

This suite includes tests for:
- Navigating through dates using the calendar's arrows.
- Creating, editing, and deleting events.
- Changing the application's theme color.
- Managing vibration settings for notifications.
- Adding custom event types with unique icons and colors.

## Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8+
- Appium Server for handling the automation bridge.
- Node.js and npm (required for Appium).
- An Android emulator or a real device set up for testing.
- The required Python libraries as listed in `requirements.txt`.

## Installation Guide

1. **Clone the Project**

    Start by cloning the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/appiumProject.git
    ```

2. **Install Dependencies**

    Navigate to the project directory and install the necessary Python libraries:
    ```bash
    cd appiumProject
    pip install -r requirements.txt
    ```

3. **Set Up Appium Server**

    Ensure your Appium server is running. You can start it via the Appium Desktop client or through the command line if you have Appium installed globally:
    ```bash
    appium
    ```

4. **Configure Your Testing Environment**

    Adjust the `appiumProject/config.json` file to match your Android device or emulator's specifications. Ensure that the `appPackage` and `appActivity` reflect the correct application settings.

## Running Tests

With the environment set up, you're ready to run tests. Each script in the `appiumProject/test/` directory is designed to test different functionalities of the TaskAgenda app. To execute a test, use:

```bash
python -m unittest appiumProject/test/appium_events_test.py
python -m unittest appiumProject/test/appium_features_test.py
```
## Contributing

Your contributions make the open-source community a better place. We encourage you to contribute to this project by submitting bug reports, feature requests, or code improvements. Please fork the repository and create a pull request for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thank you to the Appium and Selenium communities for providing the tools that make automated testing accessible and efficient.
- This project is inspired by the everyday challenges of quality assurance professionals.

Happy Testing!
```