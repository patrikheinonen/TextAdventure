import mysql.connector
import random
import pygame

#opens map

def map():
   print("the map:")
   pygame.init()     
   width=500;
   height=500
   screen = pygame.display.set_mode((width, height ))
   pygame.display.set_caption('The game map')
   image = pygame.image.load(r'C:\Users\Pate\Documents\ProjextTexdAD\Kartta2.PNG')
   screen.blit(image, (0,0)) 
   pygame.display.flip() 
   map = True
   while (map):
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               map = False

   pygame.quit()


def location():
     cur = db.cursor()
     sql = " select location.Id from location, player where location.Id = player.Location"
     cur.execute(sql)
     res = cur.fetchall()
     return res [0] [0]

def show_location():
    cur = db.cursor()
    sql = "SELECT Description, Details FROM LOCATION WHERE Id = (SELECT Location FROM Player)"
    cur.execute(sql)
    for row in cur:
        print (row[0])
        if (row[1]!=""):
            print(row[1])
    return

def show_objects():
    cur = db.cursor()
    sql = "SELECT refname FROM OBJECT WHERE Location = (SELECT location FROM player) AND Available = TRUE"
    cur.execute(sql)
    if cur.rowcount>=1:
        print("You see the following:")
        for row in cur.fetchall():
                print (" - " + row[0])
        print("")         
    return

def show_enemies():
     cur = db.cursor()
     sql = "SELECT Refname FROM enemies WHERE Location = (SELECT location FROM player)"
     cur.execute(sql)
     if cur.rowcount>=1:
          print("The living things you see:")
          for row in cur.fetchall():
               print(" - " + row[0])
     return
          
def show_passages():
    cur = db.cursor()
    sql = "select location.Description, direction.Description FROM player, location, passage inner JOIN DIRECTION ON PASSAGE.Direction=DIRECTION.Id WHERE passage.Source = player.location AND location.Id = passage.Destination"
    cur.execute(sql)
    print("you can move to these places: \n")
    for row in cur.fetchall():
        print (row[0] , row[1])        
    return

#purpose of show_passages2 is to return all directions in a list so we can
#compare the players action to that list and see if he can move or not
def show_passages2():
    cur = db.cursor()
    sql = "select direction FROM player, location, passage inner JOIN DIRECTION ON PASSAGE.Direction=DIRECTION.Id WHERE passage.Source = player.location AND location.Id = passage.Destination AND passage.locked = FALSE"
    cur.execute(sql)
    res = cur.fetchall()
    lista = []
    if cur.rowcount>=1:
        for row in res:
            lista.append(row[0])     
    return lista 

def get_target(target):
    cur = db.cursor()
    sql = "UPDATE object SET Location=NULL, Available=FALSE, Takeable = FALSE, PlayerId = 'Player' WHERE Refname= '" + target + "' AND Location= (SELECT Location FROM player) AND Available=TRUE AND Takeable=TRUE"
    cur.execute(sql)
    if cur.rowcount==1:
        print("You take the " + target + ".")
    else:
        print("You can't take the " + target + ".")
    return cur.rowcount

def drop_target(target):
    cur = db.cursor()
    sql = "UPDATE object SET Available=TRUE, Takeable=TRUE,  PlayerId = NULL, Location= (SELECT location FROM player) WHERE Refname= '" + target + "' AND PlayerId = 'Player'"
    cur.execute(sql)
    if cur.rowcount==1 and target!="stone":
        print("You drop the " + target + ".")
    elif location()=="Tomb" and target=="stone":
        print("The stone falls to the ground")
    else:
        print("You can't drop the " + target + ".")
    return cur.rowcount 


def inventory():
    cur = db.cursor()
    sql = "SELECT refname FROM object WHERE PlayerId = 'Player'"
    cur.execute(sql)
    res = cur.fetchall()
    lista2 = []
    if cur.rowcount>=1:
        print("You carry the following items:")
        for row in res:
            print (" - " + row[0])
            lista2.append(row[0])
    else:
        print("You don't carry anything.")
    return lista2

#purpose of inventory2 is that we can check if the player has an certain item
#in his inventory by appending every row to a list type
#but we do this in def inventory() this is here just to show the idea
#
def inventory2():
    cur = db.cursor()
    sql = "SELECT refname FROM object WHERE PlayerId = 'Player'"
    cur.execute(sql)
    res = cur.fetchall()
    lista = []
    if cur.rowcount>=1:
        for row in res:
            lista.append(row[0])
    return lista

