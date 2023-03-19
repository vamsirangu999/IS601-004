from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, OutOfStockException, InvalidStageException


# UCID = vr76, Data = 18-03-2023
def test_1():
    try:
        machine = BurgerMachine()
        machine.reset()
        machine.handle_patty("veggie")
        machine.handle_toppings("cheese")
        assert False
    except InvalidStageException:
        assert True


# UCID = vr76, Data = 18-03-2023
def test_2():
    try:
        machine = BurgerMachine()
        machine.reset()
        for _ in range(4):
            machine.handle_bun("White Burger Bun")
            machine.handle_patty("veggie")
            machine.handle_patty("veggie")
            machine.handle_patty("veggie")
            machine.handle_patty("next")
            machine.handle_toppings("cheese")
            machine.handle_toppings("done")
            machine.handle_pay(4.25, "4.25")
        assert False
    except OutOfStockException:
        assert True


# UCID = vr76, Data = 18-03-2023
def test_3():
    try:
        machine = BurgerMachine()
        machine.reset()
        for _ in range(4):
            machine.handle_bun("White Burger Bun")
            machine.handle_patty("veggie")
            machine.handle_patty("next")
            machine.handle_toppings("cheese")
            machine.handle_toppings("cheese")
            machine.handle_toppings("cheese")
            machine.handle_toppings("done")
            machine.handle_pay(2.75, "2.75")
        assert False
    except OutOfStockException:
        assert True


# UCID = vr76, Data = 18-03-2023
def test_4():
    try:
        machine = BurgerMachine()
        machine.reset()
        machine.handle_bun("White Burger Bun")
        machine.handle_patty("Beef")
        machine.handle_patty("Beef")
        machine.handle_patty("Beef")
        machine.handle_patty("Beef")
        assert False
    except ExceededRemainingChoicesException:
        assert True


# UCID = vr76, Data = 18-03-2023
def test_5():
    try:
        machine = BurgerMachine()
        machine.reset()
        machine.handle_bun("White Burger Bun")
        machine.handle_patty("Turkey")
        machine.handle_patty("next")
        machine.handle_toppings("pickles")
        machine.handle_toppings("pickles")
        machine.handle_toppings("pickles")
        machine.handle_toppings("pickles")
        assert False
    except ExceededRemainingChoicesException:
        assert True


# UCID = vr76, Data = 18-03-2023
def test_6():
    machine = BurgerMachine()
    machine.reset()
    machine.clean_machine()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == "$2.25"

    machine = BurgerMachine()
    machine.reset()
    machine.handle_bun("No Bun")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == "$0.25"

    machine = BurgerMachine()
    machine.reset()
    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    assert machine.calculate_cost() == "$3.0"


# UCID = vr76, Data = 18-03-2023
def test_7():
    machine = BurgerMachine()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    machine.handle_pay(2.25, "2.25")

    machine.handle_bun("No Bun")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    machine.handle_pay(2.5, "2.5")

    machine.handle_bun("Lettuce Wrap")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    machine.handle_pay(5.25, "5.25")
    assert machine.total_sales == 10.0


# UCID = vr76, Data = 18-03-2023
def test_8():
    machine = BurgerMachine()
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("Turkey")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    machine.handle_pay(2.25, "2.25")

    machine.handle_bun("No Bun")
    machine.handle_patty("next")
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done")
    machine.handle_pay(2.5, "2.5")
    assert machine.total_burgers == 2
