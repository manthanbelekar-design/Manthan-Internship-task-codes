from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# -------------------------------
# Create Edge browser instance
# -------------------------------
driver = webdriver.Edge()

# Maximize browser window
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Wait for page to load
time.sleep(2)

# Accept cookies if the button appears
try:
    accept = driver.find_element(By.XPATH, "//button[contains(.,'Accept all')]")
    accept.click()
    time.sleep(2)
except:
    pass

# -------------------------------
# Search your name
# -------------------------------
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Manthan Belekar")
search_box.send_keys(Keys.RETURN)

# Wait for search results
time.sleep(5)

# -------------------------------
# Display page information
# -------------------------------
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# Verify search results
if "Manthan Belekar" in driver.page_source:
    print("Search completed successfully!")
else:
    print("Search text not found in page source.")

# Keep browser open until user presses Enter
input("\nPress Enter to close the browser...")

# Close browser
driver.quit()