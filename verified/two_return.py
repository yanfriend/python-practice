# verify: a func can return two different types

def my_test_ret(aaa):
    if aaa == "1":
        return
    return 333

print my_test_ret("1")
print my_test_ret(0)

