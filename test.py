from playwright.sync_api import sync_playwright
import uuid 
import os

password = os.getenv('MY_PASSWORD')
email = os.getenv('MY_PASSWORD')

if email is None:
    raise EnvironmentError("email environment variable is not set")

if password is None:
    raise EnvironmentError("password environment variable is not set")

EMAIL = email
PASSWORD = password

CHROME_PATH = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"  # adjust if needed

with sync_playwright() as p:
    browser = p.chromium.launch(executable_path=CHROME_PATH, headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to Sully login page
    page.goto("https://app.sully.ai/")

    # Step 1: Enter email
    page.fill('input[name="email"]', EMAIL)
    
    # Step 2: Enter password
    page.fill('input[type="password"]', PASSWORD)

    # At this point, you are on the Sully.ai page
    page.click('button[type="submit"]')

    page.click('button[aria-label="Close"]' , force = True)

    # Wait for the input to be visible
    page.wait_for_selector('input[placeholder="Search or create patient..."]')

    # Fill the input field
    #Create a new Patient 
    patient = str(uuid.uuid4())
    page.fill('input[placeholder="Search or create patient..."]', patient)
    #Press Enter to create the patient
    page.keyboard.press("Enter")

    page.wait_for_load_state("networkidle")

    
    # Close browser or continue
    browser.close()

