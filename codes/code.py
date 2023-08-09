import numpy as np
import math 
vector=np.array([float(input("enter first component of first vector"))-float(input("enter first component of second vector")),float(input("enter second component of first vector"))-float(input("enter second component of second vector"))])
magnitude=np.linalg.norm(vector)
print("Magnitude=", magnitude)