def look_around():
    print("-"*80)
    show_location()
    if (location() != "Freedom"):
          show_enemies()
          show_objects()
          show_passages()   
    return

def look(target):
    cur = db.cursor()
    sql = "Select object.Description, Details FROM object Where Refname = '" + target + "' AND ((Location = (SELECT location FROM player) AND Available=TRUE) OR (PlayerID = 'Player'))"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall() :
            print (row[0],row[1])
    else:
        print("You see nothing of interest.");
    return


def look_enemy(target):
    cur = db.cursor()
    sql = "Select description from enemies where refname =  '" + target + "' and location = (select player.Location from player)"
    cur.execute(sql)
    if cur.rowcount>=1:
        for row in cur.fetchall() :
            print (row[0])
    else:
        print("No living things around here.");
    return

def move(direction):
    cur = db.cursor()
    sql = "UPDATE player SET location = (SELECT Destination FROM Passage WHERE Direction = '" + direction + "' AND Source = player.Location AND LOCKED = 0)"
    cur.execute(sql)
    return

def enemy_level():
     cur = db.cursor()
     sql = "SELECT lvl FROM enemies, player Where enemies.Location = player.Location"
     cur.execute(sql)
     res = cur.fetchall()
     return res[0][0]

def sword_level():
     cur = db.cursor()
     sql = "Select max(lvl) From object Where playerId = 'Player'"
     cur.execute(sql)
     res = cur.fetchall()
     return res[0][0]     

    
def kill(target):
     cur = db.cursor()
     sql = "Update enemies set location = 'Dead' Where location = (SELECT location FROM player) and refname = '" + target + "'"
     cur.execute(sql)
     return
    
def death():
     cur = db.cursor()
     sql = "update Player Set location = 'Dead'"
     cur.execute(sql)
     return
    
    
#sets master items to takeable
def master_available():
     cur=db.cursor()
     sql= "update object set takeable = TRUE where refname = 'Armour' or refname = 'MasterSword'"
     cur.execute(sql)
     return

def enemy_location1():
    cur = db.cursor()
    sql = "Select enemies.location From enemies, player Where enemies.location = player.Location"
    cur.execute(sql)
    res=cur.fetchall()
    if len(res) > 0:
        return res [0][0]
    else:
        return 'none'
      
#this and the enemy_location1 have clear purposes in the code    
def enemy_location(target):
    cur = db.cursor()
    sql = "Select location from enemies where location = (select player.Location from player) and refname = '" +target+ "'"
    cur.execute(sql)
    res = cur.fetchall()
    lista3 = []
    if cur.rowcount>=1:
        for row in res:
            lista3.append(row[0])
    return lista3

def deadlist():
     cur = db.cursor()
     sql = "SELECT id FROM enemies Where location = 'Dead'"
     cur.execute(sql)
     res = cur.fetchall()
     lista = []
     if cur.rowcount>=1:
         for row in res:
             lista.append(row[0])
     return lista
    
def doorlist():
     cur = db.cursor()
     sql = "SELECT id FROM object Where location = 'Dead'"
     cur.execute(sql)
     res = cur.fetchall()
     lista = []
     if cur.rowcount>=1:
         for row in res:
             lista.append(row[0])
     return lista

# check the code and you see why this is pretty useful    
def setobjecttodeath(target):
     cur = db.cursor()
     sql = "Update object set location = 'Dead', PlayerId = NULL Where PlayerId = 'Player' and refname = '" + target + "'"
     cur.execute(sql)
     return    

    
# Drops an item from the player permanently. player can see it but cant take it
def drop2(target):
    cur = db.cursor()
    sql = "UPDATE object SET Available = TRUE, PlayerId = NULL, Location= (SELECT location FROM player) WHERE Refname= '" + target + "' AND PlayerId = 'Player'"
    cur.execute(sql)
    return

def marco_friend():
     cur = db.cursor()
     sql = "update enemies set Relation = 'Friend' WHERE Id = 'Marco'"
     cur.execute(sql)
     return
    
def enemyupdate():
     cur = db.cursor()
     sql = "update enemies set Relation = 'Enemy' WHERE Id = 'Marco' or Id ='Lisa' or Id ='Steve'"
     cur.execute(sql)
     return

