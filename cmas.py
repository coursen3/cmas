from collections import defaultdict
from random import randint
import argparse

parser = argparse.ArgumentParser(description="Generate gift pairings")
parser.add_argument("N", type=int, help="Number of givers for each receiver")
args = parser.parse_args()

Ngift = args.N 
couples = \
(("John", "Perrine"), 
("Matt", "Mer"), 
("Laura", "Alex"), 
("Jeff", "Sarah"))

def removeRandomItem(l):
    return l.pop(randint(0, len(l)-1))
    
def draw(people, exclude, Ngift):
    gifts = defaultdict(list)
    draw = people*Ngift
    for giver in people:
        validRec = [rec for rec in draw if rec not in exclude[giver]]
        validRec = list(set(validRec))
        if len(validRec) < Ngift: 
            return None
            
        for _ in range(Ngift):
            rec = removeRandomItem(validRec)
            gifts[giver].append(rec)
            draw.remove(rec)
        
    return gifts
    
people = [p for c in couples for p in c]
exclude = dict([(p,c) for c in couples for p in c])
gifts = None
for _ in range(1000):
    gifts = draw(people, exclude, Ngift)
    if gifts is not None: break
    
if not gifts:
    print "Draw failed"    
else:
    print "Giver: Receiver"
    for giv, rec in gifts.iteritems():
        print "%s: %s" % (giv, ", ".join(rec))
