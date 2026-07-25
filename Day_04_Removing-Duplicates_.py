orignal_list = ['apple','banana','apple','orange','banana']
seen = set()
unique_items = []
for item in orignal_list:
    if item not in seen:
        seen.add(item)
        unique_items.append(item)
print(unique_items)
    
    
