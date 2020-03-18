from threading import Thread,Condition
from time import sleep
from random import randint

product=[]
con=Condition()


def producer():
    global product
    for _ in range(10):
        con.acquire()
        if len(product) == 3:
            print("No demand for product")
            con.wait()
        product.append(randint(1,20))
        print (f"Produced {product[len(product)-1]}")
        con.notify()
        con.release()
        sleep(randint(1,5))



def consumer():
    global product
    for _ in range(10):
        con.acquire()
        if not product:
            print ("no product to consume")
            con.wait()
            print ('new product produced')
        print (f"product {product.pop(0)} consumed")
        con.release()
        sleep(randint(1,5))



Producer = Thread(target=producer)
Consumer = Thread(target=consumer)

Producer.start()
Consumer.start()
# print ("hello")