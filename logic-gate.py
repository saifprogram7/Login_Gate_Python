#Logic Gate Concept AND
firstlightbulb = True
secondlightbulb = False
if firstlightbulb and secondlightbulb == True:
    print("The Lightbulb is turned on")
else:
    print("The Lightbulb is turned off")
#Logic Gate Concept AND example security
authorisationpassone = 1
authorisationpasstwo = 0
if authorisationpassone and authorisationpasstwo == 1:
    print("Access Granted to the Vault")
else:
    print("Access Denied to the Vault")
#Logic Gate Concept OR
networkswitch = True
networkswitchone = False
if networkswitch or networkswitchone == True:
    print("Network is Online")
else:
    print("Network is Offline")
#Logic Gate Concept OR Example Train Ticket
trainticket = True
contactlesspayment = False
if trainticket or contactlesspayment == True:
    print("Welcome on Board")
else:
    print("You need a ticket / contactless payment to board this train")
#Logic Gate Concept NOT
switch = True
if switch == False:
    print("Switch is OFF")
else:
    print("The Switch is ON")