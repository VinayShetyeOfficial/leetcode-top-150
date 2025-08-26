# Square Root Of Number
def sqrt_of_num(num):
    res = num

    while True:
        res = (res + num / res) / 2  # Newton-Raphson Method

        if round(res * res) == num:
            break

    return int(res)


# Driver code
if __name__ == '__main__':
    print(sqrt_of_num(36))  # ✅ Output: 6


# -----------------------------------------
# Time Complexity (TC): O(log(num)) 
#   -> Because Newton-Raphson method converges very fast.
# Space Complexity (SC): O(1) 
#   -> Only a few variables are used.
