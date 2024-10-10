import inspect


class Something:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.__C_CONST = float(3.14)

    def get_a_b_c(self):
        return self.a, self.b


def introspection_info(obj):
    type_of_object = type(obj)
    attribute = obj.__getstate__()
    methods = [meth for meth in dir(obj)]
    module = inspect.getmodule(obj)

    __local_dict = locals()
    return __local_dict


if __name__ == '__main__':
    some_obj = Something('a', 42)
    number_info = introspection_info(some_obj)
    print(number_info)
