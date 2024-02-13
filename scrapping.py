import urllib

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')

start_time = time.time()

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
          "Georgia",
          "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada",
          "New Hampshire",
          "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon",
          "Pennsylvania",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia",
          "Washington",
          "West Virginia", "Wisconsin", "Wyoming"]


# Global counter for image numbering
global_image_counter = 0


def scroll():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def download(query, max_images=1000):
    global global_image_counter  # Access the global counter

    if global_image_counter >= max_images:
        print(f"Reached the maximum limit of {max_images} images for {state}. Skipping further downloads.")
        return

    search_query = f"{state} {query}"
    # url = f"https://www.google.com/search?q={search_query}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568"
    url = f"https://www.google.com/search?tbm=isch&q={search_query}"
    # Launch the browser and open the given url in the webdriver.
    driver.get(url)

    scroll()

    img_results = driver.find_elements(By.XPATH, "//img[contains(@class,'Q4LuWd')]")

    # Access and store the src list of image URLs.
    src = []
    for img in img_results:
        img_url = img.get_attribute('src')
        if img_url:
            src.append(img_url)

    # Create the download folder for the current state if it doesn't exist
    download_folder = f"sample_data/{state}"
    os.makedirs(download_folder, exist_ok=True)

    # Retrieve and download the images for the current state.
    for img_url in src:
        try:
            image_path = os.path.join(download_folder, f"{state}_{global_image_counter:04d}.jpg")
            urllib.request.urlretrieve(img_url, image_path)
            print(f"Downloaded: {image_path}")
            global_image_counter += 1  # Increment the global counter
        except Exception as e:
            print(f"Failed to download image for {state}: {str(e)}")


# Iterate over each state
for state in states:
    download("landscape")
    download("urban landscapes")
    download("scenic views")
    download("tourist attraction")
    download("beautiful places")
    download("state parks")
    download("historical sites")

    global_image_counter = 0

driver.quit()

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Total execution time: {elapsed_time / 60} minutes")
