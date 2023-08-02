from mo_future import extend


class Test:
    pass


@extend(Test)
def test(self, a, b):
    return a + b


assert Test().test(1, 2) == 3
