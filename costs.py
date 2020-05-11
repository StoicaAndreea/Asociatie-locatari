"""
def test_create_cost():
    cost = create_cost(1, 57.5, "31.05.2001", "sewage")
    assert len(cost) == 4
    assert cost["apartment_number"] == 1
    assert (cost["sum_of_money"] - 57.5) < 0.001
    assert cost["date"] == "31.05.2001"
    assert cost["cost_type"] == "sewage"


def create_cost(apartment_number, sum_of_money, date, cost_type):
    ""
    creates a new cost
    :param apartment_number: int, the apartment number (identifier)
    :param sum_of_money: float, the amount of money a certain apartment has to pay
    :param date: string, date of time
    :param cost_type: string, the expense type: maintenance, sewage, other
    :return: cost: dictionary, contains information about the cost
    ""
    cost = {"apartment_number": apartment_number,
            "sum_of_money": sum_of_money,
            "date": date,
            "cost_type": cost_type}
    return cost
"""
def test_create_cost_str():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_apartment_number(cost) == 1
    assert get_sum_of_money(cost) - 57.5 < 0.001
    assert get_date(cost) == "31.05.2001"
    assert get_cost_type(cost) == "sewage"


def create_cost_str(apartment_number, sum_of_money, date, cost_type):
    """
      creates a new cost
      :param apartment_number: int, the apartment number (identifier)
      :param sum_of_money: float, the amount of money a certain apartment has to pay
      :param date: string, date of time
      :param cost_type: string, the expense type: maintenance, sewage, other
      :return: cost: a string
      """
    cost = str(apartment_number) + "," + str(sum_of_money) + "," + str(date) + "," + str(cost_type)
    return cost

def test_set_apartment_number():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_apartment_number(cost) == 1
    cost = set_apartment_number(cost, 3)
    assert get_apartment_number(cost) == 3


def set_apartment_number(cost, new_apartment_number):
    """
    Changes the apartment number with a new one
    :param cost:dictionary, a cost
    :param new_apartment_number: int, the new apartment number
    """
    c = cost.split(",")
    c[0] = new_apartment_number
    cost = create_cost_str(c[0], c[1], c[2], c[3])
    return cost


def test_set_sum_of_money():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_sum_of_money(cost) - 57.5 < 0.001
    cost = set_sum_of_money(cost, 25.2)
    assert get_sum_of_money(cost) - 25.2 < 0.001


def set_sum_of_money(cost, new_sum_of_money):
    """
    Changes the sum of money with a new one
    :param cost:dictionary, a cost
    :param new_sum_of_money: float, the new sum of money
    """
    c = cost.split(",")
    c[1] = new_sum_of_money
    cost = create_cost_str(c[0], c[1], c[2], c[3])
    return cost


def test_set_date():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_date(cost) == "31.05.2001"
    cost = set_date(cost, "31.05.2012")
    assert get_date(cost) == "31.05.2012"


def set_date(cost, new_date):
    """
    Changes the date with a new one
    :param cost:dictionary, a cost
    :param new_date: string, the new date
    """
    c = cost.split(",")
    c[2] = new_date
    cost = create_cost_str(c[0], c[1], c[2], c[3])
    return cost

def test_set_cost_type():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_cost_type(cost) == "sewage"
    cost = set_cost_type(cost, "maintenance")
    assert get_cost_type(cost) == "maintenance"


def set_cost_type(cost, new_cost_type):
    """
    Changes the cost type with a new one
    :param cost:dictionary, a cost
    :param new_cost_type: string, the new cost type
    """
    c = cost.split(",")
    c[3] = new_cost_type
    cost = create_cost_str(c[0], c[1], c[2], c[3])
    return cost


def test_get_apartment_number():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_apartment_number(cost) == 1


def get_apartment_number(cost):
    """
    returns the apartment number
    :param cost: string, a cost
    :return: apartment_number: int, the apartment number
    """
    c = cost.split(",")
    e = int(c[0])
    return e


def test_get_sum_of_money():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert (get_sum_of_money(cost) - 57.5) < 0.001


def get_sum_of_money(cost):
    """
    returns the amount of money a certain apartment has to pay
    :param cost: dictionary, a cost
    :return: sum_of_money: float, the amount of money
    """
    c = cost.split(",")
    e = float(c[1])
    return e


def test_get_date():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_date(cost) == "31.05.2001"


def get_date(cost):
    """
        returns the date in which an expense was registered
        :param cost: dictionary, a cost
        :return:date: string, date of time
        """
    c = cost.split(",")
    e = str(c[2])
    return e


def test_get_cost_type():
    cost = create_cost_str(1, 57.5, "31.05.2001", "sewage")
    assert get_cost_type(cost) == "sewage"


def get_cost_type(cost):
    """
    returns the expence type: maintenance, sewage, other
    :param cost: dictionary, a cost
    :return: cost_type: string, the expence type: maintenance, sewage, other
    """
    c = cost.split(",")
    e = str(c[3])
    return e

test_get_apartment_number()
test_create_cost_str()
test_get_cost_type()
test_get_date()
test_get_sum_of_money()
test_set_cost_type()
test_set_sum_of_money()
test_set_date()
test_set_apartment_number()

