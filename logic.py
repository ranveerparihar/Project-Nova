import time 
print("==============")
print("Project Nova")
print("==============")
intro = "you are outside nexus corp"
mission = "Reach the NOVA CORE and shut down the facility before the reactor overloads"
for char in mission:
    print(char,end = "",flush = True)
    time.sleep(0.02)
print()
stats = {
    "hlth": 100,
    "tkn": 2500,
    "sec_alrt":0
}
print("health: ",stats["hlth"])
print("token: ",stats["tkn"])
print("Alert%: ",stats["sec_alrt"])
lvl = 1
print("level: ",lvl)
while (lvl <= 1): 
    print(""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
          [ MAIN GATE ] 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
        NEXUS CORPORATION 
        SECURITY: ACTIVE 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
""") 
    print("you are at the main gate,make a choice!") 
    choices = ["a","b","c"] 
    print("a. Search the security booth")    
    print("b. Inspect the emergency notice board") 
    print("c. Try forcing the gate open") 
    print("d.Enter Security password for the main gate!") 
    choice_main = str(input("make a choice from a,b,c: ")) 
    time.sleep
 
    if (choice_main == "a"): 
        print(""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
        [ SECURITY BOOTH ] 
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
          __________________ 
         /                  \\ 
        /    __________      \\ 
       |    |          |      | 
       |    |           |      | 
       |    |  SKULL    |      | 
       |    |___________|      | 
       |                      | 
       |      EMPTY...        | 
       |______________________| 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
""") 
        print("the security booth is empty") 

    elif (choice_main == "b"): 
        print(""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
          [ NOTICE BOARD ] 
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
       ┌───────────────────────┐ 
       │   NEXUS CORPORATION   │ 
       │                       │ 
       │   ⚠ SECURITY NOTICE ⚠ │ 
       │                       │ 
       │  Emergency Access     │ 
       │  Code: 2749           │ 
       │                       │ 
       │  DO NOT SHARE THIS    │ 
       │  CODE WITH ANYONE.    │ 
       │                       │ 
       │  ───────────────────  │ 
       │  LAST UPDATED: 03:17  │ 
       └───────────────────────┘ 
 
       Something has been scratched 
       into the wall beneath it: 
 
             "THEY KNOW." 
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
""") 

    elif(choice_main == "c"): 
        text = "forcing the gate open..." 
        health = stats["hlth"] = 0
        sec_alert = stats["sec_alrt"] = 100
        for i in text: 
            print(i,end="",flush = True) 
            time.sleep(0.02) 
        print() 
        print("you have been caught and shot by the security turrets!!") 
        print("-100hp") 
        print("Alert%",sec_alert)
        print("remaining health: ",(stats["hlth"])) 
        print("GAME OVER!")


    elif(choice_main == "d"): 
        code = 2203
        print(""" 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
        [ SECURITY TERMINAL ] 
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
 
        ┌─────────────────────┐ 
        │                     │ 
        │   NEXUS SECURITY    │ 
        │                     │ 
        │   ENTER ACCESS CODE │ 
        │                     │ 
        │      [ _ _ _ _ ]    │ 
        │                     │ 
        │   STATUS: LOCKED    │ 
        │                     │ 
        └─────────────────────┘ 
 
        [1] [2] [3] 
        [4] [5] [6] 
        [7] [8] [9] 
        [*] [0] [#] 
 
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
""") 
        code_input = int(input("enter the Numerical code!")) 
        if (code_input == code): 
            print("ACCESS GRANTED!") 
            lvl +=1 







