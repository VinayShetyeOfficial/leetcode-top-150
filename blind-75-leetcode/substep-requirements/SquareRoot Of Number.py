# Square Root Of Number
def sqrt_of_num(num):
    
    res = num
    
    while True:
        res = ( res + num / res ) / 2
        
        if round(res*res) == num:
            break
    
    return int(res)
    
# Driver code
if __name__ == '__main__':
    print(sqrt_of_num(36))