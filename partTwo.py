import math  

def main():
    A = float(input("what is the value of A? "))
    B = float(input("what is the value of B? "))
    pythag(A, B)
    
def pythag(A, B):
    x = pow(A, 2)
    y = pow(B, 2)
    C = math.sqrt(x + y)
    D = round(C)
    print("Hypotenuse:", D)
main()
