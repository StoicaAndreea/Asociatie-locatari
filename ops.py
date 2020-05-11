from costs import *
import json
FILE = "list.json"


def foo(newList, fileName):
    prevList = load_list_json(fileName)
    prevList.append(newList)
    save_list_json(prevList, fileName)


def test_add_cost():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    assert len(costs) == 1
    assert get_apartment_number(costs[0]) == 1
    assert get_sum_of_money(costs[0]) - 57.5 < 0.001
    assert get_date(costs[0]) == "31.05.2001"
    assert get_cost_type(costs[0]) == "sewage"


def add_cost(costs, cost, FILE):
    """
    adds a new cost to the costs list
    :param costs: a list of dictionaries
    :param cost: dictionary, contains informations about a cost
    """
    costs.append(cost)
    save_list_json(costs, FILE)
    return costs


def test_delete_cost():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    assert len(costs) == 1
    delete_cost(1,"31.05.2001", costs, FILE)
    assert len(costs) == 0


def delete_cost(apartment_number, date,  costs, FILE):
    """
    deletes a cost from the costs list
    :param apartment_number: the apartment number
            date: the date
    :param costs: list, a list of dictionaries
    :return:
    """
    ok = 0
    for i in range(len(costs)):
        if get_apartment_number(costs[i]) == apartment_number and get_date(costs[i]) == date:
            del costs[i]
            ok = 1
            save_list_json(costs, FILE)
            break
    if ok == 0:
        raise AttributeError("there is no cost with the specified date and apartment number!")


def test_delete_costs():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    cost = create_cost_str(1, 55.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    cost = create_cost_str(3, 55.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    cost = create_cost_str(1, 57.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    assert len(costs) == 4
    delete_costs(1, costs, FILE)
    assert len(costs) == 1


def delete_costs(apartment_number, costs, FILE):
    """
        deletes all the costs from an apartment
        :param apartment_number: the apartment number
        :param costs: list, a list of dictionaries
        :return:
        """
    i = 0
    ok = 0
    while i != len(costs):
        if get_apartment_number(costs[i]) == apartment_number:
            del costs[i]
            ok += 1
        else:
            i += 1
    if ok == 0:
        raise AttributeError("there is no cost with the specified apartment number!")
    save_list_json(costs, FILE)


def test_modify_cost():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    modify_cost(costs, 1, 23.3, "20.03.2012", "other", FILE)
    assert get_apartment_number(costs[0]) == 1
    assert (get_sum_of_money(costs[0]) - 23.3) < 0.001
    assert get_date(costs[0]) == "20.03.2012"
    assert get_cost_type(costs[0]) == "other"


def modify_cost(costs, apartment_number, new_sum_of_money, new_date, new_cost_type, FILE):
    """
    modifies a cost
    :param costs: list od dictionaries
    :param apartment_number: int, the apartment number
    :param new_sum_of_money: float,  the new amount of money an apatment has to pay
    :param new_date: string,  the new date
    :param new_cost_type: string, cost type: maintenance, sewage, other
    """
    ok = 0
    for i in range(len(costs)):
        if get_apartment_number(costs[i]) == apartment_number:
            costs[i] = set_sum_of_money(costs[i], new_sum_of_money)
            costs[i] = set_date(costs[i], new_date)
            costs[i] = set_cost_type(costs[i], new_cost_type)
            ok = 1
            break
    if ok == 0:
        raise AttributeError("nu exista nici un apartament cu numarul dat")
    save_list_json(costs, FILE)


def test_add_value():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    cost = create_cost_str(1, 55.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    cost = create_cost_str(3, 50.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    assert (get_sum_of_money(costs[0]) - 57.5) < 0.001
    assert (get_sum_of_money(costs[1]) - 55.5) < 0.001
    assert (get_sum_of_money(costs[2]) - 50.5) < 0.001
    add_value("31.05.2089", 2, costs, FILE)
    assert (get_sum_of_money(costs[0]) - 57.5) < 0.001
    assert (get_sum_of_money(costs[1]) - 57.5) < 0.001
    assert (get_sum_of_money(costs[2]) - 52.5) < 0.001


def add_value(date, value, costs, FILE):
    """
    adds a value to a sum of money registeren in a date
    :param date: string
    :param value: float
    :param costs: a list
    :return:
    """
    ok = 0
    for i in range(len(costs)):
        if get_date(costs[i]) == date:
            new_sum_of_money = get_sum_of_money(costs[i]) + value
            costs[i] = set_sum_of_money(costs[i], new_sum_of_money)
            ok = 1
    if ok == 0:
        raise AttributeError("nu exista nici o cheltuiala inregistrata pe aceasta data")
    save_list_json(costs, FILE)


def load_list_json(FILE):
    try:
        with open(FILE, "r") as f_read:
            line = f_read.readline()
            return json.loads(line)
    except FileNotFoundError:
        list = []
        return list


def save_list_json(list, FILE):
    with open(FILE, "w") as f_write:
        f_write.write(json.dumps(list))


def ord_costs(costs, FILE):
    """
    orders a list descending by the sum of money
    :param costs: a list of costs
    :return: list: a list of costs in a descending order
    """
    list = []
    list = sorted(costs, key = get_sum_of_money)
    list.reverse()
    save_list_json(list, FILE)
    return list


def test_ord_costs():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    add_cost(costs, cost, FILE)
    cost = create_cost_str(1, 58.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    cost = create_cost_str(3, 50.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    list = ord_costs(costs, FILE)
    assert get_apartment_number(list[0]) == 1
    assert get_apartment_number(list[2]) == 3


def costs_by_date(costs):
    """
    odrerd the costs in a descending order
    :param costs:
    :return:
    """
    d_dict = {}
    for cost in costs:
        date = get_date(cost)
        if date in d_dict:
            d_dict[date].append(cost)
        else:
            d_dict[date] = [cost]
    return d_dict

def test_costs_by_date():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    costs = []
    cost = create_cost_str(1, 58.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    cost = create_cost_str(3, 50.5, "31.05.2089", "other")
    add_cost(costs, cost, FILE)
    d = costs_by_date(costs)
    assert get_apartment_number(d["31.05.2089"][0]) == 1
    assert get_apartment_number(d["31.05.2089"][1]) == 3
    assert get_date(d["31.05.2089"][0]) == "31.05.2089"


test_costs_by_date()
test_modify_cost()
test_delete_cost()
test_delete_costs()
test_add_cost()
test_add_value()
test_ord_costs()