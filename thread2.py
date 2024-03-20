import threading
def cube(num):
    print("cube {}".format(num*num*num))
def sqrt(num):
    print('sqrt {}'.format(num*num))
if __name__ == '__main__':
    t1 = threading.Thread(target = sqrt,args = (10,))
    t2 = threading.Thread(target = cube,args = (10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('done!')
