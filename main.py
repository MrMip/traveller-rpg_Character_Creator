#!/bin/python

import random

Age = 18
Str = None
Dex = None
End = None
Int = None
Edu = None
Soc = None
StrDM = None
DexDM = None
EndDM = None
IntDM = None
EduDM = None
SocDM = None
Skills = []
# Rolls num D6.
def roll(num):
        i = 0; out = 0
        while (i != num):
             out = out + round(random.uniform(1, 6))
             i +=1
        return out;
statRolls = [roll(2), roll(2), roll(2), roll(2), roll(2), roll(2)]
# Gets the DM of a stat.
def diceMod(stat):
     if stat == 0    : return -3
     elif stat < 3   : return -2
     elif stat < 6   : return -1
     elif stat < 9   : return  0
     elif stat < 12  : return  1
     elif stat < 15  : return  2
     elif stat >= 15 : return  3
     else: return "Error: Invalid input"
# Formats the DM for printing.
# Str 0, Dex 1, End 2, Int 3, Edu 4, Soc 5
def formatDM(DM):
     if DM >= 0 : return ("{}{}".format("+",DM))
     else:        return ("{}{}".format("-",DM))
# Sets the value of a stat.
# Str 0, Dex 1, End 2, Int 3, Edu 4, Soc 5
def setStat(num, statNum):
     global Str; global Dex; global End; global Int; global Edu; global Soc
     if   statNum == 0  : Str = num
     elif statNum == 1  : Dex = num
     elif statNum == 2  : End = num
     elif statNum == 3  : Int = num
     elif statNum == 4  : Edu = num
     elif statNum == 5  : Soc = num
     return
# Checks Input to see if it's in statRolls.
def checkRoll(Input,statNum):
     if statRolls[0] == Input:
          setStat(Input,statNum)
          statRolls[0] = None
     elif statRolls[1] == Input:
          setStat(Input,statNum)
          statRolls[1] = None
     elif statRolls[2] == Input:
          setStat(Input,statNum)
          statRolls[2] = None
     elif statRolls[3] == Input:
          setStat(Input,statNum)
          statRolls[3] = None
     elif statRolls[4] == Input:
          setStat(Input,statNum)
          statRolls[4] = None
     elif statRolls[5] == Input:
          setStat(Input,statNum)
          statRolls[5] = None
     else : print("You did not roll that number, or you have alredy used it!")
     
def Term(termNum):
     global Str; global Dex; global End; global Int; global Edu; global Soc
     global StrDM; global DexDM; global EndDM; global IntDM; global EduDM; global SocDM
     if termNum == 0:
          print("Please set your sats.")
          print(statRolls[0],  statRolls[1], statRolls[2], statRolls[3], statRolls[4], statRolls[5],)
          # Set stats.
          x = int(input("Str:")); checkRoll(x,0)
          #x = int(input("Dex:")); checkRoll(x,1)
          #x = int(input("End:")); checkRoll(x,2)
          #x = int(input("Int:")); checkRoll(x,3)
          #x = int(input("Edu:")); checkRoll(x,4)
          #x = int(input("Soc:")); checkRoll(x,5)
          # Sets DMs and Prints stats
          print("Your Stats are.")
          StrDM = diceMod(Str); print("Str:", Str, formatDM(StrDM))
          DexDM = diceMod(Dex); print("Dex:", Dex, formatDM(DexDM))
          EndDM = diceMod(End); print("End:", End, formatDM(EndDM))
          IntDM = diceMod(Int); print("Int:", Int, formatDM(IntDM))
          EduDM = diceMod(Edu); print("Edu:", Edu, formatDM(EduDM))
          SocDM = diceMod(Soc); print("Soc:", Soc, formatDM(SocDM))
          # Select Background Skills
          print("You can chose", (EduDM + 3), "background skills. Form this list.")
          print("1:Admin 0, 2:Animals 0, 3:Art 0, 4:Athletics 0, 5:Carouse 0, 6:Drive 0, 7:Electonics 0, 8:Flyer 0, 9:Language 0")
          print("10:Mechanic 0, 11:Medic 0, 12:Profession 0, 13:Science 0, 14:Seafarer 0, 15:Streetwise 0, 16:Survival 0, 17:Vacc Suit 0")
          i = 0;
          while i < (EduDM + 3):
               x = int(input("({} Left)".format(((EduDM + 3) - i)))
          
          
Term(0)
     
