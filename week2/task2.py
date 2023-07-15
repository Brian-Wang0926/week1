#1. Bonus should depend on salary, performance and role fields. Define your own rules and calculate a bonus for each employee based on it.
#2. The sum of bonus of all employees cannot exceed 10000 TWD based on your rules and example data.
#3. You can assume the USD to TWD Exchange Rate is 30.
#4. Salary is default to TWD if there is no specific mark.

def calculate_sum_of_bonus(data):
# performance："above average":*0.05 "average"*0.03 "below average"*0.01
# role："Engineer"+20000twd "CEO"+30000twd "Sales"+10000twd
# bonus = (salary + role) * performance
    bonus=0
    for i in range(len(data["employees"])):
        role=data["employees"][i]["role"]
        performance=data["employees"][i]["performance"]
        salary=data["employees"][i]["salary"]
        bonus=bonus+(calculate_salary(salary)+calculate_role(role))*calculate_performance(performance)
    if bonus>10000:
        print(10000)  #確認邏輯是否正確
    else:
        print(round(bonus))
def calculate_role(role):
    if role=="Engineer":
        return(20000)
    elif role=="CEO":
        return(30000)
    else:
        return(10000)

def calculate_performance(performance):
    if performance == "above average":
        return(0.05)
    elif performance == "average":
        return(0.03)
    else:
        return(0.01)

def calculate_salary(salary):
    characters="USD,"
    try:
        if "USD" in salary:
            salary=int(''.join(x for x in salary if x not in characters))*30
            return(salary)
        else:
            salary=int(''.join(x for x in salary if x not in characters))
            return(salary)
    except:
        return(salary)

calculate_sum_of_bonus({ 
    "employees":[
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob", 
            "salary":60000, 
            "performance":"average", 
            "role":"CEO"
        },
        {
            "name":"Jenny", 
            "salary":"50,000", 
            "performance":"below average", 
            "role":"Sales"
        } 
    ]
}) 