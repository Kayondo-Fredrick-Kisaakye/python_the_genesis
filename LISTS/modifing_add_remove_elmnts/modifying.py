#the book says most lists i make will be DYNAMIC
#i'll ADD and REMOVE elements as the program runs
#EG -: i might create a gam  where  a player shoots alienas, i cud store the initial set of alienas in a list and remove one when its shot
#each time a new one appears on screen, i add it to the list - increasing and decreasing in the process

#SYNTAX for modifying is similar to that of ACCESSING an element
#to CHANGE element, use NAME OF LIST, then INDEX of element u wanna change, then PROVIDE new value

spider_men = ['peter b paker', 'miles morales', 'ben riley', 'miguel ohara']
print(spider_men)  #['peter b paker', 'miles morales', 'ben riley', 'miguel ohara']

spider_men[3] = 'kayondo fredrick'.title()
print(spider_men)  #['peter b paker', 'miles morales', 'ben riley', 'Kayondo Fredrick']