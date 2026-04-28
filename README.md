this repo uses a python script to clean the sku numbers from an excel/csv file and prepare it for the main script (msds.py).
the main script uses a format string and the requests module to hit the public api of PPG to find product safety data sheets via sku.

the script can be edited to query their api with "contains ___" or region/language of the sheet. this was tested but I did not include it in the final script due to those options being out of scope for the task at hand.
