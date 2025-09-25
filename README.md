# Dynamic Selenium Automation Project

This project provides a comprehensive automation suite for https://automationexercise.com, including UI (Selenium) and API (requests) tests. It is organized for high coverage and maintainability.

## Features
- Selenium-based UI tests for all major user flows
- API tests for all public endpoints
- Helpers for both UI and API automation
- Pytest-based structure, easy to extend
- Logical test file organization

## Project Structure
```
utils/                # Helper modules for Selenium and API
api/                  # API test files
conftest.py           # Pytest fixtures (e.g., Selenium driver)
tests/                # All UI and helper tests, logically split
requirements.txt      # Python dependencies
```

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/MinionsBoy/dynamic-selenium.git
cd dynamic-selenium
```

### 2. Create and activate a virtual environment (recommended)
```
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

### 4. WebDriver Setup
- Chrome browser is required.
- The project uses `webdriver-manager` to auto-download the correct driver.

### 5. Configure test users
- Some tests require a valid user (see `test_auth.py`).
- Update credentials in the test files as needed.

## Running Tests

### Run all tests (UI + API):
```
pytest
```

### Run only API tests:
```
pytest api/
```

### Run only UI tests:
```
pytest tests/
```

### Run with coverage report:
```
pytest --cov=utils --cov=api --cov=tests
```

## Adding More Tests
- Add new UI tests in the `tests/` folder, grouped by feature.
- Add new API tests in the `api/` folder.
- Add or update helpers in `utils/` as needed.

## Notes
- For best results, use the latest Chrome browser.
- Some UI tests may require stable internet and may be affected by site changes.
- API tests use live endpoints and may be rate-limited.

## Contributing
Pull requests are welcome! Please add/modify tests and helpers as needed and ensure all tests pass before submitting.

---

© 2025 MinionsBoy
# dynamic-selenium
Zestaw testow dynamicznych z uzyciem Selenium
