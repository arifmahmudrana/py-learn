def sum(num1, num2):
    try:
        num1/num2
        # return num1/num2 # if I just return else is useless
    except (TypeError, ZeroDivisionError) as err:
        print(err)
        raise Exception('Sorry, no numbers below zero')
    except Exception as err:
        print(err)
    else:
        print('Else printed')
    finally:
        print('finally printed')

    return 'All done'


# sum(1, 0)
# sum(1, 'a')
sum(1, 1)
