#-*- coding:utf-8 -*-
#创建一个pizza方法，在里面添加作料，然后打印出pizza的尺寸
def making_pizza (size,*toppings):
    for topping in toppings:
        print "pizza's size is:"+str(size)+"toping:"+topping

#maked_pizza=making_pizza('5','potato','tomato')
#print maked_pizza