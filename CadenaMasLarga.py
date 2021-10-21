
def longest_string(arr: list) -> dict:
    max_length = 0
    string = ""
    index = -1
    for i in range(len(arr)):
        if len(arr[i]) > max_length:
            max_length = len(arr[i])
            string = arr[i]
            index = i
    return {"index": index, "string": string, "len": max_length}

array_str = ["platzi", "master", "palabra más larga", "corta", "backend", "code", "casi más larga"]
print(longest_string(array_str))