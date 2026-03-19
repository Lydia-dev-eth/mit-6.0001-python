#part_A
annual_salary = float(input("Enter your annual salary: "))
percent_saved = float(input("Enter the percent of salary to save (as decimal): "))
total_cost_home = float(input("Enter the cost of your dream home: "))

percent_down_payment = 0.25
r = 0.05  # annual return
amount_saved = 0.0
month = 0

monthly_salary = annual_salary / 12
monthly_saved = percent_saved * monthly_salary
down_payment = percent_down_payment * total_cost_home

while amount_saved < down_payment:
    amount_saved += monthly_saved
    amount_saved += amount_saved * (r / 12)
    month += 1

print("Number of months:", month)
         

