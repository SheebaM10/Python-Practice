# tom_exp_list = [2100,3400,3500]
# joe_exp_list = [200,500,700]

# total = 0
# for item in tom_exp_list:
#     total= total+item
# print("Tom's total expenses:", total)
    
# total = 0

# for item in joe_exp_list:
#     total= total+item
# print("Joe's total expenses:", total)
    

def calculate_total(exp):
    total = 0
    for item in exp:
        total=total+item
    return total    

tom_exp_list = [2100,3400,3500]
joe_exp_list = [200,500,700]

toms_total= calculate_total(tom_exp_list)
joes_total= calculate_total(joe_exp_list)

print("Tom's total expense:", toms_total)
print("Joe's total expense:", joes_total)
