def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    Total = charge + pounds
    print(f"Total £{Total:.2f}")


def pounds_to_float(d):
    d = d.replace("£", "")
    return float(d)

def percent_to_float(p):
    p = p.replace("%", "")
    return float(p) / 100

main()
  git config --global user.email "jja33@kent.ac.uk"
  git config --global user.name "Jayden Asante"