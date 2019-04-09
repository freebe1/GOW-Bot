import time

Settings.MoveMouseDelay = 0.1
Settings.WaitScanRate = 1
Settings.ObserveScanRate = 1
battle = "ToBattle.png"
bombon = Pattern("bombon.png").similar(0.75)
pheonix = Pattern("pheonix.png").similar(0.75)
pheonixtang = "pheonixtang.png"
pheonixdeath = Pattern("pheonixdeath.png").similar(0.60)
pheonixpos = Location(86, 157)
weapon = Pattern("weapon.png").similar(0.75)
red = Pattern("red.png").similar(0.80)
yellow = Pattern("yellow.png").similar(0.80)
skull = "skull.png"
blue = Pattern("blue.png").similar(0.80)
purple = Pattern("purple.png").similar(0.80)
green = Pattern("green.png").similar(0.80)
brown = Pattern("brown.png").similar(0.85)
board = Region(180,110,470,469)
screen = Region(0,0,803,632)
myside = Region(9,97,155,498)
cast = "Cast.png"
myturn1 = Region(25,49,155,97)
myturn2 = "myturn.png"

enemyturn1 = Region(657,37,155,118)
enemyturn2 = "myturn.png"
again = "again.png"
lvup = "lvup.png"
choose = "choose.png"
skip = "Skip.png"
victory = "victory.png"
loading = "loading.png"
phres = Region(3,95,170,129)
weres = Region(6,471,163,128)

match = True
running = True
battling = False
count = 0
loop = 0

#def runHotkey(event):
#        global running
#        running = False

#Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

def matchP(sx, sy, tx, ty, mArray):
    if ((tx >= 0 and tx < 8) and (ty >= 0 and ty < 8)):
        if (mArray[sx][sy]==1 and mArray[tx][ty]==1):
            return True    
    return False

def matching(mArray):
    for i in range(8):
        for j in range(8):
            if (j + 3 < 8): # check 
                if (mArray[i][j]==1 and mArray[i][j+1]==1 and mArray[i][j+2]==0 and mArray[i][j+3]==1):#ooxo
                    dragDrop(Location(192 + (59*(j+3)),130 + (59*i)), Location(192 + (59*(j+2)),130 + (59*i)))
#                    break
                if (mArray[i][j]==1 and mArray[i][j+1]==0 and mArray[i][j+2]==1 and mArray[i][j+3]==1):#oxoo
                    dragDrop(Location(192 + (59*j),130 + (59*i)), Location(192 + (59*(j+1)),130 + (59*i)))
 #                   break
            if(i + 3 < 8): #check
                if (mArray[i][j]==1 and mArray[i+1][j]==1 and mArray[i+2][j]==0 and mArray[i+3][j]==1):#Vooxo
                    dragDrop(Location(192 + (59*(j)),130 + (59*(i+3))), Location(192 + (59*(j)),130 + (59*(i+2))))
  #                  break
                if (mArray[i][j]==1 and mArray[i+1][j]==0 and mArray[i+2][j]==1 and mArray[i+3][j]==1):#Voxoo
                    dragDrop(Location(192 + (59*j),130 + (59*i)), Location(192 + (59*(j)),130 + (59*(i+1))))
#                    break

                #oxo
            if (j + 2 < 8 and mArray[i][j]==1 and mArray[i][j+2]==1):
                if(matchP(i,j,i-1,j+1,mArray)):
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i-1))), Location(192+(59*(j+1)),130+(59*(i))))
 #                   break
                if(matchP(i,j,i+1,j+1,mArray)):
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i+1))), Location(192+(59*(j+1)),130+(59*(i))))   
#                    break
                #Voxo
            if (i + 2 < 8 and mArray[i][j]==1 and mArray[i+2][j]==1):
                if(matchP(i,j,i+1,j+1,mArray)):#L
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i+1))), Location(192+(59*(j)),130+(59*(i+1))))
                    break
                if(matchP(i,j,i+1,j-1,mArray)):#R
                    dragDrop(Location(192+(59*(j-1)),130+(59*(i+1))), Location(192+(59*(j)),130+(59*(i+1))))
#                    break;
                # xxx
                #  @
                #  o
                # xxx
            if(i+1<8 and mArray[i][j]==1 and mArray[i+1][j]):
                if(matchP(i,j,i-1,j-1,mArray)):#좌상
                    dragDrop(Location(192+(59*(j-1)),130+(59*(i-1))), Location(192+(59*(j)),130+(59*(i-1))))
#                    break;
                elif(matchP(i,j,i-2,j,mArray)):#상상
                    dragDrop(Location(192+(59*(j)),130+(59*(i-2))), Location(192+(59*(j)),130+(59*(i-1))))
