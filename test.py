def increment_string(strng):
    stri = list(strng)
    num_list = []
    str_list = []
    for i in stri:
        if i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            num_list.append(i)
        else:
            str_list.append(i)


    if num_list == []:
        if str_list[-1] == "0":
            strng = strng[:-1]
            return strng + "1"
        else:
            return strng + "1"
    num_str_before = "".join(num_list)
    num_before_length = len(num_str_before)
    num = int(num_str_before) + 1
    num_str_after = str(num)
    num_str_after_length = len(num_str_after)
    if num_before_length == num_str_after_length:
        str_list.append(num_str_after)
        return "".join(str_list)
    else:
        if str_list[-1] == "0":
            str_list = str_list[:-1]
        str_list.append(num_str_after)
        return "".join(str_list)


print(increment_string("foobar001"))


