# 1
import numpy as np

ListA = [10, 20, 30, "test", 'Gayathri', 'Python', 10.5, 20.5, 4j, 3 + 7j]
print(len(ListA))

# 2

ListB = [10, 20, 30, 40, 50]
print(ListB[1:])

# 3

product = 1
ListC = [2, 6, 5, 2, 3]
print(sum(ListC))
for x in ListC:
    product *= x
print(product)

# 4

ListC = [2, 6, 5, 2, 3]
print(min(ListC))
print(max(ListC))

# 5

x = []
for i in ListC:
    if i % 2 != 0:
        x.append(i)
print(x)

# 6

norm_list = list(np.array(range(1,31))**2)

# 7

ListB = [10, 20, 30, 40, 50]
ListC = [2, 6, 5, 2, 3]
new_list = ListB[:-1] + list(ListC)
print(new_list)

# 8

a = {1:10, 2:20}
b = {3:30, 4:40}
c = a.copy()
c.update(b)
print(c)


# 9

def exp_dict(n):
    samp_dict = {}
    for i in range(0, n + 1):
        samp_dict[i] = i ** 2

    return (samp_dict)


# 10

def list_tuple():
    csv = input("Input a list of comma separated values, with no spaces")

    return list(csv), tuple(csv)