# 🚕 Urban Routes – UI Test Automation Framework

This project is part of the QA program's Sprint 8. It's a UI test automation framework designed to validate the end-to-end user flow of ordering a taxi in the **Urban Routes** web application, using Selenium WebDriver with the Page Object Model (POM) pattern.

---

## 👤 Author

**Full Name:** Luis Manco  
---

## 📌 Test Scenario Scope

This automation script covers the entire critical path of a user ordering a ride, ensuring a seamless experience. The automated steps include:

1. Setting pickup and destination addresses.
2. Selecting the "Comfort" fare tier.
3. Entering and submitting a valid phone number.
4. Intercepting and using the SMS confirmation code.
5. Adding a new payment method (credit card).
6. Leaving a message for the driver.
7. Selecting extra services (blanket, tissues, and two ice creams 🍦).
8. Submitting the final order.
9. Verifying the appearance of the "driver search" modal.
10. (Optional) Verifying that the driver's information is displayed after a successful match.

---

## ✨ Key Features & Technical Highlights

* **Page Object Model (POM):** The framework is built using the POM design pattern to ensure the code is clean, reusable, and easy to maintain. Page elements and actions are separated from the test logic.
* **Dynamic Waits:** Implements `WebDriverWait` and `expected_conditions` to handle dynamic elements and asynchronous loading, preventing flaky tests and improving script reliability.
* **Advanced User Interaction:** Simulates complex user actions, such as changing focus between input fields to trigger client-side validation (`TAB` key simulation).
* **Network Log Interception:** Utilizes Chrome DevTools Protocol (CDP) to programmatically intercept network traffic and retrieve the SMS confirmation code, a powerful technique for handling two-factor authentication flows.
* **Diverse Locator Strategy:** Employs a wide range of Selenium locators (`ID`, `CSS Selector`, `XPath`, `ClassName`, `Name`) to demonstrate versatility in element identification.

---

## 🛠️ Technologies & Tools

- Python 3
- Selenium WebDriver
- Pytest
- Page Object Model (POM)
- Git & GitHub
- Google Chrome & ChromeDriver

---

## 📁 Project Structure

```
📦qa-project-Urban-Routes-en/
├── data.py          # Stores all test data (credentials, addresses, etc.)
├── main.py          # Contains the Page Object and Test classes
└── README.md        # This documentation file
```

---

## ▶️ How to Run the Tests

### Prerequisites

* Python 3.x installed
* Google Chrome browser installed
* `ChromeDriver` downloaded and placed in your system's `PATH`. Make sure the version matches your Chrome browser version. [Download ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)

---

### 1. Clone this repository

```bash
git clone https://github.com/your-username/qa-project-Urban-Routes-en.git
cd qa-project-Urban-Routes-en
```

---

### 2. Install dependencies

It is highly recommended to use a virtual environment.

Create a `requirements.txt` file with the following content:

```
selenium
pytest
```

Then, install the dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Run the tests

Execute the test suite from your terminal:

```bash
pytest main.py
```

---

## 📬 Contact

If you have any questions or suggestions, feel free to contact me via Discord or by creating an issue in this GitHub repository.
