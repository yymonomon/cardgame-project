
def target(zone):
    print('target:')
    for i in zone:
        print(i)
    return input('')

def deal(intDamage, objTarget):
    objTarget.Life -= intDamage

