import re
n = int(input())

pattern = r'^@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+'
pattern_2 = r'\d+'

for i in range(n):
    barcode = input()
    barcode.strip()
    valid_barcode = re.finditer(pattern, barcode)
    valid_barcode_list = [match.group() for match in valid_barcode]
    if len(valid_barcode_list) > 0:
        product_group = re.findall(pattern_2, barcode)
        if len(product_group) > 0:
            print(f"Product group: {''.join(product_group)}")
        else:
            print(f"Product group: 00")
    else:
        print("Invalid barcode")
