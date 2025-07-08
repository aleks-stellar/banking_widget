def log(filename=None):
    def wrapper(function):

        def inner(*args, **kwargs):
            result = None
            try:
                result = function(*args, **kwargs)
                output_result = f"{function.__name__} ok"
            except Exception as e:
                output_result = (f"{function.__name__} "
                                 f"error: {type(e).__name__}. "
                                 f"Inputs: {args}, {kwargs}")

            if filename is None:
                print(output_result)
                return result
            with open(filename, "a", encoding="utf-8") as file:
                file.write(output_result)
                file.write("\n")
                return result
        return inner
    return wrapper
