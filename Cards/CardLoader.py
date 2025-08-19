import json
from Cards import CardFunctions as cFuncs

class Card:
    def __init__(
        self,
        strName,
        strType,
        strText,
        intStrike,
        intBlock,
        lstCost,
        lstReturn,
        fncRulesText
    ):

        self.Name     = strName
        self.Type     = strType
        self.Text     = strText
        self.Strike   = intStrike
        self.Block    = intBlock
        self.Cost     = lstCost
        self.Return   = lstReturn
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
        data['Strike'],
        data['Block'],
        data['Return'],
        data['Function']
    )
    return card
