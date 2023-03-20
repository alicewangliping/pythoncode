#learn to how to wirte interview algorithm
# FizzbuZZ
# def FizzBuzz(count):
#     isInt = isinstance(count, int)
#     if not isInt:
#         return "-1"
#     str1 = ""
#     for i in range(1,count):
#         if i % 3 == 0:
#             str1 += "Fizz"
#         elif i % 5 == 0:
#             str1 += "Buzz"
#         else:
#             str1 += str(i)
#     return str1
# 1
# if __name__ == '__main__':
#
#         d = int(input("please input FizzBuzz number:"))
#         arr=[1,2,3,4,5]
#         # arr = list(map(int, input("dfd").rstrip().split()))
#         result = FizzBuzz(d)
#         print("FizzBuff is "+result)

def fizzbuzz(n):
    """
    This function takes an integer n as input and returns a list of strings
    that corresponds to the FizzBuzz problem for numbers 1 to n.
    """
    result = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def main():
    # Example usage
    n = 15
    result = fizzbuzz(n)
    print(result)

if __name__ == "__main__":
    main()

