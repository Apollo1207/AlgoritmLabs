def find_optimum_speed(piles, hours):
    """
    search for minimum and maximum speed based on the number of bananas
    :param piles: list of piles with bananas
    :param hours: hours monkey has to eat all bananas
    :return: minimal most suitable value to pass task condition
    >>> find_optimum_speed([3, 6, 7, 11], 8)
    4
    >>> find_optimum_speed([30, 11, 23, 4, 20], 5)
    30
    >>> find_optimum_speed([30, 11, 23, 4, 20], 6)
    23
    >>> find_optimum_speed([5, 6], 2)
    6
    >>> find_optimum_speed([5, 6], 3)
    5
    """
    all_bananas = max_speed = 0
    for pile in piles:
        all_bananas += pile
        if max_speed < pile:
            max_speed = pile
    min_speed = all_bananas // hours

    if len(piles) == hours:
        return max_speed
    return binary_search(min_speed, max_speed, piles, hours)


def binary_search(min_value, max_value, piles, hours):
    """
    finds minimal most suitable value to pass task condition
    :param min_value: minimal value to start search from (1)
    :param max_value: maximal value of bananas in piles
    :param piles: list of piles with bananas
    :param hours: hours monkey has to eat all bananas
    :return: minimal most suitable value to pass task condition
    >>> binary_search(1, 11, [3, 6, 7, 11], 8)
    4
    """
    while min_value < max_value:
        possible_speed = (min_value + max_value) // 2

        if can_eat_in_time(piles, hours, possible_speed):
            max_value = possible_speed
        else:
            min_value = possible_speed + 1
    return min_value


def can_eat_in_time(piles, hours_for_eat, possible_speed):
    """
    checks condition if monkey can eat all bananas with eating speed of probable_speed in hours_to_eat
    :param piles: list of piles with bananas
    :param hours_for_eat: hours monkey has to eat all bananas
    :param possible_speed: speed to check
    :return: true if pass condition else false
    >>> can_eat_in_time([3, 6, 7, 11], 8, 6)
    True
    >>> can_eat_in_time([3, 6, 7, 11], 8, 3)
    False
    """
    real_hours = 0
    for pile in piles:
        real_hours += pile // possible_speed + (0 if pile % possible_speed == 0 else 1)
    return real_hours <= hours_for_eat


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)
