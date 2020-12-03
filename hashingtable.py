class Record:
  def __init__(self, id, data):
    self.id = id
    self.data = data

def hash(x):
  return x%5

rlist=[]
for i in range(5):
    rlist.append(Record(-1, -1))


def insertdata(rec):
  index=hash(rec.id)
  pointer=index
  
  tablefull=False

  while rlist[pointer].id != -1:
    tablefull=False
    pointer=pointer+1
    if pointer > 4:
      pointer=0
    if pointer == index:
      tablefull=True
      break

  if not tablefull:
    rlist[pointer]=rec
  else:
    print("TABLE IS FULL!")

def idsearch(searchid):
  index=hash(searchid)

  
  while rlist[index].id != searchid and rlist[index].id >= 0:
    index = index + 1

    if index > 4:
      index=0

  if rlist[index].id == searchid:
    return index
  else:
    return False


p=Record(17,"Hussain")
insertdata(p)
for i in range(5):
  print(str(rlist[i].id) + str(rlist[i].data))


point = idsearch(17)
print(point)