import inspect


def introspection_info(obj):
    type_of_object = type(obj)
    attribute = [attr for attr in dir(obj) if attr.isalnum()]
    methods = [meth for meth in dir(obj) if not meth.isalnum()]
    module = inspect.getmodule(obj)

    __local_dict = locals()
    return __local_dict


if __name__ == '__main__':
    number_info = introspection_info(42)
    print(number_info)