def relation():
     cur = db.cursor()
     sql = "select relation FROM enemies, player WHERE enemies.Location = player.Location"
     cur.execute(sql)
     res = cur.fetchall()
     if len(res) > 0:
         return res [0] [0]
     else:
         return 'none'
        
def friend():
     cur = db.cursor()
     sql = "update enemies set Relation = 'Friend' WHERE enemies.Location = (Select location from player)"
     cur.execute(sql)
     return
       

def survname(name):
    cur = db.cursor()
    sql = "select id FROM enemies WHERE id= '" + name + "'"
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) > 0:
        return res[0][0]
    else:
        return 'none'      


def surv_loc(name):
    cur = db.cursor()
    sql = "select location FROM enemies WHERE id='" + name + "'"
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) > 0:
        return res[0][0]
    else:
        return 'none'

def update_passage(lock, sourc, dest):
    cur = db.cursor()
    sql = " update passage set locked = " + lock + " where source = '" +sourc+ "' and destination = '" + dest + "'"
    cur.execute(sql)
    return


def object_available(available, name):
    cur = db.cursor()
    sql = "update object set available = " + available + " where refname = '" + name + "'"
    cur.execute(sql)
    return
   

def CogWheels(name):
    cur = db.cursor()
    sql = "select id from object where refname = '" + name + "'"
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) > 0:
        return res[0][0]
    else:
        return 'none'

     
def tombdoorblock():
    cur = db.cursor()
    sql = "select available from object where refname = 'tombdoor'"
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) > 0:
        return res[0][0]
    else:
        return 'none'

def objects(target):
    cur = db.cursor()
    sql = "select refname from object where refname = '" + target + "'"
    cur.execute(sql)
    res = cur.fetchall()
    if len(res) > 0:
        return res[0][0]
    else:
        return 'none'
        

#well moves things located in the enemies table theres also survivals.
def move_enemies(location, name):
   cur = db.cursor()
   sql = "update enemies set location = '" + location + "' where id =  '" + name + "'"
   cur.execute(sql)
   return



#connection open
db = mysql.connector.connect(host="localhost",
                      user="PatrikH",
                      passwd="dbpass",
                      db="tekstiseikkailutest",
                      buffered=True)






action = ""
# angry counter

angry = 0

# different counters to ensure that things wont happen any more times than we want them

count = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count7 = 0

#clear console
print("\n"*1000)

#show the player his/her location
look_around()


helplist = ["quit", "get", "take", "drop", "look", "examine", "view", "inventory", "i", "use", "kill", "hit", "talk", "ask", "e = east", "w = west", "n = north", "s = south", "ne = northeast", "sw = southwest", "reset", "rules", "map"]
steveasklist = ["ship"]
marcoasklist = ["steve", "steelsword", "sircularsaw"]
rules = ["To win the game you must escape the island.", "You cant take, use or drop if an enemy is in the same area.", "Your actions will affect the relationship between you and the survivals"]