#                    break;
                elif(matchP(i,j,i-1,j+1,mArray)):#우상
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i-1))), Location(192+(59*(j)),130+(59*(i-1))))
#                    break;

                if(matchP(i,j,i+2,j-1,mArray)):#좌하
                    dragDrop(Location(192+(59*(j-1)),130+(59*(i+2))), Location(192+(59*(j)),130+(59*(i+2))))
 #                   break;
                elif(matchP(i,j,i+3,j,mArray)):#하하
                    dragDrop(Location(192+(59*(j)),130+(59*(i+3))), Location(192+(59*(j)),130+(59*(i+2))))
#                    break;
                elif(matchP(i,j,i+2,j+1,mArray)):#우하
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i+2))), Location(192+(59*(j)),130+(59*(i+2))))
#                    break;

                # x  x
                # x@ox
                # x  x
            if(j+1<8 and mArray[i][j]==1 and mArray[i][j+1]):
                if(matchP(i,j,i-1,j-1,mArray)):#좌상
                    dragDrop(Location(192+(59*(j-1)),130+(59*(i-1))), Location(192+(59*(j-1)),130+(59*(i))))
#                    break;
                elif(matchP(i,j,i,j-2,mArray)):#좌좌
                    dragDrop(Location(192+(59*(j-2)),130+(59*(i))), Location(192+(59*(j-1)),130+(59*(i))))
#                    break;
                elif(matchP(i,j,i+1,j-1,mArray)):#좌하
                    dragDrop(Location(192+(59*(j+1)),130+(59*(i-1))), Location(192+(59*(j-1)),130+(59*(i))))
#                    break;
              
                if(matchP(i,j,i-1,j+2,mArray)):#우상
                    dragDrop(Location(192+(59*(j+2)),130+(59*(i-1))), Location(192+(59*(j+2)),130+(59*(i))))
#                    break;
                elif(matchP(i,j,i,j+3,mArray)):#우우
                    dragDrop(Location(192+(59*(j+3)),130+(59*(i))), Location(192+(59*(j+2)),130+(59*(i))))
#                    break;
                elif(matchP(i,j,i+1,j+2,mArray)):#우하
                    dragDrop(Location(192+(59*(j+2)),130+(59*(i+1))), Location(192+(59*(j+2)),130+(59*(i))))
#                    break;

def Toarray(color,count):
    try:
        AA = findAll(Pattern(color).similar(0.85))
        mm = getLastMatches()
#        print mm
        a = [[0]*8 for i in range(8)]
        while mm.hasNext():
            cord = mm.next().getTarget()
            a[(cord.y/59)-2][(cord.x/58)-3] = count
        matching(a)
    except FindFailed:
         pass

def ToBattle():
#    wait(battle,3)
    if exists(battle,3):
        screen.click(battle)
        global battling
        battling = True

def exp():
    Toarray(skull,1)
#    spell() 
    Toarray(red,1)
 #   spell()        
    Toarray(purple,1)
#    spell()         
    Toarray(green,1)
#    spell()     
    Toarray(brown,1)
#    spell()     
    Toarray(blue,1)
#    spell()     
    Toarray(yellow,1)
#    spell()

def spell():
    if myturn1.exists(myturn2,1) and screen.exists(bombon,1):
        try:
            screen.click(bombon)
            screen.click(cast)
            wait(2)
        except FindFailed:
            pass
    
    if myturn1.exists(myturn2,1) and (phres.exists(pheonixdeath,1) or phres.exists(pheonixtang,1) or phres.exists(pheonix,1)):
        try:
            screen.click(phres)
            screen.click(cast)
            wait(2)
        except FindFailed:
            pass
#weapon
    if myturn1.exists(myturn2,1) and weres.exists(weapon,1):
        try:
            screen.click(weres)
            screen.click(cast)
            wait(2)
        except FindFailed:
            pass
    regame()
    return 1
    
def regame():
#    stopObserver()
#    wait(4)
    if screen.exists(again):
        screen.click(again)
        global count
        count = 0
        global battling 
        battling = False
        global match 
        match = False
        if screen.exists(lvup):
            screen.click(lvup)
            screen.wait(choose,3)
            stat = find(choose)
            t = stat.getTarget()
            off = t.x
            click(Location(t.x-450, t.y))
            wait(2)
            match = False
            return 1
        else:
            return 1
    else:
        return 1
    return 1

        
while running:
    global match
    match = True
    global count
    loop = loop + 1
    print loop
    now = time.localtime()
    s = "%04d-%02d-%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    print s
#    if not battling:
    ToBattle()

    while match:
#        while(count<2):
#            if screen.exists(bombon):
#                wait(2)
#                screen.click(bombon)
 #               click(cast)
 #               count+=1
 #               wait(2)
        spell()
#        if match and screen.exists(loading,1):
#            wait(2)
#            regame()
#        if match and screen.exists(again,1):
#            regame()
        if match and not screen.exists(loading,1) and not screen.exists(victory,1) and not screen.exists(again,1) and not phres.exists(pheonix,1) and not screen.exists(bombon,1) and not weres.exists(weapon,1):
            exp()
        observe(1)
        screen.onAppear(Pattern("again"),regame)
        
    else:
        pass
            