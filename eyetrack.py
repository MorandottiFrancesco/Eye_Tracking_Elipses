import numpy as np
import matplotlib.pyplot as plt


def create_blank_image(X , Y):
    try:
        IMAGE = np.array([[0 for i in range(X)] for j in range(Y)])
        return(IMAGE)
    except:
        print("create image error occurred")
        return(-1)

def writepixel(IMAGE, X,  Y, value):
    ## write a n-bit number in position (X,Y)
    try:
        IMAGE[Y][X] = value
        return(IMAGE)
    except:
        print("writepixel error occurred")
        return(-1)


def write_eye(IMAGE, X,  Y, radius):
    ## write a n-bit number in position (X,Y)
    try:
        i = 0
        while i < radius:
            j = 0
            writepixel(IMAGE , X+i , Y , 256-(i*i*i))
            writepixel(IMAGE , X-i , Y , 256-(i*i))
            ##writepixel(IMAGE , X-i , Y , 256-(i*i*i))
            while j*j < radius*radius - i*i:
                writepixel(IMAGE , X+i , Y+j , 256-(2**j)-(2**i))
                writepixel(IMAGE , X+i , Y-j , 256-(2**j)-(2**i))
                writepixel(IMAGE , X-i , Y+j , 256-(2**j)-(2**i))
                writepixel(IMAGE , X-i , Y-j , 256-(2**j)-(2**i))



                ##writepixel(IMAGE , X-i , Y-j , 256-(j*j*j)-(i*i*i)+1)
                j += 1
            i += 1
        return(IMAGE)

    except:
        print("writepixel error occurred")
        return(-1)



def readpixel(IMAGE, X,  Y):
    ## read a n-bit number in position (X,Y)
    try:
        value = 0
        return(value)
    except:
        print("readpixel error occurred")
        return(-1)

def printimage_to_terminal(IMAGE):
    try:  
        print(IMAGE)
        return()
    except:
        print("print to terminal error occurred")
        return(-1)
    return## read a n-bit number in position (X,Y)

def printimage_to_text(IMAGE):
    try:
        return()
    except:
        print("print to text error occurred")
        return(-1)


    return## read a n-bit number in position (X,Y)




blanks = create_blank_image(200,100)
printimage_to_terminal(blanks)
ones = write_eye(blanks, 50,  25, 8)
printimage_to_terminal(ones)

plt.imshow(ones, interpolation='none')
plt.show()