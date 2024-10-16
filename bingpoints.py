from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import os
import random
import time

# Load environment variables from .env file
load_dotenv()

# Fetch email, password, and URL from environment variables
bing_email = os.getenv("BING_EMAIL")
bing_password = os.getenv("BING_PASSWORD")
bing_login_url = os.getenv("BING_LOGIN_URL")

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
# Optional if you want to run headless mode
chrome_options.add_argument("--headless")

# Initialize the Chrome driver with the service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

print("Opening Bing login page...")

# Go to Bing login page
driver.get(bing_login_url)

# Log in with your credentials
email_field = driver.find_element(By.NAME, 'loginfmt')
email_field.send_keys(bing_email)
email_field.send_keys(Keys.RETURN)
time.sleep(2)

print("Email entered, proceeding to password...")

password_field = driver.find_element(By.NAME, 'passwd')
password_field.send_keys(bing_password)
password_field.send_keys(Keys.RETURN)
time.sleep(2)

print("Successfully logged in!")

# Optional: Handle any 2FA or additional security prompts here if needed
# Example: you may need to handle security questions or input a code

print("Navigating to Bing search page...")

# Navigate to Bing search page
driver.get('https://www.bing.com')

# Perform 40 random searches
search_terms = [
    "AI news", "Python tutorials", "Best tech blogs", "ChatGPT updates",
    "Data science trends", "Machine learning tools", "Blockchain technology",
    "Cybersecurity tips", "Quantum computing", "Cloud computing benefits",
    "Deep learning", "Natural language processing", "Artificial intelligence",
    "Neural networks", "AI applications", "Data mining", "Big data",
    "AI ethics", "Self-driving cars", "AI startups", "Tech innovations",
    "Robotics", "Augmented reality", "Virtual reality", "Generative AI",
    "AI regulations", "GPT models", "AI research papers", "AI development",
    "Machine learning applications", "AI jobs", "Automation in industries",
    "Ethical AI development", "Future of AI", "Tech companies to watch",
    "AI and health", "AI in education", "AI for social good"
]

for i in range(5):
    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.clear()

    # Choose a random search term
    random_search = random.choice(search_terms)
    print(f"Search {i+1}/40: Searching for '{random_search}'...")
    search_bar.send_keys(random_search)
    search_bar.send_keys(Keys.RETURN)

    # Wait for a few seconds to simulate human behavior
    time.sleep(random.randint(3, 7))

    # Navigate back to Bing for the next search
    driver.get('https://www.bing.com')

    print(f"Search {i+1}/40 completed.")


# Close the browser when done
driver.quit()
