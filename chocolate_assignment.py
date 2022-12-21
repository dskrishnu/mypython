
def choco_func(no_of_chocolates, no_of_wrappers, wrappers_for_free_choc):

    if no_of_wrappers >= wrappers_for_free_choc:
        no_of_new_chocolates = (no_of_wrappers // wrappers_for_free_choc)
        no_of_remaining_wrappers = (no_of_wrappers % wrappers_for_free_choc)
        no_of_new_wrappers = no_of_new_chocolates + no_of_remaining_wrappers
        no_of_chocolates += no_of_new_chocolates        
        return choco_func(no_of_chocolates, no_of_new_wrappers, wrappers_for_free_choc)
    else:
        return no_of_chocolates

cost = int(input('Enter the cost of each chocolate: '))
wrappers_for_free_choc = int(input('Enter the no of wrappers required to get free chocolate: '))
money = int(input('Enter the amount of money you have: '))

no_of_chocolates = money // cost    

total_chocs = choco_func(no_of_chocolates, no_of_chocolates, wrappers_for_free_choc)

print(f'You can have {total_chocs} chocolates')