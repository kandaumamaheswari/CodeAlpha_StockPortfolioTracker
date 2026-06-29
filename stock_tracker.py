stocks={"AAPL":180,"TSLA":250,"GOOGLE":150,"MSFT":320,"AMZN":140}
total=0
print("===== Stock Portfolio Tracker =====")
while True:
    stock=input("Enter stock name (or DONE to finish): ").upper()
    if stock=="DONE":
        break
    if stock in stocks:
        quantity=int(input("Enter quantity: "))
        amount=stocks[stock]*quantity
        total+=amount
        print("Added:",stock,"-",amount)
    else:
        print("Stock not found.")
print("Total Investment Value: $",total)
with open("portfolio.txt","w") as f:
    f.write("Total Investment Value: $"+str(total))
print("Portfolio saved successfully.")
