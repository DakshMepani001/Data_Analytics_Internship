#Filtering unique value or non-nagitive values from a given list 

def clean_data(data):
    # Remove duplicates
    unique_data = list(set(data))

    # Keep only positive numbers
    filtered_data = []

    for num in unique_data:
        if num > 0:
            filtered_data.append(num)

    return filtered_data


data = [10, -5, 20, 10, 30, -2, 20, 40]

cleaned_data = clean_data(data)

print("Original Data:", data)
print("Cleaned Data:", cleaned_data) # because of set output comes into defferent order than original list.