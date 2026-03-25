import csv
import re

"this script uses regex to clean the sku's from the file andrea sent me"'

def extract_skus(input_file, output_file):

    sku_pattern = re.compile(r'\b[a-zA-Z]{0,2}\d{4,8}\b')
    
    skus = []

    try:
        with open(input_file, mode='r', encoding='utf-8-sig') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                
                # Check Column A
                cell_content = str(row[0]).strip()
                match = sku_pattern.search(cell_content)
                
                if match:
                    skus.append(match.group())

        # Save to TXT
        with open(output_file, mode='w', encoding='utf-8') as f:
            f.write(", ".join(skus))
            
        print(f"Success! {len(skus)} SKUs saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

# Usage - updated to match folder structure
extract_skus('c:/Users/siste/Desktop/MSDS/products.csv', 'skus.txt')