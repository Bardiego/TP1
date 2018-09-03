import numpy as np
import networkx as nx
import matplotlib as plt
import random

def ldata(archive):
        f=open(archive)
        data=[]
        for line in f:
            line=line.strip()
            col=line.split()
            data.append(col)	
        return data
    
delf=ldata("dolphinsGender.txt")
print(delf)

###Una forma de ver la red, súper homofílica
#G=nx.Graph(delf)
#nx.draw(G, with_labels=True, font_weight='bold', size_nodes=10)

#
#todo=dict(delf)
#todo.keys()
#todo.values()

#
#delfines=[]
#
#for i in todo.keys():
#    delfines.append(i)
#    
#print(delfines)
#
#sexo=[]
#
#for i in todo.values():
#    sexo.append(i)
#    
#print(sexo)
#print("nuevas condiciones")
###Nuevas condiciones, mezclo las listas y tiro el grafo de nuevo
#    
#random.shuffle(delfines)
#print(delfines)
#random.shuffle(sexo)
#print(sexo)
#
#todos=list(zip(delfines, sexo))
#print(todos)
#
#print("y el grafo se ve así:")
#G1=nx.Graph(todo)
#nx.draw(G1, with_labels=True, font_weight='bold', size_nodes=10)
print("CORTE")


G1=nx.Graph(delf)
a=list(G1.edges)
print(len(a))
b=[]
for pares in a:
        n1=random.randint(0,len(a)-1)
        n2=random.randint(0,len(a)-1)
        b.append((a[n1], a[n2]))



for i in range(len(b)):
    G1.add_edges_from([(b[i][0], b[i][1])])


nx.draw(G1, with_labels=0, font_weight='bold', size_nodes=10)







    
    