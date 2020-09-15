Mat1 = [[3, 4, -6], 
      [12,71,24], 
      [21,3,21]]

Mat2 = [[2, 16, -16],
           [1,7,-3], 
           [-1,3,3]]
Mat3 = [[0,0,0,],
     [0,0,0,],
     [0,0,0,]]

for i in range(len(Mat1)):
    for j in range(len(Mat2)):
        Mat3[i][j] = Mat1[i][j] + Mat2[i][j]
        
print(M3)

for i in range(len(Mat1)):
    for j in range(len(Mat2)):
        Mat3[i][j] = Mat1[i][j] * Mat2[i][j]
        
print(M3)
