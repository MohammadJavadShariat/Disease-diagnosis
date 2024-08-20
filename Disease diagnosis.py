#health number
health = 100

#Examining the location of the pain
while(True):
    mahal_dard = input("محل درد را بنویسید(شکم , گلو , سینه , هیچکدام):")
    if mahal_dard == "شکم" :
        print("*****ویزیت پزشک*****\nآپاندیس شما آسیب دیده است! هرچه زودتر به بیمارستان مراجعه کنید.")
        health -= 40
        break
    elif mahal_dard == "گلو" :
        #Checking whether or not you have a fever
        while(True):
            tab = input("آیا تب دارید؟(بله , خیر):")
            if tab == "بله" :
                print("*****ویزیت پزشک*****\nدر گلوی شما باکتری گلودرد چرکی وجود دارد.")
                health -= 10
                break
            elif tab == "خیر" :
                print("*****ویزیت پزشک*****\nبیماری شما ویروسی است.")
                health -= 15
                break
            else:
                print("داده غلط است.")
        break
    elif mahal_dard == "سینه" :
        print("*****ویزیت پزشک*****\nشما یک سکته ی ناموفق داشته اید. هرچه سریعتر به بیمارستان بروید.")
        health -= 50
        break
    elif mahal_dard == "هیچکدام" :
        sorfe = input("(بله , خیر)آیا سرفه می کنید؟:")
        #Check whether you have a cough or not
        while(True):
            if sorfe == "خیر" :
                print("*****ویزیت پزشک*****\nچرا وقتی مریضی ندارید مزاحم می شوید؟ شما به بیماری روانی مبتلا هستید. هرچه سریعتر خود را به یک آسایشگاه روانی معرفی کنید.")
                health -= 90
                break
            elif sorfe == "بله" :
                #Checking whether or not you have a fever
                s_tab = input("آیا تب دارید؟(بله , خیر):") 
                if s_tab == "خیر" :
                    print("*****ویزیت پزشک*****\nشما سرما خورده اید.")
                    health -= 20
                    break
                elif s_tab == "بله" :
                    print("*****ویزیت پزشک*****\nمتاسفانه شما به بیماری آنفولانزا مبتلا هستید.")
                    health -= 25
                    break
                else:
                    print("داده غلط است.")
        break
    else:
        print("داده غلط است.")
#Checking health percentage
if health >= 80 :
    print(f"سلامتی شما{health} درصد است.")
elif health <= 10 :
    print(f"شما در وضعیت وخیم قرار دارید. متاسفانه سلامتی شما{health} درصد است.")
else:
    print(f"متاسفانه سلامتی شما{health} درصد است.")                    
            
            
            
            
            
            
            
            
    