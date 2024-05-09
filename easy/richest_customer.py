
def maximumWealth(accounts):
    # accounts: List[List[int]]    
    maxWealth = 0
    # Iterate through the accounts
    for i in range(len(accounts)):
        # Initialize totalPerAccount to 0
        totalPerAccount = 0
        # Iterate through the accounts[i]
        for j in range(len(accounts[i])):
            # Add the current element to totalPerAccount
            totalPerAccount += accounts[i][j]
            
        # Update maxWealth with the maximum value between maxWealth and totalPerAccount
        maxWealth = max(maxWealth, totalPerAccount)    

    return maxWealth  
    
if __name__ == "__main__":
    input_arr = [[3,4,58,90,81,97],[3,4,58,90,81,97],[3,4,58,90,81,97]]
    print(maximumWealth(input_arr))