def calculate_total(exp):
    total = 0

    for item in exp:
        total = total + item
    
    return total


tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

print(calculate_total(tom_exp_list))
print(calculate_total(joe_exp_list))