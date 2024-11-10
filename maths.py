import numpy as np

data = [2, 3, 5, 4]
index = ['a', 'b', 'c', 'd']

# Create a structured array to mimic a Series
dtype = [('index', 'U1'), ('data', 'i4')]
structured_array = np.array(list(zip(index, data)), dtype=dtype)


def print_structured_array(arr):
    print("index  data")
    for item in arr:
        print(f"{item['index']}     {item['data']}")


print_structured_array(structured_array)

 # i love sam
