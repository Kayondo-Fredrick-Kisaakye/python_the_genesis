#you can add  a new element at any position with 'insert()'
#u do this by -  specifying the index of the new element and the value of new item -

motorcycles= ['suzuki', 'yamaha', 'bajaj', 'haojue']
print(motorcycles)  #['suzuki', 'yamaha', 'bajaj', 'haojue']

motorcycles.insert(0, 'honda')
print(motorcycles)  #['honda', 'suzuki', 'yamaha', 'bajaj', 'haojue']

#You notice it shifts evry other value in the list one position to the right