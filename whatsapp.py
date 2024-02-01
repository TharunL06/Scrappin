from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_whatsapp(phone_number):
    options = Options()
    # Remove headless mode for debugging
    # options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    whatsapp_url = f'https://web.whatsapp.com/send?phone={phone_number}'
    
    driver.get(whatsapp_url)
    
    try:
        # Waiting for QR code scan
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.CLASS_NAME, '_1awRl')))
        registration_status = "Yes"
    except:
        registration_status = "No"

    name = status = last_seen = "N/A"
    
    if registration_status == "Yes":
        try:
            # Waiting for contact info to load
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, '_19vo_')))
            name = driver.find_element_by_class_name('_19vo_').text
            status = driver.find_element_by_class_name('_315-i').text
            last_seen = driver.find_element_by_class_name('_315-i').text
        except Exception as e:
            print("Error:", e)

    driver.quit()
    
    output = {
        'Platform': 'WhatsApp',
        'Registered': registration_status,
        'Name': name,
        'Status': status,
        'Last Seen': last_seen
    }
    return output

phone_numbers = ["+91 8268291167", "+91 9867913757", "+91 8779278482"]

for number in phone_numbers:
    whatsapp_data = scrape_whatsapp(number)
    print("\nWhatsApp Data:")
    print(whatsapp_data)
    time.sleep(5)  # Adding a delay between scraping attempts to avoid potential issues
