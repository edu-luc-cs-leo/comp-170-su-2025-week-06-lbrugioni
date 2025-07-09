#Reads temperature values from specifced file and returns a list of floats.
def load_to_list(filepath:str)->list[float]:
    numbers=[]
    with open(filepath,'r') as file:
        for line in file:
            value=float(line.strip()) #Convert each line to float and then add to the list.
            numbers.append(value)
    return numbers

#This function calculates and prints count,average,min and max of temperature list.
def descriptive_statistics(source_data:list[float])->None:
    count=len(source_data)
    total=sum(source_data)
    average=round(total/count,2)
    smallest=min(source_data)
    largest=max(source_data)

    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {largest} and the smallest value is {smallest}.")

#This function reads lines from a file and applies simple markup rules for formatting text.
#Words starting with '.' are printed in uppercase.
#Words starting with '_' are expanded by adding spaces between the letters. 
def apply_markup(filepath:str)->None:
    with open(filepath,'r') as file:
        for line in file:
            words=line.strip().split()
            result=[]

            for word in words:
                if word.startswith('.'):
                    result.append(word[1:].upper()) #Remove the dot and make uppercase.
                elif word.startswith('_'): #Remove the underscore and add spaces between letters.
                    expanded=' '.join(word[1:])
                    result.append(expanded)
                else:
                    result.append(word)
            print(' '.join(result))

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

