
def target(lstZone):
    print('target:')
    for i in range(len(lstZone)):
        print(f'{i+1}) {lstZone[i]}')
    return input('')

def deal(intDamage, objTarget):
    objTarget.Life -= intDamage