while action!="quit" and location() !="Freedom":
    print("")
    input_string=input("Your action? ").split()
    if len(input_string)>=1:
        action = input_string[0].lower()
    else:
        action = ""
    if len(input_string)>=2:
        target = input_string[len(input_string)-1].lower()
    else:
        target = ""
    print("")

    #get
    if (action=="get" or action=="take") and target!="":
        if enemy_location1() == location() and relation() == "Enemy":
            print ("I don't think that is a smart move.")
        if objects(target) not in inventory2():
           if location() == 'Camparea' and target == 'sircularsaw':
              if survname('troll2') in deadlist() and survname('Marco') not in deadlist():
                 print('Marco gives you the sircular saw with a great smile. You know that it is not just for cutting wood.')
                 get_target(target)
                
              elif survname('Marco') in deadlist():
                 print ("You take the sircularsaw and there is no one who can stop you.")
                 get_target(target)
              else:
                 print ('Marco: "Hey! Do not take that!"')

            #get torch    
           elif location() == 'Shelter1' and target == 'torch':
              if relation() == 'Friend':
                get_target(target)
              elif survname('Lisa') in deadlist():
                 print("Lisa died so she cant tell me not to take her torch.")
                 get_target(target)
              else: 
                 print('Lisa: "If you bring me a Rope you can take my torch."')
                
            #get redkey   
           elif location() == 'Shelter2' and target == 'redkey':
              if relation() == 'Friend':
                 get_target(target)
              elif survname('Steve') in deadlist():
                 print("This key must be powerfull.")
                 get_target(target)
              else:
                 print('Steve: "You like that key?  So do I. Make me happy and you might get it."')

           #get steelsword
           elif location() == 'Camparea' and target == 'steelsword':
              if relation() == 'Friend':
                 print('Marco gives you the steel sword. \nMarco: "Good luck! My friend."')
                 get_target(target)
              elif survname('Marco') in deadlist():
                 print ("You take the steel sword over Marco's dead body.")
                 get_target(target)
              else:
                 if angry <= 1:
                     print ('Marko: "Hands off! That is not yours."')
                     angry = angry + 1
                 else:
                     print('Marco picks the steel sword and points it at you. \nMarco: "I think it is the time, for you to leave the camp."')
                     enemyupdate()
                     print("Survivors do not look friendly anymore...")
           else:
               get_target(target)
        else:
           print("You allready have a " + target)
                              
    #help
    elif action == "help":
         print("The possible actions are: " )
         print("")
         for action in helplist:
              print("- " + action)
    #clear
    elif action == "clear":
         print("\n"*1000)
         look_around()


    #rules
    elif action == "rules":
         print("The rules are: ")
         print("")
         for rule in rules:
              print(rule)

    #map
    elif action == "map":
        map()

 
    # drop
    elif action=="drop" and target!="":
         if location () == enemy_location1() and relation() == "Enemy":
              print("I dont think that is a smart move.")
         else:
              drop_target(target)
         

    # look
    elif (action=="look" or action=="examine" or action=="view"):
        if target=="" and location() != "Jng2":
             look_around()
        else:
            look(target)
    
        if location()=="Jng2" and target =="":
            object_available('TRUE', 'Greenkey')
            look_around()                  
                  

        elif target == "troll" or target == "giantspider" or target == "demon" or target == "lisa" or target== "steve" or target== "marco":
              look_enemy(target)


    # inventory
    elif action=="inventory" or action=="i":
        inventory()

       # use pitääks olla if putki vai elif
    elif action=="use" and relation()!="Enemy":
        if target=="":
            print("I do not know what to use.")
        if location () == enemy_location1() and relation() == "Enemy":
             print("I do not think that is a smart move")
        elif location() =="Cave" and (target== "smallcogwheel" or target=="sircularsaw" or target=="largecogwheel"):
            setobjecttodeath(target)
            print("You put the " + target+ " into the door.")

        elif objects(target) in inventory2() and (target=="greenkey" or target =='bluekey' or target=='redkey'):
           if location()=="Cave":
              if target=="greenkey":
                  if tombdoorblock() == 1:
                       if objects('GreenKey') in inventory2():
                            update_passage('FALSE', 'Cave', 'Tomb')
                            print("The door to the tomb unlocks.")
                            
                  else:
                       print("I do not know where to use this key.")
              if target =='bluekey' or target=='redkey':
                
                  if tombdoorblock() == 1:
                       print("The key does not work.")
                  else:
                       print("I do not know where to use this key.")
           else:
              print("I do not know where to use this key.")
             
        elif target=="lighter" or target=="torch":
             if objects('Lighter') in inventory2() and objects('Torch') in inventory2():
                  print("I ignite the torch with a lighter, I should be able to see in dark now.")
                  update_passage('FALSE', 'Jng3', 'Cave')
                  steveasklist.append("stonedoor")
             elif objects('Lighter') in inventory2() and objects('Torch') not in inventory2():
                print("The lighter seems to work.")
             else:
                print("You can not do that.")

        elif location()=="Tomb" and target=="stone" and objects('Stone') in inventory2():
             y = random.randint(0, 1)
             if y == 1:
                  print("I hit the shot and manage to drop the weapon and armour!")
                  print("The stone vanishes after hitting those powerfull items. ")
                  master_available()
                  setobjecttodeath(target)
             else:
                  print("I missed the throw!")
                  drop_target(target)
        else:
            print("You can not do that.")
                             

     
    #hit ( if you wonder why we did it like this it is becouse we wanted different kind of outcomes to situations)   
    elif action=="kill" or action=="hit":
        if target == ""  and relation() != "Enemy":
            print("There is nothing to kill.")
        elif target == "" and relation() == "Enemy":
             print("You see an enemy just type its name after kill.")
        if location()!="Dead":
            if target=="giantspider" or  target=="troll"  or target=="demon" or target=="marco" or target=="lisa" or target=="steve":  
                if location() in enemy_location(target):                
                    if sword_level() != None  and sword_level() != 0:
                        if enemy_level() <= sword_level():
                            kill(target)

                            if target=="marco":
                                if objects('Steelsword') not in inventory2():
                                    print("Marco tries to reach for his sword, but he is too slow for you.")
                                else:
                                    print('Marco sees that you are raising your sword. He tries to take something to defence himself, but you are too strong for him."')
                            elif target=="lisa":
                                print("Lisa's eyes look at you with great terror.")
                            elif target=="steve":
                                print('Steve: "How can you live with yourself?"')
                                
                            print("You killed " + target)
                        elif enemy_level() > sword_level():
                           if objects('Armour') in inventory2() and target == 'demon': 
                               print("Your weapon does not harm the " + target)
                           else:
                              death()
                              print("The best weapon you had was too weak. You died.")          
                    else: 
                         if target =="marco":
                              print('Marco picks up his sword. \nMarco: "You are a fool!"')
                              death()
                         elif target == "steve":
                              print("You and Steve start fighting. Steve manages to grab a metal pipe and hits you with great force.")
                              print("You died.")
                              death()
                         elif target == "lisa":
                              print("You and Lisa start fighting. Lisa takes a torch and sets you on fire.")
                              print("You died.")
                              death()
                         if objects('Armour') in inventory2() and target == "demon":
                              print("Fighting a demon without any weapons, a brave move")
                         else:
                            print("You died.")
                            print("You fought a person/monster without a weapon, smart.")
                            death()
                else:
                     print("I do not see " + target + " around here")   
            else:
                print("You can not kill a " + target)
        else:
           print("You are dead, you are too weak to kill anything that does not work here")

        
 #talk (keep in mind that neither steve or marco will talk to an enemy. Steve will only talk to a friend while marco will also talk to a neutral.)
    elif (action=="talk" or action=='ask'):
         if (surv_loc('Marco') == location() or surv_loc('Steve') == location()):     
              if relation() == 'Friend' and surv_loc('Steve') == location():
                 if target == 'steve' or target == "tombdoor" or target == "stonedoor" or target == "ship" or target == "demon":
                    if target == 'steve':
                       print ('Steve: "What you would like to ask about?"')
                       for question in steveasklist:
                          print(" - ", question)
                    elif target =='tombdoor':
                       print('Steve: "I think you should search the jungle area with thick vegitation. "')
                    elif target =='stonedoor':
                       print('Steve: "Look for cogwheels i have seen them on my adventures."')
                    elif target =='ship':
                       print('Steve: "We have fixed the ship on the shore but a demon is guarding it and we can not leave the island."')
                       steveasklist.append("demon")
                    elif target =='demon':
                       print('Steve: "I have never seen it personally but I know for sure that its guarding the ship. It seems that the demon wants no one to leave the island. The demon seems to think that we are its possesion."')
                 else:
                    print('Steve: "I do not understand you"')
              elif relation()!= "Enemy" and surv_loc('Marco') == location():
                 if target == 'marco' or target == "steve" or target == "steelsword" or target =="sircularsaw":
                    if target == 'marco':
                       print ("Greetings young one. \nAsk about: ")
                       for question in marcoasklist:
                          print(" - ", question)
                    elif target =='steve':
                        print('Marco: "Steve is a hard person to get to know. Bring him a coconut. I think that might work."')
                    elif target == 'steelsword':
                        print('Marco: "This sword is strong enough to kill a giant spider. Only my friends can borrow it. And my friends are those who are Steves friends."')
                    elif target == 'sircularsaw':
                        print('Marco: "That is very important to us since we use it to chop our firewood. It is as important as water. It is so hard to get water nowadays becouse there is a troll guarding the lake near the mountains"' )
                 else:
                    print('Marco: "I do not understand you"')
              if surv_loc('Steve') == location() and relation()=='Neutral':
                 print('Steve: "Hmph."')
              if relation() == "Enemy":
                 print('"I will not talk to you."')
         else:
            print("You cant talk to a " + target)

               
        
    # move
    elif action=="n" or action=="e" or action=="s" or action=="w" or action=="ne" or action=="sw":
        if action in show_passages2():
           move(action)
           look_around()
        else:
           print("You can not move to that direction.")

    #reset       
    elif action == "reset":
         print("\n"*1000)
         db.rollback()
         look_around()
         count = 0
         count2 = 0
         count3 = 0
         count4 = 0
         count5 = 0
         count7 = 0
         angry = 0

         
    elif action == "":
         print("You wrote nothing.")
                   
    elif action!="quit" and action!="":
        print("I do not know how to. " + action)

     # siirtää mainbossin caveeb ja luktisee reitin cavesta junglee
    if location() == "Tomb" and surv_loc('Mainboss') != "Dead":
        update_passage('TRUE', 'Cave', 'Jng3')
        move_enemies('Cave', 'Mainboss')


    if surv_loc('Mainboss') == "Dead" and count7 < 1:
         update_passage('FALSE', 'Cave', 'Jng3')
         count7 += 1
         if surv_loc('Steve') != "Dead":
             move_enemies('BchWs', 'Steve')
         if surv_loc('Marco') != 'Dead':
             move_enemies('BchWs', 'Marco')
         if surv_loc('Lisa') != 'Dead':
             move_enemies('BchWs', 'Lisa')              
       
          
    if CogWheels('SmallCogWheel') in doorlist() and CogWheels('LargeCogWheel') in doorlist() and CogWheels('SircularSaw') in doorlist():
        if count < 1:
           print("The stone door unlocks.")
           object_available('TRUE', 'Tombdoor')
           steveasklist.append("tombdoor")
           count = count +1

            
     #The armor not in inventory player dies     
    if location() == surv_loc('Mainboss'):
        if objects('Armour') not in inventory2():
            print("Last thing you see is the Demon raising its hand. The nails look very sharp.")
            death()
            look_around()

        #the boss cant harm the player if he has master armour    
        if count2 < 1:
             if objects('Armour') in inventory2():
                  count2 += 1
                  print("The Demon can not harm you. But it blocks your way. Time to get rid of that annoyance.")
                  

     # if someone doesent like you go away (each of them will only tell you this one time when you roam in their territory once you leave it they can say it again.
    if location() == 'Camparea' and relation() == 'Enemy':
         if count3 < 1:
              print('Marco looks at you with burning eyes.')
              count3 = count3 +1
    if location() == 'Shelter2' and relation() == 'Enemy':
         if count4 < 1:
              print('Steve: " I am not your friend. Go away!"')
              count4 = count4 +1
    if location() == 'Shelter1' and relation() == 'Enemy':
         if count5 < 1:
              print('Lisa: "Please step out of my tent."')
              count5 = count5 +1
    if (location() == 'planepiece'):
       count3 = 0
       count4 = 0
       count5 = 0
         
    if location() == 'BchWs' and (surv_loc('Lisa') == location() or surv_loc('Steve') == location() or surv_loc('Marco') == location()):
         if relation() == 'Enemy':
              print('You hear a shout: "Hey! Where do you think you are going with our ship?"')
              print("Player: 'Heres alot of supplies to make another ship. Bye!")
         else:
              print("Survivals are glad and ready to  escape the island with you.")
              

    if survname('Marco') not in  deadlist() and survname('Lisa') not in  deadlist() and survname('Steve') not in  deadlist():
       if objects('Coconut') in inventory2() and location() == 'Shelter2':
          friend()
          drop2('coconut')
          print('Steve is very glad when you bring a coconut to him. \nSteve: "Thank you fellow!"')
     #Pelaaja tuo köyden Lisalle
       if location() == 'Shelter1' and objects('Rope') in inventory2():
          friend()
          drop2('rope')
          print('Lisa: "Thank you! Now I can make more torches. Wait what? You killed a giantspider?"')
     #Jos steve on kaveri, niin marcokin on
       if location() == "Shelter2" and relation() == 'Friend':
          marco_friend()
     #Enemy, jos kukaan NPC:tä on kuollut
    else:
       enemyupdate()


          
if location()=="Freedom":
    print("You managed to escape the island. \nwell done, You win!!!")
else:
    print("I hope you will play again. ")


db.close()

