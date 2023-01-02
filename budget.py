ledger = []
import math
class Category:
  
  def __init__(self, name):
    self.name = name
    self.ledger = []
    self.total = 0.0
    
  def __repr__(self):
    n = self.name
    intio = []
    strio = []
    chaine = ""
    s = self.ledger
    for i in range(len(s)):
      for k,v in (s[i].items()):
        if type(v) == float or type(v) == int:
          v = "{:.2f}".format(float(v))
          intio.append(v)
        else:
          strio.append(v)
    for i in range(len(intio)):
      if len(intio[i]) == 7:
        chaine = chaine + str(strio[i].ljust(23, " ")) + str(intio[i]) + "\n"
      elif len(strio[i]) >= 23 and float(intio[i]) >= 0:
        chaine = chaine + str(strio[i][:23]) + "  " + str(intio[i]) + "\n"
      elif len(strio[i]) >= 23 and float(intio[i]) < 0:
        chaine = chaine + str(strio[i][:23]) + " " + str(intio[i]) + "\n"
      elif len(strio[i]) < 23 and float(intio[i]) >= 0 and len(intio[i]) >= 6:
          chaine = chaine + str(strio[i].ljust(23, " ")) + " "  + str(intio[i]) + "\n"
      elif len(strio[i]) < 23 and float(intio[i]) >= 0 and len(intio[i]) < 6:
          chaine = chaine + str(strio[i].ljust(23, " ")) + "  "  + str(intio[i]) + "\n"
      elif len(strio[i]) < 23 and float(intio[i]) < 0:
          chaine = chaine + str(strio[i].ljust(23, " ")) + " "  + str(intio[i]) + "\n"
        
    string = n.center(30, '*') + "\n" + chaine + "Total: " + str(self.total)
    return string  
  
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount": amount, "description": description})
    self.total += amount
  
  def withdraw(self, amount, description = ""):
    canw = self.check_funds(amount)
    if canw:
      self.ledger.append({"amount": -amount, "description": description})
      self.total -= amount
    return canw
    
  def get_balance(self):
    return self.total
    
  def transfer(self, amount, instance):
    cant = self.check_funds(amount)
    if cant:
      self.withdraw(amount, "Transfer to {}".format(instance.name))
      instance.deposit(amount, "Transfer from {}".format(self.name))
    return cant  
    
      
  def check_funds(self, amount):
    if amount > self.total:
      return False
    else:
      return True
     

    
def create_spend_chart(categories):
  listt = []
  listtt = []
  per = []
  wh = []
  imd = []
  r = 100
  title = "Percentage spent by category" + "\n"
  withdrawl = 0.0
  w = 0
  t = 0
  si = ""
  ch = ""
  bb = ""
  cha = ""
  line = "-"
  for j in range(len(categories)):
    s = categories[j].ledger
    for i in range(len(s)):
      for k,v in (s[i].items()):
        if type(v) == float or type(v) == int:
          if v < 0:
            withdrawl -= v
    w = withdrawl - t
    t = w + t
    listt.append(str("{:.2f}".format(float(w))))
  for i in range(len(listt)):
    ri = (float(listt[i]) * 100) / (withdrawl * 10)
    res = str("{:.1f}".format(ri))
    listtt.append(str(math.floor(float(res)) * 10))
  
  for i in range(11):
    ch = ""
    if len(str(r)) == 3:
      c = str(r) + "|" 
      per.append(c)
    elif len(str(r)) == 2:
      c = " " + str(r) + "|"
      per.append(c)
    else:
      c = "  " + str(r) + "|"
      per.append(c)
    for j in range(len(listtt)):
      if int(listtt[j]) == r:
        ch = ch + " o "
        listtt[j] = int(listtt[j]) - 10
      else:
        ch = ch + "   "
    ch = ch + " "
    wh.append(ch)
    r -= 10
  for i in range(11):
    cha = cha + per[i] + wh[i] + "\n"
  for i in range(len(listtt)):
    line = line + "---"
  j = 1
  b = " "
  for i in range(len(categories)):
    if len(b) < len(categories[i].name):
      b = categories[i].name
  for i in range(len(b)):
    for k in range(len(categories)):
      bi = categories[k].name
      if len(bi) > i:
        si = si + bi[i:j] + "  "
      else:
        si = si + "   "
    imd.append(si)
    si = ""
    j = j + 1
  for i in range(len(imd)):
    if i + 1 < len(imd):
      bb = bb + "     " + imd[i] + "\n"
    else:
      bb = bb + "     " + imd[i]
  percentage = title + cha + "    " + line + "\n" + bb
  return percentage