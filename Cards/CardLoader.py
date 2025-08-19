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

def parseCardFunction(lstCardText):
    data = []
    for i in range(len(lstCardText)):
        match lstCardText[i]:
            case 'target':
                i++
                data.append(cFuncs.target(lstCardText[i]))
            case 'deal':
                i++
                data.append(cFuncs.attack)

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
