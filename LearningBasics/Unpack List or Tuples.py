item_list = ["December 24, 2016", "Cool Gloves", 8.51]
date, name, price = ["June 13m 2018", "Better Gloves", 8.42]


def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)


drop_first_last([65, 213, 33, 23, 21])
drop_first_last([1, 2, 2, 2, 2, 2, 1])
