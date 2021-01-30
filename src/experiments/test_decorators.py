from pyutils.decorators import CallCount, Tracer

@CallCount
def test():
    print("Test")

test()
test()
test()

print("Method used: ", test.count)

tracer = Tracer()

@tracer
def test2():
    print("Test 2")

test2()

tracer.enabled = True

test2()
