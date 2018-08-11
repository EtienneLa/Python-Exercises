while True:
    try:
        number = int(input("What's your fav number?\n"))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number.")
    except ZeroDivisionError:
        print("Do not pick zero.")
    except:
        break
    finally:
        print("Loop complete!")
