from costs import *
from ops import *
FILE = "list.json"
UNDO = "undo.json"
REDO = "redo.json"


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
    print("10) Afisare cheltuieli")
    print("11) REDO")


def print_type():
    print("The new cost type is:")
    print("    a) maintenance")
    print("    b) sewage")
    print("    c) other")


def main():
    costs = []
    prevList = []
    listRedo = []
    save_list_json(prevList, UNDO)
    save_list_json(listRedo, REDO)
    costs = load_list_json(FILE)
    prevList.append(costs)
    save_list_json(prevList, UNDO)
    undo = 0
    redo = 0
    sem = True
    while sem:
        print_menu()
        opt = input("\n My option is: ")
        if opt == "1":
            try:
                apartment_number = int(input("\n Apartment number= "))
            except ValueError:
                print("Value error: the apartment number is not int")
            else:
                try:
                    sum_of_money = float(input(" The sum of money= "))
                except ValueError:
                    print("Value error: the sum of money is rational")
                else:
                    date = input(" Date= ")
                    print_type()
                    option = input("Choose one option: ")
                    if option == "a":
                        cost_type = "maintenance"
                    elif option == "b":
                        cost_type = "sewage"
                    elif option == "c":
                        cost_type = "other"
                    else:
                        cost_type = "other"
                    foo(costs, UNDO)
                    cost = create_cost_str(apartment_number, sum_of_money, date, cost_type)
                    costs = add_cost(costs, cost, FILE)
                    undo += 1
                    redo = 0
                    save_list_json([], REDO)
                    foo(costs, UNDO)
        elif opt == "2":
            try:
                apartment_number = int(input("\n write the apartment number you want to delete the costs from"))
            except ValueError:
                print("Value error: the apartment number is not int")
            else:
                date = input("write the date associated with the cost")
                try:
                    undo += 1
                    redo = 0
                    save_list_json([], REDO)
                    foo(costs, UNDO)
                    delete_cost(apartment_number, date, costs, FILE)
                except AttributeError as e:
                    print(e)

        elif opt == "3":
            try:
                apartment_number = int(input("\n The apartment number of the cost you want to modify= "))
            except ValueError:
                print("Value error: the apartment number is not int")
            else:
                try:
                    sum_of_money = float(input(" The new sum of money= "))
                except ValueError:
                    print("Value error: the sum of money is rational")
                else:
                    date = input(" New Date= ")
                    print_type()
                    option = input("Choose one option: ")
                    if option == "a":
                        cost_type = "maintenance"
                    elif option == "b":
                        cost_type = "sewage"
                    elif option == "c":
                        cost_type = "other"
                    else:
                        cost_type = "other"
                    try:
                        undo += 1
                        redo = 0
                        save_list_json([], REDO)
                        foo(costs, UNDO)
                        modify_cost(costs, apartment_number, sum_of_money, date, cost_type, FILE)
                    except Exception as e:
                        print(e)
        elif opt == "4":
            try:
                apartment_number = int(input("\n The apartment number of the costs you want to delete= "))
            except ValueError:
                print("Value error: the apartment number is not int")
            else:
                try:
                    undo += 1
                    redo = 0
                    save_list_json([], REDO)
                    foo(costs, UNDO)
                    delete_costs(apartment_number, costs, FILE)
                except AttributeError as e:
                    print(e)
        elif opt == "5":
            date = input("\n write the date in which you want to increase the sum of money")
            try:
                value = float(input("the value you want to add to the cost"))
            except ValueError:
                print("Value error: the sum of money is rational")
            else:
                try:
                    undo += 1
                    redo = 0
                    save_list_json([], REDO)
                    foo(costs, UNDO)
                    add_value(date, value, costs, FILE)
                except Exception as e:
                    print(e)
        elif opt == "6":
            foo(costs, UNDO)
            undo += 1
            redo = 0
            save_list_json([], REDO)
            foo(costs, UNDO)
            lists = ord_costs(costs, FILE)
            print("the list was ordered")
            print(lists)
        elif opt == "7":
            d = costs_by_date(costs)
            print(d)
        elif opt == "8":
            if undo > 0:
                prevList = load_list_json(UNDO)
                listRedo = prevList.pop()
                costs = prevList[-1]
                prevList.pop()
                save_list_json(prevList, UNDO)
                save_list_json(costs, FILE)
                foo(listRedo, REDO)
                undo -= 1
                redo += 1
            else:
                print("nu se poate efectua comanda undo")
                # costs = load_list_json(UNDO)
                # save_list_json(costs, FILE)
        elif opt == "9":
            sem = False
        elif opt == "10":
            for i in range(len(costs)):
                print("cheltuiala nr ", i, ":    ", costs[i])
        elif opt == "11":
            if redo > 0:
                prevList = load_list_json(REDO)
                listRedo = prevList.pop()
                costs = listRedo
                save_list_json(prevList, REDO)
                save_list_json(costs, FILE)
                foo(costs, UNDO)
                undo += 1
                redo -= 1
            else:
                print("nu se poate efectua comanda redo")
            for cost in costs:
                print(cost)
        else:
            print("invalid Command!")

main()

