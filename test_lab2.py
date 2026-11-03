import Lab2

def test_calc_average():
    numbers = [10, 20, 30]

    result = Lab2.calc_average(numbers)
    assert result == 20

def test_find_min_max():
    numbers = [10, 20, 30]

    result = Lab2.find_min_max(numbers)

    assert result == (10, 30)

def test_calc_median_temperature():
    numbers = [10, 20, 30]

    result = Lab2.calc_median_temperature(numbers)

    assert result == 20