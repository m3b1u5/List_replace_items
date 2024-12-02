# ДЗ: Замена элементов списка


def main():
    my_list = ["string1", "string2", "string3", "string4", "string5"]

    print(my_list)

    my_list[0], my_list[len(my_list) - 1] = my_list[len(my_list) - 1], my_list[0]

    print(my_list)


main()
