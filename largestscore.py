scoreList = [86, 86, 85, 85, 85, 83, 23, 45, 84, 1, 2, 0 ]

print(" =========== SYSTEM LOG ============= ")
print("scores ", scoreList)

#iiterate?
count = 0

while count < 11:
 print(scoreList[count])
 if count == 0:
     highehstscore = scoreList[count]
     secondhighest = 0
 if scoreList[count] > highehstscore:
     print("set ", scoreList[count] ,"as 1st number ")
     secondhighest = highehstscore
     highehstscore = scoreList[count]
 if scoreList[count] > secondhighest:
     if scoreList[count] == highehstscore:
         print("same 1st and 2nd dont count as 2nd highest proceed")
         secondhighest = secondhighest
     else:
         print("set ", scoreList[count] ,"as 2nd number ")
         secondhighest = scoreList[count]
 if count == 10:
     print("======================================")
     print("The highest number is ", highehstscore)
     print("The second number is ", secondhighest)
 count += 1
 
 


