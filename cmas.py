from collections import defaultdict
from random import randint
import argparse

parser = argparse.ArgumentParser(description="Generate gift pairings")
parser.add_argument("recPerGiver", type=int, help="Number of receivers per giver")
args = parser.parse_args()

couples = \
(("John", "Perrine"), 
("Matt", "Mer"), 
("Laura", "Alex"), 
("Jeff", "Sarah"))

def removeRandomItem(l):
    return l.pop(randint(0, len(l)-1))
    
def draw(givers, receivers, exclude, recPerGiver, giverPerRec):
    gifts = defaultdict(list)
    draw = receivers * giverPerRec
    for giver in givers:
        validRec = [rec for rec in draw if rec not in exclude[giver]]
        validRec = list(set(validRec))
        if len(validRec) < recPerGiver: 
            return None
            
        for _ in range(recPerGiver):
            rec = removeRandomItem(validRec)
            gifts[giver].append(rec)
            draw.remove(rec)
        
    return gifts
    
def computeGiftsPerRec(recPerGiver, receivers):
    recPerGiver = args.recPerGiver
    totGifts = len(givers) * recPerGiver
    if totGifts % len(receivers) != 0:
        raise Exception("Total gifts (givers * receivers per giver) must be multiple of receivers") 
    return totGifts / len(receivers)    

def validate(receivers, gifts, giverPerRec):
    recCount = defaultdict(int)
    for _, rec in gifts.iteritems():
        for r in rec: recCount[r] += 1
    for rec, count in recCount.iteritems():
        if count != giverPerRec:
            raise Exception("%s has only %d givers, expecting %d" % (rec, count, giverPerRec))

givers = couples    
receivers = [p for c in couples for p in c]
exclude = dict([(c,c) for c in couples for p in c])
recPerGiver = args.recPerGiver
giverPerRec = computeGiftsPerRec(recPerGiver, receivers)

gifts = None
for _ in range(1000):
    gifts = draw(givers, receivers, exclude, recPerGiver, giverPerRec)
    if gifts is not None: break
    
if not gifts:
    print "Draw failed"    
else:
    print "\nEach person will receive %d gift(s)\n" % (giverPerRec)
    print "Giver: Receiver"
    print "---------------"
    for giv, rec in gifts.iteritems():
        print "%s: %s" % (" & ".join(giv), ", ".join(rec))

    validate(receivers, gifts, giverPerRec)