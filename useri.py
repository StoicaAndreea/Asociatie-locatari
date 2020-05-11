from costs import *
from ops import *

def print_menu():
    print("1) Adaugare cheltuiala")
    print("2) Stergere cheltuiala")
    print("3) Modificare cheltuiala")
    print("4) Stergerea tuturor cheltuielilor pentru un apartament dat")
    print("5) Adunarea unei valori la toate cheltuielile dintr-o data citita")
    print("6) Ordonarea cheltuielilor descrescator dupa suma")
    print("7) Afisarea sumelor lunare pentru fiecare apartament")
    print("8) UNDO")
    print("9) IESIRE")


def print_type():
    print("The new cost type is:")
    print("    a) maintenance")
    print("    b) sewage")
    print("    c) other")


def delete_spaces(date):
    """for x in date:
        for i in range(len(x)):
            if x[i] == " ":
                del x[i]
                """
    while ("" in date):
        date.remove("")
    for x in date:
        while ("" in x):
            x.remove("")
    return date

def main():
    costs = []
    print_menu()
    sem = True
    date = []
    opt = []
    while sem:
        print("tastati lista")
        opt = [x for x in input().split(";")]
        for x in opt:
                date.append(x.split(" "))
        date = delete_spaces(date)
        print(opt, date)
        for x in date:
                if x[0] == "add":
                    try:
                        x[1] = int(x[1])
                    except ValueError:
                        print("the apartment number is natural")
                    else:
                        try:
                            x[2] = float(x[2])
                        except ValueError:
                                print("the sum of money is rational")
                        else:
                            cost = create_cost(x[1], x[2], x[3], x[4])
                            add_cost(costs, cost)
                elif x[0] == "modify":
                    try:
                        x[1] = int(x[1])
                    except ValueError:
                        print("the apartment number is natural")
                    else:
                        try:
                            x[2] = float(x[2])
                        except ValueError:
                            print("the sum of money is rational")
                        else:
                            modify_cost(costs, x[1], x[2], x[3], x[4])
                elif x[0] == "delete":
                    try:
                        x[1] = int(x[1])
                    except ValueError:
                        print("the value needs to be rational")
                    else:
                        delete_costs(x[1], costs)
        print(costs)
        yup = input("mai doriti? da/nu")
        if yup == "nu":
            sem = False

main()
