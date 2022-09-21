from tkinter import *
import random

# Window and Window Title
Screen = Tk()
Screen.title("MW2 Class Randomizer v1.0")

InputLevel = StringVar()

primaryWeapon = 'N/A'
secondaryWeapon = 'N/A'
equipment = 'N/A'
specialGrenade = 'N/A'
perk1 = 'N/A'
perk2 = 'N/A'
perk3 = 'N/A'
deathStreak = 'N/A'

primaryWeaponList = [("M4A1", 1), ("FAMAS", 4), ("SCAR-H", 8), ("TAR-21", 20), ("FAL", 28), ("M16A4", 40), ("ACR", 48), ("F2000", 60), ("AK-47", 70),
("MP5K", 1), ("UMP45", 1), ("VECTOR", 12), ("P90", 24), ("MINI-UZI", 44),
("L86 LSW", 1), ("RPD", 1), ("MG4", 16), ("AUG HBAR", 32), ("M240", 52),
("INTERVENTION", 1), ("BARRET .50CAL", 1), ("WA2000", 36), ("M21 EBR", 56),
("RIOT SHIELD", 1)]
secondaryWeaponList = [("PP2000", 1), ("G18", 22), ("M93 RAFFICA", 38), ("TMP", 58),
("SPAS-12", 1), ("AA-12", 18), ("STRIKER", 34), ("RANGER", 42), ("M1014", 54), ("MODEL 1887", 67),
("USP .45", 1), (".44 MAGNUM", 26), ("M9", 46), ("DESERT EAGLE", 62),
("AT4-HS", 1), ("THUMPER", 14), ("STINGER", 30), ("JAVELIN", 50), ("RPG-7", 65)]
equipmentList = [("FRAG", 1), ("SEMTEX", 1), ("THROWING KNIFE", 7), ("TAC INSERT", 11), ("BLAST SHIELD", 19), ("CLAYMORE", 31), ("C4", 43)]
specialGrenadeList = [("FLASH GRENADE", 1), ("STUN GRENADE", 1), ("SMOKE GRENADE", 1)]
perk1List = [("MARATHON" , 1), ("SLEIGHT OF HAND", 1), ("SCAVENGER", 13), ("BLING", 21), ("ONE MAN ARMY", 45)]
perk2List = [("STOPPING POWER" , 1), ("LIGHTWEIGHT", 1), ("HARDLINE", 9), ("COLD BLOODED", 25), ("DANGER CLOSE", 33)]
perk3List = [("STEADY AIM" , 1), ("SCRAMBLER", 17), ("NINJA", 29), ("SITREP", 37), ("LAST STAND", 41)]
deathStreakList = [("COPYCAT", 1), ("PAINKILLER", 6), ("MARTYRDOM", 27), ("FINAL STAND", 39)]

def reroll(levelNum):
    global primaryWeapon, secondaryWeapon, equipment, specialGrenade, perk1, perk2, perk3, deathStreak
    if levelNum <= 3:
        return
    # Primary Weapon Randomization
    while(0==0):
        randNum = random.randrange(0,len(primaryWeaponList))
        if primaryWeaponList[randNum][1] <= levelNum:
            print('success: ' + primaryWeaponList[randNum][0] + " at level " + str(primaryWeaponList[randNum][1]))
            primaryWeapon = str(primaryWeaponList[randNum][0])
            break
    # Secondary Weapon Randomization
    while(0==0):
        randNum = random.randrange(0,len(secondaryWeaponList))
        if secondaryWeaponList[randNum][1] <= levelNum:
            print('success: ' + secondaryWeaponList[randNum][0] + " at level " + str(secondaryWeaponList[randNum][1]))
            secondaryWeapon = str(secondaryWeaponList[randNum][0])
            break
    # Equipment Randomization
    while(0==0):
        randNum = random.randrange(0,len(equipmentList))
        if equipmentList[randNum][1] <= levelNum:
            print('success: ' + equipmentList[randNum][0] + " at level " + str(equipmentList[randNum][1]))
            equipment = str(equipmentList[randNum][0])
            break
    # Special Grenade Randomization
    while(0==0):
        randNum = random.randrange(0,len(specialGrenadeList))
        if specialGrenadeList[randNum][1] <= levelNum:
            print('success: ' + specialGrenadeList[randNum][0] + " at level " + str(specialGrenadeList[randNum][1]))
            specialGrenade = str(specialGrenadeList[randNum][0])
            break
    # Perk 1 Randomization
    while(0==0):
        randNum = random.randrange(0,len(perk1List))
        if perk1List[randNum][1] <= levelNum:
            print('success: ' + perk1List[randNum][0] + " at level " + str(perk1List[randNum][1]))
            perk1 = str(perk1List[randNum][0])
            break
    # Perk 2 Randomization
    while(0==0):
        randNum = random.randrange(0,len(perk2List))
        if perk2List[randNum][1] <= levelNum:
            print('success: ' + perk2List[randNum][0] + " at level " + str(perk2List[randNum][1]))
            perk2 = str(perk2List[randNum][0])
            break
    # Perk 3 Randomization
    while(0==0):
        randNum = random.randrange(0,len(perk3List))
        if perk3List[randNum][1] <= levelNum:
            print('success: ' + perk3List[randNum][0] + " at level " + str(perk3List[randNum][1]))
            perk3 = str(perk3List[randNum][0])
            break
    # Death Streak Randomization
    while(0==0):
        randNum = random.randrange(0,len(deathStreakList))
        if deathStreakList[randNum][1] <= levelNum:
            print('success: ' + deathStreakList[randNum][0] + " at level " + str(deathStreakList[randNum][1]))
            deathStreak = str(deathStreakList[randNum][0])
            break         
    return

def Randomize():
    try:
        inp = int(InputLevel.get())
    except ValueError:
        OutputVar.set('Incompatible Input.\nPlease enter a number from 1 to 70.')
        return
    if(inp <= 70 and inp >= 1):
        reroll(inp)
    else:
        OutputVar.set('Incompatible Input.\nPlease enter a number from 1 to 70.')
        return
    OutputVar.set('PRIMARY:\t\t\t' + primaryWeapon + "\nSECONDARY:\t\t" + secondaryWeapon + "\nEQUIPMENT:\t\t" + equipment + "\nSPECIAL GRENADE:\t\t" + specialGrenade
    + "\nPERK 1:\t\t\t" + perk1 + "\nPERK 2:\t\t\t" + perk2 + "\nPERK 3:\t\t\t" + perk3 + "\nDEATH STREAK:\t\t" + deathStreak)
    return
    
 

Label(Screen,text="Enter Text").grid(row=2,column =0)
InputLevel = StringVar()
TextBox = Entry(Screen,textvariable=InputLevel).grid(row=2,column = 1)
 
Label(Screen,text=" ").grid(row=3,column =0)
OutputVar = StringVar()
TextBox = Label(Screen,anchor="w",textvariable=OutputVar).grid(row=3,column = 1)

B = Button(Screen,text="Randomize",command=Randomize, relief = GROOVE).grid(row=2,column=2,columnspan = 3)
 
mainloop()