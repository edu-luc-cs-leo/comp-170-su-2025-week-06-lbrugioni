#This fucntion reads temperature values from a file
#and returns them as a lsit of floats
def load_to_list(filepath:str)->list[float]:
    numbers=[]
    with open(filepath,'r') as file:
        for line in file:
            value=float(line.strip())
            numbers.append(value)
    return numbers
#This fucntion prints basic statistics or a list of numbers
def descriptive_statistics(source_data:list[float])->None:
    count=len(source_data)
    total=sum(source_data)
    average=round(total/count,2)
    smallest=min(source_data)
    largest=max(source_data)

    print(f"There are {count} values in the data source.")
    print(f"The average value is {average}")
    print(f"The highest value is {largest} and the smallest value is {smallest}.")

#This function reads lines from a file and applies
#simple markup rules for formatting text
def apply_markup(filepath:str)->None:
    with open(filepath,'r') as file:
        for line in file:
            words=line.strip().split()
            result=[]

            for word in words:
                if word.startswith('.'):
                    #remove the dot and make uppercase
                    result.append(word[1:].upper())
                elif word.startswith('_'):
                    #remove the underscore and add spaces between letters 
                    expanded=''.join(word[1:])
                    result.append(expanded)
                else:
                    result.append(word)
            print(' '.join(result))

#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

