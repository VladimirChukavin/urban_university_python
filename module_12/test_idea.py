import idea_unit_testing


def test_add():
    if idea_unit_testing.add(1, 2) == 3:
        print('Test add is OK')
    else:
        print('Test add is FAIL')


test_add()
