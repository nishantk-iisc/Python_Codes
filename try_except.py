## Handling Exceptions
## To make the program more robust, you need to handle the exception once it occurs. In other words, you need to catch exception and inform the users so that they can fix it.
## So what the python interpreter returns. Insted, you replace the error message with a more user-friendly one.
## try...except
# CODE
try:
    print('Enter the net sales for')
    
    previous = float(input('-- Prior Period: '))
    current = float(input('-- Current Period: '))

    change = (current - previous)*100 / previous

    if change > 0:
        result = f"sales increase {abs(change)}%"
    else:
        result = f"sales decrease {abs(change)}%"

    print(result)

except ValueError:
    print('error! please enter a number for net sales.')

except ZeroDivisionError:
    print('error! the prior net sales cannot be zero.')
except Exception as error:
    print(error)
finally:
    # the code is always executes
    print("Finishing..")
