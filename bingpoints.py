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
from termcolor import colored  # Import termcolor for colored prints

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

# Purple print for welcome message
print(colored("... Welcome to AutoBingSearch Points Bot ...", "magenta"))

# Purple print for opening the Bing login page
print(colored("Opening Bing login page...", "magenta"))

# Go to Bing login page
driver.get(bing_login_url)

# Log in with your credentials
email_field = driver.find_element(By.NAME, 'loginfmt')
email_field.send_keys(bing_email)
email_field.send_keys(Keys.RETURN)
time.sleep(2)

# Purple print for email entry
print(colored("Email entered, proceeding to password...", "magenta"))

password_field = driver.find_element(By.NAME, 'passwd')
password_field.send_keys(bing_password)
password_field.send_keys(Keys.RETURN)
time.sleep(2)

# Green print for successful login
print(colored("Successfully logged in!", "green"))

# Purple print for navigating to Bing search page
print(colored("Navigating to Bing search page...", "magenta"))

# Navigate to Bing search page
driver.get('https://www.bing.com')
time.sleep(15)


# Perform 40 random searches
search_terms = [
    "CapiSys AI news", "CapiSys Python tutorials", "CapiSys Best tech blogs", "CapiSys ChatGPT updates",
    "CapiSys Data science trends", "CapiSys Machine learning tools", "CapiSys Blockchain technology",
    "CapiSys Cybersecurity tips", "CapiSys Quantum computing", "CapiSys Cloud computing benefits",
    "CapiSys Deep learning", "CapiSys Natural language processing", "CapiSys Artificial intelligence",
    "CapiSys Neural networks", "CapiSys AI applications", "CapiSys Data mining", "CapiSys Big data",
    "CapiSys AI ethics", "CapiSys Self-driving cars", "CapiSys AI startups", "CapiSys Tech innovations",
    "CapiSys Robotics", "CapiSys Augmented reality", "CapiSys Virtual reality", "CapiSys Generative AI",
    "CapiSys AI regulations", "CapiSys GPT models", "CapiSys AI research papers", "CapiSys AI development",
    "CapiSys Machine learning applications", "CapiSys AI jobs", "CapiSys Automation in industries",
    "CapiSys Ethical AI development", "CapiSys Future of AI", "CapiSys Tech companies to watch",
    "CapiSys AI and health", "CapiSys AI in education", "CapiSys AI for social good",
    "CapiSys AI impact on society", "CapiSys AI for beginners", "CapiSys AI conferences 2024", 
    "CapiSys AI startups 2024", "CapiSys AI funding", "CapiSys AI projects", "CapiSys Data visualization tools", 
    "CapiSys Data engineering", "CapiSys AI and machine learning", "CapiSys Top AI courses", 
    "CapiSys AI-powered apps", "CapiSys AI for business", "CapiSys AI in finance", "CapiSys AI innovations", 
    "CapiSys AI automation tools", "CapiSys AI for healthcare", "CapiSys AI industry news", 
    "CapiSys AI tools for developers", "CapiSys Tech startups", "CapiSys AI writing tools", 
    "CapiSys AI for marketing", "CapiSys AI in retail", "CapiSys AI-driven research", "CapiSys AI content creation", 
    "CapiSys AI breakthroughs", "CapiSys AI in agriculture", "CapiSys AI cloud services", "CapiSys AI chatbots", 
    "CapiSys AI productivity tools", "CapiSys AI in security", "CapiSys AI talent acquisition", 
    "CapiSys AI in automation", "CapiSys AI in transportation", "CapiSys AI tools comparison", 
    "CapiSys Future of work with AI", "CapiSys AI platform reviews", "CapiSys AI-powered solutions", 
    "CapiSys AI for e-commerce", "CapiSys AI-driven analytics", "CapiSys Ethical AI practices", 
    "CapiSys Top AI frameworks", "CapiSys AI for mobile apps", "CapiSys AI coding tools", 
    "CapiSys AI in government", "CapiSys AI models 2024", "CapiSys Future of machine learning", 
    "CapiSys AI for legal", "CapiSys Open-source AI", "CapiSys Top AI innovations", 
    "CapiSys AI learning resources", "CapiSys AI and education", "CapiSys AI-driven diagnostics", 
    "CapiSys AI-enhanced tools", "CapiSys AI future predictions", "CapiSys AI in media", 
    "CapiSys AI for content marketing", "CapiSys AI for startups", "CapiSys AI use cases", 
    "CapiSys AI-powered assistants", "CapiSys AI in art", "CapiSys AI research trends", 
    "CapiSys AI in the public sector", "CapiSys AI in tech"
]

search_counter = 0
while search_counter < len(search_terms):
    # Perform 3 searches
    for i in range(3):
        if search_counter >= len(search_terms):
            break
        search_term = search_terms[search_counter]
        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()

        # Purple print for search status
        print(colored(f"Search {search_counter+1}: Searching for '{search_term}'...", "magenta"))
        
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.RETURN)

        # Wait for 7 seconds between each search to simulate human-like behavior
         # Wait for a few seconds to simulate human behavior
        time.sleep(random.randint(5, 9))

        # Navigate back to Bing for the next search
        driver.get('https://www.bing.com')

        # Green print for search completion
        print(colored(f"Search {search_counter+1} completed.", "green"))

        search_counter += 1

    # Wait 18 minutes before performing the next batch of 3 searches
    print(colored("Waiting for 18 minutes before the next batch of searches...", "yellow"))
    time.sleep(18 * 60)

# Close the browser when done
driver.quit()