def single_image(input_list, max_size):
    if max_size[-2:] == "KB":
        new_size = int(max_size[:-2]) * (10**3)
    elif max_size[-2:] == "MB":
        new_size = int(max_size[:-2]) * (10**6)
    elif max_size[-2:] == "GB":
        new_size = int(max_size[:-2]) * (10**9)

    new_list = []
    for i in input_list:
        url, size = i[0], int(i[1])
        new_i = []
        new_i.append(url)
        print(size, new_size)
        if size < new_size:
            new_i.append("TRUE")
        else:
            new_i.append("FALSE")
        new_list.append(new_i)
    return new_list
