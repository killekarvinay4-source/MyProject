Write a function to print table of given user input
def table():
num = int(input("enter a number : "))
for i in range(1,11):
  print(f"{num} * {i} = {num * i}")
  table()


    # Rewrite table function using while  Loop
 def table():
    num = int(input("enter a number : "))
    i = 1
    while i <= 10:
        print(f"{num} * {i} = {num * i}")
            i += 1
table()
