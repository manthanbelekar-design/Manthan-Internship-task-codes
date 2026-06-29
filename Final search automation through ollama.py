import ollama
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# -------------------------------
# Step 1: Send command to Ollama
# -------------------------------
prompt = "Search Manthan Belekar on Google"

response = ollama.chat(
    model="llama3",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("Ollama Response:")
print(response["message"]["content"])

# -------------------------------
# Step 2: Open browser using Selenium
# -------------------------------
driver = webdriver.Edge()

# Maximize browser
driver.maximize_window()

# -------------------------------
# Step 3: Open Google
# -------------------------------
driver.get("https://www.google.com")

time.sleep(2)

# -------------------------------
# Step 4: Search your name
# -------------------------------
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Manthan Belekar")
search_box.send_keys(Keys.RETURN)

time.sleep(5)

# -------------------------------
# Step 5: Verify results page loaded
# -------------------------------
print("\nGoogle Search Completed!")
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

if "Manthan Belekar" in driver.page_source:
    print("Search results displayed successfully.")
else:
    print("Search verification failed.")

# -------------------------------
# Step 6: Keep browser open
# -------------------------------
input("\nPress Enter to close browser...")

driver.quit()