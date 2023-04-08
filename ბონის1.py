#დავალება2
def count_ways_to_climb_stairs(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_ways_to_climb_stairs(n-1) + count_ways_to_climb_stairs(n-2)
n = 8
ways = count_ways_to_climb_stairs(n)
print(f"There are {ways} ways to climb {n} stairs")
#დავალება3
class Roman:
    def __init__(self):
        self.roman_to_integer_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    def roman_to_integer(self, roman_numeral):
        if not roman_numeral:
            return 0
        prev_num = 0
        total = 0
        for numeral in roman_numeral:
            current_num = self.roman_to_integer_dict[numeral]
            if prev_num < current_num:
                total += current_num - 2 * prev_num
            else:
                total += current_num
            prev_num = current_num
        return total
rti = Roman()
print(rti.roman_to_integer('XIM'))
#დავალება4
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar, int):
            raise ValueError("უნდა იყოს მთელი რიცხვი")
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2
v4 = v2 * 2
v5 = 3 * v1
print("v1: ({}, {})".format(v1.x, v1.y))
print("v2: ({}, {})".format(v2.x, v2.y))
print("v1 + v2: ({}, {})".format(v3.x, v3.y))
print("v2 * 2: ({}, {})".format(v4.x, v4.y))
print("3 * v1: ({}, {})".format(v5.x, v5.y))



