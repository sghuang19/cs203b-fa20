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
S1=B12-B22
S2=A11-A12
S3=A21+A22
S4=B21-B11
S5=A11+A22
S6=B11+B22
S7=A12-A22
S8=B21+B22
S9=A11-A21
S10=B11+B12
P1=Strassen(A11,S1)
P2=Strassen(A11,B22)
P3=Strassen(S3,B11)
P4=Strassen(A22,S4)
P5=Strassen(S5,S6)
P6=Strassen(S7,S8)
P7=Strassen(S9,S10)
C11=P5+P4-P2+P6
C12=P1+P2
C21=P3+P4
C22=P5+P1-P3-P7
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
the writers of the paper provided, Paolo D'Alberto and Alexandru Nicolau talked about an easy-to-use adaptive algorithm which combines a novel implementation of Strassen's idea with matrix multiplication from different systems like ATLAS. The Strassen's algorithm has decreased the running time of matrix multiplication significantly, by replacing one discrete matrix multiplication with several matrix additions. However, for modern architectures with complex memory hierarchies, the matrix additions have a limited in-cache data reuse and thus poor memory-hierarchy utilization. The first benefit writers listed is their algorithm divides the MM problems into a set of balanced sub-problems without any matrix padding or peelingIn addition;Second, their  algorithm applies Strassen’s strategy recursively as many time as a function of the problem size.Third, they store matrices in standard row or column major format so that they can yield control to a highly tuned matrix multiplication. The writers' algorithm applies to any size and shape matrices. These are the advantages of adaptive algorithm provided by the writers of the given paper.

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

Compare to the Obvious matrix multiplication, The Strassens Algorithm replace matrix multiplying with matrix into the matrix addition. In this algorithm, the operated matries are divided into some submatries and define some other submatries to be the basic operated matries which are calculated by the addtion or subtraction of those submatries divided from the operated matries. Then repeat these procedure on all submatries and get the result submatries which we define as "P". Then get the submatries of the product of the original operated matries. Finally add all these submatries to get the result.
Since the Strassens Algorithm replace the one separated matrix multiplication with several new matrix additions. It can significantly reduce the running time of matrix multiplication lower. The pseudocode for Strassens method used in two-ordered matrix can be written as follows:

```python
Strassen(A,B)
S1=B12-B22
S2=A11-A12
S3=A21+A22
S4=B21-B11
S5=A11+A22
S6=B11+B22
S7=A12-A22
S8=B21+B22
S9=A11-A21
S10=B11+B12
P1=Strassen(A11,S1)
P2=Strassen(A11,B22)
P3=Strassen(S3,B11)
P4=Strassen(A22,S4)
P5=Strassen(S5,S6)
P6=Strassen(S7,S8)
P7=Strassen(S9,S10)
C11=P5+P4-P2+P6
C12=P1+P2
C21=P3+P4
C22=P5+P1-P3-P7
return C
```

According to the recurrence relation, the running time for Strassens method is T(n)=7T(n/2)+‚.n2/. When $n$ is very large, the time is significantly lower than the standard matrix multiplication.

For the standard matrix multiplication, the running time is about n^3, and the pseudocode is given below:

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

---

## Experiment Design

<!-- describes your implementation of the two algorithms and the way you generate test problems (ie matrices to multiply). -->

<!-- TODO -->

### Class `Matrix`

#### Data Storage

#### Indexing

#### Operators Override

#### Other Operations

### Function `random_matrix_gen()`

### Function `adaptive_add()` and `adaptive_minus()`

### Function `square_matrix_multiply()`

### Function `strassen_matrix_multiply()`

### Performance Benchmark

### Data Collecting

---

## Empirical Analysis

<!-- provides your results of parts 3 and 4 evaluating the adaptive method for matrix multiplication, Strassen’s algorithm, and the basic method. You should use [1] as an example of the type of results you should put in this section (tables, graphs, type of discussion) because when marking will expect to see graphs and results that are of comparable quality to this and measure similar quantities. -->

<!-- TODO -->

### Testing Platform

The specifications of our main testing platform is as follows:

- Hardware
  - AMD Ryzen 9 3900X, with 12 cores, running at 3.8GHz, **maximum turbo frequency 4.6GHz**
  - ADATA DDR4 3200MHz 16GB × 4, **running at 2666MHz**, quad channel
  - Gigabyte X570 Gaming X
- Software
  - Windows 10 Professional 20H2
  - Python 3.7, built in Visual Studio Community 2019

Special thanks to SUN Jiachen, for providing us with this powerful testing platform.

<!-- TODO: add platform info -->

Some other lightweight tests are conducted on our own platform Surface Pro 6, the specifications are shown below.

- Hardware
  - Surface Pro 6 1796
  - Intel Core i7-8650U 1.99GHz, running at 2.11GHz, **maximum Turbo frequency 4.2GHz**
  - 8GB of RAM, dual channel, **running at 1867MHz**
- Software
  - Windows 10 Professional 20H2
  - WSL2, Kali Linux
  - Python 3.9, running in WSL2
  - PyCharm 2020.3 Professional Edition
  - Visual Studio Code, with Pylance engine

### Preparation

Firstly, we run the performance benchmark, to figure out the run time of `float` addition and `float` multiplication. We tested 1,000,000 (1 million) additions and multiplications, the total runtime is shown below.

| Floating point addition | Floating point multiplication |       Ratio       |
| :---------------------: | :---------------------------: | :---------------: |
|   0.09375667572021484   |   0.07808113009113098144531   | 0.832806085447587 |

Which is obvious a questionable result, since the runtime for addition cannot be longer than multiplication.

### Crossover Point Test

In this experiment, the larger size of the matrices is, the more convincing the result is. However, too large matrices would lead to unacceptable runtime for a single test. After doing several brief test on multiplication of different matrices size, taking the pace of our work into consideration, we chose 512 by 512 matrices for finding the crossover point.

<!-- TODO: add runtime -->

In all, are done, with a total runtime of. The complete testing result in `.xlsx` format can be retrieved at.

<!-- TODO: add links -->

---

## Conclusion
