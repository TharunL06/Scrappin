from selenium import webdriver;
from selenium.webdriver.chrome.options import Options;


def scrape_whatsapp(phone_number):
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    
    whatsapp_url = f'https://web.whatsapp.com/send?phone={phone_number}'
    
    driver.get(whatsapp_url)
    driver.implicitly_wait(10)
    
    registration_status = "Yes" if "window.Parse_APP_DATA" in driver.page_source else "No"
    name = driver.find_element_by_class_name('_3TEwt').text
    status = driver.find_element_by_class_name('_315-i').text
    last_seen = driver.find_element_by_class_name('_1xJ3z').text
    
    
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

    