def calculate_net_salary(basic_salary, hours):
    try:
        basic_salary = int(basic_salary)
        hours = int(hours)
        if basic_salary <= 20000:
            return "Invalid input!"
        overtime_allowance = 0.025 * hours * basic_salary
        living_expenses_allowance = 0.25 * basic_salary
        epf = 0.08 * basic_salary
        paf = 0.0125 * basic_salary
        gross_salary = basic_salary + overtime_allowance + living_expenses_allowance
        taxes = 0
        if gross_salary > 500000:
            taxes = 0.19 * gross_salary
        elif gross_salary > 400000:
            taxes = 0.17 * gross_salary
        elif gross_salary > 300000:
            taxes = 0.14 * gross_salary
        elif gross_salary > 200000:
            taxes = 0.10 * gross_salary
        elif gross_salary > 100000:
            taxes = 0.05 * gross_salary
        net_salary = gross_salary - taxes - epf - paf

        return f"Basic Salary : {basic_salary}\nOver time : {int(overtime_allowance)}\nLiving Expenses Allowance : {int(living_expenses_allowance)}\nTax : {int(taxes)}\nEPF : {int(epf)}\nPAF : {int(paf)}\nNet Salary : {int(net_salary)}"
    except ValueError:
        return "Invalid input!"

# Read the input basic salary and hours
input_data = input()
basic_salary, hours = input_data.split()
result = calculate_net_salary(basic_salary, hours)
print(result)
