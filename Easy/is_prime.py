# 1 --> T
# 2 --> T
# 4 --> F
# 5 --> T


def is_prime(num):

    if num > 2: 
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

is_prime(1)
is_prime(2)
is_prime(4)
is_prime(5)




