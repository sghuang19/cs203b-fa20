# DSAA Project Report of Group 2

This is the report for the project of DSAA course, written by Group 2, with following members.

- HUANG Guanchao, SID 11912309 from SME
- ZHENG Shuhan, SID 11712401 from PHY
- Li Yuru, SID 11911035 from EIE
- Tian Yuqiong, SID 11911039 from EIE

[toc]

---

## Introduction

Matrix mltiplication (MM) is a practical application of Linear Algebra. It is used in many fields, including mathematics, physics and electrical engineering (**Cite**). In real life, no matter calculating the path between two place or solving the profit problem of goods, it always be of great use.

Previously, people used traditional matrix multiplication, which was based on the definition of MM, to calculate the product of two matrices. It's pseudocode is

```python
SQUARE MATRIX MULTIPLY(A,B)
n=A.rows
let C be a new n*n matrix
for i=1 to n
   for j=1 to n
      Cij=0
      for k=1 to n
      Cij=Cij+aik*bkj
return C
```

According to the pseudocode, the algorithm contains three circulations. Concretely, $C_{ij}=A_{ik}B_{kj}$, each index ($i,j,k$) runs from 1 to $n$. Therefore, the time complexity is $\Theta(n^3)$, where $n$ is the length of the square matrix. The time complexity of traditional method is large. Hence, since the extensive application of MM, how to optimize the operation of MM becomes more and more important. Without considering the degree of matrix density, how to effectively reduce the number of use of the arithmetic multiplication in MM is a major optimized direction.

The earliest MM optimized algorithm was proposed by German mathematician Volker Strassen in 1969 and was named Strassen algorithm (**Cite**). It's main idea is to replace multiplication by addition and subtraction. The answer is calculated by piecing some indirect terms together and using the addition and subtraction on these indirect terms to cancel out part of the terms. For a two order square matrix, the pseudocode of Strassen's algorithm is

```python
Strassen(A,B)
S1 = B12 - B22
S2 = A11 - A12
S3 = A21 + A22
S4 = B21 - B11
S5 = A11 + A22
S6 = B11 + B22
S7 = A12 - A22
S8 = B21 + B22
S9 = A11 - A21
S10 = B11 + B12
P1 = Strassen(A11,S1)
P2 = Strassen(A11,B22)
P3 = Strassen(S3,B11)
P4 = Strassen(A22,S4)
P5 = Strassen(S5,S6)
P6 = Strassen(S7,S8)
P7 = Strassen(S9,S10)
C11 = P5 + P4 - P2 + P6
C12 = P1 + P2 
C21 = P3 + P4 
C22 = P5 + P1 - P3 - P7
return C
```

For Strassen algorithm, the time complexity is O(n^(\lg7)). For a two order matrix multiplication, we need to spend 8*(2^3) with Obvious matrix multiplication algorithm but we just need 7*(2^(\lg7)) by using Strassen's algorithm. The time complexity is decreased. But the space complexity of Strassen algorithm may be increased since the more spaces are needed to save the submatrix.

After Strassen came up with this algorithm, more and more optimized algrithms were proposed by different people (**Cite**). But in this project, we will focus on the Strassen algorithm. We will apply it to higher order matrix multiplication and discuss more details about it.

---

## Background

<!--
A 1-page summary of the contributions of the paper in [1]. Discuss why the authors of [1] think the topic of their paper is useful, a summary of the implementation of the adaptive method (how does it work?), and their experiment design and results. Also include some examples or particular situations where you think their results could be useful for the scientific community or industry.
-->

<!-- TODO -->
the writers of the paper provided, Paolo D'Alberto and Alexandru Nicolau talked about and easy-to-use adaptive algorithm which combines a novel implementation of Strassen's idea with matrix multiplication from different systems like ATLAS. The Strassen's algorithm has decreased the running time of matrix multiplication significantly, by replacing one discrete matrix multiplication with several matrix additions. However, for modern architectures with complex memory hierarchies, the matrix additions have a limited in-cache data reuse and thus poor memory-hierarchy utilization. The first benefit writers listed is their algorithm divides the MM problems into a set of balanced sub-problems without any matrix padding or peelingIn addition;Second, their  algorithm applies Strassen’s strategy recursively as many time as a function of the problem size.Third, they store matrices in standard row or column major format so that they can yield control to a highly tuned matrix multiplication. The writers' algorithm applies to any size and shape matrices. These are the advantages of adaptive algorithm provided by the writers of the given paper.

The concrete implementation of the adaptive algorithm is realized by several steps. To begin with, writers declared several notations and computations. As the writer suggests, their algorithm reduces the number of passes as well as the number of computations because of a balanced division process. For matrix C=A*B, where σ(A)=m×n, decompose A to four small matrices A0, A1, A2 and A3. The size of four small matrices are A0 with σ(A0)=d m2e×d n2 e, A1 with σ(A1)=d m2e×b n2 c, A2 with σ(A2)=b m2c×d n2 e and A3 with σ(A3)=b m2 c×b n2 c. The same with matrix B. When we do matrix addition, we expand the scope of matrix addition to different sizes. For example, we define matrix X=Y+Z, if the size of Y and Z is not the same, then we expand the size of X to the largest of them and the redundant part of X is set 0. After that, the adaptive algorithm begin. Several matrix additions and multiplications is performed and are put into practice to several systems. Through this process, the writers found that the same algorithm applied to different systems can have different results.

