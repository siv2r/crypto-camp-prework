DAYS_IN_YEAR = 365

def no_two_people(n):
    assert n <= DAYS_IN_YEAR
    prob = 1
    for i in range(n):
        prob = prob * (1 - i / DAYS_IN_YEAR)
    assert 0 <= prob <= 1
    return prob

def at_least_two_people(n):
    return 1 - no_two_people(n)

if __name__ == "__main__":
    print(no_two_people(30))
    print(at_least_two_people(30))