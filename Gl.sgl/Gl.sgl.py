s=input()
gl=0
sgl=0
a=0
e=0
i=0
o=0
u=0
y=0
for k in s:
   b=k.lower()
   if b == "a":
       gl+=1
       a+=1
   elif b == "e":
       gl+=1
       e+=1
   elif b == "i":
       gl+=1
       i+=1
   elif b == "o":
       gl+=1
       o+=1
   elif b == "u":
       gl+=1
       u+=1
   elif b == "y":
       gl+=1
       y+=1
   else:
       sgl+=1
print("Glasn " ,gl)
print ("Soglasn ", sgl)
if a==0 or e==0 or o==0 or i==0 or u==0 or y==0:
    print("False")
else:
    print ("a - ", a, "e - ", e, "o - ", o, "i - ", i, "u - ", u, "y - ", y, sep=' ')

