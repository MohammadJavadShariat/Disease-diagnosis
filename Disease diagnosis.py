#health number
health = 100

#Examining the location of the pain
while(True):
    location_of_pain = input("Write the location of the pain (abdomen, throat, chest, none):")
    if location_of_pain == "abdomen" :
        print("*****Doctor's visit*****\nYour appendix is ​​damaged! Go to the hospital as soon as possible.")
        health -= 40
        break
    elif location_of_pain == "throat" :
        #Checking whether or not you have a fever
        while(True):
            fever = input("Do you have a fever? (Yes, No):")
            if fever == "yes" :
                print("*****Doctor's visit*****\nThere is pus sore throat bacteria in your throat.")
                health -= 10
                break
            elif fever == "No" :
                print("*****Doctor's visit*****\nYour illness is viral.")
                health -= 15
                break
            else:
                print("The data is incorrect.")
        break
    elif location_of_pain == "chest" :
        print("*****Doctor's visit*****\nYou have had a failed stroke. Go to the hospital as soon as possible.")
        health -= 50
        break
    elif location_of_pain == "none" :
        cough = input("(Yes, No) Do you cough?:")
        #Check whether you have a cough or not
        while(True):
            if cough == "No" :
                print("*****Doctor's visit*****\nWhy bother when you are not sick? You have a mental illness. Introduce yourself to a mental institution as soon as possible.")
                health -= 90
                break
            elif cough == "Yes" :
                #Checking whether or not you have a fever
                c_fever = input("Do you have a fever? (Yes, No):") 
                if c_fever == "No" :
                    print("*****Doctor's visit*****\nYou have a cold.")
                    health -= 20
                    break
                elif c_fever == "Yes" :
                    print("*****Doctor's visit*****\nUnfortunately, you have the flu.")
                    health -= 25
                    break
                else:
                    print("The data is incorrect.")
        break
    else:
        print("The data is incorrect.")
#Checking health percentage
if health >= 80 :
    print(f"Your health is {health}%.")
elif health <= 10 :
    print(f"You are in critical condition. Unfortunately, your health is {health}%.")
else:
    print(f"Unfortunately, your health is {health}%.")                    
            
            
            
            
            
            
            
            
    
