# manipulates sales_data.txt

with open('sales_data.txt') as f:
    cleaned_data = clean_up(f)
    cleanded_data[:4]

 
"""
-*- .split vs .replace -*-
- replace creates strings
- split creates a list full of strings
"""

def clean_up(raw_data):
    cleaned_lines = []

    for line in raw_data:
        cleaned_line = line.replace('$', '')
        cleaned_line = cleaned_line.replace('\n', '')

        # split the line into a list
        cleaned_line = cleaned_line.split('\t')

        cleaned_line[3] = float(cleaned_line[3]) 

        cleaned_lines.append(cleaned_line)

    return cleaned_lines

