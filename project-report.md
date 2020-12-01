# DSAA Project Report of Group 2

This is the report for the project of DSAA course, written by Group 2, with following members.

- HUANG Guanchao, SID 11912309 from SME
- ZHENG Shuhan, SID 11712401 from PHY
- Li Yuru, SID 11911035 from EIE
- Tian Yuqiong, SID 11911039 from EIE

[toc]

---

## Introduction
We know that for normal matrix multiplication, the time complexity is \theta(n^3). It use to be though the only way to compute matrix multiplication, but Strassen had found a new way to compute it and faster than normal method with time complexity (n^lg7). In this project, we will relize the Strassen's algorithm and make more discussion about it.
---

## Background

<!--
A 1-page summary of the contributions of the paper in [1]. Discuss why the authors of [1] think the topic of their paper is useful, a summary of the implementation of the adaptive method (how does it work?), and their experiment design and results. Also include some examples or particular situations where you think their results could be useful for the scientific community or industry.
-->

<!-- TODO -->

---

## Theoretical Analysis

<!--
Uses an abstract model to estimate the crossover point analytically. You can provide this based on a review of academic papers and the textbook but make sure you explain it clearly and discuss the structure, constants, assumptions, and limitations of the theoretical model.
-->

<!-- TODO -->

---

## Methodology

<!-- in which you explain Strassens Algorithm, standard matrix multiplication and give pseudocode and further explanation. Include your runtime analysis from Part 2 here. -->

<!-- TODO -->
the strassens Algorithm can make the running time of matrix multiplication lower by replacing one separated matrix multiplication with several new matrix additions. The pseudocode for Strassens method can be written as follows:
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

From the recurrence we can know that the running time for Strassens method is T(n)=7T(n/2)+‚.n2/. When n is very large, the time is a lot smaller than the standard matrix multiplication.

For the standard matrix multiplication, the running time is about n^3, and the pseudocode is given below:
SQUARE MATRIX MULTIPLY(A,B)
n=A.rows
let C be a new n*n matrix
for i=1 to n
   for j=1 to n
      Cij=0
      for k=1 to n
      Cij=Cij+aik*bkj
return C



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
