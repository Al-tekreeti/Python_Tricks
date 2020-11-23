def greet():
    return "Hello"

def uppercase_decorator(func):
    def wrapper():
        originalResult = func()
        modifiedResult = originalResult.upper()
        return modifiedResult
    return wrapper

@uppercase_decorator
def salam():
    return "salam"

def lowercase_decorator(func):
    def wrapper():
        originalResult = func()
        modifiedResult = originalResult.lower()
        return modifiedResult
    return wrapper

if __name__ == "__main__":
    # apply the decorator manually and assign it to greet1 to keep the original behaviour of greet() unchanged
    greet1 = uppercase_decorator(greet)
    print(greet1())
    # apply the decorator at the definition of salam(). The original behaviour is lost
    print(salam())
    print(greet())
    greet2 = lowercase_decorator(greet)
    print(greet2())
