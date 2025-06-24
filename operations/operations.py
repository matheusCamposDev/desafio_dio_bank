from utils.operation_messages import *

balance = 0
limit = 500
statement = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3

def deposit():
    global balance, statement

    valor = float(input(MSG_ENTER_DEPOSIT_AMOUNT))

    if valor > 0:
        balance += valor
        statement += f"Depósito: R$ {valor:.2f}\n"

    else:
        print(FAIL_INVALID_OPERATION)

def withdrawal():
    global balance, statement, withdrawal_count
    valor = float(input(MSG_ENTER_WITHDRAWAL_AMOUNT))

    excedeu_saldo = valor > balance

    excedeu_limite = valor > limit

    excedeu_saques = withdrawal_count >= WITHDRAWAL_LIMIT

    if excedeu_saldo:
        print(FAIL_INSUFFICIENTE_FUNDS)

    elif excedeu_limite:
        print(FAIL_WITHDRAWAL_AMOUNT_EXCEEDS_LIMIT)

    elif excedeu_saques:
        print(FAIL_ERR_MAX_WITHDRAWALS_REACHED)

    elif valor > 0:
        balance -= valor
        statement += f"Saque: R$ {valor:.2f}\n"
        withdrawal_count += 1

    else:
        print(FAIL_ERR_INVALID_AMOUNT)

def statement_print():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")