anime =["kimi no na wa", "Demon Slayer", 56,"Haiykuu", "Tower of God", "God of High school"]    #Mixed List
print(anime[1::]) # default values[start,length,1]
print(anime)
print(anime[::-2]) # Recommended not to take step less than -2
print(anime[1:5:-2]) #  As it only works when the start and stop values are left blank
print(anime[-3:-1:-2]) #    and gives a blank List in return
print(len(anime))
anime.append("AOT")
anime[len(anime):] = ["Fullmetal Alchemist Brotherhood"]
# print(anime)
# anime.pop()
# print(anime)
# anime.remove(56)
# print(anime)
# anime.sort()
# print(anime)
# anime.reverse()
# print(anime)
# anime[1]=56
# print(anime)
# anime.insert(0,"DBZ")
print(anime)
anime.pop(2)
print(anime)
