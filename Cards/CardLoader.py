import json
from Cards import CardFunctions as cFuncs

class Card:
    def __init__(
        self,
        strName,
        strType,
        strText,
        intCost,
        intReturn,
        fncRulesText
    ):

        self.Name     = strName
        self.Type     = strType
        self.Text     = strText
        self.Cost     = intCost
        self.Return   = intReturn
        self.Function = fncRulesText

<<<<<<< HEAD
    def play(self):
        '''
        1. Pay Cost
        2. For i in self.Function: excute i.
        '''
        pass

def parseCardFunction(lstCardText):
    pass

def parseCardFunctionIntoStack(objCard):
    stack = []
    for i in range(len(objCard.Function)):
        match objCard.Function[i]:
            pass
            #TODO: Add cardFunctions -> stack.
            
>>>>>>> refs/remotes/origin/main
def loadCard(strFileName):
    with open(strFileName, 'r') as f:
        data = json.load(f)

    card = Card(
        data['Name'],
        data['Type'],
        data['Text'],
        data['Cost'],
        data['Return'],
        data['Function']
    )
    return card
