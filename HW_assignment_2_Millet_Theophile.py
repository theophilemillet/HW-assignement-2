{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <center>HW assignment 2</center>\n",
    "<center> <img src='https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Seal_of_University_of_California%2C_Berkeley.svg/1200px-Seal_of_University_of_California%2C_Berkeley.svg.png' width=\"200\" height=\"200\" style='margin-bottom:0.6em;'> </center>\n",
    "<center>Théophile MILLET</center>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1. Name: Millet Théophile\n",
      "\n",
      "\n",
      "2. The matrix A with size (3,5) containing random numbers is \n",
      " A = [[2 0 1 0 5]\n",
      " [9 3 4 5 6]\n",
      " [9 4 4 5 4]]\n",
      "\n",
      "\n",
      "3. The size of matrix A is (3, 5)\n",
      "The length of matrix A is 15\n",
      "\n",
      "\n",
      "4. The resized matrix A to size (3,4) is \n",
      " A = [[2 0 1 0]\n",
      " [5 9 3 4]\n",
      " [5 6 9 4]]\n",
      "\n",
      "\n",
      "5. The transpose of matrix A is \n",
      " B = [[2 5 5]\n",
      " [0 9 6]\n",
      " [1 3 9]\n",
      " [0 4 4]]\n",
      "\n",
      "\n",
      "6. The minimum value in column 1 of matrix B is 0\n",
      "\n",
      "\n",
      "7. The minimum value for the entire matrix A is 0 and the maximum value is 9\n",
      "\n",
      "\n",
      "8. The vector X with 4 random numbers is X = [83 44 18 20]\n",
      "\n",
      "\n",
      "9. The function was created by passing the vector X and the matrix A in it\n",
      "\n",
      "\n",
      "10. Here is what the function return after having multiplied X with A now, \n",
      " D = [[166   0  18   0]\n",
      " [415 396  54  80]\n",
      " [415 264 162  80]]\n",
      "\n",
      "\n",
      "11. Z with absolute and real parts different from 0 is Z = (36+74j)\n",
      "\n",
      "\n",
      "12. real part: 36.0  imaginary part: 74.0  Absolute value: 82.29216244576394\n",
      "\n",
      "\n",
      "13. C is the multiplication of D with the absolute value of Z, C = [0, 2, 3, 9, 4, 9]\n",
      "\n",
      "\n",
      "14. We convert matrix B from a matrix to a string and overwrite B, B = 2,5,50,9,61,3,90,4,4\n",
      "\n",
      "\n",
      "15. Millet Théophile is done with HW2\n"
     ]
    }
   ],
   "source": [
    "#1. Include a section with your name\n",
    "Name = \"Millet Théophile\"\n",
    "print('1. Name:',Name)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#2. Create matrix A with size (3,5) containing random numbers\n",
    "import numpy as np\n",
    "A = np.random.randint(10,size = (3,5))\n",
    "print('2. The matrix A with size (3,5) containing random numbers is \\n A =',A)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#3. Find the size and length of matrix A\n",
    "rows = len(A)\n",
    "columns = len(A[0])\n",
    "size = (rows,columns)\n",
    "print(\"3. The size of matrix A is\",size)\n",
    "\n",
    "length = rows*columns\n",
    "print('The length of matrix A is',length)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#4. Resize (crop/slice) matrix A to size (3,4)\n",
    "A = np.resize(A,(3,4))\n",
    "print('4. The resized matrix A to size (3,4) is \\n A =',A)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#5. Find the transpose of matrix A and assign it to B\n",
    "B = A.T\n",
    "print('5. The transpose of matrix A is \\n B =',B)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#6. Find the minimum value in column 1 of matrix B\n",
    "min_value_B = min(B[:,0])\n",
    "print('6. The minimum value in column 1 of matrix B is',min_value_B)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#7. Find the minimum and maximum values for the entire matrix A\n",
    "C = []\n",
    "for i in A:\n",
    "    C.append(min(i))\n",
    "    C.append(max(i))\n",
    "min_value_A = min(C)\n",
    "max_value_A = max(C)\n",
    "print(\"7. The minimum value for the entire matrix A is\",min_value_A, \"and the maximum value is\",max_value_A) \n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "\n",
    "#8. Create vector X (an array) with 4 random numbers\n",
    "X = np.random.randint(1,101,4)\n",
    "print('8. The vector X with 4 random numbers is X =',X)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#9. Create a function and pass vector X and matrix A in it\n",
    "def assignement(X,A): \n",
    "    print('9. The function was created by passing the vector X and the matrix A in it') \n",
    "    print(\"\\n\")\n",
    "    \n",
    "#10. In the new function multiply vector X with matrix A and assign the result to D\n",
    "    D = X*A\n",
    "    return D \n",
    "print('10. Here is what the function return after having multiplied X with A now, \\n D =',assignement(X,A))\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#11. Create a complex number Z with absolute and real parts != 0\n",
    "Z = complex(np.random.randint(1,100),np.random.randint(1,100))\n",
    "print('11. Z with absolute and real parts different from 0 is Z =',Z)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#12. Show its real and imaginary parts as well as it’s absolute value\n",
    "real = Z.real\n",
    "imag = Z.imag\n",
    "absZ = abs(Z)\n",
    "\n",
    "print(\"12. real part:\",real, ' imaginary part:',imag,' Absolute value:',absZ)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#13. Multiply result D with the absolute value of Z and record it to C\n",
    "def assignement(X,A):\n",
    "    D = A*X\n",
    "    C = D*absZ\n",
    "print('13. C is the multiplication of D with the absolute value of Z, C =',C)\n",
    "print(\"\\n\")\n",
    "\n",
    "\n",
    "#14. Convert matrix B from a matrix to a string and overwrite B\n",
    "B = \"\".join([\",\".join([str(i) for i in sub]) for sub in B])\n",
    "print('14. We convert matrix B from a matrix to a string and overwrite B, B =',B)\n",
    "print(\"\\n\")\n",
    "\n",
    "#15. Display a text on the screen: ‘Name is done with HW2‘, but pass your ‘Name’ as a string variable\n",
    "Name = \"Millet Théophile\"\n",
    "print('15.',Name,'is done with HW2')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
