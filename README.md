# 🚀 Playwright Pytest Automation Framework

A scalable UI automation framework built using **Python, Playwright, Pytest, and Page Object Model (POM)** with **Allure reporting integration**.

Designed with maintainability, scalability, and clean architecture in mind.

---

## 📂 Project Structure


## 🛠 Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- Allure Reports

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/shambaditya-ghosh/playwright-pytest-framework.git

cd playwright-pytest-framework

### 2️⃣ Create Virtual Environment

python -m venv venv

### Mac/Linux 
source venv/bin/activate 

### Windows
venv\Scripts\activate 

### 3️⃣ Install Dependencies

pip install -r requirements.txt
playwright install

## ▶️ Running Tests

Run all tests: pytest -v

Run with Allure results: pytest --alluredir=allure-results

Generate Allure report: allure serve allure-results

Run above commands in one go :  pytest -v && pytest --alluredir=allure-results && allure serve allure-results

## 📊 Allure Reporting

- Automatically captures test execution details
- Can be configured to capture screenshots
- Supports step-level reporting

## 🧩 Framework Features

✔ Page Object Model structure  
✔ Scalable fixture design  
✔ Centralized configuration  
✔ Allure reporting support  
✔ Clean project structure  
✔ Ready for CI/CD integration  

## 🔥 Future Enhancements

- Parallel execution
- Environment-based execution (QA/Stage/Prod)
- CI integration (GitHub Actions / Jenkins)
- Docker support
- API test integration

## 👨‍💻 Author

**Shambaditya Ghosh**  
Software QA Engineer 




