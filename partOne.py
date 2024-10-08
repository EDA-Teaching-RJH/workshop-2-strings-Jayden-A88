def main():
    slow = input("Press Enter ")
    myFunction(slow)

def myFunction(slow):
  name = input("what's your full name? ")
  name = name.replace(" ", "...").strip().title()
  print("Hello, " + name)
main()
