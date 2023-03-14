# Python program for naive string matching algorithm
# Searching algorithm

def find_Pattern( MainString:str, StringToFind:str ):
    #lenth Of MainString, lenth Of StringToFind 
    
    lms= len(MainString)
    lsf= len(StringToFind)
    
    # forloop for pointing index values 'i' focus on main string 'j' focus on Pattern(string to find)
    for i in range(lms-lsf+1):
        j = 0
        
        while j < lsf:
            # if condition to break the while loop, else to increment 'i' and 'j'
            if MainString[i+j] != StringToFind[j]:
                break
            j = j + 1
        
        if j == lsf:
            # 'f' string fromatting  
            print(f'Sting found, form index {i} to {i+lsf}')

    
# Driver's code   
if __name__ == "__main__":
    #taking input strings for main string and Pattern to find
    MainString = str(input("Enter the string : "))
    StringToFind = str(input("Enter the string to find : "))
    
    #function call:
    find_Pattern(MainString, StringToFind)

    
            
    
