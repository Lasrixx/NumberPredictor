class Solution:

    def number_prediction(self, input):
        input="0"*10+input
        while input.find("_") != -1:
            #Whilst there is still an underscore in the input
            #Find the index of the underscore
            print("loop")
            swapped=False
            usIndex = input.index("_")
            print(usIndex)
            specialCase = "0"*(10-len(input[:usIndex]))+input[:usIndex]            
            if specialCase == "0000000000" and swapped == False:
                input=input.replace("_","0",1)
                swapped = True
            for i in range(10,-1,-1):
                print("i="+str(i))
                #count back i characters and compare i characters against input
                #moving backwards 1 character at a time
                if i == 0 and swapped == False:
                    #replace underscore with previous character
                    input=input.replace("_",input[usIndex-1],1)
                    print(input)
                    swapped=True
                if swapped == True:
                    break
                matchGroup = input[:usIndex][usIndex-i:]
                for j in range(usIndex-(2*i),-1,-1):
                    print("Search:"+str(input[j:j+i]))
                    print("Match:"+str(matchGroup))
                    if input[j:j+i] == matchGroup:
                        print("Yes")
                        #Get character immediately after match
                        #And replace underscore
                        replacement = input[j+i]
                        input=input.replace("_",replacement,1)
                        print(input)
                        swapped = True
                    if swapped == True:
                        break
                if swapped==True:
                    break
        return input[10:]
                

solution=Solution()
print(solution.number_prediction("43127435926350613352415886760955388_8983743325219_168_926629293_776892_9_1_8_8049287_298_9343647_9_2334_4_6_7__57__30785__7__62_1____4_____382__1226816__04__67___0119_47__0_0_7___0___0_3__3_____06_37_"))