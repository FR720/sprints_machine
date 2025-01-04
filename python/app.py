import sys
from helper.fibonacci import fibonacci
from helper.traditionalFibonacci import traditionalFibonacci


n=10000

#generators
fibGen = fibonacci(n)
print(f"Memory used by generator (function object): {sys.getsizeof(fibGen)} bytes")


#traditional list
fibNumbers = traditionalFibonacci(n)
print(f"Memory used by traditional list: {sys.getsizeof(fibNumbers)} bytes")