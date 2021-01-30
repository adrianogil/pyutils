from pyutils.decorators import timer, ObservableInstance


class SimpleObject(ObservableInstance):
    def __init__(self):
        super().__init__()
        self.x = 0

    def __del__(self):
        print("SimpleObject destructor")
        super().__del__()

    @property
    def objdata(self):
        return [self.x]

    @property
    def objdatatuple(self):
        return (self.x,)


class SampleObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

    @property
    def objdata(self):
        return [self.x, self.y, self.z]


class SampleObject2:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.z1 = 0
        self.x2 = 0
        self.y2 = 0
        self.z2 = 0

    @property
    def objdata1(self):
        return [self.x1, self.y1, self.z1]

    @property
    def objdata2(self):
        return [self.x2, self.y2, self.z2]


@timer
def generate_instances(object_class, max_instances=1000):

    all_instances = []

    for i in range(0, max_instances):
        all_instances.append(object_class())

    print("generated: %s instances" % (max_instances,))


if __name__ == "__main__":
    generate_instances(SimpleObject)
    generate_instances(SampleObject)
    generate_instances(SampleObject2)
