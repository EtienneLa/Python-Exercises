def get_gender(sex="Unknown"): #setting a default value
    if sex is "m":
        sex = "male"
    elif sex is "f":
        sex = "female"
    print(sex)


get_gender("m")
get_gender("f")
get_gender()
