
# 5! = 120
#
# 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))

# Fibonacci numbers:
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...


def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums
print('via lists: ')
for n in fibonacci(1000000):
    print(n, end=', ')

# Sama Generator-metodeilla, jolloin ei kerätä laskelmaa listana muistiin vaan muistissa pidetään vain 1 item kerralla:
"""HUOMAA KUN RETURN KORVATAAN YIELDILLÄ PASSATAAN LASKETTU
ITEM VÄLITTÖMÄSTI WHILE-LOOPISTA ETEENPÄIN EIKÄ NIITÄ KERÄTÄ 
PUSKURIMUISTIIN KUTEN RETURN TEKISI WHILE-LOOPISSA!"""
def fibonacci_co():

    current = 0
    next = 1

    while True:
        current, next = next, next + current
        # Sanon yieldillä Python-tulkille että laske 1 item (=current) kerralla koko sekvenssistä
        yield current


print()
print('with yield: ')
for n in fibonacci_co():
    if n > 1000000:
        break

    print(n, end=', ')


