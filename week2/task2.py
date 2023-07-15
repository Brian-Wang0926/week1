#1. Bonus should depend on salary, performance and role fields. Define your own rules and calculate a bonus for each employee based on it.
#2. The sum of bonus of all employees cannot exceed 10000 TWD based on your rules and example data.
#3. You can assume the USD to TWD Exchange Rate is 30.
#4. Salary is default to TWD if there is no specific mark.

def calculate_sum_of_bonus(data):
# performance："above average":*0.05 "average"*0.03 "below average"*0.01
# role："Engineer"+2000twd "CEO"+3000twd "Sales"+1000twd
# bonus = (salary + role) * performance
    sum=0
    for i in range(len(data["employees"])):
        role=data["employees"][i]["role"]
        performance=data["employees"][i]["performance"]
        salary=data["employees"][i]["salary"]
        sum=sum+(calculate_salary(salary)+calculate_role(role))*calculate_performance(performance)
    if sum <10000:
        print(round(sum))

def calculate_role(role):
    if role=="Engineer":
        return(2000)
    elif role=="CEO":
        return(3000)
    else:
        return(1000)

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