Their algorithm can be useful in some real-world problems involving matrix multiplication, especially for those matrix which size is big and  not fixed. For practical application, this algorithm can be applied to many industrial problems. For instance, the circuits equations which include several unknown parameters can be solved quickly by using matrix divisions, which means matrix multiplications as well. What's more, the signal processing can make good use of the algorithm, too. The input and output signals' relationship can be expressed in matrix, too. With the advantage of changeable size and comparatively fast speed, the adaptive method has great potential in real-world problems.

In conclusion, the adaptive algorithm is based on the Strassen method and have some advanced operations. The Strassen method has its run-time advantage when the matrix size is quite big, but this edge cannot be exhibited when the size is not big enough, because it add quite a lot matrix additions compared to the old standard matrix multiplication. For instance, the size has to be bigger than about 1000*1000 when Strassen method begin to show its superiority. However,  speedups up to 30% are observed over already tuned MM using this hybrid approach.

---

## Theoretical Analysis

<!--
Uses an abstract model to estimate the crossover point analytically. You can provide this based on a review of academic papers and the textbook but make sure you explain it clearly and discuss the structure, constants, assumptions, and limitations of the theoretical model.
-->

<!-- TODO -->

---

## Methodology

<!-- in which you explain Strassen Algorithm, standard matrix multiplication and give pseudocode and further explanation. Include your runtime analysis from Part 2 here. -->

<!-- TODO -->

Compare to the Obvious matrix multiplication, The Strassens Algorithm replace matrix multiplying with matrix into the matrix addition. In this algorithm, the operated matrices are divided into some submatries and define some other submatrices to be the basic operated matrices which are calculated by the addtion or subtraction of those submatrices divided from the operated matrices. Then repeat these procedure on all submatrices and get the result submatrices which we define as "P". Then get the submatrices of the product of the original operated matrices. Finally add all these submatrices to get the result.
Since the Strassens Algorithm replace the one separated matrix multiplication with several new matrix additions. It can significantly reduce the running time of matrix multiplication lower. The pseudocode for Strassens method used in two-ordered matrix can be written as follows:

```python
Strassen(A,B)
S1 = B12 - B22
S2 = A11 - A12
S3 = A21 + A22
S4 = B21 - B11
S5 = A11 + A22
S6 = B11 + B22
S7 = A12 - A22
S8 = B21 + B22
S9 = A11 - A21
S10 = B11 + B12
P1 = Strassen(A11,S1)
P2 = Strassen(A11,B22)
P3 = Strassen(S3,B11)
P4 = Strassen(A22,S4)
P5 = Strassen(S5,S6)
P6 = Strassen(S7,S8)
P7 = Strassen(S9,S10)
C11 = P5 + P4 - P2 + P6
C12 = P1 + P2 
C21 = P3 + P4 
C22 = P5 + P1 - P3 - P7
return C
```

For Strassen's method, make the recursion tree less bushy. Perform only 7 recursive multiplications of $(n/2)\times(n/2)$ matrices, rather than 8 for divide and conquer algorithm. Since it divide the operated matrices into submatrices, it will cost several additions of $(n/2)\times(n/2)$ matrices, but just a constant number more which can still absorb the constant factor for matrix addition into the $\Theta(n/2)$ term.

For this algorithm:
First, as in the recursive method, partition each of the matrices into four $(n/2)\times(n/2) $ submatrices. The time is $\Theta(1)$.

Second, create 10 matrices $S_1$,$S_2$,...,$S_10$. Each is $(n/2) \times (n/2)$ and is the sum or difference of two matrices created in previous step. The time is $\Theta(n^2)$ to create all 10 matrices.

Third, recursively compute 7 matrix products $P_1$, $P_2$,..., $P_7$, each equals to $(n/2) \times (n/2)$.

Last, compute $(n/2)\times(n/2)$ submatrices of C by adding and subtracting various combinations of the $P_i$. The time is $\Theta(n^2)$.

Hence, the recurrence will be

$$
T(n) =
\begin{cases}
\Theta(1) \quad & \text{if}\, n = 1 \\
7T(n/2) + \Theta(n^2) \quad & \text{if}\, n > 1
\end{cases}
$$
By the master method, since $n^(\log_ba)$ = $n^(\log_27)$ = $n^(\lg7)$ is larger than $f(n)$ which equals to $n^2$, hence for case one of master method, the solution is $T(n) = \Theta(n^(\lg7))$.

For the standard matrix multiplication, the pseudocode is given below:

```python
SQUARE MATRIX MULTIPLY(A,B)
n=A.rows
let C be a new n*n matrix
for i=1 to n
   for j=1 to n
      Cij=0
      for k=1 to n
      Cij=Cij+aik*bkj
return C
```

As we can see, this method contains three circulations. Therefore,the running time is about $n^3$

Compare to these two method, we can see that when $n$ is very large, the time of Strassen's algorithm is significantly lower than the time of standard matrix multiplication.

---

## Experiment Design

<!-- describes your implementation of the two algorithms and the way you generate test problems (ie matrices to multiply). -->

<!-- TODO -->
 
---

## Empirical Analysis

<!-- provides your results of parts 3 and 4 evaluating the adaptive method for matrix multiplication, Strassen’s algorithm, and the basic method. You should use [1] as an example of the type of results you should put in this section (tables, graphs, type of discussion) because when marking will expect to see graphs and results that are of comparable quality to this and measure similar quantities. -->

<!-- TODO -->

---

## Conclusion
