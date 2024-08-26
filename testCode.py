#import PyMatrix as pymat

#import numpy
#
#A = numpy.array([[0,1],[-25,-6]])
#print(numpy.linalg.eig(A)[0])
#
    

def fibonacci(max = 10,output = [0,1]):

    output.append(output[len(output)-1]+output[len(output)-2])
    if max < 0:
        return output
    return fibonacci(max-1,output)

print(fibonacci(100))
