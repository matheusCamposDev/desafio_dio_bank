from operations.operations import deposit, withdrawal, statement_print
from utils.menu import menu
from utils.operation_messages import FAIL_ERR_INVALID_OPERATION

while True:

    option = input(menu).lower()

    if option == "d":
        deposit()
    elif option == "s":
        withdrawal()
    elif option == "e":
        statement_print()
    elif option == "q":
        break
    else:
        print(FAIL_ERR_INVALID_OPERATION)
