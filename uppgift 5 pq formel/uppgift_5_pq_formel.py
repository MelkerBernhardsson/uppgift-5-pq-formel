underskrift=" "*50
print(underskrift, "+","-"*20, "+")
print(underskrift,"|", "Melker Bernhardsson", " |")
print(underskrift,"|", "TE21C","\t","\t"," |")
print(underskrift,"|", "Pq formel raknare", "   |") #namn på projekt här
print(underskrift, "+","-"*20, "+")
print("\n"*4)

p=float(input("vilket ar ditt p varde ? "))
q=float(input("vilket ar ditt q varde ? "))


if q<((p/2)**2)-q :
    a= -p/2+(((p/2)**2)-q)**0.5
    
    b= -p/2-(((p/2)**2)-q)**0.5
    
    if (((p/2)**2)-q) > 0 :
        print("dina x varden: \n x1=",a,"\n x2=",b)
    elif (((p/2)**2)-q) == 0 :
        print("dina x varden: \n x1=",a,"\n x2 saknar reell losning")


else:
    print("saknar reell losning")