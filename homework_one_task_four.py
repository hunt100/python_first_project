#Запросите у пользователя значения выручки и издержек фирмы.
#Определите, с каким финансовым результатом работает фирма
#(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
#Выведите соответствующее сообщение. Если фирма отработала с прибылью,
#вычислите рентабельность выручки (соотношение прибыли к выручке).
#Далее запросите численность сотрудников фирмы и определите
#прибыль фирмы в расчете на одного сотрудника.

revenue = float(input("Enter the company's revenue: "))
cost = float(input("Enter the company's costs: "))
revenue_cost_diff = revenue - cost
is_profit_text = "Profit" if revenue_cost_diff >= 0 else "Loss"
print(f"Financial results - {is_profit_text}. {is_profit_text} amount: {revenue_cost_diff}")
if revenue_cost_diff >= 0:
    return_on_revenue_percent = revenue_cost_diff / revenue
    print(f"Return on revenue = {return_on_revenue_percent:.2f}")
    number_of_employee = int(input("Enter the number of employees of the company: "))
    profit_per_employee = revenue_cost_diff / number_of_employee
    print(f"Company profit per employee = {profit_per_employee:.1f}")
