def modify(a):
    a = a + 10

x = 5
modify(x)
print(x)

def mutable(a):
    a.append(10)

nums = [5]
mutable(nums)
print(nums)