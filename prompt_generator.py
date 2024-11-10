import random
from random import choice
prompt=open("Connections_Data.csv", encoding="utf8")
prompt_r=prompt.read()
prompts=prompt_r.split("\n")
bigprompt=[]
for i in prompts:
    bigprompt.append(i.split(","))
bigprompt.pop(len(bigprompt)-1)
for i in bigprompt:
    i.pop(6)
    i.pop(5)
give_prompt=[]

#function for getting a list of same id and level
def getGame(game_id, level):
    sameGame=[]
    for j in bigprompt:
        if j[0]==game_id and j[4]==level:
            sameGame.append(j[2])
    return sameGame

id_list=[]
for i in bigprompt:
    if i[0] in id_list:
        continue
    else:
        id_list.append(i[0])

#getting the final prompt list
while len(give_prompt)<16:
    count=1
    level=0
    exclude_list=[]
    while count<5:
        id_num=choice([i for i in range(len(id_list)) if i not in exclude_list])
        exclude_list.append(id_num)
        id=str(id_num)
        give_prompt.extend(getGame(id,str(level)))
        level+=1
        count+=1
give_prompt=give_prompt[0:16]
random.shuffle(give_prompt)
print(give_prompt)
