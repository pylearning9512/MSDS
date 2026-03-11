import time
import random
import os
import glob
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


#WARNING: i made this script to be run once when scraping the entire list of products, if you run it twice it will overwrite the old files in the MSDS folder

#made it with dynamic path so it can be run anywhere and will make an MSDS folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "MSDS")

#checks for directory:
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

sku_input = input("please enter your product id(s) separated by comma: \n")
sku_list = sku_input.split(",")

options = Options()
prefs = {
    "download.default_directory": DOWNLOAD_DIR,
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True,
    "download.directory_upgrade": True
}
options.add_experimental_option("prefs", prefs)
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service(ChromeDriverManager(driver_version="145.0.7632.159").install())
driver = webdriver.Chrome(service=service, options=options)

for i in sku_list:
    i = i.strip() # Clean whitespace
    url = f"https://buyat.ppg.com/EHSDocumentManagerPublic/documentSearchInnerFrame.aspx?NameCondition=BeginsWith&NameValue=&CodeCondition=Contains&CodeValue={i}&CompCondition=Contains&CompValue=&Form=5a6203a3352c2bce0000&SortBy=ProductName&Language=es-MX&SBU=&From=&To=&SuppressSearchControls=False&AlwaysShowSearchResults=False&PageSize=20&FolderID1=0&FolderID2=0&FolderID3=0&FolderID4=0&FolderID5=0&FolderID6=0&FolderID7=0&FolderID8=0&FolderID9=0&FolderID10=0&SearchAllPublicFolders=True"
    
    print(f"Processing SKU: {i}")
    driver.get(url)
    
    # Wait for download
    time.sleep(random.randint(5, 8)) 
    
    # Check for .crdownload files (still downloading)
    while glob.glob(f"{DOWNLOAD_DIR}/*.crdownload"):
        time.sleep(1)

    # Identify the latest PDF file
    list_of_files = glob.glob(f"{DOWNLOAD_DIR}/*.pdf")
    if list_of_files:
        latest_file = max(list_of_files, key=os.path.getctime)
        new_name = os.path.join(DOWNLOAD_DIR, f"{i}.pdf")
        
        # Handle case where file already exists
        if os.path.exists(new_name):
            os.remove(new_name)
            
        shutil.move(latest_file, new_name)
        print(f"Successfully saved as: {i}.pdf")
    else:
        print(f"No PDF found for SKU: {i}")

driver.quit()
print("Process finished.")