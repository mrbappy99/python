# Simple & compund interest

principle = int(input("Enter principle :"))
time = int(input("Enter time: "))
rate = int(input("Enter rate: "))

simple_interest = (principle * time * rate) / 100
compound_interest = principle * pow((1 + (rate/100)), time)

print("The simple interest is ", simple_interest)
print("The compound interest is ", compound_interest)

