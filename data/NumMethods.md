
# Lecture notes on Numerical Analysis

Instructor: LIU Jie1

The lecture notes are based on Tim Sauer’s “Numerical Analysis” 2nd edition and Burden, Faires, and Burden’s “Numerical Analysis” 2nd edition.






# Weeks Topics

| 0.5 | Computer Arithmetic                                   |
| --- | ----------------------------------------------------- |
| 2   | Nonlinear Equations and System of Nonlinear Equations |
| 1.5 | Interpolation                                         |
| 2   | Numerical Differentiation and Integration             |
| 2.5 | Numerical ODE                                         |
| 2.5 | Numerical Linear Algebra                              |
| 1.5 | Polynomial and Trigonometric Polynomial Approximation |
| 1.5 | Numerical PDEs                                        |





# Grading policy:

| 4 Quizzes  | 40% |
| ---------- | --- |
| 5 Projects | 30% |
| Final      | 30% |

Email: liujie@xmu.edu.my




# Contents

# 1 Computer Arithmetic

# 1.1 Why numerical analysis

7

# 1.1.1 Computer won’t lie. However,

8

# 1.2 Binary numbers

9

# 1.2.1 Binary to decimal

9

# 1.2.2 Decimal to binary

10

# 1.3 Floating point and machine representations of real numbers

12

# 1.4 Numbers from a computer’s point of view

15

# 1.5 Addition of numbers

16

# 1.6 Loss of significance

18

# 1.7 Evaluating a polynomial

20

# 1.8 Matlab

21

# 1.9 Homework 1

22





# 2 Nonlinear equation and system of nonlinear equations

# 2.1 Bisection method

24

# 2.2 Fixed-point iteration

25

# 2.3 Newton’s method for a single nonlinear equation f(x) = 0

29

# 2.4 Homework 2

30

# 2.5 Matrix norm

32

# 2.5.1 Singular value decomposition and Frobenius norm

35

# 2.5.2 Condition number

36

# 2.6 Newton’s method in Rⁿ

37

# 2.6.1 Proof of quadratic convergence

38

# 2.7 Secant method for a single nonlinear equation

40

# 2.8 Quasi-Newton Method in Rⁿ

41

# 2.8.1 Broyden’s Method for System of Nonlinear Equations

42

# 2.8.2 Convergence Proof of Broyden’s Method

42

# 2.8.3 Symmetric Broyden’s method for Minimization Problem

44

# 2.9 Homework 3

45

# 2.10 Computer Project 1

47




# 3 Interpolation

# 3.1 Lagrange interpolation

48

# 3.2 Newton’s formula

51

# 3.3 Interpolation error

54

# 3.3.1 Properties of divided differences

55

# 3.4 Hermite Interpolation polynomial

56

# 3.5 Error estimates for the Hermite interpolation polynomials

57

# 3.6 Newton’s divided difference and Hermite interpolation polynomial

57

# 3.7 Homework 4

58





# 3.8 Computer Project

59



# 3.9 Cubic splines

59



# 3.9.1 Constructing a cubic spline

62



# 3.10 Homework 5

64



# 4 Numerical differentiation and integration

65



# 4.1 Numerical differentiation

65



# 4.2 Rounding error

68



# 4.3 Richardson extrapolation

69



# 4.4 Homework 6

72



# 4.5 Numerical integration (numerical quadrature)

72



# 4.6 Interpolatory formula and Newton-Cotes formula

75



# 4.7 Composite rule

77



# 4.8 Error estimates of composite rule

79



# 4.9 Romberg integration

81



# 4.10 π: Zu Chongzhi, Richardson and Romberg

86



# 4.11 Homework 7

88



# 4.12 Two Computer Projects and Their Solutions

88



# 4.13 Peano kernel

98



# 4.14 Euler-Maclaurin formula

100



# 4.15 Adaptive quadrature

102



# 4.16 Gaussian quadrature

106



# 4.16.1 Weighted Gaussian quadrature

107



# 4.16.2 Properties of Gauss quadrature

110



# 4.17 Homework 8

111



# Numerical methods for ODEs

112



# 5.1 System of ODEs

114



# 5.2 Some basic numerical methods

116



# 5.2.1 System of ODEs

117



# 5.2.2 Higher order equations

119



# 5.3 Local truncation errors and one-step errors

119



# 5.4 Taylor series methods

120



# 5.5 Runge-Kutta method

121



# 5.6 Embedded methods and error estimation

126



# 5.7 Backward Euler revisit and its stability

128



# 5.8 Homework 9

130



# 5.9 Linear multistep methods

130



# 5.9.1 local truncation error

132



# 5.9.2 Characteristic polynomials

133



# 5.9.3 Starting values

134



# 5.9.4 The predictor-corrector methods

134



# 5.10 Backward differentiation formula methods

135



# 5.11 Homework 10

# 5.12 Computer Project 3

# 5.13 Stability and convergence

# 5.13.1 The test problem

# 5.13.2 One-step methods

# 5.13.3 Forward Euler method on nonlinear problems

# 5.13.4 General one-step methods

# 5.14 Zero stability of linear multistep methods

# 5.14.1 Solving linear difference equations

# 5.15 A zero-stable method may perform badly if ∆t is large

# 5.16 Stability region



# 5.16.1 Stability region for linear multistep methods

# 5.17 A-stability and A(α)-stability

# 6 Numerical Methods in Linear Algebra

# 6.1 Direct methods for solving linear system of equations

# 6.1.1 Gaussian elimination

# 6.1.2 LU decomposition

# 6.1.3 Operation counts

# 6.1.4 Error magnification and condition number

# 6.1.5 Swamping

# 6.1.6 Gaussian elimination with partial pivoting

# 6.1.7 Permutation Matrix



# 6.1.8 P A = LU factorization

# 6.1.9 Remark on P A = LU factorization

# 6.1.10 The P A = LU algorithm and its mathematical theory

# 6.1.11 Properties of Gauss transform matrix

# 6.1.12 The theorem on P A = LU factorization

# 6.1.13 Uniqueness and avoidance of pivoting

# 6.1.14 Homework 11

# 6.2 Iterative methods for linear systems

# 6.2.1 Jacobi and Gauss-Seidel iterations

# 6.2.2 Symmetric positive-definite matrices

# 6.2.3 Steepest descent



# 6.2.4 Conjugate gradient

# 6.2.5 Krylov space and convergence rate of conjugate gradient method

# 6.2.6 Preconditioned conjugate gradient

# 6.2.7 Homework 12

# 6.3 Eigenvalue problem

# 6.3.1 Power iteration and Rayleigh quotient

# 6.3.2 QR factorization and Gram-Schmidt orthogonalization

# 6.3.3 QR algorithm without shifts

# 6.3.4 Why the QR algorithm works and its relation to block power iteration

# 6.3.5 Real Schur decomposition and the QR algorithm

194



# 6.3.6 Household reflection

198



# 6.3.7 Reduction to Hessenberg matrices

199



# 6.3.8 Least square solution to linear systems of equations

202



# 6.3.9 Homework 13

204



# 6.3.10 Computer Project 4

204



# 7 Least Squares, Trigonometric Interpolation and FFT

206



# 7.1 Fitting models to data

206



# 7.2 Least squares approximation of a function

208



# 7.3 Least square fitting with trigonometric functions

209



# 7.4 Discrete Fourier transform

212



# 7.5 Fast Fourier Transform

214



# 7.6 Trigonometric interpolation

216



# 7.7 Orthogonality and interpolation

220



# 7.8 Orthogonal matrix and eigenvectors related to DFT

223



# 7.9 Revisit of the least square fitting with trigonometric functions

226



# 7.10 Discrete cosine transform

229



# 7.11 Two-dimensional DCT

233



# 7.12 Image compression

235



# 7.13 Homework 14

242



# 8 Boundary Value Problems and Initial Boundary Value Problems

243



# 8.1 Shooting method

244



# 8.2 Finite difference methods

246



# 8.3 Homework 15

250



# 8.4 Computer Project 5

251



# 8.5 Error estimation of finite difference method for Poisson equation in 1-D

251



# 8.5.1 Local truncation error

⇒ = global error

252



# 8.5.2 Local truncation error

253



# 8.5.3 Global error

253



# 8.5.4 Stability

254



# 8.5.5 Consistency

254



# 8.5.6 Convergence

255



# 8.5.7 Stability and convergence in the 2-norm

255



# 8.5.8 Max-norm estimates

256



# 8.5.9 How to handle Neumann boundary conditions

257



# 8.6 Poisson equation in 2-D

258



# 8.6.1 The 5-point stencil for the Laplace operator

258



# 8.6.2 Ordering the unknowns

259



# 8.6.3 Accuracy and stability

261



# 8.6.4 Higher order methods and the 9-point Laplacian

262



# 8.6.5 Maximum norm estimates

263



# 8.7 Heat equations in 1-D

265



# 8.7.1 Local truncation error and order of accuracy

267



# 8.7.2 Method of lines discretizations

268



# 8.7.3 Stability theory

270



# 8.7.4 Stiffness of the heat equation

271



# 8.7.5 Convergence

271



# 8.7.6 von Neumann analysis

274



# 8.8 Homework 16

275



Computer Arithmetic

# 1.1 Why numerical analysis

One of Gauss’s most valuable talents is that he is capable to compute. Here is an example. Let π(n) be the prime-counting function that gives the number of primes less than or equal to n, for any real number n. By generating a large table of prime numbers and computing π(n) for a lot of n, Gauss made his conjecture that π(n) ∼ n/ ln(n) (called prime number theorem). Later he proved that conjecture. A good mathematician should be able to compute. Like physicists would do experiments to check their theorem, mathematicians should also be able to perform “experiments” to check and explore new ideas. That laboratory is called “Matlab”. Mat does not stand for mathematics, but for matrix.

The following is the Matlab code that verifies the prime number theorem. You see, you have much better tools than Gauss ever had. The question is whether you are able to use it efficiently. That is why you take this course. The code is mainly due to F. Michel and is taken from http://cnx.org/content/m12764/1.1/.

Here one starts with a list of the natural numbers. Then starting with 2, one removes every even number. The next number is 3, so now one removes every third number (half of these have already been removed by the 2). Here it is easiest to simply replace the values with zero, rather than literally removing the numbers. Now the next (non-zero) number is 5, and we set every fifth number to zero. Then 7 and then 11. By eleven, the first 121 non-zero numbers will all be primes (i.e., 11 squared). The alternative of testing each successive number to see if a smaller prime divided it would be hopelessly inefficient.

% the code is due to Michel, F.
% The Prime Number Theorem (PNT),
% http://cnx.org/content/m12764/1.1/, Apr 25, 2005.
N = 1e5; %largest possible prime in list
rpr=linspace(1,N,N); %starting list=all numbers up to N
nextp = 2; %next prime to remove from list (this is ALSO its location)
for j=2:N
if (nextp*nextp)

We numerically compute the limit with small x.

lim √x + 16000000 − 4000 .
x→0 x
for x=2.^(-(2:4:40)),disp((sqrt(x+16000000)-4000)/x),end
1.2500e-04 1.2500e-04 1.2500e-04 1.2500e-04 1.2505e-04 1.2589e-04 1.2207e-04 0 0 0



# 1. Binary numbers

A binary number is expressed as (...b₂b₁b₀.b−₁b−₂...)₂ where each bi is either 0 or 1. The base 10 equivalent of the above number is · · · + b₂2² + b₁2¹ + b₀2⁰ + b−₁2−¹ + b−₂2−² + · · · .



# 1.2 Binary to decimal

Example: Convert the binary number (0.101)₂ to decimal.

Solution: (0.101)₂ means b−₁ = 1, b−₂ = 0, b−₃ = 1. So, it is

b−₁2−¹ + b−₂2−² + b−₃2−³ = 1 × 2−¹ + 0 × 2−² + 1 × 2−³ = 1/2 + 1/8 = 5/8. □

Example: Convert the binary number (0.101 101 101 101 101 · · · ) def (0 101)₂ = . 2 to decimal.




# Solution:

(0.101)₂ = (0.101 101 101 101 101 · · · )₂

= 1 × 2−¹ + 0 × 2−² + 1 × 2−³ + 1 × 2−⁴ + 0 × 2−⁵ + 1 × 2−⁶ + · · ·

= 1 × 2−¹ + 0 × 2−² + 1 × 2−³ + 2−³ × 1 × 2−¹ + 0 × 2−² + 1 × 2−³ + · · ·

= 1 + 2−³ + 2−⁶ + · · · 1 × 2−¹ + 0 × 2−² + 1 × 2−³

= 1 + 2−³ + 2−⁶ + · · · × 5.

Now, what is 1 + 2−³ + 2−⁶ + · · · . Recall that when −1 &#x3C; r &#x3C; 1,

1 + r + r² + r³ + · · · = 1.

1 − r

So, we let r = 2−³ = 1/8 and obtain 1 + 2−³ + 2−⁶ + · · · = 1 1 = 8.

So, finally (0.101)₂ = 8 5 = 5.

□





# 1.2.2 Decimal to binary

Example: Show that the decimal number 4 is expressed as (100.)₂.

Solution: (100.)₂ means b0 = 0, b1 = 0 and b2 = 1. So, it is b22 + b11 + b00 = 1 × 22 + 0 × 21 + 0 × 20 = 4.

□




# Example:

Show that 3 is represented as (0.11)₂.

# Solution:

(0.11)₂ means b−1 = 1, b−2 = 1. So, it is b−12−1 + b−22−2 = 1 × 2−1 + 1 × 2−2 = 1/2 + 1/4 = 3/4.

□






# Example: Determine the binary representation of 53.7.

# Solution:

We break 53.7 into integer part 53 and fractional part 0.7. First, we work on the integer part:

53/2 = 26 + 1/2,
26/2 = 13 + 0/2,
13/2 = 6 + 1/2,
6/2 = 3 + 0/2,
3/2 = 1 + 1/2,
1/2 = 0 + 1/2.

The above calculation means

53 = 2 × 26 + 1 = 2 × (2 × 13 + 0) + 1 = 2 × (2 × (2 × 6 + 1) + 0) + 1 = 2 × (2 × (2 × (2 × 3 + 0) + 1) + 0) + 1 = 2 × (2 × (2 × (2 × (2 × 1 + 1) + 0) + 1) + 0) + 1.

So (53)10 = (110101)2. The 0’s and 1’s that are generated before should be recorded starting at the decimal point and then moving away.

Now, we work on the fractional part:

.7 × 2 = .4 + 1,
.4 × 2 = .8 + 0,
.8 × 2 = .6 + 1,
.6 × 2 = .2 + 1,
.2 × 2 = .4 + 0,
.4 × 2 = .8 + 0,
· · · · · .

The above calculation means

0.7 = 2−1 × 0.4 + 2−1 × 1 = 2−1 × (2−1 × 0.8 + 2−1 × 0) + 2−1 × 1 = 2−1 × (2−1 × (2−1 × 0.6 + 2−1 × 1) + 2−1 × 0) + 2−1 × 1 = · · · .






So (.7)10 = (.101...)2 = (.1011001100110...)2 = (.10110)2. The recording of the 0’s and 1’s starts at the decimal point and then moves away.

So,

(53.7)10 = (110101.10110)2. □

Check: Note that (53.7)10 = (110101.10110)2 can be directly verified:

25 + 24 + 22 + 20 + 2−1 + 2−3 + 2−4 + 2−7 + 2−8 + · · ·

= 53 + 2−1 + 2−3 + 2−4 = 53.7 □ 1 − 2−4





# 1.3 Floating point and machine representations of real numbers

We want to answer the following question: Given a decimal number, say 4, −3 or 53.7, what steps a computer would take in order to store this number? And what is the result that is being stored?

We assume the computer use the double precision format of the IEEE 754 floating point standard. So, storing any number in the computer will take 64 bits. Among the 64 bits, 1 bit is used for the sign of the number, M = 11 bits is used for the exponent and N = 52 bits is used for the mantissa. So, in the computer, a number is stored consecutively as s1...eMb1...bN. (1)

s = 0 if the number is positive and s = 1 if the number is negative. Number 0 can be stored either as 00102...0M0102...0N or as 10102...0M0102...0N.




# Table 1: Floating point formats

| Precision   | M  | N  |
| ----------- | -- | -- |
| single      | 8  | 23 |
| double      | 11 | 52 |
| long double | 15 | 64 |

Now, let us go back to the question we raised before. Let us look at an example first:

Example: As we can check, the binary representation of (9.4)10 is 1001.0110011001100110011001100110011001100110011001100110...

Then we shift the radix point to the left most and obtain 1.0010110011001100110011001100110011001100110011001100 110... × 23.

So, to store this number, we will store the exponent 3 (but after adding 1023 or 2M−¹ − 1) and then store whatever is inside the box after rounding off. Now, after rounding off, what is inside the box should change to 0010110011001100110011001100110011001100110011001101.

So, we will store three things: (1) the sign bit; (2) the binary format of number 3+1023; and (3) the 0010110011001100110011001100110011001100110011001101 (see (1)).





For the general case, the computer would take the following 4 steps.

# Step 1: Overflow or underflow.

The largest number we can represent is 21024 − 2971 and the smallest number we can represent is 2−1074. Only numbers lie in between can be represented exactly or approximately.

For general M and N, the largest and smallest numbers are (2 − ϵmach) × 22M−¹−1 and ϵmach × 22−2M−¹, where by definition ϵmach = 2−N. (For those who are interested in why, we will figure it out later.)



# Step 2: Change the number from decimal to binary.

After that, we get something like (1b1b2b3.b4b5...)2 or (0.00001b1b2b3b4b5...)2. For example:

- (4)10 = (100.)2
- − 3 = −(0.11)2
- (53.7)10 = (110101.¹0110)2



Step 3: Change it to a normalized binary numbers.

It is left most 1 is shifted to the left of the radix point. The shift is compensated by a change in the exponent. For example, (100.)₂ = (1.)₂ × 2², −(0.11)₂ = −(1.1)₂ × 2⁻¹, and (110101.10110)₂ = (1.1010110110)₂ × 2⁵.

After this step, we obtain something of the form ±(1.a₁ᵃ₂ᵃ₃ᵃ₄...)₂ × 2ᵖ. (2)



# Step 4: Looking at p to decide if it is “normal”

(when −1022 ≤ p ≤ 1023 or 2 − 2ᴹ−¹ ≤ p ≤ 2ᴹ−¹ − 1 in general) or “subnormal” (when −1074 ≤ p &#x3C; −1022).

If it is normal. Determine the ei’s so that (e₁...e₁₁)₂ = p + 1023 (or p + (2ᴹ−¹ − 1) for general M). Then apply the round to even rule to (a₁a₂a₃a₄...)₂ to obtain (b₁...b₅₂)₂.

| Input (a₁...aN aN₊₁aN₊₂...)₂ | Output (b₁...bN )₂          |
| ---------------------------- | --------------------------- |
| > the median, round up       | (b₁...bN )₂ = (a₁...aN )₂+1 |
| < the median, round down     | (b₁...bN )₂ = (a₁...aN )₂   |
| = the median, make aN even   | (b₁...bN )₂ = (a₁...aN )₂   |
| = the median, make aN even   | (b₁...bN )₂ = (a₁...aN )₂+1 |

Table 2: Round to even rule. If you need to do (1₁...1N ) + 1, you have to store it as (1₁0₂0₃...0N₊₁) and then increase p by 1.

If it is subnormal. Set (e₁...e₁₁)₂ = (0...0)₂ and put (1.a₁a₂a₃a₄...)₂ × 2ᵖ to the - mat of (0.b₁b₂...b₅₂)×2−¹⁰²². To do that, we have to shift the radix point when necessary and then apply the round to even rule to the resulting (0.0...01a₁a₂a₃...)₂.

Eventually, we store ±e₁..e₁₁b₁..b₅₂. [Remark: the subnormal case is used to represent tiny numbers. But it is some advanced topics. So, you do not need to know it if you do not like it.]

# Example:

4 = (1.)₂ × 2². So p = 2. p + 1023 = 2¹⁰ + 2⁰ = (1₁00001₁₁)₂. We have used the fact that 2¹⁰ = 1024. So, it is stored as 0 100...001 00...00 . □

# Example:

−3 = −(1.1)₂ × 2−¹. So p = −1. p + 1023 = 2¹⁰ − 2¹ = (10...0)₂ − (0...010)₂ = (011...110). So, it is stored as 1 011...110 100...00 . □

# Example:

53.7 = (1.1010110110)₂ × 2⁵. So p = 5. p + 1023 = 2¹⁰ + 2² = (100...00100)₂. 1010110110 = 101011 0110... 0110 01 10 0110 and will be round off to 101011 0110... 0110 10 . So, 53.7 is stored as 0 100...00100 101011 0110...0110 10 . □

# Example:

If some number is stored in the computer exactly as (or, we say it is machine representation is) 0 01...1 0000000000...000000000 . What is this number?

Solution: (01...1)₂ = (10...0)₂ − (0...01)₂ = 2¹⁰ − 2⁰ = 1023. So, p = 1023 − 1023 = 0. So, this number is (1.0)₂ × 2ᵖ = 1. □




Example: If some number is stored in the computer exactly as (or, we say it is machine representation is) 0 01...1 0000000000...000000001. What is this number?

Solution: (01...1)₂ = (10...0)₂ − (0...01)₂ = 2¹⁰ − 2⁰ = 1023. So, p = 1023 − 1023 = 0. So, this number is (1.0₁0₂...0₅₁1₅₂)₂ × 2ᵖ = 1 + 2−⁵². □

Remark: For general M and N, the above number is 1 + ϵmach with ϵmach = 2−ᴺ . (3)

In the following, we use fl(x) to denote the number that is associated to x after the rounding to even rule. It is called IEEE double precision floating point number. You should remember that in computer arithmetic, a real number x is replaced by fl(x). You can image that for a computer fl(x) is nothing but the machine number se₁...eMb₁...bN corresponding to x after applying the rounding to even rule. So, fl(x) is just the round off of x. When we do the computer arithmetic by hand (pretending we are computers), we would write se₁...eMb₁...bN as 1.b₁...bN × 2ᵖ with p = (e₁...eM)₂ − 2ᴹ−¹ − 1. They are equivalent. Well, I should add, in general, se₁...eMb₁...bN can be subnormal. When we are asked to find fl(x), we choose to write the result as a real number which exactly equals to fl(x) and which is simple to write down. The procedure is (x)₁₀ (......)₂ −→ fl(x).

Example: Find fl(9.4).

Solution: Recall the first Example in Section 1.3. To obtain the floating point representation, we first discard the infinite tail .1100×2−⁵² ×2³ = 2−¹⁺²−² ×2−⁴⁹ = 8+4 ×2−49 = .4×2−48 from the right end and then adding 2−⁵² × 2³ = 2−⁴⁹ 1−2−4 16−1 Therefore, in the rounding step.

fl(9.4) = 9.4 + 2−⁴⁹ − 0.4 × 2−⁴⁸ = 9.4 + 0.2 × 2−⁴⁹. □

Remark: We call 0.2 × 2−⁴⁹, which is fl(9.4) − 9.4, the rounding error.

Example: Find fl(0.4).

Solution: After some calculation, we can find (0.4)₁₀ = (.0110)₂. So 0.4 = 1.1001 × 2−² = 1. 1001 1001 ....1001 1001... × 2−².

Hence fl(0.4) = 1. 1001 1001 ....1010 × 2−² = 0.4 − 0.1001 × 2−⁵² × 2−² + 1 × 2−⁵² × 2−² = 0.4 + 1 − 2−¹ + 2−⁴ 2−⁵⁴ = 0.4 + (1 − 0.6) × 2−⁵⁴ 1 − 1/2⁴ = 0.4 + 0.1 × 2−⁵². □

Remark: So fl(0.4) − 0.4 = 0.1 × 2−⁵² = 0.1ϵmach with ϵmach = 2−⁵². So fl(0.4)−0.4 = 1 ϵmach.





We have the following general result which we will state without giving a proof.

fl(ˣ) − x ≤ 1 ϵmach (4)




# 1.4 Numbers from a computer’s point of view

Let us now look at numbers from a computer’s point of view, and you will find the world is really simple. So, our starting point is a machine number se1...Mb1...N. Then we have three cases:

1. (e1...M) = (0...0) and (e1...M) = (1...1). Then se1...Mb1...N is interpreted as normalized floating point

±1. b1...N × 2p, (e1...M)2 = p + 2M−1 − 1. (5)
2. (e1...M) = (1...1). Then se1...Mb1...N represents ∞ if b1...N = 0...0, and represents NAN which stands for “Not a Number” if b1...N = 0...0.
3. (e1...M) = (0...0). Then se1...Mb1...N is interpreted as the subnormal floating point number

±0. b1...N × 22−2M−1. (6)

Those numbers are tiny.

Note that ±0. b1...N × 22−2M−1 = ±b1.b2...N 2p with p = (0...0)2 − (2M−1 − 1).

Remark: (This remark is absolutely not required for the exam. But provided only for those who are curious.) Now, if you check our previous definition, you see that with (e1...M) = (0...0), p = (e1...M)2 − (2M−1 − 1) = (0...0)2 − (2M−1 − 1) = 1 − 2M−1. Then you might ask why (6) is not ±0. b1...N × 21−2M−1 since (e1...M) = (0...0). This change comes naturally because of the “Note that” before this remark. In addition, the smallest normalized floating point is 1.000...0 × 22−2M−1 (with (e1...M) = (0...01) and machine representation.

The denormalized numbers are small numbers and they try to bridge the gap between 1.000 × 22−2M−1 and 0. So, they start from 0 point something times 22−2M−1. Otherwise, the gap between the largest denormalized number and the smallest normalized number is unnecessarily large.

Now you can ask yourself how 0 is represented by the computer. It indeed has two ways to be presented: +0 and −0. Number 0 can be stored either as 00102...0M0102...0N or as 10102...0M0102...0N.

Note that for a normalized floating point, (0...01)2 ≤ p + 2M−1 − 1 ≤ (1...10)2, which means 2−2M−1 ≤ p ≤ 2M−1 − 1 (please check!). For M = 11, that is the −1022 ≤ p ≤ 1023 when a number is normal, which appears in “Step 4” in Section 1.3.





So the smallest nonzero representable number is 0 0...0 0...01, which is subnormal and is 2−ᴺ × 2²−²ᴹ−¹. It equals to 2−¹⁰⁷⁴ ≈ 4.94 × 10−³²⁴ for double precision (M = 11, N = 52).

Many numbers below ϵmach = 2−N are machine representable, even though adding them to 1 may have no effect (we will see that later). On the other hand, numbers below 2−ᴺ × 2²−²ᴹ−¹ cannot be represented at all.




# Example: What is the largest number that can be represented by double precision floating point representation (recall M = 11 and N = 52)?

Solution: That number should have the machine representation 0 1...10 1111...1.

So the number is (1.111...1)₂ × 2ᵖ with p = (1...10)₂ − (2ᴹ−¹ − 1) = 2¹ + 2² + ... + 2ᴹ−¹ − 2ᴹ−¹ + 1 = 2⁰ + 2¹ + ... + 2ᴹ−² = 2ᴹ−¹ − 1 = 1023. (1.111...1)₂ = 2 − ϵmach. So that number is (2 − ϵmach) × 2²ᴹ−¹−¹ = (2 − ϵmach) × 2¹⁰²³ = 2¹⁰²⁴ − 2⁹⁷¹. (Note that 2¹⁰²⁴ ≈ 1.8 × 10³⁰⁸).

Now, I hope you can go back and read Section 1.3 again. You should understand how those limits in Steps 1-4 are determined by now.






# 1.5 Addition of numbers

Now, we want to know what happens if we type in 2−53 + 1 in a computer (using C/C++, Java, Fortran, Matlab or whatever) and ask the computer to compute the sum. The computer first changes 2−53 and 1 to their machine representations. So, some rounding off may be required at this step. Then the computer grabs these two machine numbers, puts them into the register. Now, the computer needs to line up the radix points of the two numbers to be added. Then it will do the addition exactly4. The result is a floating point number. Then the computer changes the result into its machine representation. Some rounding off may be required.

4 The IEEE standard requires that the addition in this step is done so accurately that we can consider as if the addition is done exactly. The register is designed specifically for that purpose.

To summarize, the IEEE standard indeed says, when doing x + y, it is in fact

x ⊕ y def fl(fl( ) fl( )) = x + y.

Similarly, x − y is done by x ⊖ y = fl(fl(x) − fl(y)). It is important to realize that computer arithmetic, because of the truncation and rounding that it carries out, can sometimes give surprising results.

# Example: Add 2−53 to 1 using double precision arithmetic.

Solution: First of all, we recognize that the computer can save both 1 and 2−53 exactly. 1 is saved as 0 01...1 0...0 after being rewritten as 1.0...0 × 20. 2−53 is saved as 0 e1...1 0...0 with some (e1...1)₂ = (−53+1023)₁₀. Remember, to save 2−53, we have to first rewrite 2−53 as 1.0...0 × 2−53. But when we want to do the addition, we have to line up the radix points of the two numbers to be added. So, we have to change the exponents and the addition would appear as follows:

1. 01...05₂ × 20
2. 1. 01...05₂ 1 × 20
= 1. 01...05₂ 1 × 2





which is saved as 1 after applying the IEEE rounding to even rule. You see, when we line up the numbers to be added, we have to make them have the same exponents. Then some part of the mantissa can be pushed outside of the box, and that can bring trouble in some situation. □

Remark: From the 4th and 5th Examples after “Step 4” in Section 1.3, we see that the distance between 1 and the smallest machine number greater than 1 is ϵmach. By definition (see (3)), ϵmach is 2−N which is 2−52 for double precision. If we add ϵmach to 1, the result is 1. 01...05₁₁ × 20 and will be saved as 0 011...11 0...01. The result being saved is exactly right.

# Example: Find the double precision floating point sum (1 + 3 × 2−53) − 1.

Solution: Once again, both 1 and 3 × 2−53 = (1.1)₂ × 2−52 can be stored exactly. The addition would appear as follows:

1. 01...05₁₀ × 20
2.   1. 01...05₁₁ 1 × 20
= 1. 01...05₁₁ 1 × 21

After rounding off, it would be 1. 01...05₀10 × 20. Then we subtract 1. 01...05₀00 × 20. So the result is 1 × 2−51 which is 4 × 2−53 instead of 3 × 2−53. □

# Example: Recall that the IEEE rounding to even rule requires the halfway case is rounded to even (means that the rounded result has its least significant digit be even).

Another rule might simply round up in the halfway case. Suppose the machine representation we adapted in the computer is se₁e₂...eMb₁b₂ for some large M. So for 1.b₁b₂b₃...×2p we have to truncate from b₃. Now, compute (x + y) − y in the computer with x = (1.00)₂ and y = (1.11)₂ × 2−¹ using the above two different rounding rules.





Solution:

1. If the halfway case is rounded up, we get (1.01)₂ because (x ⊕ y) ⊖ y = fl(fl[(1.00)₂ + (0.111)₂]−(0.111)₂)) = fl(fl[(1.111)₂]−(0.111)₂) = fl((10.0)₂−(0.111)₂) = fl((1.001)₂) = (1.01)₂.
2. If the halfway case is rounded to even, we get (1.00)₂ because (x⊕y)⊖y = fl(fl[(1.00)₂ + (0.111)₂]−(0.111)₂)) = fl(fl[(1.111)₂]−(0.111)₂) = fl((10.0)₂−(0.111)₂) = fl((1.001)₂) = (1.00)₂.

The truth is, if the halfway case is always rounded up, computations can gradually drift upward. Similarly, always rounding down the halfway case is also problematic. □

For your information, Reiser and Knuth [1975] offer the following reason for preferring round to even. The proof of the theorem is not required.



# Theorem 1

Let x and y be floating point numbers of base β: ±b₀.b−₁b−₂... × βp for some β. Define x0 = x, x1 = (x0 ⊖ y) ⊕ y, ..., xn+1 = (xn ⊖ y) ⊕ y. If ⊖ and ⊕ (in base β) are exactly rounded using round to even, then either xn = x for all n or xn = x1 for all n ≥ 1.



# 1.6 Loss of significance

An advantage of knowing the details of computer arithmetic is that we are therefore in a better position to understand potential pitfalls in computer calculations. One major problem that arises in many forms is the loss of significant digits that results from subtracting nearly equal numbers. For example, in the subtraction problem

123.4567 − 123.4566 = 0.0001.

We started with two input numbers that we knew to seven-digit accuracy, and ended with a result that has only one-digit accuracy. Although this example is quite straightforward, there are other examples of loss of significance that are more subtle, and in many cases, this can be avoided by restructuring the calculations.

# Example:

Calculate √9.01 − 3 on a 3-decimal-digit computer. A 3-decimal-digit computer is an imaginary computer which directly uses decimal numbers instead of binary numbers to compute. But the computation result is stored with only 3 significant digits.

# Solution:

Since √9.01 ≈ 3.0016662, when we store this intermediate result to three significant digits, we get 3.00. Subtracting 3.00, we get a final answer of 0.00. No significant digits in our answer are correct.

# Remark:

Surprisingly, there is a way to save this computation, even on a 3-decimal-digit computer:

√(√9.01 − 3)(√9.01 + 3)

9.01 − 3 = √9.01 + 3

= 9.01 − 3² = 0.0100 = 1.67 × 10−3.

3.00 + 3 6.00

Note that we get all three digits correct this way. The lesson is that it is important to find ways to avoid subtracting nearly equal numbers, if possible.



The quadratic formula states that the roots of ax² + bx + c = 0 are

x₁ = −b + √b² − 4ac , x₂ = −b − √b² − 4ac.

2a 2a

Consider this formula applied to the equation x² + 62.10x + 1 = 0, whose roots are

approximately x₁ = −0.01610723 and x₂ = −62.08390. Use 4-decimal-digit rounding

arithmetic in the calculations to determine x₁.



Solution:

√b² − 4ac = (62.10)² − (4.000)(1.000)(1.000) = √3856. − 4.000 = 3852. = 62.06. So x₁ = −62.10 + 62.06 = −0.04000 = −0.02000

2.000 2.000

a poor approximation to x₁ = −0.01611 (the 4-decimal-digit representation of the exact x₁).



# Example:

Find both roots of the quadratic equation x² + 9¹²x = 3 using double precision computation.



# Solution:

Using the quadrature formula,

x± = −b ± √b² − 4ac = −9¹² ± √9²⁴ + 4 × 3.

2a 2

For the plus sign root, if you use double precision computation, you get 0. The computation of the minus sign root is standard and x− = −⁹¹²−√⁹²⁴⁺⁴×³ = −282429536481 using double precision computation. Note that −282429536481 is precisely 9.

Remark: Look at the plus sign root. Although the correct answer is close to zero, the answer of the plus sign root has no correct significant digits, even though the numbers defining the problem were specified exactly and despite the fact that double precision computation means approximately 16 significant digits (ϵmach = 2−⁵² ≈ 2.²² × 10−¹⁶). A better approach is to use x₊ = √(−4ac) which gives 1.602 × 10−¹¹ in double precision.




Example:

Compute x − sin(x) for x = 0.01000 using a 4-decimal-digit computer, supposing the sin(x) can be computed exactly (but the result may not be stored exactly).

Solution: sin(0.01) = 0.009999833334... and will be stored as 0.01000. So, x − sin(x) would be 0 by a 4-decimal-digit computer. But the exact result, after keeping 4 significant digits, is 1.667 × 10−7. □

( ) for f( )






# Example: Find the degree 4 Taylor polynomial P4(x) = sin x centered at the point x0 = 0.

Estimate the maximum possible error when using P4(x) to estimate sin x for |x| ≤ 0.01. Then looking back at the last Example, you should be able to find a better way to compute x − sin(x) for x = 0.01000 using 4-decimal-digit computer.

# Solution:

By the formula

sin(x) = sin(0) + cos(0)(x − 0) + − sin(0) (x − 0)2 + − cos(0)(x − 0)3 + sin(0) (x − 0)4 + cos(c)(x − 0)5.

So, the polynomial is P4(x) = x − x3/6. Note that degree 4 term is absent, since its coefficient is zero. The remainder term is |x5 cos c|/120 which in absolute value cannot be larger than |x|5/120. For |x| ≤ 0.01, the remainder is at most 10−10/120. We can compute x − sin(x) ≈ x − x + x3/6 = x3 ≈ 1.667 × 10−7. □





# 1.7 Evaluating a polynomial

Polynomials are the basic building blocks for many computational techniques we will structure. Because of this, it is important to know how to evaluate a polynomial efficiently.

The best way to evaluate

P(x) = a0 + a1x + a2x2 + a3x3 + · · · + anxn

is to use nested multiplication, which represents P(x) as follows

P(x) = a0 + x × (a1 + x × (a2 + x × (a3 + x × (· · · · · · )))).

We need n multiplications and n additions.

Polynomials should always be expressed in nested form before performing an evaluation because this form minimizes the number of arithmetic calculations. The reduction in the number of computations can further reduce the round-off errors.




# 1.8 Matlab

# Generate number, vector and matrix.

a=5

a=sin(10)

a=0:1:10

a=0:0.01:0.1

a=linspace(0,0.1,11)

a=[1 2; 3 4]

a=zeros(3,3)

a=rand(3,2)

# Matrix manipulation.

A=rand(4,4)

a=A([2,1],:)

b=A(2:4,1)

p=[2,1,4,3]

| P | \[0,1,0,0; | 1,0,0,0; | 0,0,0,1; | 0,0,1,0] |
| - | ---------- | -------- | -------- | -------- |

AP

AP-A(:,p)

A(1,:)=[]

B=[A,eye(3)]

# Inverting a matrix and solving a linear system

A=[0,1,0,pi; 1,0,0,0; 0,-1.01,0,1; 0,0,1,0];

inv(A)A

b=((-1:2).^2)’;

x=A\b

Ax-b

x-inv(A)*b

# 1D plot

a=linspace(0,2,100);

b=sin(a);

plot(a,b)

grid on

# 2D plot

[x,y]=meshgrid(-1:0.1:1,-2:0.1:2);

z=sin(x.^2+y.^2);

mesh(x,y,z)

# Symbolic computation

syms t

diff(sin(t))

int(sin(t))

int(sin(t),0,pi)

f = exp(-1/2*t^2);

int(f,-inf,inf)

taylor(sin(t),7)

syms t

ezplot(sin(t),[0,10])

sin(sym(’pi’))

# Variable precision arithmetic

sin(pi)

sin(vpa(pi,20))






# 1.9 Homework 1

Based on textbook: Tim Sauer, Numerical Analysis, 2nd edition

- Page 7, 0.2 Exercises, 3(d),
- Page 15, 0.3 Exercises, 1(a)(c), 5,
- Page 19, 0.4 Exercises, 1

• Run the following Matlab commands, and then explain what you see.

a=2^(-1075)
a=2^(-1074)
a=2^(1024)
a=2^(1024)-2^(971)
a=2^(971)*(2^(53)-1)
a=1+2^(-52)-1
a=1+2^(-53)-1
a=2+2^(-52)-2
a=2-2+2^(-52)
a=4+2^(-51)-4
a=4+2^(-50)-4
a=4+2^(-51)-4-2^(-51)
a=4+2^(-50)-4-2^(-50)

• Calculate the expressions that follow in double precision arithmetic (using Matlab, for example) for x = 10-1, . . . , 10-14. Then, using an alternative form of the expression that doesn’t suffer from subtracting nearly equal numbers, repeat the calculation and make a table of results. Report the number of correct digits in the original expression for each x.



a) 1 − sec x.

tan² x




# Problem Statement

b) 1 − (1 − x)³.

Consider a right triangle whose legs are of length 3344556600 and 1.2222222. How much longer is the hypotenuse than the longer leg? Give your answer with at least four correct digits.





# 2 Nonlinear equation and system of nonlinear equations

In this chapter, we want to study how to solve nonlinear equation (Chapter 1 of Sauer’s book) like

cos(x) − x = 0

or system nonlinear equation Chapter 2.7 of Sauer’s book like

x₁ + x² = 4
sin(x₁) − 4x₂ = 0



# 2.1 Bisection method

Given a function f, we want to find a number r (call a root of f) so that f(r) = 0. Let us start with the bisection method to find a root of f. The basic idea is that if f(a) and f(b) have different sign, then there is a root between a and b. So, the algorithm is as follows:

Given initial interval [a, b] such that f(a)f(b) &#x3C; 0

while (b − a)/2 > Tolerance
c = (a + b)/2
if f(c) = 0, stop, end
if f(a)f(c) &#x3C; 0
b = c
else
a = c
end

Figure 1: The bisection method.



# Finding Roots Using the Bisection Method

The final interval [a, b] contains a root. The approximate root is (a + b)/2. Use Matlab and the bisection method to find the root of the function f(x) = x³ + x − 1 on the interval [0, 1]. The error is required to be less than 0.001. (How would you guarantee the error is less than 0.001, if you do not know the exact solution?)

# Solution:

Note that in the end, exact solution is in [a, b] and the approximate solution is (a + b)/2. Hence the error is ≤ (b−a)/2.

xc = bisect(@(x) x^3+x-1,0,1,1e-8)

# where bisect.m is defined as

%Program 1.1 Bisection Method
%Computes approximate solution of f(x)=0
%Input: inline function f; a,b such that f(a)f(b)&#x3C;0, % and tolerance tol
%Output: Approximate solution xc
function xc = bisect(f,a,b,tol)
if sign(f(a))sign(f(b)) >= 0
error('f(a)f(b)&#x3C;0 not satisfied!')
%ceases execution
end
fa=f(a);
fb=f(b);
k = 0;
while (b-a)/2>tol
c=(a+b)/2;
fc=f(c);
if fc == 0
%c is a solution, done
break
end
if sign(fc)*sign(fa)&#x3C;0
%a and c make the new interval
b=c;
fb=fc;
else
%c and b make the new interval
a=c;
fa=fc;
end
end
xc=(a+b)/2; %new midpoint is best estimate



# 2.2 Fixed-point iteration

Suppose you have a scientific calculator. You enter an arbitrary positive number, say, 2, and then press the square root button. After a while, you obtain 1. If instead you keep pressing cos, you obtain 0.7390851332, at least to the first 10 decimal places.

Definition 1 A number r is a fixed point of the function g if g(r) = r.



# Definition 2

Given any x₀, the following iteration is called fixed-point iteration

xi+1 = g(xi) for i = 0, 1, 2, 3, ... (1)

If g is continuous and there is an x∗ so that xi → x∗ when i → ∞. Letting i → ∞ in (1), one immediately obtain x∗ = g(x∗). If the iteration converges, fixed-point iteration solves the fixed-point problem x = g(x). So one may ask, can any equation f(x) = 0 be turned into a fixed point problem x = g(x)? The answer is yes, and in many different ways. For example, if we want to solve x³ + x − 1 = 0, we can rewrite it as

x = 1 − x³ = g₁(x), (2)

or

x = √(3 1 − x) = g₂(x), (3)

or

x = 1 + 2x³ = g₃(x), (4)

or

x = 2x − 1 + x³ = g₄(x). (5)

The following table shows the fixed-point iteration for the preceding four choices of g(x). The starting point x = 0.5 is chosen somewhat arbitrary.

| i  | xi = g₁(xi−₁) | xi = g₂(xi−₁) | xi = g₃(xi−₁) | xi = g₄(xi−₁)  |
| -- | ------------- | ------------- | ------------- | -------------- |
| 0  | 0.50000000    | 0.50000000    | 0.50000000    | 0.50000000     |
| 1  | 0.87500000    | 0.79370053    | 0.71428571    | 0.12500000     |
| 2  | 0.33007812    | 0.59088011    | 0.68317972    | -0.74804688    |
| 3  | 0.96403747    | 0.74236393    | 0.68232842    | -2.9146814     |
| 4  | 0.10405419    | 0.63631020    | 0.68232780    | -31.590654     |
| 5  | 0.99887338    | 0.71380081    | 0.68232780    | -31590.687     |
| 6  | 0.00337606    | 0.65900615    | 0.68232780    | -3.1526605e13  |
| 7  | 0.99999996    | 0.69863261    | 0.68232780    | -3.1335139e40  |
| 8  | 0.00000012    | 0.67044850    | 0.68232780    | -3.0767690e121 |
| 9  | 1.00000000    | 0.69072912    | 0.68232780    | -Inf           |
| 24 | 0.00000000    | 0.68227157    | 0.6823278     |                |
| 25 | 1.00000000    | 0.68236807    | 0.6823278     |                |





# Figure 2: Geometry of fixed-point iteration.

- (a) g(x) = 1 − x³.
- (b) g(x) = (1 − x)¹/³.
- (c) g(x) = 1 + 2x³ / (1 + 3x²)

Figure 2 shows the three different g(x) along with the first few steps of fixed-point iteration in each case. The fixed point r is the same for each g(x). It is represented by the point where the graphs y = g(x) and y = x intersect.

The convergence properties of fixed-point iteration can be easily explained by a careful look at the algorithm in the simplest possible situation. Figure 3 shows fixed-point iteration for two linear functions:





(a) g₁(x) = − 3 x + 5

(b) g₂(x) = − 1 x + 3

In each case the fixed point is x = 1. Let ei = |xi − r|. Then:




(a)

xi+1 − 1 = g₁(xi) − 1 = g₁(xi) − g₁(1) = − 3 (xi − 1) which means ei+1 = 3 ei. Hence the error becomes larger and larger and the iteration diverges.






(b)

xi+1 − 1 = g₂(xi) − 1 = g₂(xi) − g₂(1) = − 1 (xi − 1) which means ei+1 = 1 ei. Hence the error becomes smaller and smaller and the iteration converges.

| y         | y      |
| --------- | ------ |
| 2         | 2      |
| 1         | 1      |
| 1 → x → x | $x\_0$ |
| 2         | $0$    |
| $1$       | $x\_2$ |






# Figure 3: Fixed-point iteration.

- (a) g₁(x) = − 3 x + 5.
- (b) g₂(x) = − 1 x + 3.

...ei+k ≤ |g′(r)|2 ek → 0 as i → ∞. Hence xi+k → r as i → ∞. So ci+k → r. Letting i → ∞ in xi+1 = g(ci), we proved (6).






# Definition 4

An iterative method is called locally convergent to r if the method converges to r for initial guesses sufficiently close to r.






# Example:

Explain why the fixed-point iteration with g(x) = cos(x) converges.

# Solution:

The fixed-point r satisfies r = cos(r). r ≈ 0.74 and |g′(r)| = |-sin(r)| &#x3C; 1. Hence by Theorem 1, the iteration is locally convergent. In fact, for any initial guess the iteration would converge to r.





# 2.3 Newton’s method for a single nonlinear equation f(x) = 0

Suppose x∗ is the root of function f(x). Since 0 = f(x∗) ≈ f(xₙ) + f′(xₙ)(x∗ − xₙ),

x∗ ≈ xₙ − f(xₙ)/f′(xₙ). Hence we obtain the so called Newton iteration with initial guess x₀:

xₙ₊₁ = xₙ − f′(xⁿ) . (7)




# Example

Use Newton’s method to solve for x³ + x − 1 = 0 with initial guess x₀ = −0.7.

# Solution:

x = x − x³ + xⁿ−¹ = 2ˣ³ + 1.

| y  | x | x | x | q2 | 2→x |
| -- | - | - | - | -- | --- |
| -2 |   |   |   |    |     |







# Figure 5:

Three steps of using Newton’s method to solve for x³ + x − 1 = 0. Inserting (7) from initial guess x₀ = −0.7 yields x₁ ≈ 0.1271, x₂ ≈ 0.9577. Further steps are given in the following table. After only 6 steps, the root is known to 8 correct digits.

| Step | xₙ     | f(xₙ)  | f′(xₙ) | xₙ₊₁   |
| ---- | ------ | ------ | ------ | ------ |
| 0    | -0.7   | -0.343 | 0.51   | 0.1271 |
| 1    | 0.1271 | 0.002  | 0.48   | 0.9577 |
| 2    | 0.9577 | 0.0001 | 0.29   | 0.9999 |
| 3    | 0.9999 | 0.0000 | 0.00   | 1.0000 |
| 4    | 1.0000 | 0.0000 | 0.00   | 1.0000 |
| 5    | 1.0000 | 0.0000 | 0.00   | 1.0000 |

| i | xi           | ei = xi − x∗ | ei/e²  |
| - | ------------ | ------------ | ------ |
| 0 | −0.700000000 | 1.38232780   |        |
| 1 | 0.12712551   | 0.55520230   | 0.2906 |
| 2 | 0.95767812   | 0.27535032   | 0.8933 |
| 3 | 0.73482779   | 0.05249999   | 0.6924 |
| 4 | 0.68459177   | 0.00226397   | 0.8214 |
| 5 | 0.68233217   | 0.00000437   | 0.8527 |
| 6 | 0.68232780   | 0.00000000   | 0.8541 |
| 7 | 0.68232780   | 0.00000000   |        |

# Definition 5

Let ei denotes the error after step i of an iterative method. The iteration is quadratically convergent if M = lim ei+1 &#x3C; ∞.

# Theorem 2

Let f be twice continuously differentiable and f(x) = 0. If f′(x) = 0, then Newton’s method is locally and quadratically convergent to x*. The error ei satisfies lim ei+1 = f′′(x*).

Proof: To prove local convergence, note that Newton’s method is a particular form of fixed-point iteration, where g(x) = x − f′(x) with derivative g′(x) = 1 − f′(x)² − f(x)f′′(x) = f(x)f′′(x). Since g′(x*) = 0, by Theorem 1, Newton’s method is locally convergent.

Now, we prove the quadratic convergence. By Taylor expansion, 0 = f(x) = f(xi) + f′(xi)(x − xi) + f′′(ci) (x* − xi)². Hence xi+1 − x = xi − f′(xi) − x = (x* − xi)² f′′(ci).






So ei+1 = e2 f′′′(ci). Since ci lies between x and xi, it converges to x just as xi does. We prove the quadratic convergence by letting i go to infinity.






# Homework 2

Based on textbook: Tim Sauer, Numerical Analysis, 2nd edition and Burden, Faires, Numerical Analysis, 10th edition.

1. (Sauer) Page 43, 1.2 Exercises, 1,2 (You need to design a proper fixed point iteration using Theorem 1 and use a calculator to do the computation.)






# 2. (Sauer) Page 58, 1.4 Exercises, 1(a), 2(a), 10, 11

# 3. (Burden) Page 65, 2.2 Exercises, 19.

# 4. (Burden) Page 85, 2.4 Exercises, 10.

# 5.

Show that the Newton’s method for the function f(x) = xr − a, x > 0, where r > 1 and a > 0, converges globally to b = a1/r > 0 as long as the initial guess x0 ≥ b. [Hint: You can use the fact that a bounded monotone sequence converges to a finite number. The r is not necessarily an integer.]






# Proof:

xk+1 = xk − k (xkr − br) / (r xk) = xk − (xkr − br) / (r xk) for some θ1 ∈ [0, 1]. Since g(x) = r xr−1 is an increasing function, if xk − b ≥ 0, then g(xk) − g(xk − θ1(xk − b)) ≥ 0 which implies xk+1 − b ≥ 0. By induction, we can prove xk ≥ b ∀k.

Then, since xk ≥ b, from the equation above, we know xk+1 ≤ xk. Hence xk ∈ [b, x0] and is monotonically decreasing. So it converges. Let us denote the limit by x* which is in [b, x0].

Then let k → ∞ in the equation above, we obtain x = x − (xr − br) / (r x) Hence x* = b.






# 2.5 Matrix norm

This topic is mentioned very briefly in Sauer’s book. See Section 2.3.1 (after equation (2.19)). It can also be found in Section 7.1 of Burden’s book. But we will add a bit more material.

Recall that in Linear Algebra course, you have learned that a norm on a space X is a function ∥ · ∥: X → R that assigns a real value to each vector and also satisfies the following three conditions:

1. ∥ˣ∥ ≥ 0 and ∥ˣ∥ = 0 if and only if x = 0.
2. ∥ˣ + y∥ ≤ ∥ˣ∥ + ∥ʸ∥.
3. ∥αx∥ = |α|∥ˣ∥.

When X = Rⁿ or Cⁿ, we know the following function defines the p-norm on X:

∥ˣ∥ₚ = ∥(ˣ₁, ..., xₙ)∥ₚ = p (|ˣ₁|ᵖ + ... + |ˣₙ|ᵖ).

When X = Rᵐ×ⁿ or Cᵐ×ⁿ, we want to define the matrix norm in a way so that ∥Ax∥ ≤ ∥ᴬ∥∥ˣ∥ for any x ∈ Rⁿ or Cⁿ.

In order for this property to be true, we introduce the matrix norm induced by a vector norm:

∥ᴬ∥ = sup ∥ᴬˣ∥ = sup ∥ᴬˣ∥.

There are also matrix norms that satisfy i) to iii) yet they are not induced by a vector norm. For example, one can verify that ∥A∥ = tr(A⊤A) = ∑i,j a²ij is a matrix norm, but it is not induced by a vector norm.

The following is a list of the properties of the induced matrix norm:

1. ∥ᴬˣ∥ ≤ ∥ᴬ∥∥ˣ∥ for any x where ∥ˣ∥ and ∥ᴬˣ∥ are vector norm and ∥ᴬ∥ is the induced matrix norm. [Proof: by definition]
2. ∥ᴬ∥ = sup∥ₓ∥=1 ∥ᴬˣ∥. [Proof: Take α = ∥1∥ in the identity ∥αAx∥ = |α|∥ᴬˣ∥ and note that the norm of y = ∥ˣ∥ equals 1.]
3. ∥ᴬ∥ ≥ 0 and ∥ᴬ∥ = 0 if and only if A = 0. [Proof: for any x, ∥ᴬˣ∥ ≤ ∥ᴬ∥∥ˣ∥ = 0 and therefore Ax = 0. So, A = 0. Note that we have used 0 to denote both number zero, zero vectors and zero matrices.]
4. ∥ᴬ + B∥ ≤ ∥ᴬ∥ + ∥ᴮ∥. [Proof: It follows from ∥(ᴬ + B)ˣ∥ ≤ ∥ᴬˣ∥ + ∥ᴮˣ∥.]
5. ∥αA∥ = |α|∥ᴬ∥.
6. ∥ᴬᴮ∥ ≤ ∥ᴬ∥∥ᴮ∥. [Proof: It follows from ∥(ᴬᴮ)ˣ∥ = ∥A(Bx)∥ ≤ ∥A∥∥Bx∥ ≤ ∥ᴬ∥∥ᴮ∥∥ˣ∥ after using property (1) twice. So ∥ᴬᴮ∥ = supx=0 ∥(ᴬᴮ)ˣ∥ ≤ ∥ᴬ∥∥ᴮ∥.]






# 1

x ∞ = 1 Ax with A = [−1,2; 1,0]

| 1    | 1    |
| ---- | ---- |
| 0.5  | 0.5  |
| 0    | 0    |
| −0.5 | −0.5 |
| −1   | −1   |

−3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

x 2 = 1 Ax with A = [−1,2; 1,0]

| 1    | 1    |
| ---- | ---- |
| 0.5  | 0.5  |
| 0    | 0    |
| −0.5 | −0.5 |
| −1   | −1   |

−3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

x 1 = 1 Ax with A = [−1,2; 1,0]

| 1    | 1    |
| ---- | ---- |
| 0.5  | 0.5  |
| 0    | 0    |
| −0.5 | −0.5 |
| −1   | −1   |

−3 −2 −1 0 1 2 3 −3 −2 −1 0 1 2 3

Figure 6: A = [−1, 2; 1, 0]. A⊤A = [2, −2; −2, 4] with eigenvalues ≈ 0.7639 and 5.2361.

∥ᴬ∥∞ = 3. ∥ᴬ∥₂ ≈ 2.2882. ∥ᴬ∥₁ = 2.

(7) ∥ᴬ∥∞ = ᵐᵃˣ₁≤i≤ₙ n |ᵃij | . (max row-sum)

j=1

Proof of (7):






∥ᴬ∥∞ = sup ∥ᴬˣ∥∞ = ˢᵘᵖ max | aij xj|

∥x∥∞=1 maxj |xj|=1 i j

≤ sup max |ᵃij ||ˣj| = ᵐᵃˣ |ᵃij |.

maxj |xj|=1 i j i j

So, we have proved ∥A∥∞ ≤ max1≤i≤n |ᵃij | and are only left to prove ∥A∥∞ ≥ max1≤i≤n |ᵃij | . The idea is to choose a vector of the form x = (±1, ±1, ..., ±1)

(Note that ∥x∥∞ = 1). So we assume max1≤i≤n |ᵃij | = n |ᵃkj | and choose x = (sign(ak,1), sign(ak,2), ..., sign(ak,n)).

Then ∥A∥∞ = sup∥ₓ∥ =1 ∥Ax∥∞ ≥ max1≤i≤n |ᵃij | . □

(8) ∥ᴬ∥₁ = ᵐᵃˣ1≤j≤n ( n |ᵃij |). (max column-sum) [Proof: See Homework]

Now, introduce the spectral radius of a matrix:

ρ(A) = max |λj(A)|1≤j≤n

which is the maximum of the absolute eigenvalues.

(9) ∥ᴬ∥₂ = ρ(A⊤A). ∥ ∥ ≤ ⊤ ⊤

Proof of (9): (Step 1. prove A2 ρ(A A).) Because A A is symmetric, it has n orthonormal eigen vector u1, ..., un with nonnegative eigen value λ1, ..., λn. For any x ∈ Rn with ∥x∥₂ = 1, we have x = αjuj with ∥x∥² = x⊤x = ⟨x, x⟩ = α² = 1.

So

∥ᴬˣ∥² = ⟨Ax, Ax⟩ = Aαjuj, Aαk uk (9)

2

j k

= αjαk (u⊤A⊤A<uj) = α²λj ≤ max λj. (10)</u

(Step 2. prove ∥A∥₂ ≥ ρ(A⊤A).) Let λs = maxj λj. Take x = us. Then ∥Ax∥² = λs.

2





□



# Theorem 3

If ∥A∥ &#x3C; 1, then (I − A)−¹ exists and ∥(I − A)−¹∥ ≤ 1 / (1−∥A∥)

Proof: For any y, consider the vector x = ∞ Aʲy whose existence is guaranteed by ∥A∥ &#x3C; 1. It is easy to verify that (I − A)x = y and hence (I − A)−¹ exists. Moreover, ∥(I − A)−¹y∥ = ∥x∥ ≤ 1 / ∥y∥ and hence

∥(I − A)−¹∥ = sup∥y∥=1 ∥(I − A)−¹y∥ ≤ 1 / (1 − ∥A∥) . □



# Theorem 4

We have ρ(A) ≤ ∥A∥ for any matrix norm induced by a vector norm. On the other hand, for any ε > 0, there is a matrix norm induced by a vector norm so that ρ(A) > ∥A∥ − ε.

Proof: Let λ be the largest eigenvalue and u the associated eigenvector. Then

∥ᴬ∥ = ˢᵘᵖ ∥ᴬˣ∥ ≥ ∥ᴬᵘ∥ = |λ| = ρ(ᴬ).

x=0 ∥ˣ∥ ∥ᵘ∥

(The rest of the proof is not required for the exam as it is too complicated.) On the other hand, let

T AT−¹ = J = diag(C₁, ..., Cₚ)

where Cj = tridiag(1, λj, 0) is the Jordan form. Let Dε be an n × n diagonal matrix with diagonal entries being [1, ε−¹, ε−², ..., ε1−ⁿ]. Then one can verify that

D−¹JDε = diag(E₁, ..., Eₚ)

with Ej = tridiag(ε, λj, 0). Hence ∥D−¹JDε∥∞ = ρ(A) + ε. Define the vector norm

∥ˣ∥ = ∥ᴰ−¹T ˣ∥∞.

5Recall that if an n × n matrix B satisfies “for any y, there is an x so that Bx = y”, then B is invertible.

Then ∥ᴬʸ∥ ∥ᴰ−¹T ᴬʸ∥∞ ∥ᴰ−¹T ᴬᵀ−¹ᴰεᶻ∥∞ ∥ᴬ∥ = ˢᵘᵖ ∥ʸ∥ = sup ∥ ε−¹ ∥ = sup ε ∥ ∥ y=0 y=0 Dε T y ∞ z=0 z ∞ = ∥D−¹T AT−¹Dε∥∞ = ρ(A) + ε

where z = D−¹T y. □



# Theorem 5

The following three conditions are equivalent:

1. limk→∞ ∥B∥k = 0 for some matrix norm induced by a vector norm.
2. limk→∞ ∥Bk∥ = 0 for any matrix norm induced by a vector norm.
3. ρ(B) &#x3C; 1.

Proof:

(1) ⇒ (2): ∥Bk∥ ≤ ∥B∥k → 0.

(2) ⇒ (3): Let ρ(B) = |λ|, Bu = λu. By (2), ∥B u∥ = |λ| ∥u∥ → 0, hence |λ| &#x3C; 1.

(3) ⇒ (1): By Theorem 4, there is a vector norm induced matrix norm so that ∥B∥ &#x3C; ρ(B) + ε &#x3C; 1.

□

Remark: If (1) is true for some matrix norm, it may not be true for another matrix norm as there is a matrix B so that ∥B∥1 &#x3C; 1 &#x3C; ∥B∥∞. (see the homework). If (2) is true for some matrix norm, then it is true for any matrix norm as on the finite dimensional space Rn×n, any two norms are equivalent.



# Theorem 6

limk→∞ ∥Ak ∥1/k = ρ(A).

Proof: ρ(A)k = ρ(Ak) ≤ ∥Ak ∥, hence ρ(A) ≤ ∥Ak ∥1/k. Let B = ( A . Then ρ(B) &#x3C; 1 and ρ(A) + ε hence ∥Bk ∥ → 0 by (2) of Theorem 5. Hence ∥Bk ∥ &#x3C; 1 when k > K for some K, which can be rewritten as ∥Ak ∥1/k ≤ ρ(A) + ε. □




# 2.5.1 Singular value decomposition and Frobenius norm

1/2 ∥ᴬ∥F = ∑i,j aij² = tr(A⊤A)

Because tr(BC) = tr(CB), it is easy to see that for any orthonormal matrix Ω, ∥A∥F = ∥Ωᴬ∥F = ∥ᴬΩ∥F. Actually, since ∥ᴬ∥2 = ρ(A⊤A) and ρ(ΩBΩ⊤) = ρ(B), we also have ∥ᴬ∥2 = ∥Ωᴬ∥2 = ∥ᴬΩ∥2.

Recall the singular value decomposition R := U V with U, R, V ∈ Rn×n, Λ ∈ Rm×n, U and V are orthonormal and Λ is diagonal with nonnegative entries {σ1, ..., σp} (p = min{m, n}) which are called the singular values of A. Then ∥A∥2 = ρ(A⊤A) leads to ∥A∥2 = maxi σi and one can prove ∥A∥F = σ1² + ... + σp². For the proof, see “Numerical Linear Algebra” by Trefethen and Bau.





# 2.5.2 Condition number

This definition is used when solving system of equations Ax = b which we have not touch yet, even though you’ve learned method like Gauss elimination. It is included here for completeness and also to show you how the relative error of solution is related to the input error.

The condition number of a matrix A with respect to p-norm is defined as

Condp(A) = ∥A∥p∥A−1∥p

Note that ∥A∥p∥A−1∥p ≥ ∥AA−1∥p = 1. Suppose we want to solve Ax = b and suppose the input vector b has an error ∆b and hence we are solving A(x + ∆x) = Ay = b + ∆b. Then A∆x = ∆b and because ∥b∥p ≤ ∥A∥p∥x∥p

∥∆x∥p ≤ ∥A∥p∥A−1∆b∥p ≤ Condp(A)∥∆b∥p

∥x∥p ∥b∥p ∥b∥p

The above equation is discussed on Page 91 of Sauer’s book.




# 2.6 Newton’s method in Rn

We have introduced linear convergence and quadratic convergence. More generally, we can define order of convergence in the following way:






# Definition 6 (Order of convergence)

A sequence of vector x0, x1, ... ∈ Rn converges cally to x* with order r if for sufficient all large k, and some positive constant C independent of k.

∥xk+1 − x∥ ≤ C ∥xk − x∥r

If r = 1 and C &#x3C; 1, we have so called linear convergence. r > 1 means superlinear convergence. In the special case of r = 2, it is called quadratic convergence. Note that if we define ek = C∥xk − x*∥, we get ek+1 ≤ ek2.

Given F : Rn → Rn, Newton’s method for finding zeros of the nonlinear function F(x) = 0 is given by

xk+1 = xk − F′(xk)−1F(xk).

(11)

Given f : Rn → R, Newton’s method for finding a minimizer of f is given by

xk+1 = xk − H(xk)−1g(xk).

(12)

where g = ∇f ∈ Rn, H = D2f ∈ Rn×n.

The requirement on the initial guess x0 that we need in order to guarantee the convergence of Newton’s method is stated in the next section. Bad initial guess can make xk diverge.






# Example:

Use Newton’s Method with starting guess x0 = (1, 2)⊤ to find a solution of the system

- v − u3 = 0
- u2 + v2 = 1.

2 x0

x1

−1 2→x






# Solution:

F(u, v) = 2v − u³, DF(u, v) = −³ᵘ² 1

x₁ = x₀ − −3 1 1 = 1

x₂ = x₁ − −3 1 −1 0 = 7/8.

| step | u                | U                |
| ---- | ---------------- | ---------------- |
| 0    | 1.00000000000000 | 2.00000000000000 |
| 1    | 1.00000000000000 | 1.00000000000000 |
| 2    | 0.87500000000000 | 0.62500000000000 |
| 3    | 0.82903634826712 | 0.56434911242604 |
| 4    | 0.82604010817065 | 0.56361977350284 |
| 5    | 0.82603135773241 | 0.56362416213163 |
| 6    | 0.82603135765419 | 0.56362416216126 |
| 7    | 0.82603135765419 | 0.56362416216126 |





# 2.6.1 Proof of quadratic convergence

(This proof is not required for the exam.)

Assume F has a zero value at x∗, F′(x∗) is invertable, F′ is Lipschitz continuous in the region {x, ∥ˣ − x∗∥ ≤ a} with a Lipschitz constant K. Define the solution ⁿᵉⁱᵍʰᵇᵒʳ Ω = {x ∈ Rⁿ, ∥x − x∗∥ ≤ min(a, ∥ ′1 −1 )} and eₖ = ∥xₖ − x∗∥.

# Lemma 1

xₖ₊₁ − x∗ = F′(xₖ )−¹ 01[F′(xk + t(x∗ − xk )) − F′(xk )]dt(x∗ − xk )

Proof: Because 01 F′(xk + t(x∗ − xk ))(x∗ − xₖ )dt = F(x∗) − F(xₖ ) = −F(xₖ ), the right hand side equals to

F′(xₖ )−¹ (−F(xₖ ) − F′(xₖ )(x∗ − xₖ )) = −F′(xₖ )−¹F(xₖ ) − (x∗ − xₖ ). □

# Lemma 2

If x ∈ Ω, then ∥F′(x)−¹∥ ≤ 2∥F′(x∗)−¹∥.

Proof: The idea is to use Theorem 3 (If ∥A∥ &#x3C; 1, then (I − A)−¹ exists and ∥(I − A)−¹∥ ≤ 1 1−∥A∥).

∥ᴵ − F′(ˣ)F′(ˣ∗)−¹∥ = ∥ (F′(ˣ∗) − F′(ˣ)) F′(ˣ∗)−¹∥ ≤ K∥ˣ − x∗∥∥F′(ˣ∗)−¹∥ ≤ 1.

So, F′(x)F′(x∗)−¹ is invertible and ∥ (F′(x)F′(x∗)−¹)−¹ ∥ ≤ 1 1 = 2. In particular, F′(x) is non-singular. So,

∥F′(ˣ)−¹∥ = ∥F′(ˣ∗)−¹F′(ˣ∗)F′(ˣ)−¹∥ ≤ ∥F′(ˣ∗)−¹∥2. □



# Theorem 7

If \( x_k \in \Omega \), then \( e_{k+1} \leq K \|F'(x^*)^{-1}\| e^2 \) and \( x_{k+1} \in \Omega \).




Proof:

By Lemma 1 and then Lemma 2,

( ek+1 ≤ F'(xk)-1 ∫01 K (x - xk)2 dt ≤ K2 F'(x)-1 &#x26;frac{1}{2} e2.)

If ( xk ∈ Ω ), ( xk+1 - x ≤ &#x26;frac{1}{4K} F'(x)-1 ) and so ( xk+1 ∈ Ω.) □





# 2.7 Secant method for a single nonlinear equation

This is from Chapter 1.5.1 of Sauer’s book.

Given a nonlinear function f, suppose we want to find x∗ so that f(x∗) = 0. The secant method is as follows: Given xₖ−₁ and xₖ, draw a secant line through (xₖ−₁, f(xₖ−₁)), (xₖ, f(xₖ)) which intersect the x-axis at xₖ₊₁

xₖ₊₁ = xₖ − f(xₖ) (xₖ − xₖ−₁) / (f(xₖ) − f(xₖ−₁)) (13)

Because f(x∗) = 0, from (13), we get

xₖ₊₁ − x∗ = xₖ − x∗ − (f(xₖ) − f(x∗)) (xₖ − xₖ−₁) / (f(xₖ) − f(xₖ−₁))

= xₖ − x∗ − (f(xᵏ) − f(x∗)) = (xₖ − x∗) (1 − f[xₖ, x∗] / f[xₖ−₁, xₖ])

= (xₖ − x∗)(xₖ−₁ − x∗) f[xᵏ−¹, xᵏ, x∗] / f[xₖ−₁, xₖ]

= (xₖ − x∗)(xₖ−₁ − x∗) f′′′(ξ²) / (2f(ξ₁))

where for the proof, we have assume f ∈ C² and we further assume x∗ is a simple root of f. Hence in a sufficient small neighborhood of x∗, there is a M > 0 so that

f′′′(ξ₂) ≤ M / (2f(ξ₁))

Define eₖ = M |xₖ − x∗|, then

eₖ₊₁ ≤ eₖ eₖ−₁ ⇒ ≤ ηₖ₊₁ ηₖ + ηₖ−₁ with ηₖ = ln eₖ




One can then prove that ηk ≤ c0rk with r = 1+√5 by induction where c0 depends on e0 and e. Note that r is the positive root of the characteristic equation η = ηk + 1. Hence rek α with α = ec0 &#x3C; 1 if e0 &#x3C; 1, e1 &#x3C; 1. Note that if ek = αrk, then ek+1 = αrkr = αrk = (ek)r. So, we sometimes say that the secant method has order of convergence 1+√5.

Remark: Note that f(xk) (x − xk) can be viewed as an approximation of f( xk)/f′( xk) used in the Newton method which has order of convergence 2. We will go back to this point when we talk about quasi-Newton in Rn.





# Example:

Apply the Secant Method with starting guesses x0 = 0, x1 = 1 to find the root of f(x) = x3 + x − 1.




# Solution:

xi+1 = xi − (f(xi)(xi − xi−1))/(f(xi) − f(xi−1)).

Starting from x0 = 0 and x1 = 1, we compute:

x2 = 1 − (1)(1 − 0)/(1 − 0) = 2, x3 = 2 − (1)(1 − 0)/(8 − 3 − 1) = 11.

| i | xi               |
| - | ---------------- |
| 0 | 0.00000000000000 |
| 1 | 1.00000000000000 |
| 2 | 0.50000000000000 |
| 3 | 0.63636363636364 |
| 4 | 0.69005235602094 |
| 5 | 0.68202041964819 |
| 6 | 0.68232578140989 |
| 7 | 0.68232780435903 |
| 8 | 0.68232780382802 |
| 9 | 0.68232780382802 |





# 2.8 Quasi-Newton Method in Rn

The computation of F′(xk) (11) can be expensive. One can try to use finite difference to replace the derivative. An example that we have already seen is the secant method. We will use matrix Bk to approximate F′(xk). Since

F′(xk+1)(xk+1 − xk) ≈ F(xk+1) − F(xk),

we will enforce the following secant condition (also called quasi-Newton condition)

Bk+1(xk+1 − xk) = F(xk+1) − F(xk).

If we define sk = xk+1 − xk, vk = F(xk+1) − F(xk), we have

Bk+1sk = vk. (15)

The secant condition is just a system of n equations and therefore is not sufficient to uniquely determine the n² unknowns from Bk+1. It is necessary to enforce further conditions on Bk+1.



# 2.8.1 Broyden’s Method for System of Nonlinear Equations

We would like to update Bk+1 by using Bk from the last iteration. Some formula can be worked out if we consider the following rank one update:

Bk+1 = Bk + ukwk⊤. (16)

From secant condition, we have

vk = Bk+1sk = (Bk + ukwk⊤)sk

which implies

uk = vk − Bksk. (17)

One example of wk that ensures wksk = 0 is wk = sk. This leads to the following Broyden’s method:

⊤

Solve sk so that Bksk = −F(xk)

xk+1 = xk + sk, vk = F(xk+1) − F(xk)

Bk+1 = Bk + (vk − Bksk)sk⊤



# 2.8.2 Convergence Proof of Broyden’s Method

(This proof is not required for the exam.)

We will use L² matrix norm in the following discussion because it involves projection matrix. A projection matrix P is an n × n square matrix that gives a vector space projection from Rⁿ to a subspace W. A square matrix P is a projection matrix if and only if P = P².

It is possible that P > 1. For example, P = [1, 1; 0; 0]. But if we also require P = P then P u, (I − P)u = 0, u² = P u² + (I − P)u². So P = 1 if P = 0.

Assume F has a zero value at x∗, F(x∗) is invertible, F is Lipschitz continuous in the region {x, x − x∗ ≤ a} with a Lipschitz constant K. Let A = F′(x∗) and ek = xk − x∗.

Define the solution neighbor Ω = {(x, B), x − x∗ ≤ a, B − A + 3K x − x∗ ≤ 1−1}.

To prove the convergence of Broyden’s method, we need the following lemma, which is an immediate consequence of Theorem 3.



# Lemma 3

If A−¹ exists, ∥A−¹∥∥A − B∥ &#x3C; 1, then B−¹ exists and

∥B−¹∥ ≤ ∥A−¹∥

1 − ∥A−¹∥∥A − B∥




Proof:

By Theorem 3, because ∥I − A−¹B∥ ≤ ∥A−¹∥∥A − B∥ &#x3C; 1, I − (I − A−¹B) = A−¹B is invertible, which implies B is non-singular. And ∥ A−¹B−¹ ∥ ≤ − ∥ 1 − ≤ − 1 .

1 I − A 1B∥ 1 − ∥A 1∥∥A − B∥

Then the result follows from ∥B−¹∥ ≤ ∥B−¹A∥∥A−¹∥. □





# Theorem 8

If (xk, Bk) ∈ Ω, then (xk+1, Bk+1) ∈ Ω and ek+1 &#x3C; 1 ek.



# Proof:

The proof contains the following 6 steps:




(a) Claim that

1. xk+1 − x = B−1 Bk − A − [F′(xk + t(x − xk)) − F′(x)]dt (xk − x). (18)

The proof is very simple, because the right hand side equals (xk − x) − B−1 (F(xk) − F(x)) = (xk − x*) − B−1F(xk).




We are going to use the Lipschitz condition on the integral. If (xk, Bk) ∈ Ω, then by (a) and Lemma 3

ek+1 ≤ ∥B−1∥ ∥Bk − A∥ + K ek ek ≤ ∥A−1∥ ∥Bk − A∥ + K ek ek

k2 1 − ∥A−1∥∥A − Bk∥2 ≤ ∥A−1∥ 1 ek = 1 ek.

1 − 1 3∥A−1∥2 3

We are almost done, except we need to estimate ∥Bk+1 − A∥ in order to finish the induction. That’s why the next few steps.






One can easily verify that the last equation of Broyden’s method can be immediately rewritten as

sk s⊤ (vk − Ask)s⊤

Bk+1 − A = (Bk − A) I − s⊤ k + ⊤ k

k sk sk sk






(d)

One recognizes that *sks⊤ and I - sks⊤ are simply projection matrices. Therefore sks⊤ ≤ k s⊤sk s⊤sk s⊤sk*
*k k k*
*1 and I - sks⊤ ≤ 1*
*k s⊤sk*

(e) Simply plugging in the definition, one can verify that

*1 vk - Ask = 0 [F′(xk + t(xk+1 - xk)) - F′(x*)]dtsk.*

(f) If *∥xk - x*∥ ≤ a and ∥xk+1 - x*∥ ≤ a*, plugging (e) into (c), using (d) and the Lipschitz condition we get

*1 ∥Bk+1 - A∥ ≤ ∥Bk - A∥ + 0 K∥xk + t(xk+1 - xk) - x*∥dt*

*≤ ∥Bk - A∥ + K (∥xk - x*∥ + ∥xk+1 - x*∥)*

Here we have used the inequality *1 ∥a + tb∥dt ≤ 1 (∥a∥ + ∥a + b∥) which follows from the fact that the function t f(t) = a + tb is a convex function. Recall that a convex function means f(θt1 + (1 − θ)t2) ≤ θf(t1) + (1 − θ)f(t2) for any θ ∈ [0, 1] and any t1, t2. So if ∥xk+1 - x*∥ ≤ 1 ∥xk - x*∥*, from the above inequality, we can easily get

*∥Bk+1 - A∥ + 3K ∥xk+1 - x*∥ ≤ ∥Bk - A∥ + 3K ∥xk - x*∥.*

*2 2*

By (b) and the above inequality, *(xk+1, Bk+1) ∈ Ω.* This finishes the proof. □





# 2.8.3 Symmetric Broyden’s method for Minimization Problem

(For your information only. It won’t be tested.) If we want to solve x = argminf(x) with f : Rⁿ → R, since the Hessian is symmetric, it seems reasonable to ask that each Bₖ₊₁ be symmetric as well. If we still use rank one update (16), and of Bₖ is symmetric, we would require wₖ = γₖ uₖ with γₖ a scalar. From (17), we know uₖ (and hence wₖ ) is in the direction of vₖ − Bₖ sₖ. We can then obtain the unique symmetric rank one update

Bₖ₊₁ = Bₖ + (vᵏ − Bᵏ sᵏ)(vᵏ − Bᵏ sᵏ)⊤.

(vₖ − Bₖ sₖ)⊤sₖ

Symmetric Broyden’s method for minimization problem x = argminf(x) is given by:

1. Solve pₖ so that Bₖpₖ = −∇f(xₖ).
2. Perform a line search along the quasi-Newton direction, i.e., compute the αₖ that minimizes f(xₖ + αpₖ) over α > 0.
3. xₖ₊₁ = xₖ + αₖpₖ
4. sₖ = xₖ₊₁ − xₖ = αₖpₖ, vₖ = ∇f(xₖ₊₁) − ∇f(xₖ)
5. Bₖ₊₁ = Bₖ + (ᵛᵏ−ᴮᵏˢᵏ)(ᵛᵏ−ᴮᵏˢᵏ)⊤
6. (vₖ−Bₖsₖ)⊤sₖ

Remark: It is not obvious what is the best method for minimizing f(xₖ + αpₖ) for general f. Perhaps we could use a one-dimensional Newton or secant method. The number of iterations required for convergence depends on the problem and it is common to restart the problem after say every n or 2n iterations.

If we want Bₖ not just symmetric, but also symmetric positive definite, we can go to rank two update, and have the so called BFGS and DFP formula. See S. G. Nash and A. Sofer, “Linear and nonlinear programming” (1996) for details.




# 2.9 Homework 3

1. (Sauer) Page 136, 2.7 Exercises, 1(a),(b), 4.
2. (Sauer) Page 63. Read Sauer’s brief remark on Muller’s method.
3. (Burden) Page 645. Read Theorem 10.6 and Example 2.
4. Prove ∥A∥₁ = max₁≤j≤ₙ ( n |ᵃij |). (max column-sum) Proof:
∥ᴬ∥₁ = sup ∥ᴬˣ∥₁ = sup | aij xj| ≤ sup |ᵃij xj|

∥x∥₁=1 ∥x∥₁=1 i j ∥x∥₁=1 i j

= sup |ᵃij ||ˣj| = sup |ᵃij ||ˣj|

∥x∥₁=1 i j ∥x∥₁=1 j i

= sup |ˣj| |ᵃij |

|x₁|+...+|xₙ|=1 j i

≤ max |ᵃij | sup |ˣj| = ᵐᵃˣ |ᵃij |.

j i |x₁|+...+|xₙ|=1 j j i

As long as we can also prove ∥A∥₁ ≥ maxj i |aij |, we are done. That follows from taking e = (0, ..., 0, 1, 0, ..., 0)⊤ so that ∥e∥₁ = 1 and Ax will select say, the k−th column vector of A whose 1-norm is assumed to be the largest among all the column vectors of A. So, ∥ᴬ∥₁ ≥ ∥ᴬᵉ∥¹ = i |aik | = maxj i |aij |. □
5. Consider the following iteration xₖ₊₁ = G(xₖ ) (19) where xₖ ∈ Rⁿ and G(xₖ ) ∈ Rⁿ. When it converges, we obtain x that satisfies x = G(x). If we want to solve H(x) = 0, we can write it as x = αH(x) + x for some scalar or matrix α and use the above method to try to find the solution. The issue is whether such iteration will converge.
1. a) Show that the Newton’s method to solve F(x) = 0 can be written into (19) and figure out the specific form of G.
Proof: G(x) = x − (F′(x))−¹F(x) or α = −(F′(x))−¹. Note that one cannot write F′((x)) since F′(x) is a matrix and dividing a matrix does not make sense. □






# b) Prove the following fact:

If the mapping G : Rⁿ → Rⁿ is contractive, i.e., there is a constant λ &#x3C; 1 such that

∥G(x) − G(y)∥ ≤ λ∥x − y∥ for some vector norm ∥ · ∥, then there is an x and only one x such

that

lim ∥xₖ − x∥ = 0

k→∞

and this x satisfies G(x) = x.

Proof: ∥xₙ − xₙ₊ₖ ∥ ≤ k ∥xₙ+i−₁ − xₙ+i∥ ≤ k λⁿ⁺ⁱ−¹∥x₀ − x₁∥ ≤ ∥x₀ − x₁∥ λⁿ → ∞

i=1

i=1

≤ { 1−λ 0 when n λ &#x3C; 1. Hence xₙ is a Cauchy sequence and therefore converge. Let us

call the limit x. Because ∥G(x) − G(y)∥ ≤ λ∥x − y∥, G is continuous. Then because G is

continuous, by letting n → ∞ in xₙ₊₁ = G(xₙ) we obtain x = G(x).

If we start from different x₀, we have different {xₙ}. One might wonder if the different

sequence will converge to different limit. Suppose x∗ is another limit. We still have x∗ = G(x∗). Then ∥x − x∗∥ = ∥G(x) − G(x∗)∥ ≤ λ∥x − x∗∥ for λ &#x3C; 1. Hence ∥x − x∗∥ = 0. So

sequences with different x₀ will converge to the same limit.





# 6. Verify the following formula for rank one updated matrix

A + uv⊤ −¹ = A−¹ − A−¹uv⊤A−¹.

# Proof:

A + uv⊤ A−¹ − A−¹uv⊤A−¹ = I − uv⊤A−¹ + uv⊤A−¹ − u v⊤A−¹u v⊤A−¹

1 + v⊤A−¹u 1 + v⊤A−¹u

= I + uv⊤A−¹ − 1 1 + 1 − α = I

α 1 + α

where the scalar α = v⊤A−¹u. □



# 7. Let us introduce the Golden section search method to find the minimizer of f(x).

Suppose we are given x₁, x₃ and x₂ so that x₁ &#x3C; x₃ &#x3C; x₂ and f(x₁) > f(x₃) &#x3C; f(x₂) (20) and suppose x₃ − x₁ &#x3C; x₂ − x₃. Certainly, a minimizer exists in the interval [x₁, x₂]. We want to shrink this interval of uncertainty. So we take an x₄ ∈ (x₃, x₂) (which is the longer interval) and according to the size of f(x₄) we choose either [x₁, x₄] (when f(x₃) &#x3C; f(x₄)) or [x₃, x₂] (when f(x₃) > f(x₄)) as the new “existence” interval. We should choose x₄ so that the two possible uncertain intervals have the same length: x₄ − x₁ = x₂ − x₃.

This requirement is based on the following intuition: If they are not, a run of “bad luck” could lead to the wider interval being used many times, thus slowing down the rate of convergence.

Then we rename the three points in this new interval of uncertainty and repeat. The golden section search chooses the spacing between x₁, x₃, x₂ in such a way that these three points have the same proportion of spacing as the subsequent triple x₁, x₃, x₄ or x₃, x₄, x₂. By maintaining the same proportion of spacing throughout the algorithm, we avoid a situation in which x₃ is very close to x₁ or x₂, and guarantee that the interval width shrinks by the same constant proportion in each step.

Based on the above requirements, figure out given x₁ and x₂, how the point x₃ and x₄ should be located. Then prove that the length of the interval of uncertainty decreases at a constant rate √₅−₁ ≈ 0.618.

# Solution:

x₁ − − − −a − − − −x₃ − − − b − − − x₄ − − − c − − − x₂.

Let a = x₃ − x₁, b = x₄ − x₃, c = x₂ − x₄. Then x₄ − x₁ = x₂ − x₃ implies a = c. The “same proportion of spacing” requirement implies a = b (obviously, it cannot be a = c). Together with a = c, we can solve for b = 1.

Each step, the size of the uncertain interval reduce by a factor a a⁺ᵇ = 1 a = 1 = √₅−1.




# 2.10 Computer Project 1

1. (Sauer) Page 136, 2.7 Computer Problems, Question 4.

The solution you submit should contains the code as well as the plot of k v.s. ∥F(u, v, ʷ)∥₂.





# 3 Interpolation

We will use Pn to denote polynomials of degree at most n. A function is said to interpolate a set of data points if it passes through those points. In other words, we say the function p(x) interpolates the data points (x1, f1), ..., (xn, fn) if p(xi) = fi for i = 1, ..., n. See Figure 1 for an example.

# Figure 1: Interpolation by parabola.

The points (0, 1), (2, 2), (3, 4) are interpolated by the function p(x) = 1/2 x² - 1/2 x + 1.



# Example

Find the polynomial of degree 3 or less that interpolates the points (0, 2), (1, 1), (2, 0), and (3, −1).




# Solution:

Assume the 3rd order polynomial is

p(x) = a1 + a2x + a3x² + a4x³.

Then, from the requirement p(xi) = fi for i = 1, 2, 3, 4, we obtain 4 equations which can be written as

| 1 | x1 | x1² | x1³ | a1 |
| - | -- | --- | --- | -- |
| 1 | x2 | x2² | x2³ | a2 |
| 1 | x3 | x3² | x3³ | a3 |
| 1 | x4 | x4² | x4³ | a4 |

and we obtain (a1, a2, a3, a4) = (2, −1, 0, 0). So, p(x) = 2 − x.  □





# 3.1 Lagrange interpolation

The previous approach gives a possible way to determine the interpolation polynomial. But sometimes it is not so easy to solve for a 4 by 4 system of equations. So, there is another approach which is based on the following observation: Let

ℓi(x) = x − xj.(2)

j=1,..,n,j=i xi − xj

Example: Suppose n = 4. Then

ℓ2(x) = (x − x1) (x − x3) (x − x4) ∈ P3

(x2 − x1) (x2 − x3) (x2 − x4)

and it is easy to check that ℓ2(x2) = 1 and ℓ2(x1) = ℓ2(x3) = ℓ2(x4) = 0. □

The observation is that that ℓi(x) ∈ Pn−1 and

ℓi(xj) = δij = 1 if i = j
0 otherwise

Hence if we define

n
pn−1(x) = ∑i=1n fiℓi(x). (3)

Then pn−1(x) ∈ Pn−1 and pn−1(xi) = ∑j=1n fjℓj(xi) = ∑j=1n fjδji = fi.

Example: Find an interpolation polynomial of degree 2 or less for the data points (0, 1), (2, 2) and (3, 4).

Solution: By the Lagrange interpolation formula,

p2(x) = f1ℓ1(x) + f2ℓ2(x) + f3ℓ3(x)

= 1 (x − 2)(x − 3) + 2 (x − 0)(x − 3) + 4 (x − 0)(x − 2)

(0 − 2)(0 − 3) (2 − 0)(2 − 3) (3 − 0)(3 − 2)




1 x2 − 1 x + 1.

One can check that p2(0) = 1, p2(2) = 2, and p2(3) = 4. □

# Example: Find an interpolation polynomial of degree 3 or less for the data points (0, 2), (1, 1), (2, 0) and (3, −1).

Solution: By the Lagrange interpolation formula,

p3(x) = f1ℓ1(x) + f2ℓ2(x) + f3ℓ3(x) + f4ℓ4(x)

= 2 (x − 1)(x − 2)(x − 3) + 1 (x − 0)(x − 2)(x − 3)



# Theorem 1

Let (x₁, f₁),...,(xₙ, fₙ) be n points in the plane with distinct xᵢ. Then there exists one and only one polynomial P of degree n − 1 or less that satisfies P(xᵢ) = fᵢ for i = 1, ..., n.




# Proof:

The existence is proved by the explicit formula for Lagrange interpolation. To show that there is only one, assume for the sake of argument that there are two, say, P(x) and Q(x), that have degree at most n − 1 and that both interpolate all n points. That is, we are assuming that P(x₁) = f₁ = Q(x₁), ..., P(xₙ) = fₙ = Q(xₙ). Now define the new polynomial H(x) = P(x) − Q(x). Clearly, the degree of H is also at most n − 1, and note that 0 = H(x₁) = ... = H(xₙ); that is, H has n distinct zeros. According to the fundamental theorem of algebra, a degree d polynomial can have at most d zeros, unless it is the identically zero polynomial. Therefore, H is identically zero polynomial, and P(x) = Q(x). We conclude that there is a unique P(x) of degree ≤ n − 1 interpolating the n points (xᵢ, fᵢ). □





# Example:

Find interpolation polynomials of degree 3 or less for the data points (0, 1), (2, 2) and (3, 4).



Solution:

From Example 3.3, we already know the following 2nd order polynomial interpolates the data.

p₂(x) = 1x² − 1x + 1.

Then for any constant a, p₃(x) = p₂(x) + a(x − 0)(x − 2)(x − 3) would interpolate the same data. So, there are infinitely many interpolation polynomials of degree 3 or less, but only one polynomial if we require the degree is 2 or less. □



Example:

Let x₀, x₁, ..., xₙ be distinct real points and consider the following interpolation problem.

Choose a function

P(z) = cₖ eᵏᶻ such that P(xᵢ) = yᵢ for i = 0, 1, ..., n with the given data {yᵢ}. Show that this problem can be reduced to an ordinary polynomial interpolation and then use Lagrange interpolation polynomial to find a general formula for P(x).




# Solution:

Let P(z) = cₖ eᵏᶻ. Define q(x) by q(x) = P(ln(x)) = cₖ xᵏ. Let x = eᶻ, then q(eᶻ) = P(z) = cₖ eᵏᶻ.

So if P(xᵢ) = yᵢ, then q(eᵢ) = P(xᵢ) = yᵢ and therefore (the polynomial is q(x), the data points are (eᵢ, yᵢ)i=0n)

q(x) = yᵢℓᵢ(x) where ℓᵢ(x) = x − eˣʲ.

i=0 j=0,...,n,j=i eˣᵢ − eˣⱼ

So P(x) = p(eˣ) =

For our example,

| 0 | 1 | 1 |   |
| - | - | - | - |
| 2 | 1 |   |   |
| 2 |   | 2 | 2 |
|   | 2 |   |   |
| 3 | 4 |   |   |

Hence the polynomial is

p₂(x) = 1 + 1 (x − 0) + 1 (x − 0)(x − 2) = 1 x² − 1 x + 1. □

# Example:

Suppose we add the fourth data point (1, 0) to the previous example. Determine the interpolation polynomial.

Solution:

| 0 |   | 1   | 1 |
| - | - | --- | - |
|   | 2 | 1   |   |
| 2 | 2 | 2   | 1 |
|   | 2 | − 2 |   |
| 3 | 4 | 0   |   |
|   | 2 |     |   |

Hence the polynomial is

p₃(x) = p₂(x) + − 1 (ˣ − 0)(ˣ − 2)(ˣ − 3). □






# Proof of Theorem 2

We prove it by induction. Formula (7) is true when n = 1. (Why? Because p₀(x) = d₁ = f[x₁] = f₁ is the desired 0th order polynomial.) Suppose (7) is true for k − 1. Then

pₖ−₂(x) = f[x₁] + f_{x₁, x₂} + ... + f_{x₁, ..., xₖ−₁} · · · (x − xₖ−₂) interpolates at x₁, ..., xₖ−₁ and

qₖ−₂(x) = f[x₂] + f_{x₂, x₃} + ... + f_{x₂, ..., xₖ} · · · (x − xₖ−₁) interpolates at x₂, ..., xₖ.

Define

qₖ−₁ = (x − x₁)qᵏ−₂(x) − (x − xₖ)pᵏ−₂(x).

xₖ − x₁

Then qₖ−₁(x₁) = pₖ−₂(x₁) = f₁, qₖ−₁(xₖ) = qₖ−₂(xₖ) = fₖ. For i = 2, ..., k − 1, qₖ−₁(xᵢ) = (x − x₁)fᵢ − (x − xₖ)fᵢ = fᵢ. So qₖ−₁ interpolates at x₁, ..., xₖ. On the other hand, as qₖ−₁ ∈ Pₖ−₁, we can always write it as

qₖ−₁(x) = c₁ + c₂(x − x₁) + ... + cₖ−₁(x − x₁) · · · (x − xₖ−₂) + cₖ(x − x₁) · · · (x − xₖ−₁)

since span{1, x − x₁, ..., (x − x₁) · · · (x − xₖ−₁)} = span{1, x, x², ..., xₖ−₁} = Pₖ−₁. By pairing the coefficient of xₖ−₁ in

c₁ + c₂(x − x₁) + ... + cₖ−₁(x − x₁) · · · (x − xₖ−₂) + cₖ(x − x₁) · · · (x − xₖ−₁)

= (x − x₁) (... + f_{x₂, ..., xₖ} · · · (x − xₖ−₁)) − (x − xₖ) (... + f_{x₁, ..., xₖ−₁} · · · (x − xₖ−₂)),

we get

c = f[x₂, ..., xₖ] − f[x₁, ..., xₖ−₁] def f[ ]

for k = xₖ − x₁ = x₁, x₂, ..., xₖ. To determine cᵢ for i &#x3C; k. Consider

pₖ−₂(x) = qₖ−₁(x) − cₖ(x − x₁)(x − xₖ−₁) = c₁ + ... + cₖ−₁(x − x₁) · · · (x − xₖ−₂)

which is in Pₖ−₂ and interpolates x₁, ..., xₖ−₁. We already know the formula (7) is true when there are k − 1 interpolation points. So cᵢ = f[x₁, ..., xᵢ] for i = 1, ..., k − 1. □






# Example:

The following data are taken from a polynomial of degree ≤ 5. What is the degree of the polynomial?

| x    | −2 | −1 | 0 | 1 | 2 | 3  |
| ---- | -- | -- | - | - | - | -- |
| p(x) | −5 | 1  | 1 | 1 | 7 | 25 |

# Solution:

−2 | −5
− | 6
1 | 1 −3
| 0 1
0 | 1 0 0
| 0 1 0
1 | 1 3 0
| 6 1
2 | 7 6
| 18
− 3 | 25

Hence p(x) = 5 + 6(x + 2) − 3(x + 1)(x + 2) + x(x + 1)(x + 2) ∈ P3. □





# Theorem 3

Let i0, i1, ..., in be a rearrangement of the integers 0, 1, ..., n. Suppose x0, x1, ..., xn are distinct points. Prove that

f[xi0], xi1], ..., xin ] = f[x0, x1, ..., xn].

Proof: One can comparing the coefficients of xn in the different ways of representing the same interpolation polynomial

pn = f[x0] + f<x0, x1 + ... + f<x0, ..., xn · · · (x − xn−1)</x</x

= f[xi0 ] + f<xi0, xi1 + ... + f<xi0, ..., xin · · · (x − xin−1).</x</x

□



# 3.3 Interpolation error

# Theorem 4

Let x₁,...,xₙ be n distinct points on [a, b]. If f ∈ Cⁿ([a, b]) (Cⁿ([a, b]) is the set of functions which are nth order differentiable on [a, b] and whose nth order derivatives are continuous on [a, b]) and pₙ−₁ ∈ Pₙ−₁ is the interpolant of f at x₁, ..., xₙ, which means pₙ−₁(xi) = f(xi) for i = 1, ..., n. (Or, we say pₙ−₁ interpolates f at x₁, ..., xₙ.) Then for any x ∈ [a, b], there is a ξ depends on x₁, ..., xₙ, x and lies between the smallest and largest numbers of x₁, ..., xₙ, x so that

f(x) − pₙ−₁(x) = f(ⁿ)(ξ)(x − x₁)...(x − xₙ). (8)

Here we use f(ⁿ) to denote the nth derivative of f. (Note that this is not fⁿ which is the nth power of f.)




# 1.

Given a function f(x) = 1 and the data points (1, 1), (2, 1), (3, 1), find the degree 2 interpolating polynomial using Newton’s divided difference formula.

# 2.

Use the result of (a) to approximate f3.

# 3.

Use Theorem 4 to give an error bound for the approximation in part (b).

# 4.

Compare the actual error to your error bound.






# Solution:

1. | 1 1
2. | 1 − 2 1
3. | 2 1 6
4. | − 6
5. | 1

So, p₂(x) = 1 − 1(x − 1) + 1(x − 1)(x − 2).

p₂ = 1 − 1 1 + 1 1 − 1 = 1 − 1 − 1 = 17.

f2 = 3 = 16

f′(x) = −1 24′′(x) = (3)(x2) − 6

x = x3. f(x) = x4.

So, by the theorem f3 − p₂(3) = f(3)(ξ) (1.5 − 1)(1.5 − 2)(1.5 − 3) = −1 3 = 3.

Since ξ ∈ [1, 3], 1 ≤ |ξ|4 ≤ 81, 1 ≥ |ξ|14 ≥ 1 and 34 ≤ 3. So, the error bound is 3.

|f(1.5) − p₂(1.5)| = 1 ≤ 3.

Actually, we can determine since we know. From p₂ = 4, we know |ξ|4 = 9 and ξ = √3 ∈ [1, 3].

Example: If f(x) = anxn + an−1xn−1 + ... + a1x + a0. Then f(ⁿ)!(ξ) = an and by the above theorem f(x) = pn(x) + an−1(x − x1)...(x − xn).

This can also be proved by observing that f(x) − pn−1(x) ∈ Pn which vanishes at x1, ..., xn.

Hence f(x) − pn−1(x) = c(x − x1)...(x − xn) and by comparing the leading coefficient, we obtain c = an.






# Proof of Theorem 4:

This is Theorem 3.3 in Sauer’s book whose proof is in Section 3.2.2. (8) is true when x = xi for some i. Given any x which does not equal to xi for any i, fix this x, and then let g(t) = f(t) − pn−1(t) − λω(t). Here ω(t) = (t−x1)(t−x2) · · · (t−xn) = n (t−xi) and λ is a number which is chosen so that g(x) = 0. In particular, f(x) = pn−1(x) + λω(x). So, we are left to prove that λ = f(ⁿ)!(ξ) for some ξ.

Note that g(t) = 0 at t = x1, ..., xn, x which are n + 1 distinct points. By Rolle’s theorem, there are n distinct yi’s so that g′(yi) = 0. Applying Rolle’s theorem to function g′, we know there are n − 1 distinct zi’s so that g′′(zi) = 0. Continue this argument. In the end, there is a ξ so that g(ⁿ)(ξ) = 0.

But g(ⁿ)(ξ) = f(ⁿ)(ξ) − λn! because p(ⁿ) = 0 and ω(ⁿ) = dn (xn + d1xn−1 + d2xn−2 + · · · ) = n!.

So, λ = f(ⁿ)!(ξ).





# 3.3.1 Properties of divided differences

Given a function f, let fi = f(xi) for i = 1, 2, ... and define f[x1, ..., xn] recursively using (6). This mapping which maps a function f to a number f[x1, ..., xn] is denoted by its image f[x1, ..., xn]. The following are some properties of it:

1. Linearity: (αf + βg)[x1, ..., xn] = αf[x1, ..., xn] + βg[x1, ..., xn].
2. Symmetry: f[x1, ..., xn] = f[xi₁, ..., xiₙ] with i₁, ..., iₙ a rearrangement of 1, ..., n.
3. f[x1, ..., xn] = n n f(xi) − .

Let f be a continuous differentiable function on [a, b]. If f(a) = f(b), then there exists a number c between a and b so that f ′(c) = 0.




# 4) Remainder term:

Let pn−1 ∈ Pn−1 interpolates f at x1, ..., xn. Then

f(x) − pn−1(x) = f[x1, ..., xn, x] ∏i=1n(x − xi), ∀x = xi.





If f ∈ Cn([a, b]) and x = xi, then there is a ξ depending on xi and x so that

f[x1, ..., xn, x] = f(n)(ξ) / n!




# 6)

Given n distinct x1, ..., xn and assume f ∈ Cn−1. Then there is a ξ so that

f[x1, ..., xn] = f(n−1)(ξ) / (n − 1)!

Proof: Property 1) is obvious from the definition. Property 2) and 3) follow from the uniqueness of pn−1 (Theorem 1): One can compare the coefficients of xn−1 in the different ways of representing the same interpolation polynomial

pn−1 = f[x1] + fx1, x2 + ... + fx1, ..., xn · · · (x − xn−1)

= f[xi₁] + fxi₁, xi₂ + ... + fxi₁, ..., xiₙ · · · (x − xiₙ−1)

= ∑i=1n f(xi) ∑k=1, k≠in (x − xk) / (xi − xk)

To prove property 4), let pn ∈ Pn which interpolate f at x1, ..., xn, x. Then pn(t) = pn−1(t) + fx1, ..., xn, x...(t − xn). Let t = x and we obtain 4). Then 5) follows from 4) and Theorem 4 since ∏i=1n(x − xi) = 0. 6) is simply another way to write 5). □





# 3.4 Hermite Interpolation polynomial

Given n distinct points x1, ..., xn ∈ [a, b]. Given f1, ..., fn and f′1, ..., f′n. We want to find a polynomial p of degree 2n − 1 (once again, there are 2n equations and 2n unknowns) such that

p(xi) = fi, p′(xi) = f′i, ∀i = 1, ..., n.

Motivated by our understanding of Lagrange interpolation polynomial, we assume

p(x) = ∑i=1n fiφi(x) + ∑i=1n f′iψi(x)

where φi and ψi satisfy

| φi(xj) = 1 | i = j | φ′(xj) = 0 | ∀j |
| ---------- | ----- | ---------- | -- |
| 0          | i = j |            |    |

| ψ′(xj) = 1 | i = j | ψi(xj) = 0 | ∀j |
| ---------- | ----- | ---------- | -- |
| 0          | i = j |            |    |

Note that {xj : j = 1, ..., n, j = i} are double roots of φi and ψi. Moreover, x = xi is a single root of ψi. Let ℓi(x) = ∏j=1,..,n,j=i (x−xj) ∈ Pn−1. Then we can set

φi(x) = (αix + βi)ℓ²(x), so that φi(xi) = 1, φ′(xi) = 0 (11)

ψi(x) = γi(x − xi)ℓ²(x), so that ψ′(xi) = 1. (12)

We can determine (αi, βi, γi) using (11)–(12) so that the φi and ψi defined above would make the p(x) satisfy (9). First, we determine αi and βi from φi(xi) = 1 and φ′(xi) = 0. Then, we determine γi from ψ′(xi) = 1:

φi(x) = (1 − 2ℓ′(xi)(x − xi))ℓ²(x), (13)

ψi(x) = (x − xi)ℓ²(x). (14)




# 3.5 Error estimates for the Hermite interpolation polynomials

Theorem 5 Let f ∈ C²ⁿ([a, b]). Suppose p(x) ∈ P2n−1 is the Hermite interpolation polynomial of f at x1, ..., xn, i.e., p(xi) = f(xi) and p′(xi) = f′(xi) for i = 1, ..., n. Then

f(x) − p(x) = f(2n)(ξ) / (2n)! ∏i=1n (x − xi)² (15)

for some ξ ∈ [a, b] which depends on x, x1, ..., xn.

Proof: Let g(t) = f(t) − p(t) − λ ( ∏i=1n (t − xi))² where λ is chosen so that g(x) = 0. Now, g(t) has 2n + 1 roots x1, x1, ..., xn, xn, x. If x = xi for some i, (15) is automatically true. We only need to consider x = xi ∀i. Assume x ∈ (xk−1, xk). Then by Rolle’s theorem, g′(t) has 2n roots in the 2n disjoint intervals [x1, x1], (x1, x2), [x2, x2], ..., (xk−1, x), (x, xk), [xk, xk],..., (xn−1, xn), [xn, xn]. Keep applying Rolle’s theorem, eventually, we know g(2n) has a root, call it ξ, in [a, b]. Hence g(2n)(ξ) = 0 = f(2n)(ξ) − λ(2n)!. So λ = f(2n)(ξ) / (2n)!.





# 3.6 Newton’s divided difference and Hermite interpolation

We have learned the formula for the Hermite interpolation polynomial. But there is an alternative method for generating them which uses Newton’s divided difference. Suppose the x = x0 is a double root of q(x) if q(x0) = 0 = q′(x0). For example, x = 1 is a double root of (x− 1)2 = 0.

Distinct numbers x1, ..., xn are given together with the values of f and f′ at these numbers. Define a new sequence z1, ..., z2n by

z2i−1 = z2i = xi ∀i

and construct the divided difference table as we have used before using z1, ..., z2n. Since z2i−1 = z2i, f[z2i−1, z2i] = f[z2i−1]−f[z2i] = f(z2i−1)−f(z2i) is of the type 0 and is undetermined.

But thinking about l’Hospital’s law, we recognize that ratio is nothing but xi which is the given data f′. This allows the construction and finishing of the table.




# Example 1

Find the Hermite interpolating polynomial for the following data using Newton’s divided difference formula and then check your answer is correct by directly verifying p(xi) = f(xi) and p′(xi) = f′(xi) for i = 1, 2, 3.

| x     | 0 | 1 | 3  |
| ----- | - | - | -- |
| f′(x) | 0 | 1 | −1 |
| f(x)  | 1 | 0 | 0  |

# Solution:

0              0
1
0                 0 0
1        −¹ 7
1     1        −¹ 1     18 5
0 1 6     1 − 54
1       1 − 2 1      9
−¹          1     2
3     −¹          2
0
3     −¹

Hence p(x) = x − x²(x − 1) + 7 x²(x − 1)² − 5 x²(x − 1)²(x − 3).

Check: p(0) = 0, p(1) = 1, p(3) = 3. p (x) = 1 x(3x²) + 9 x(x − 1)(2x − 1) − 5 (x²(x − 1)² + 2(x² − x)(2x − 1)(x − 3)). p′(0) = 1, p′(1) = 0, p′(3) = 1−21+ 70 − 10 = 54.





# 3.7 Homework 4

1. (Sauer) Page 149, 3.1 Exercises, 1(b)
2. (Sauer) Page 149, 3.1 Exercises, 2(b)

(Sauer) Page 156



# 3.2 Exercises

1. (Sauer) Page 155. Read Section 3.2.3. “Runge phenomenon” to see the limitation of use uniform grid to do global interpolation.
2. (Sauer) Page 158. Read equation (3.9) and Figure 3.7. Try to understand why using uniform grid to do global interpolation is not a good idea. Know the fact about Theorem 3.6 and equation (3.14)
3. (Sauer) Page 165. 3.3 Exercise 3.



# 3.8 Computer Project 2

1. (Sauer) Page 151, 3.1 Computer Problems, Question 3. You may directly use the Matlab code nest or re-implement it using the language you have chosen. nest.m is on page 3 of the textbook and is also used in my solution to Project 1. You have to think of a way to confirm that your code produce the correct value. The solution you submit should contain the complete Matlab (or the language you have chosen) code as well as the data (and how it is generated) to test your code.
2. (Sauer) Page 151, 3.1 Computer Problems, Question 1: Apply the code in Question 3 to solve Question 1. Your solution should contain the values of the different interpolation polynomials at 1980.



# 3.9 Cubic splines

|   | 4.5 | 4 | 3.5 | 3 | 2.5 | 2 | 1.5 | 1 | 0.5 |
| - | --- | - | --- | - | --- | - | --- | - | --- |
|   | 1.5 | 2 | 2.5 | 3 | 3.5 | 4 | 4.5 | 5 |     |

Figure 2: Left: the graph of a linear spline. Right: the graph of a cubic spline.

In our previous discussion, a single formula is used to meet all data points. Splines present an alternative approach to data interpolation: use piecewise low-degree polynomials, to pass through the data points. The simplest example of a spline is a linear spline, in which one “connects the dots” with straight-line segments. However, linear spline lack smoothness. Cubic splines are meant to address this shortcoming of linear splines. A cubic spline replaces linear functions between the data points by cubic polynomials and is globally C²:

Given x₁, ..., xₙ, and y₁,...,yₙ, find a piecewise cubic interpolant p(x) with the property that p, p′ and p′′ are continuous.

More precisely, suppose we are given n data points (x₁, y₁),...,(xₙ, yₙ) where the xi’s are distinct and in increasing order. The cubic spline would defined piecewisely as (there are 3n − 3 unknowns)

S₁(x) = y₁ + b₁(x − x₁) + c₁(x − x₁)² + d₁(x − x₁)³ on [x₁, x₂],

S₂(x) = y₂ + b₂(x − x₂) + c₂(x − x₂)² + d₂(x − x₂)³ on [x₂, x₃],

· · · · · ·

Sₙ−₁(x) = yₙ−₁ + bₙ−₁(x − xₙ−₁) + cₙ−₁(x − xₙ−₁)² + dₙ−₁(x − xₙ−₁)³ on [xₙ−₁, xₙ].

with the following properties (there are (n − 1) + (n − 2) + (n − 2) = 3n − 5 equations since Si(xi) = yi is automatically satisfied)




# 1.

Si(xi) = yi and Si(xi+1) = yi+1 for i = 1, ..., n − 1.

# 2.

S′− (xi) = S′(xi) for i = 2, ..., n − 1.

# 3.

S′′ (xi) = S′′ (xi) for i = 2, ..., n − 1.

# 4.

| 4.5                                | 4   | 2                           | 3                    |   |     |   |     |   |
| ---------------------------------- | --- | --------------------------- | -------------------- | - | --- | - | --- | - |
| S1=y1+b1(x−x1)+c1(x−x1)²+d1(x−x1)³ | 3.5 | S1’=b1+2c1(x−x1)+3d1(x−x1)² | S’’=2c₁ + 6d₁ (x−x₁) |   |     |   |     |   |
| 3                                  | S3  | 2.5                         | S2                   |   |     |   |     |   |
| 2                                  | 1.5 | 1                           | X1 X2 X3 X4          |   |     |   |     |   |
| 0.5                                | 1.5 | 2                           | 2.5                  | 3 | 3.5 | 4 | 4.5 | 5 |

Figure 3: The graph of a cubic spline.

Example: An example of a cubic spline that interpolates the points (1, 2), (2, 1), (4, 4), (5, 3) is shown in Figure 4. The equations defining the spline are





# 4.5

# 4

# 3.5

# 3

# 2.5

# 2

# 1.5

# 1

# 0.5

# 1.5

# 2

# 2.5

# 3

# 3.5



# 4

# 4.5

# 5

Figure 4: The graph of a natural cubic spline.
S₁(x) = 2 − 13(x − 1) + 0(x − 1)² + 5 (x − 1)³ on [1, 2]
S₂(x) = 1 + 1 (x − 2) + 15(x − 2)² − 5 (x − 2)³ on [2, 4]
S₃(x) = 4 + 1 (x − 4) − 15(x − 4)² + 5 (x − 4)³ on [4, 5]

Check that the {S₁, S₂, S₃} defined above satisfies all spline properties for the data points (1, 2), (2, 1), (4, 4), and (5, 3).




# Solution:

- There are 4 data points. We must check S₁(1) = 2, S₁(2) = 1; S₂(2) = 1, S₂(4) = 4; S₃(4) = 4, S₃(5) = 3. These follow easily from the definition of S₁ to S₃.
- S′ (x) = − 13 + 15(x − 1)² on [1, 2]

S′ (x) = 1 + 15(x − 2) − 15(x − 2)² on [2, 4]

S′ (x) = 1 − 15(x − 4) + 15(x − 4)² on [4, 5]

From the above expression, we can check S′ (2) = 1 = S′ (2) and S′ (4) = 1 = S′ (4).
- S′′ (x) = 15(x − 1) on [1, 2]

S′′ (x) = 15 − 15(x − 2) on [2, 4]

S′′ (x) = − 15 + 15(x − 4) on [4, 5]

From the above expression, we can check S′′ (2) = 15 = S′′ (2) and S′′ (4) = − 15 = S′′ (4). □





# 3.9.1 Constructing a cubic spline

The derivation presented here is taken from the textbook. The derivation is rather complicated. In the exam, the precise formulas in this section will not be tested. But the ideas behind them, for example, properties 1)-3) of cubic splines which we have mentioned before can be tested.

From (16), we see that we need to determine 3n − 3 unknowns {(bi, ci, di), i = 1, ..., n − 1}, but we only have 3n−5 equations. We need 2 additional equations to close the system. For the moment, let us consider the case that we take S′′ (x₁) = 0 = S′′ (xₙ) (which is called natural spline).

Let δi = xi+1 − xi and ∆i = yi+1 − yi. The 3n − 5 equations are:

1. Property 1). [Si(xi+1) = yi+1 for i = 1, ..., n − 1.]

y₂ = S₁(x₂) = y₁ + b₁δ₁ + c₁δ² + d₁δ³,

yₙ = Sₙ−₁(xₙ) = yₙ−₁ + bₙ−₁δₙ−₁ + cₙ−₁δₙ−₁ + dₙ−₁δₙ−₁.
2. Property 2). [S′− (xi) = S′(xi) for i = 2, ..., n − 1.]

Note that S′(xi) = bi.

0 = S′ (x₂) − S′ (x₂) = b₁ + 2c₁δ₁ + 3d₁δ² − b₂,

0 = Sₙ−₂(xₙ−₁) − Sₙ−₁(xₙ−₁) = bₙ−₂ + 2cₙ−₂δₙ−₂ + 3dₙ−₂δₙ−₂ − bₙ−₁.
3. Property 3). [S′′ (xi) = S′′ (xi) for i = 2, ..., n − 1.]

Note that S′′ (xi) = 2ci.

0 = S′′ (x₂) − S′′ (x₂) = 2c₁ + 6d₁δ₁ − 2c₂,

0 = Sₙ−₂(xₙ−₁) − Sₙ−₁(xₙ−₁) = 2cₙ−₂ + 6dₙ−₂δₙ−₂ − 2cₙ−₁.

Instead of solving the equations in this form, the system can be simplified drastically by decoupling the equations. With a little algebra, a much smaller system of equations in ci can be solved first, followed by explicit formulas for the bi and di in terms of the unknown ci.

From (19), we know:

di = cⁱ⁺¹−cⁱ / (3δi)

8Si(x) = yi + bi(x − xi) + ci(x − xi)² + di(x − xi)³ on [xi, xi + 1].




9S′(x) = bi + 2ci(x − xi) + 3di(x − xi)² on [xi, xi + 1].

10S′′ (x) = 2ci + 6di(x − xi) on [xi, xi + 1].

for i = 1, ..., n − 2. Now, define cₙ = S′′− (xₙ)/2. Then 0 = S′′− (xₙ) − S′′− (xₙ) =

|   |   |   |   |   |
| - | - | - | - | - |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |
|   |   |   |   |   |

2cₙ−₁ + 6dₙ−₁δₙ−₁ − 2cₙ would imply (20) is true for i = n − 1.

From (17), we know

bi = ∆ⁱ − ciδi − diδ² = ∆ⁱ − ciδi − δⁱ (ci+1 − ci) = ∆i − δi (2ci + ci+1) (21) for i = 1, ..., n − 1.

Substituting (20) and (21) into (18) results in the following n 2 equations for c₁, ..., cₙ

δ₁c₁ + 2(δ₁ + δ₂)c₂ + δ₂c₃ = 3 ∆₂ − ∆₁ δ₂ c + 2(δ n−2 + δ n−1)c + δ · · · · · · ∆ₙ−₁ − ∆ₙ−₂ (22)

n−2 n−2 n−2 n−1 n−1 n−1cn = 3 δₙ−₁ δₙ−₂.

Two more equations are given by the natural spline condition S′′ (x ) = 0 = S′′ (x ) ⇒ 1 1 n−1 n = c₁ = 0 = cₙ.

Finally, we end up with a tridiagonal system of the form

Ac = f (23)

where c = (c₁, ..., cₙ)⊤, A is a tridiagonal matrix of the form

| 1                                             | 0          | 0           | 0   | 0           | · · · · · ·    | 0    |
| --------------------------------------------- | ---------- | ----------- | --- | ----------- | -------------- | ---- |
| δ₁                                            | 2(δ₁ + δ₂) | δ₂          | 0   | 0           | · · · · · ·    | 0    |
| · ⁰                                           | δ₂         | 2(δ₂ + δ₃)  | δ₃  | 0           | · · · · · ·    | 0    |
| · · · · · · · · · · · · · · · · · · · · · · · | 0          | · · · · · · | · ⁰ | δₙ−₂        | 2(δₙ−₂ + δₙ−₁) | δₙ−₁ |
| 0                                             | 0          | 0           | 0   | · · · · · · | 0              | 1    |

and f = 0, 3 ∆₂ − ∆₁, ..., 3 ∆ₙ−₁ − ∆ₙ−₂, 0 ⊤.

δ₂ δ₁ δₙ−₁ δₙ−₂

Note that A is a tridiagonal matrix. So, we can apply the result from a previous midterm problem and conclude that we can solve Ac = f with O(5n) multiplication/divisions.

Example: Find the natural cubic spline through (0, 3), (1, −2), and (2, 1).

Solution: δ₁ = 1 and δ₂ = 1. ∆₁ = −5 and ∆₂ = 3. So






1 0 0 c₁ 0

1 4 1 c₂ 24

0 0 1 c₃ 0

Hence (c₁, c₂, c₃) = (0, 6, 0). Then (20) and (21) yield

| d₁  | = c² − c¹            | = 6          | = 2   |
| --- | -------------------- | ------------ | ----- |
| 3δ₁ |                      |              | 3     |
| d₂  | = c³ − c²            | = −6         | = −2  |
| 3δ₂ |                      |              | 3     |
| b₁  | = ∆¹ − δ¹ (2c₁ + c₂) | = −5 − 1 (6) | = −7  |
| δ₁  |                      |              | 3     |
| b₂  | = ∆² − δ² (2c₂ + c₃) | = 3 − 1 (12) | = −1. |
| δ₂  |                      |              | 3     |

Therefore, the natural cubic spline is

S₁(x) = 3 − 7x + 0x² + 2x³ on [0, 1],

S₂(x) = −2 − 1(x − 1) + 6(x − 1)² − 2(x − 1)³ on [1, 2].

Remark on “end point conditions”: Recall we are short of two conditions to determine (bi, ci, di) if we merely using Properties 1)-3) of cubic spline. Instead of setting S′′ (x₁) = 0 = S′′ (xn−1), we can specify, for example, the value of S′′ (x1) and S′′ (xn) to some values chosen by the user, say, v₁ and vₙ. These two additional conditions are called end point conditions.

There are many different choices for the end point conditions and they will give different (bi, ci, di). I hope you are aware of those facts, but they are not required for the exam. If you are interested to learn more, more details can be found in the textbook.





# 3.10 Homework 5

1. (Sauer) Page 176, 3.4 Exercises, 4 (find k₁, k₂, k₃ only)
2. (Sauer) Page 176, 3.4 Exercises, 7(b)
3. (Sauer) Page 177, 3.4 Exercises, 13(a,b)
4. (Sauer) Read section 3.5 and also the reality check “Fonts from B´ezier curves” on page 183.



# 4 Numerical differentiation and integration

# 4.1 Numerical differentiation

By definition, the derivative of f(x) at a value x is

f′(x) = limh→0 (f(x + h) − f(x)) / h. (1)

This leads to a useful formula for approximating the derivative at x. Taylor’s theorem11 says that if f is twice continuously differentiable, then

f(x + h) = f(x) + hf′(x) + (h² f′′(ξ)) / 2

where ξ is some number between x and x + h. By moving f and f′′ terms to the left and then dividing everything by h, the above equation implies the following formula (two-point forward difference formula)

f′(x) = (f(x + h) − f(x) − h f′′(ξ)) / 2 (2)

where ξ is between x and x + h.

In a finite calculation, we cannot take the limit in (1), but the above equation implies that the quotient will closely approximate the derivative if h is small. So

f′(x) ≈ (f(x + h) − f(x)) / h (3)

and − (h f′′(ξ)) / 2 can be treated as error. Because the error made by the above approximation is proportional to the increment of h, we can make the error small by making h small.

The two-point forward difference formula is a first-order method for approximating the first derivative. In general, if the error is O(hk), we say the formula is an order k approximation.

A subtle point about calling the formula “first order” is that the ξ in the error − (h f′′(ξ)) / 2 depends on h. The idea of first order is that the error should be proportionally to h as h → 0. As h → 0, ξ is a moving target, and as the result, the proportionality constant changes. But as long as f′′ is continuous, the proportionality constant f′′(ξ) tends towards f′′(x) as h → 0, making it legitimate to call the formula first order.

Example: Use the two-point forward difference formula with h = 0.1 to approximate the derivative of f(x) = 1/x at x = 2.

11 Taylor theorem: If f(n+1) is continuous, there is a ξ between a and x so that




# Taylor's Theorem

f(x) = f(a) + f ′(a)(x − a) + (1/2!) f′′(a)(x − a)² + · · · + (1/n!) f(n)(a)(x − a)ⁿ + (1/(n + 1)!) f(n+1)(ξ)(x − a)ⁿ⁺¹.

Solution: ′ f(x + h) − f(x) 21 − 1

f (x) ≈ h = .1 2 ≈ −0.²³⁸¹.

0.1

The difference between the correct derivative f′(x) = −x−² at x = 2 and the above approximation is the error

−0.²⁵⁰⁰ − (−0.2381) = −0.⁰¹¹⁹. h ′′

Compare this to the error predicted by the formula, which is − 2 f (ξ) for some ξ ∈ (2, 2.1).

Since f′′(x) = 2x−³ (which is monotone), the error must be between

−(0.1)²−³ ≈ −0.0125 and − (0.1)².¹−³ ≈ −0.⁰¹⁰⁸.

This is consistent with our result. □

A second order formula can be developed by a more advanced strategy. According to Taylor’s theorem, if f is three times continuously differentiable, then

f(x + h) = f(x) + hf′(x) + h² f′′(x) + h³ f′′′(ξ₁)

2 6

and f(x − h) = f(x) − hf′(x) + h² f′′(x) − h³ f′′′(ξ₂)

2 6

where ξ₁ ∈ (x, x + h) and ξ₂ ∈ (x − h, x), assuming h ≥ 0. Taking the difference of the above two equations and dividing by 2h, we obtain

f′(x) = f(x + h) − f(x − h) − h² (f′′′(ξ₁) + f′′′(ξ₂))

2h 12

Claim that there is a ξ ∈ (x − h, x + h) so that (three-point centered difference formula)

f′(x) = f(x + h) − f(x − h) − h² f′′′(ξ). (4)





# Theorem 1

Let f be a continuous function on the interval [a, b]. Let x₁, ..., xₙ be points in [a, b], and a₁, ..., aₙ > 0. Then there exists a number c between a and b such that

(a₁ + · · · + aₙ)f(c) = a₁f(x₁) + · · · + aₙf(xₙ).

# Proof:

Let f(xi) = minₖ f(xₖ ) and f(xj) = maxₖ f(xₖ ). Then

a₁f(xi) + · · · + aₙf(xi) ≤ a₁f(x₁) + · · · + aₙf(xₙ) ≤ a₁f(xj) + · · · + aₙf(xj).

Hence f(xi) ≤ a¹f(x¹) + · · · + aⁿf(xⁿ) ≤ f(xj).

By intermediate value theorem, there is a number c between xi and xj such that

a₁ + · · · + aₙ = f(c). □




# Example:

Use the three-point centered-difference formula with h = 0.1 to approximate the derivative of f(x) = 1/x at x = 2.






# Solution:

f'(x) ≈ f(x + h) − f(x − h) 21 − 1

f'(x) ≈ 2h = .1 0.21.9 ≈ −0.²⁵⁰⁶.

The error is 0.0006, an improvement on the two-point forward-difference formula in the previous example. □






# Approximation formulas for higher derivatives

can be obtained in the same way. For example, by Taylor expansion, there are some ξ₁ ∈ (x, x + h) and ξ₂ ∈ (x − h, x) so that

f(x + h) = f(x) + f′(x)h + 1f′′(x)h² + 1f(3)(x)h³ + 1f(4)(ξ₁)h⁴

−²ᶠ(ˣ) = −²ᶠ(ˣ) ′ 1 ′′ 2 1 (3) 3 1 (4) 4

f(x − h) = f(x) − f'(x)h + 2f''(x)h² − 6f(3)(x)h³ + 24f(4)(ξ₂)h⁴.

Adding the above three equations together, and then dividing by h², we obtain three-point centered-difference formula for second derivative

f′′(x) = f(x + h) − 2f(x) + f(x − h) + 1f(4)(ξ)h², (5)

where ξ is some number in [x − h, x + h] so that f(4)(ξ) = 1f(4)(ξ₁) + f(4)(ξ₂) (see - rem 1).







# 4.2 Rounding error

Example: Approximate the derivative of f(x) = eˣ at x = 0.

Solution: The two-point formula gives

f′(x) ≈ eˣ⁺ʰ − eˣ, (5.9)

while the three-point formula yields

f′(x) ≈ eˣ⁺ʰ − eˣ−ʰ. (5.10)

The results of these formulas at x = 0, together with the errors f′(x) − eˣ⁺ʰ−ᵉˣ and f′(x) − eˣ+h−eˣ−h are documented in the following table.

| h         | formula (5.9)    | error             | formula (5.10)   | error             |
| --------- | ---------------- | ----------------- | ---------------- | ----------------- |
| $10^{-1}$ | 1.05170918075648 | −0.05170918075648 | 1.00166750019844 | −0.00166750019844 |
| $10^{-2}$ | 1.00501670841679 | -0.00501670841679 | 1.00001666674999 | −0.00001666674999 |
| $10^{-3}$ | 1.00050016670838 | −0.00050016670838 | 1.00000016666668 | −0.00000016666668 |
| $10^{-4}$ | 1.00005000166714 | -0.00005000166714 | 1.00000000166689 | −0.00000000166689 |
| $10^{-5}$ | 1.00000500000696 | -0.00000500000696 | 1.00000000001210 | −0.00000000001210 |
| $10^{-6}$ | 1.00000049996218 | −0.00000049996218 | 0.99999999997324 | 0.00000000002676  |
| $10^{-7}$ | 1.00000004943368 | −0.00000004943368 | 0.99999999947364 | 0.00000000052636  |
| $10^{-8}$ | 0.99999999392253 | 0.00000000607747  | 0.99999999392253 | 0.00000000607747  |
| $10^{-9}$ | 1.00000008274037 | −0.00000008274037 | 1.00000002722922 | −0.00000002722922 |

At first, the error decreases as h decreases, following closely the expected errors O(h) and O(h²), respectively, for the two-point forward-difference formula (5.9) and the three-point centered-difference formula (5.10). However, notice the deterioration of the approximations as h is decreased still further.

The reason that the approximations lose accuracy for very small h is loss of significance. Both formulas subtract nearly equal numbers, lose significant digits, and then, to make matters worse, magnify the effect by dividing by a small number.

Denote the floating point version of f(x + h) by ˆf(x + h) which will differ from the correct value f(x + h) by a number on the order of machine epsilon in relative terms. Since ˆf(x + h) = f(x + h) + ϵ₁ and ˆf(x − h) = f(x − h) + ϵ₂, where ϵ₁, ϵ₂ ≈ ϵmach,

f′(x)correct − f′(x)machine = f′(x) − ˆf(x + h) − ˆf(x − h) = f′(x) − f(x + h) − f(x − h) − ϵ¹ − ϵ²

Hence





f′(x)correct − f′(x)machine ≤ h² M f′′′(c) + 2ϵmach ≤ M h² + ϵmach



# 4.3 Richardson extrapolation

Assume that we are presented with an order n formula Fₙ(h) for approximating a given quantity Q. Fₙ is an order n approximation means that

Q = Fₙ(h) + K(h)hⁿ

where K = K(h) is roughly constant over the range of h in which we are interested in. By the way, the absolute error when you use Fₙ(h) to approximate Q is |Q − Fₙ(h)| which equals |K(h)hⁿ|.

A relevant example is

f′(x) = (f(x + h) − f(x − h)) / (2h) − (f′′′(ξ(h)) h²) / 6.

Here we use ξ(h) instead of ξ to emphasize that ξ depends on h. So Q = f′(x), Fₙ(h) = f(x+h) − f(x−h) and K(h)hⁿ = − f′′′(ξ(h))h². We know ξ(h) lies between x and x + h, and

69

where M = maxc∈[x−h,x+h] |f′′′(c)|. To minimize the right hand side g(h), we set g′(h) = 0 and obtain the optimal

h = 3√(ϵmach/M).

In double precision, this is approximately √ϵ ≈ 10−5, consistent with the last column of the previous table.

depends on h. Even though ξ(h) is not a constant, if the function f′′′ is continuous and h is not large, then values of K(h) = − f′′′(ξ(ʰ)) should not vary far from − f′′′(ˣ).

In a case like this, a little bit of algebra can be used to leverage an order n formula into one of higher order. For that, after computing Fₙ(h), we also compute Fₙ(h/2). Then

Q − Fₙ(h/2) = K(h/2)(h/2)ⁿ ≈ 1 K(h)hₙ = 1 (Q − Fₙ(h)).

We have applied the assumption K(h/2) ≈ K(h). Note that this is readily solved for the quantity Q in question to give the following formula (Extrapolation of order n formula)

Q ≈ 2ⁿFⁿ(h/2)−Fⁿ(ʰ) := Fₙ₊₁(h).

This is the Richardson extrapolation formula for Fₙ(h).

The above derivation of Fₙ₊₁(h) is not completely satisfactory since it contains an ≈ in the derivation. We now want to prove that the formula of Fₙ₊₁(h) is indeed a higher-order




# Approximation of Q than Fₙ

For that, we need to assume K(h) = K₀ + O(h).

Then we can write

Q = Fₙ(h) + K₀hⁿ + O(hⁿ⁺¹).

By the way, many people might be confused now. Does the above formula say the error of Fₙ(h) is O(hⁿ⁺¹). No! Because the error, or the absolute value of the error is |Q − Fₙ| which is K₀hⁿ + O(hⁿ⁺¹), which is O(hⁿ) because the K₀hⁿ term dominates.

# Example

Rewrite into a form of type (11), by using the Taylor expansion f(x + h) = f(x) + hf′(x) + h² f′′(x) + h³ f′′′(x) + h⁴ f(4)(x) + h⁵ f(5)(ξ).

# Remark

In fact, we will find for this example that the O(h) term in can be further improved to O(hⁿ⁺²). But in more general examples, this will not happen.

# Solution

f(x + h) = f(x) + hf′(x) + h² f′′(x) + h³ f′′′(x) + h⁴ f(4)(x) + h⁵ f(5)(ξ₁).

f(x − h) = f(x) − hf′(x) + h f′′(x) − h f′′′(x) + h⁴ f(4)(x) − h⁵ f(5)(ξ₂).

Subtracting the above three equations, and then dividing by 2h, we obtain

f(x + h) − f(x − h) = f′(x) + f′′′(x)h² + f(5)(ξ₁) + f(5)(ξ₂)h⁴.

From (7), we see that K(h) = − f′′′(ξ(ʰ)). Now, we see that in this example, K₀ = − f′′′(ˣ) which is independent of h. Then the total error contains both K₀h and a higher order term.

12 If you think about K(h) = K(0) + K′(c)h = K₀ + O(h), it is a formal Taylor expansion of K(h) around h = 0.

O(h³). In this example, because of the cancelation happened to f(4)(x) terms, the higher order term is indeed O(h⁴). □





# Claim:

With the assumption (10), the right hand side of (9) gives a higher-order approximation of Q than Fₙ(h).




Proof:

If we change h to h/2 in (11), we obtain

Q = Fₙ(h/2) + 1 K₀hₙ + O(hₙ₊₁). (12)

Hence

Fₙ₊₁(h) = 2ⁿFⁿ(h/2) − Fⁿ(h)

= 2 (Q − K₀h /2 − O(ʰ)) − (Q − K₀h − O(ʰ))

= Q + −K₀h + K₀h + O(hⁿ⁺¹) = Q + O(hₙ₊₁).

Therefore, F (h) is (at least) 2ⁿ − 1 formula for Q an order n + 1 approximating the quantity.

□






# Example:

Apply extrapolation to three-point centered-difference formula for f′(x) (see (4)).

# Solution:

n = 2

Fₙ₊₁(h) = 2ⁿFⁿ(h/2) − Fⁿ(h)

= (2ⁿ − 1) 4 f(x+h/2)−f(x−h/2) − f(x+h)−f(x−h)

= h 3 2h

= f(x − h) − 8f(x − h/2) + 8f(x + h/2) − f(x + h).

This is a five-point centered-difference formula. The previous argument guarantees that this formula is of order at least three. But it turns out to have order 4, because the order three error terms cancel out. In fact, since Fₙ₊₁(h) = Fₙ₊₁(−h) by inspection, the error f′(x) − Fₙ₊₁(h) must be the same for h and −h. Therefore the error can be even powers of h only. □






# Example:

Apply extrapolation to three-point centered-difference formula for f′′(x) (see (5)).

# Solution:

n = 2

Fₙ₊₁(h) = 2ⁿFⁿ(h/2) − Fⁿ(h)

= (2ⁿ − 1) 4 f(x+h/2)−2f(x)+f(x−h/2) − f(x+h)−2f(x)+f(x−h)

= h²/4 3 h²

= −f(x − h) + 16f(x − h/2) − 30f(x) + 16f(x + h/2) − f(x + h).

This is a five-point centered-difference formula for f′′(x). The previous argument guarantees that this formula is of order at least three. But it turns out to have order 4, because the order three error terms cancel out, for the same reason as the previous example.





Homework 6

# 4.4 Homework 6

1. (Sauer) Page 252, 5.1 Exercises, 1(b,c), 2(b,c), 5(b,c), 7, 8, 10, 15, 19
2. (Sauer) Page 252, 5.1 Exercises, 25







# 4.5 Numerical integration (numerical quadrature)

Now, we want to study how to compute definite integral   *ab f(x)dx*. The most popular method is a kind of weighted average of the function values, with some formula like the following:

*I(f) =*





# 1.5

# 1

0.5

00 0.5 1 00 0.5 1

1.5

1

0.5

00 0.5 1 00 0.5 1

# Figure 6: Left point rectangular rule; midpoint rule; trapezoidal rule; Simpson’s rule.

• Simpson’s rule, m = 3

b f(x)dx ≈ f(a) + 4f(a + b) + f(b) b − a.

a 2 6

# Example: Apply the trapezoidal rule and Simpson’s rule to approximate ∫12 ln xdx.

Solution: The exact integral can be computed using integration by parts

∫12 ln xdx = x ln x|x=2 - ∫12 dx = 2 ln 2 - 1 ln 1 - 1 ≈ 0.386294.

The trapezoidal rule estimates that

∫12 ln xdx ≈ 1/2 (ln 1 + ln 2) = ln 2 ≈ 0.346574.

The Simpson’s rule estimates that

∫12 ln xdx ≈ 1/6 (ln 1 + 4 ln 3 + ln 2) ≈ 0.385835.

# Example: Determine the associated degree of precision for (a) left point rectangular rule, and (b) midpoint rule.



Solution:

Let I(f) = ∫ab f(x)dx and In(f) = ∑k=1n Ak fk. Note that both I and In are linear operators on f, namely, I(αf + βg) = αI(f) + βI(g) and In(αf + βg) = αIn(f) + βIn(g). If I(1) = In(1), I(x) = In(x), ...., I(xℓ) = In(xℓ), then

I(a0 + a1x + · · · + aℓxℓ) = a0I(1) + a1I(x) + · · · + aℓI(xℓ) = a0In(1) + a1In(x) + · · · + aℓIn(xℓ) = In(a0 + a1x + · · · + aℓxℓ).

So, quadrature In(f) has degree of precision m if and only if I(xℓ) = In(xℓ) for ℓ = 1, ..., m, and I(xm+1) = In(xm+1).




Let I1(f) = f(a)(b − a). If f = 1, I(1) = b − a, I1(1) = b − a = I(1). If f = x, I(x) = ∫ab x dx = &#x26;frac{b2 − a2}{2}, I1(x) = a(b − a) = I(x). So m = 0.






Let I1(f) = f &#x26;frac{a+b}{2} (b − a). If f = 1, I(1) = b − a, I1(1) = &#x26;frac{b + a}{2} (b − a) = I(1). If f = x, I(x) = ∫ab xdx = &#x26;frac{b2 − a2}{2}, I1(x) = &#x26;frac{b + a}{2} (b − a) = I(x). If f = x2, I(x2) = ∫ab x2dx = &#x26;frac{2b3 − a3}{3}, I1(x2) = &#x26;frac{b + a}{2} (b − a) = I(x2). So m = 1. □






# Example

Determine constant a, b, c that will produce a quadrature formula

∫-11 xf(x)dx ≈ af(−c) + bf(c) that has the highest degree of precision. Determine the degree of precision.

Solution: We take f = 1, x, x2, x3.

- 0 = a + b
- 2 = −ac + bc
- 0 = ac2 + bc2
- 2 = −ac3 + bc3

So, (a, b, c) = (− &#x26;frac{5}{27}, − &#x26;frac{5}{27}, &#x26;frac{3}{5}) or (&#x26;frac{5}{27}, − &#x26;frac{5}{27}, − &#x26;frac{3}{5}). But they correspond to the same quadrature &#x26;frac{5}{27}f(− &#x26;frac{3}{5}) + &#x26;frac{5}{27}f(&#x26;frac{3}{5}). Take f = x4 and we find that 0 = ac4 + bc4. Take f = x5, we find that 7 = −ac5 + bc5. Hence the degree of precision is 4. □





# 4.6 Interpolatory formula and Newton-Cotes formula

Recall that given x1, ..., xn, for any given function f(x), we can construct its interpolation polynomial of degree at most n − 1

n Ln(f)(x) := pn−1(x) = f(xk)ℓk(x) (14)

to approximate f. Here ℓk(x) = ∏j=1,...,n,j=k (x−xj). A formula

b n a f(x)dx ≈ ∑k=1 Ak f(xk)

with Ak = b ℓk(x)dx is called an interpolatory formula. In other words, interpolatory formula defined (14). If

In = I Ln (f) (f) defined (14) by moreover the -polation points are equispaced, then it is called Newton-Cotes formula.




# Example (derivation of Trapezoid rule)

Recall Theorem 4.

f(x) = f(a)x − b + f(b)x − a + (x − a)(x − b)f′′(ξ(x)). Here we use ξ(x) to emphasize that ξ depends on x.

b f(x)dx = b f(a)x − b + f(b)x − a + (x − a)(x − b)f′′(ξ(x))dx

a a a − b b − a 2! = b − a (f(a) + f(b)) + E.

2 b ( − )( − ) f′′( ¯) b ¯

Here the error term E = a x a2!x b f′′(ξ(x))dx = 2 ξ a (x − a)(x − b)dx for some ξ in [a, b] and we have used mean value theorem for integrals 13 in the last step. Then simple calculation shows E = − 12ξ (b − a)³.

So

b f(x)dx = b 2 a (f(a) + f(b)) − ξ (b − a)³.

(15)






# Example (derivation of Simpson’s rule)

Tale (x₁, x₂, x₃) = (a, c, b) with c = a⁺ᵇ.

f(x) = f(a)(x − c)(x − b) + f(c)(x − a)(x − b) + f(b)(x − a)(x − c) + (x − a)(x − c)(x − b)f′′′(ξ(x))

| (a − c)(a − b) | (c − a)(c − b) | (b − a)(b − c) |
| -------------- | -------------- | -------------- |

3! 13[mean value theorem for integrals] Let f be a continuous function on the interval [a, b], and let g be an integrable function that does not change sign on [a, b]. Then there exists a number c between a and b such that

b f(x)g(x)dx = f(c) g(x)dx.

a a

and simple calculation shows

14 b f(x)dx = b − a (f(a) + 4f (c) + f(b)) + E

a 6

with E = b (x−a)(x−c)(x−b) f′′′(ξ(x))dx. But this time, since (x − a)(x − c)(x − b) changes sign on [a, b], we cannot directly apply mean value theorem for integrals. But with some additional work, later in this chapter, we will show that E = 90 ξ² for some ¯ ∈ [a, b].

(How to calculate E for Simpson’s rule in fact is not required for the exam. But you need to remember the result.)

b f( ) b − a (f( ) f (( )/2) f( )) − 1 f(4)(¯) b − a 5 (16)

a x dx = 6 a + 4 a + b + b 90 ξ².

# Example:

We have apply the trapezoidal rule and Simpson’s rule to approximate 2 ln xdx in a previous Example. Now, find an upper bound for the error in your approximations.

# Solution:

The absolute error for trapezoidal rule is 12 ξ with = x² and ξ ¯ ∈ [1, 2]. So ≈ 1 ≤ (2−1) |ᶠ′′(¯)| ≤ 1 ≈ , 0.0208 | 12×22 −¹² ξ | ≈ 12×12 0.0833. The actual absolute error in this example is about 0.386294 0.346574 0.0397.

for Simpson’s rule is 90 ξ with = x⁴ and ξ ¯ ∈ [1, 2]. So ≈ 6 ≤ 1 |ᶠ(4)(¯)| ≤ 6 ≈ 0.00013 25×90×24| 25×90 − ξ 25×90×14 0.0021. The actual absolute error in this example is about 0.386294 0.385835| ≈ 0.00046.






For example, b (x−c)(x−b) dx = 1 [(b−a)y+a−c][(b−a)y+a−b] (b − a)dy with y = x−a.

Continue, we get a (a−c)(a−b) 0 1 (b−a)(b−a) b−a 2 (b − a) 1 (y− 1 )(y−1) dy = (b − a) 1(2y2 − 3y + 1)dy = (b − a) 2 − 3 + 1 = 1 (b − a). By symmetry, b (x−a)(x−c) = 1 (b −a). Then b (x−a)(x−b) = 2 (b −a) because b −a = b 1dx = b (x−c)(x−b) + (x−a)(x−b) + a (b−a)(b−c) 6 a (c−a)(c−b) 3 a (a−c)(a−b) (c−a)(c−b) (x−a)(x−c) dx.

Do you know why 1 = (x−c)(x−b) + (x−a)(x−b) + (x−a)(x−c)?

(b−a)(b−c) (a−c)(a−b) (c−a)(c−b) (b−a)(b−c)





# 4.7 Composite rule

When we are asked to compute



\( b f(x)dx \approx h f(a) + f(b) + 2 \sum_{j=1}^{m-1} f(x_j) \).



# Composite Simpson’s Rule

Let m be an integer, h = b−a, xj = a + jh, j = 0, ..., 2m. We break interval [a, b] into m subintervals [x2j−2, x2j] of size 2h, j = 1, ..., m and apply Simpson’s rule on each subinterval:

x2j f(x)dx ≈ 2h (f(x2j−2) + 4f(x2j−1) + f(x2j)), j = 1, ..., m. If we take m on both sides of the above equation, we obtain:

b f(x)dx ≈ h f(a) + f(b) + 4 ∑j=1m f(x2j−1) + 2 ∑j=1m−1 f(x2j).

(19)




# Example:

Carry about a 4-subinterval approximation of 12 ln xdx using the composite trapezoidal rule and composite Simpson’s rule.





# Solution:

# Composite Trapezoidal:

h = 1/4. {xj} = {1, 5/4, 6/4, 7/4, 2}.

2 ln xdx ≈ 1/4 (ln 1 + ln 2 + 2 (ln(5/4) + ln(6/4) + ln(7/4))) ≈ 0.3837.




# Composite Simpson:

h = 1/8. {xj} = {1, 9/8, 5/4, 11/8, 6/4, 13/8, 7/4, 15/8, 2}.

2 ln xdx ≈ 1/8 (ln 1 + ln 2 + 4 {ln(9/8) + ln(11/8) + ln(13/8) + ln(15/8)} + 2 (ln(5/4) + ln(6/4) + ln(7/4)) ≈ 0.386292.

Recall that we know the exact value of 12 ln xdx is 2 ln 2 − 1 ≈ 0.386294. □





# 4.8 Error estimates of composite rule

Recall the composite trapezoid rule: (h = b−a , xj = a + jh, j = 0, ..., m.)

m b f(x)dx ≈ h f(a) + f(b) + 2 m−¹ f(xj)

a 2 j=1

and recall the composite Simpson’s rule: (h = b−a , xj = a + jh, j = 0, ..., 2m.)

2m b f(x)dx ≈ h f(a) + f(b) + 4 m f(x2j−₁) + 2 m−¹ f(x2j)

a 3 j=1 j=1

By (15) on each subinterval [xj−₁, xj],

xj f(x)dx − h (f(xj−₁) + f(xj)) = − h3 f′′(ξj).

xj−1 2 12

So, summing it up and use the mean value theorem (Theorem 1) with ai = h,

ETrapezoidal(f) = b f(x)dx − h f(a) + f(b) + 2 m−¹ f(xj)

a 2 j=1

= − h2 m (h)f′′(ξj) = − h2 (b − a)f′′(ξ)

(22) for some ξ ∈ (b, a). So, it is a method of order 2.

By (16), on [x2j−₂, x2j],

x2j f(x)dx− h (f(x2j−₂) + 4f(x2j−₁) + f(x2j)) = − 1 h5f(4)(ξj).

(Here x2j−x2j−2.)

x2j−2 3 (with 90)

h = 2 Adding up and using mean value theorem again ai = 2h we see that composite Simpson is a method of order 4 with

ESimpson(f) = b f(x)dx − h f(a) + f(b) + 4 m f(x2j−₁) + 2 m−¹ f(x2j)




# Example: Find the number of subintervals m necessary for the composite Simpson’s rule to approximate 3π sin² xdx within 6 correct decimal places.

Solution: 0.5 × 10−⁶. We know the error is − h4 3 πf(4)(ξ) and we want its absolute value is less than h4 3 π8 &#x3C; 0.5 × 10−⁶.

Hence h &#x3C; 0.0494 and m = ceil(³ π/(2h)) = 20. We need 20 subintervals. If you implement a Matlab code to compute, you can check that when n = 12, the error is already.





4.9847e-007

When n = 20, the error is 6.4481e-008. The numerics is consistent with the theory.

# Example:

The error term for composite trapezoidal rule Tₙ for approximating I = ab f(x)dx can be written as

I − Tₙ = − h² (f′(b) − f′(a)) + O(h⁴)

where h = b−a and n is the number of subintervals. The composite midpoint rule Mₙ is obtained by applying the midpoint rule to each of the n subintervals and we have

I − Mₙ = h² (f′(b) − f′(a)) + O(h⁴)

Using these results, obtain a new numerical integration formula Sₙ combining Tₙ and Mₙ, with error O(h⁴).



Solution:

So I = 1 Tₙ + 2 Mₙ + O(h⁴). I − Tₙ + 2(I − Mₙ) = O(h⁴).

On each subinterval, say, xi, xi+1

1 Tₙ + 2 Mₙ = (xi+1 − xi) (1 f(xi) + f(xi+1) + 2 f((xi + xi+1)/2))

= (xi+1 − xi) (f(xi) + 4f((xi + xi+1)/2) + f(xi+1))

which is Simpson’s rule. □



# 4.9 Romberg integration

Romberg integration is the result of applying Richardson extrapolation to the composite trapezoidal rule. It can be shown that for an infinitely differentiable function f

**b f(x) = h f(a) + f(b) + 2 m−¹ f(xj) + c₂h² + c₄h⁴ + c₆h⁶ + · · · ,**

**a 2 j=1**

where the ci depend only on higher derivatives of f at a and b, and not on h. This result is the so called Euler-Maclaurin formula. For example, c₂ = f (ᵃ)−ᶠ′(ᵇ). The absence of odd powers in the error gives an extra bonus when extrapolation is done: If we have

**Q = Fₙ(h) + K₀hⁿ + O(hⁿ⁺²).**

Then

**Q = Fₙ(h/2) + 1 K₀hₙ + O(hₙ₊₂).**

Hence

**Fₙ₊₁(h) = 2ⁿFⁿ(h/2) − Fⁿ(h)**

**n 2ⁿ − 1ₙ n n n+2 n n+2**

**= 2 (Q − K₀h /2 − O(ʰ )) − (Q − K₀h − O(ʰ ))**

**=Q + −K⁰h + K₀h + O(hⁿ⁺²) = Q + O(hₙ₊₂).**

Therefore, Fₙ₊₁(h) is (at least) an order n + 2 (instead of n + 1) formula for approximating the quantity Q.

Foreshadowing where we are headed, define the following series of step size

**h₁ = b − a**

**h₂ = 1 (b − a)**




# 2

· · · 1 ( − )

hj = 2j−₁ b a

The quantity being approximated is Q = ab f(x)dx. Define the approximation formulas Rj,1 to be the composite trapezoidal rule, using hj. Thus Rj+1,₁ is exactly Rj,1 with step size cut in half, as needed to apply extrapolation. Second, notice the overlapping of the formulas. Some of the same function evaluations f(x) are needed in both Rj,1 and Rj+1,₁.





# Romberg Integration

For example, we have

R11 = h1 (f(a) + f(b))

R21 = h2 f(a) + f(b) + 2f(a + b/2)

= 1 R11 + h2 f(a + b/2)

We can prove by induction that

Rj1 = 1 Rj−1,1 + hj 2j−2 f (a + (2i − 1)hj)

for j = 2, 3, ....

Equation (24) gives an efficient way to calculate the composite trapezoidal rule mentally.

The second feature of Romberg integration is extrapolation. Form the tableau,

| R11 | R21 | R22 | R31 | R32 | R33 |
| --- | --- | --- | --- | --- | --- |
| R41 | R42 | R43 | R44 |     |     |

where we define the second column Ri2 as the extrapolations of the first column

R22 = 22R21 − R11 / 22 − 1

R32 = 2 R31 − R21 / 22 − 1

R42 = 2 R41 − R31

So, the second column consists of 4th-order approximations of Q. The define the third column

R33 = 42R32 − R22 / 24 − 1

R43 = 4 R42 − R32 / 24 − 1

R53 = 4 R52 − R43

The third column consists of 6th-order approximations of Q. The general jth entry of the kth column (which is 2kth-order approximation of Q) is given by the formula

Rj,k = 4k−1Rj,k−1 − Rj−1,k−1 / 4k−1 − 1

(Note that 22k−2 = 4k−1.) The tableau is a lower triangular triangular matrix that extends infinitely down and across. The best approximation for the definite integral ∫ab f(x)dx is Rn,n, the bottom rightmost entry computed so far, which is a 2nth-order approximation.



# Romberg integration of ab f(x)dx up to a 2nth order approximation

R1,1 = (b − a)f(a) + f(b)

2

for j = 2 : n

hj = (b−a) / (2j−1 2j−2)

Rj,1 = 1 Rj−1,1 + hj ∑i=1 f(a + (2i − 1)hj)

2

for k = 2 : j

Rj,k = (4k−1Rj,k−1 − Rj−1,k−1) / (4k−1−1)

end

end




# Example: Apply Romberg integration to approximate 12 ln(x)dx.

# Solution:

The code romberg.m is an implementation of the above algorithm and is provided in the textbook.

vpa(romberg(inline('log(x)'),1,2,4),14)

ans =

[ .34657359027997       0.              0.                  0.]
[ .37601934919407 .38583460216543 0.          0.]
[ .38369950940944 .38625956281457 .38628789352451 0.]
[ .38564390995210 .38629204346631 .38629420884310 .38629430908625]

For example, we can check

vpa((.37601934919407*2^2-.34657359027997)/(2^2-1),14)

ans =

.38583460216544

vpa((.38625956281457*2^4-.38583460216543)/(2^4-1),14)

ans =

.38628789352451

Compare with the exact value 2 ln 2 − 1 ≈ 0.38629436111989. □





# Determine the 4 missing entries in the following table for the approximation of the integral

# 1 1 4 2 dx

# 0 + x

| n | h   | Rn,₁     | Rn,₂     | Rn,₃     | Rn,₄ |
| - | --- | -------- | -------- | -------- | ---- |
| 1 | 1   | 3.000000 |          |          |      |
| 2 | 1/2 | R₂,₁     | R₂,₂     |          |      |
| 3 | 1/4 | R₃,₁     | 3.141568 | 3.142117 |      |
| 4 | 1/8 | 3.138988 | 3.141592 | 3.141594 | R₄,₄ |

# Solution

2² × 3.138988 − R₃,₁ = 3.141592.

R₃,₁ = 3.131176. 2² − 1

2² × 3.131176 − R₂,₁ = 3.141568.

R₂,₁ = 3.100000. 2² − 1

2⁴ × 3.141568 − R₂,₂ = 3.142117.

R₂,₂ = 3.133333. 2⁴ − 1

2⁶ × 3.141594 − 3.142117 = R₄,₄.

R₄,₄ = 3.141586. □ 2⁶ − 1




i) If f(x) is a continuous differentiable function over the interval [0, 1], then the length of the curve is given by

1

0 1 + |f′(x)|²dx.

84






# Approximation of the Length of the Graph of f(x)

Given the following table, use composite trapezoidal rule with 4 subintervals to approximate the length of the graph of f(x) over the interval [0, 1]. Then find an upper bound for the error in the approximation assuming f(x) = − ln(cos x).






# Solution:

1 + ∫01 |f′(x)|² dx ≈ 0.25 (1 + |0|² + 1 + |1.56|²)

0 + 2 (1 + |0.26|² + 1 + |0.55|² + 1 + |0.93|²) ≈ 1.24.

If we denote by Tn(f) the composite trapezoidal rule applied to function f, we know:

∫ab f(x) dx − Tn(f) = − (b−a)h² f′′(ξ) for ξ ∈ (a, b).

For x ∈ (0, 1), 1 + |f′(x)|² = 1. Hence d²/ dx² (1 + |f′(x)|²) = 2−cos² x. We know when x ∈ (0, 1), cos(x) is a decreasing (positive) function, so 2−cos² x is an increasing (positive) function.

Hence maxx∈[0,1] d²/ dx² |f′(x)|² = cos³ 1. So the upper bound for:

∫ab (1 + |f′(x)|²) dx − Tn(1 + |f′(x)|²) is (1/4)² (2−cos² 1) ≈ 0.0564.

We can verify that by finding ∫01 (1 + |f′(x)|²) dx for f = − ln(cos x). The exact integral is:

∫01 cos x dx = 2 ln(1−sin x)x=0 ≈ 1.226191. The absolute value of the error is about 0.01.

This checks that the upper bound 0.0564 is correct.






# ii) Use the table of data in part (i) and Romberg integration to obtain a better approximation for the length of the curve.

# Solution:

We have:

R1,1 = 1 (1 + 02 + 1 + 1.562) ≈ 1.43.

R2,1 = 1 (1 + 02 + 1 + 1.562 + 2 (1 + 0.552)) ≈ 1.28.

So, we can build the following table:

| n | Rn,1 | Rn,2 | Rn,3 |
| - | ---- | ---- | ---- |
| 1 | 1.43 |      |      |
| 2 | 1.28 | 1.23 |      |
| 3 | 1.24 | 1.23 | 1.23 |

|R3,3 − I| = 0.00.





# 4.10 π: Zu Chongzhi, Richardson and Romberg

6 = 3. For a general n-sided regular polygon inscribed in the unit circle, it is perimeter is n × 2 × sin(π / n).">

We want to find the approach taken by the Chinese mathematician Zu Chongzhi (429-500) to obtain the value of π more than 1500 years ago. According to wiki, he obtained the result by approximating a circle with a 12288 (=3 × 2¹²) sided regular polygon. His best approximation was between 3.1415926 and 3.1415927. This was an impressive feat for the time, especially considering that the device counting rods he used for recording intermediate results were merely a pile of wooden sticks laid out in certain patterns. The resulting π ≈ 355 / 113 is called the Zu Chongzhi π rate.

But according to what I read and remembered, nowadays it is not so clear how Zu Chongzhi computed as his book which is called “Zhui Shu” (used to be the math textbook for Chinese scholars) was lost after the Song Dynasty. In particular, we do not know how many sides the regular polygon he used has. I once read that Zu Chongzhi used the ideas of Richardson acceleration. We will repeat this process, assuming we know how to calculate sin exactly.

One can use half angle formula to compute cos(30⁰) = √3 / 2, cos(15⁰) = 1 + cos(30⁰) / 2, cos(7.5⁰) = 1 + cos(15⁰) / 2 etc. and then used sin(θ) = √(1 − cos²(θ) / 2). We shall see how a simple trick can save a lot of man power.

So, suppose we have a 3 × 2ʲ sided regular polygon inscribed inside a unit circle. The perimeter of the polygon is 2 sin(π / (3 × 2ʲ)). It means π = perimeter of a unit circle ≈ perimeter of a 3 × 2ʲ-sided polygon = sin(π / (3 × 2ʲ)).

By Taylor expansion sin(x) = x − x³ + x⁵ − x⁷ + · · · , So we know Zj,1 = sin   π   3 × 2j = π + c1   1 + c2   1 + c3   1 + c4   1 + · · · .



# 4.11 Homework 7

1. (Sauer) Page 263, 5.2 Exercises, 1(c), 4(c), 11(c), 12
2. (Sauer) Page 268, 5.3 Exercises, 2(c), 3




# 4.12 Two Computer Projects and Their Solutions

# 1. (Sauer’s book, Page 264, 5.2 Computer Problems, Question 9 + an additional question)

For ∫ 01 ex dx and π ∫ 0h x2 sin(x) dx, calculate the approximation error of the composite ∫ 0h for h = 1, 2, 4, ... , 28, and plot. Make a log-log plot, using, for example, Matlab’s loglog command. What is the slope of the plot, and does it agree with theory? If you are not using Matlab and cannot produce a log-log plot, you can just produce a table to demonstrate what is happening. [5 marks]

Report the results and briefly explain the difference when applying composite Trapezoid to ∫ 01 sin(14πx + √2) + 2 dx and ∫ 01 sin(14.1πx + √2) + 2 dx.

Solution: ∫ 01 sin(14πx + √2) + 2 dx

Why the performances of composite trapezoid are so different on ∫ 01 sin(14.1πx + √2) + 2 dx? Recall the formulas on Page 91 of the lecture notes. After citing

∫ 01 f(x) dx = ½ (f(0) + f(1)) + m B2ℓ f(2l−1)(0) − f(2l−1)(1) − B2m+2 f(2m+2)(ξ),

we use change of variable, apply it to each ∫ 0n xj f(x) dx, and obtain an error formula for ∫ ab composite Trapezoid rule (note the red n, which is a typo m in the notes)

b f(x) = ∫ an xj f(x) dx

= ∫ an h (f(xj−1) + f(xj)) + m B2ℓ h2l f(2l−1)(xj−₁) − f(2l−1)(xj) − B2m+2 h2m+2 f(2m+2)(ξj)

j=1

= ∫ an h (f(xj−1) + f(xj)) + m B2ℓ h2l f(2l−1)(a) − f(2l−1)(b) − m B2m+2 h2m+2 f(2m+2)(ξj).

j=1

This is true for any m as long as f ∈ C2m+2([a, b]).






# When f is periodic on [a, b]

f(2l−1)(a) − f(2l−1)(b) = 0,

b f(x) =

hold on; loglog(h,h.^2,’b:’); legend(’error’,’reference line’) xlabel(’h’) ylabel(’error ’) grid on;

# function f=fcn(x)

%f=sin(2pi7.05x+sqrt(2))+2;
f=sin(2pi7x+sqrt(2))+2;
%f=x.exp(x);
%f=x.^2.sin(x);

# Julia Code

using Printf
function myCompTrapezoid()
a=0.0
b=1.0
N=8
NN=2^8
h=zeros(N+1)
for i=0:N
h[i+1]=(b-a)/(2^i)
end
hsmallest=h[N+1] # the smallest h
f=zeros(NN+1)
for i=0:NN
f[i+1]=fcn(a+ihsmallest) # all the function evalutions
end
fa=f[1]
fb=f[NN+1]
r=zeros(N+1)
for i=1:N+1
r[i]=-fa-fb
for xindex=1:2^(N+1-i):(NN+1) # including the end points
r[i]=r[i]+2f[xindex]
end
r[i]=r[i]*h[i]/2.0
end




exact value the integral

ex = (cos(sqrt(2)) - cos(14.1 pi + sqrt(2)))/(14.1 pi) + 2.0

ex = 2.0

ex = 1.0

ex = cos(1.0) + 2.0*sin(1.0) - 2.0
err=zeros(N+1)
for i=1:N+1
err[i]=abs(r[i]-ex)
end

@printf "\begin{tabular}{|rrr|}\hline \n"
regular_str = r"$i$ &#x26; $h_i$ &#x26; $e_i = |I_i-I_{ex}|$ \hline"
println(regular_str)
for i=1:N+1
@printf "%d &#x26; %2.16f &#x26; %2.16f \\ \hline \n" i h[i] err[i]
end
@printf "\end{tabular}\n"
return r,err
end

function fcn(x)






f=sin(2pi7.05*x+sqrt(2))+2
f=sin(2pi7*x+sqrt(2))+2
f=x.*exp(x)
f=x^2*sin(x) return f end
myCompTrapezoid()
91





# 10-1

# 10-2

# 10-3

error

reference line




# 10-4

# 10-5

# 10-6

# 10-3

# 10-2

# 10-1

# 100

Figure 9: The result of 1 xexdx. The slope is 2. Theoretical result, (5.24) of the textbook, says that the error is proportional to h. Hence log error = log constant + 2 log h. Hence the slope should be 2 in the log-log plot, which is verified numerically.





# 10-1

error

reference line



# 10-2

# 10-3

# 10-4

# 10-5

# 10-6

# 10-3

# 10-2

# 10-1

# 100

Figure 10: The result of π x² sin(x)dx. The slope is 2.

0

92



# Figures

# Figure 11

The result of ∫ sin(14πx + √2) + 2 dx. It is almost exact once h &#x3C; 1.



# Figure 12

The result of ∫ sin(14.1πx + √2) + 2 dx. The slope is 2.




# Table 3: 01 xexdx

| i | hi                 | ei = Ii − Iₑₓ      |
| - | ------------------ | ------------------ |
| 1 | 1.0000000000000000 | 0.3591409142295225 |
| 2 | 0.5000000000000000 | 0.0917507747897934 |
| 3 | 0.2500000000000000 | 0.0230644790527570 |
| 4 | 0.1250000000000000 | 0.0057741073678195 |
| 5 | 0.0625000000000000 | 0.0014440270677076 |
| 6 | 0.0312500000000000 | 0.0003610380466998 |
| 7 | 0.0156250000000000 | 0.0000902614669056 |
| 8 | 0.0078125000000000 | 0.0000225654889323 |
| 9 | 0.0039062500000000 | 0.0000056413798710 |







# Table 4: 01 x2 sin(x)dx

| r | i                  | hi                 | ei = Ii − Iₑₓ |
| - | ------------------ | ------------------ | ------------- |
| 1 | 1.0000000000000000 | 0.1974912169200155 |               |
| 2 | 0.5000000000000000 | 0.0470516630435667 |               |
| 3 | 0.2500000000000000 | 0.0116248312714503 |               |
| 4 | 0.1250000000000000 | 0.0028976820504708 |               |
| 5 | 0.0625000000000000 | 0.0007238892676896 |               |
| 6 | 0.0312500000000000 | 0.0001809391392895 |               |
| 7 | 0.0156250000000000 | 0.0000452327116133 |               |
| 8 | 0.0078125000000000 | 0.0000113080483339 |               |
| 9 | 0.0039062500000000 | 0.0000028270039856 |               |

i hi ei = |Ii − Iₑₓ|

| i | hi                 | ei = |Ii − Iₑₓ|    |
| - | ------------------ | ------------------ |---|---|
| 1 | 1.0000000000000000 | 0.9877659459927353 | | |
| 2 | 0.5000000000000000 | 0.0000000000000000 | | |
| 3 | 0.2500000000000000 | 0.0000000000000004 | | |
| 4 | 0.1250000000000000 | 0.0000000000000009 | | |
| 5 | 0.0625000000000000 | 0.0000000000000000 | | |
| 6 | 0.0312500000000000 | 0.0000000000000004 | | |
| 7 | 0.0156250000000000 | 0.0000000000000009 | | |
| 8 | 0.0078125000000000 | 0.0000000000000000 | | |
| 9 | 0.0039062500000000 | 0.0000000000000009 | | |

# Table 5: 01 sin(14πx + √2) + 2 dx

i hi ei = |Ii − Iₑₓ|

| i | hi                 | ei = |Ii − Iₑₓ|    |
| - | ------------------ | ------------------ |---|---|
| 1 | 1.0000000000000000 | 0.9806251505034251 | | |
| 2 | 0.5000000000000000 | 0.0132188971149834 | | |
| 3 | 0.2500000000000000 | 0.0493705256651666 | | |
| 4 | 0.1250000000000000 | 0.0570239333943314 | | |
| 5 | 0.0625000000000000 | 0.0052178650697212 | | |
| 6 | 0.0312500000000000 | 0.0011655924392082 | | |
| 7 | 0.0156250000000000 | 0.0002842389385407 | | |
| 8 | 0.0078125000000000 | 0.0000706315371679 | | |
| 9 | 0.0039062500000000 | 0.0000176314085398 | | |





# Table 6:

01 sin(14.1πx + √2) + 2 dx




# 2. (Sauer’s book, Page 268, 5.3 Computer Problems, Question 1(a))

Use Romberg Integration approximation R55 to approximate the definite integral

4 ∫ √ x dx.

0 x2 + 9

Compare with the correct integral, and report the error. You can directly call the Romberg integration program in Sauer’s book. If you choose other language, you need to rewrite the Romberg integration code in Sauer’s book by your own language. [3 marks]






# Matlab Code

function err = testRomberg()
r = romberg(@fcn, 0, 4, 5);
syms y;
ex = double(int(fcn(y), 0, 4));
err = abs(r(end, end) - ex);

function f = fcn(x)
f = x ./ sqrt(x.^2 + 9);

# Program 5.1 Romberg integration

Computes approximation to definite integral

- Inputs: Matlab function specifying integrand f,
- a, b integration interval, n = number of rows
- Output: Romberg tableau r

function r = romberg(f, a, b, n)
h = (b - a) ./ (2.^(0:n-1));
r(1, 1) = (b - a) * (f(a) + f(b)) / 2;
for j = 2:n
subtotal = 0;
for i = 1:2^(j-2)
subtotal = subtotal + f(a + (2 * i - 1) * h(j));
end
r(j, 1) = r(j-1, 1) / 2 + h(j) * subtotal;
for k = 2:j
r(j, k) = (4^(k-1) * r(j, k-1) - r(j-1, k-1)) / (4^(k-1) - 1);
end
end
end






# Julia Code

function testRomberg()
n = 5
r = romberg(0,4,n)
ex = 2.0 # for the function x/sqrt(x^2+9)
err = abs(r[n,n]-ex)
return err
end

function romberg(a,b,n)
h=(b-a)/2.0
r=zeros(n,n)
r[1,1]=(b-a)(fcn(a)+fcn(b))/2
for j=2:n
subtotal = 0.0
for i=1:2^(j-2)
subtotal = subtotal + fcn(a+(2i-1)h)
end
r[j,1] = r[j-1,1]/2+hsubtotal
for k=2:j
r[j,k]=(4^(k-1)*r[j,k-1]-r[j-1,k-1])/(4^(k-1)-1)
end
h=h/2.0
end
return r
end

function fcn(x)
return x/sqrt(x^2+9.0)
end

testRomberg()

The error is 1.0412374340518227e − 7.





# 4.13 Peano kernel

First note that by integration by part, we can prove that

f(x) = f(a) + f′(a)(x − a) + ... + f(ᵐ)(a)(x − a)ᵐ +

1 x f(m+1)(t)(x − t)ᵐdt.

m! m! a

= f(a) + f′(a)(x − a) + ... + f(ᵐ)(a)(x − a)ᵐ +

1 b f(m+1)(t)(x − t)ᵐdt

m! m! a

where (y)₊ = y, y > 0.

# Proof:

1! x f(m+1)(t)(x − t)ᵐdt

m a

= 1! x(x − t)ᵐdf(m)(t)

m a

= 1 (x − t)ᵐf(ᵐ)(t) t=x +

1 x f(m)(t)(x − t)ᵐ−1dt

m! t=a (m − 1)! a

= − 1 (x − a)ₘf(ₘ)(a) +

1 x f(m)(t)(x − t)ᵐ−1dt

· · m! (m − 1)! a

= − 1! (x − a)ₘf(ₘ)(a) − · · · − (x − a)f′(a) + f′(t)dt

= − 1! (x − a)ₘf(ₘ)(a) − · · · − (x − a)f′(a) − f(a) + f(x). □



(The following theorem won’t be tested in the exam. It is provided for your information only.)




# Theorem 2

Define sm(x) = (x − t)m. Let a ≤ x1 &#x3C; ... &#x3C; xn ≤ b and suppose I(ᶠ) = t + b f(x)dx ≈ ∑k=1n Ak f(xk) = In(f) has degree of precision m ≥ 1, then

en(f) = I(f) − In(f) = a f(m+1)(t)Km(t)dt

where Km(t) = 1 en(sm(x)) = 1 b(x − t)mdx −

m! t m! a + k +

Proof: f(x) = pm(x) + 1 b f(m+1)(t)sm(x)dt = pm(x) + Rm(x). Then

en(f) = I(f) − In(f) = I(pm + Rm(x)) − In(pm + Rm(x)) = I(Rm(x)) − In(Rm(x))

= I 1 b f(m+1)(t)sm(x)dt − In 1 b f(m+1)(t)sm(x)dt

m! a t m! a t

= 1 b f(m+1)(t)dt[I(sm(x)) − In(sm(x))].

In the last step, we have used the fact that both I and In are integration or numerical integration with respect to the variable x, not t. We have switched the order of dt and dx and switched the order of dt and In.






# Examples of the Peano kernel Kₘ(t):

For trapezoidal rule, m = 1, Kₘ(t) = b(x − t)+dx − b−a ((a − t)+ + (b − t)+). So Kₘ(t) = (x − t)dx − b−a (b − t) = 0 if t ≤ 0.

For Simpson’s rule, m = 3, Kₘ(t) = 1/6 b(x − t)³ dx − b − a ((a − t)³ + 4(c − t)³ + (b − t)³). So 6Kₘ(t) = b(x − t)³dx − b−a ((b − t)³ + 4(c − t)³) if t &#x3C; c and 6Kₘ(t) = b(x − t)³dx − b−a ((b − t)³) if t ≥ c.

Since (x − t)³dx = b, 6Kₘ(t) = b−t) − b−a ((b − t)³) if t &#x3C; c and 6Kₘ(t) = (b − t) 12 0 if t ≥ c.

To see why g(t) = (b−t)⁴ − b−a ((b − t)³ + 4(c − t)³) ≤ 0 when t &#x3C; c, one way is to let b−ₐ τ = 2, and write g(t) as 12 (b a) 3τ 1 2τ 8(τ 1 2), then use Matlab to plot the graph of g(τ) = 4 − 3 − 8(τ − 2)³ for τ ∈ (1]. You will see that the plot is below the x axis and gradually increasing to zero. If you want to make the proof rigorous, you can start to prove that g(τ) is an increasing function on (1 1] (i.e., g'(τ) − 1 (τ − 1)² ≥ 0) (1) τ and g(τ) = 0. Hence g(t) is negative.

To summarize, we have worked out an expression of Kₘ for trapezoidal and Simpson’s rule and showed by brute force that they are non-positive on [a, b].

For a surprisingly large class of integration rule, the Peano’s kernel Kₘ(t) has a constant sign on [a, b]. For example, the Peano kernels for the Newton-Cotes formulas are of constant sign (see for instance J. F. Steffensen, Interpolation, 2nd edition, (1950)) and we have shown by brute force that this is true for trapezoidal rule and Simpson’s rule. In these cases, the mean value theorem (the key is to show that Kₘ has a constant sign) gives eₙ(f) = f(ᵐ+1)(ξ) Kₘ(t)dt for some ξ ∈ [a, b]. The above integral of Kₘ(t) does not depend on f and can therefore be determined by applying eₙ(f) to the polynomial xᵐ⁺¹: eₙ(xᵐ⁺¹) = (m + 1)! b Kₘ(t)dt.

This gives eₙ(f) = f(ᵐ+1)(ξ)eₙ(xᵐ⁺¹).

For Simpson’s rule, m = 3, eₙ(xᵐ⁺¹) = 1/90 b x⁴dx − b − a (a⁴ + 4((a + b)/2)⁴ + b⁴) = −1/90 (b − a)⁵.

So b f(x)dx = b − a f(a) + 4f(a + b) + f(b) − 1 f(4)(ξ) (b − a) 5 (29)






for some ξ ∈ [a, b].

• For the trapezoidal rule, m = 1,

eₙ(xᵐ⁺¹) = 1 b x2dx − b − a a2 + b2 = − 1 (b − a)3. (m + 1)! 2! a2 12

So

b f(x)dx = b − a (f(a) + f(b)) − 1 f(2)(ξ) (b − a)3 (30)

for some ξ ∈ [a, b].





# 4.14 Euler-Maclaurin formula

(This section is not required for the exam.)

b f(x) = h f(a) + f(b) + 2 m−¹ f(xj) + c₂h² + c₄h⁴ + c₆h⁶ + · · · . (31)

We shall not provide the proof of the following classical theorem. One can find its proof in, for example, Section 3.3 of “Introduction to Numerical Analysis” by Stoer and Bulirsch.




# Theorem 3 (Euler-Maclaurin)

Let f ∈ C²ᵐ⁺²([0, 1]). Then

1 f(x)dx = 1 (f(0) + f(1)) 0 2
m B₂ℓ f(2ˡ−1)(0) − f(2ˡ−1)(1) − B₂ₘ₊₂ f(2ᵐ+2)(ξ) (32)

ℓ=1 (2ℓ)! (2m + 2)! for some ξ ∈ (0, 1). Here Bₖ are the Bernoulli numbers

| B₂    | 1  |
| ----- | -- |
| B₄    | −1 |
| B₆    | 1  |
| B₈    | −1 |
| · · · |    |

6 30 42 30 100

If we are interested in b f(x)dx. Then let g(t) = f(a + t(b − a)). Letting x = a + t(b − a),

So

b f(x)dx ≈ b H(x)dx = f(a)b − a + f(b)b − a + f′(a)(b − a)2 − f′(b)(b − a)2 (35)

a a 2 2 12 12

where we have used b 1 − 2 x−ᵃ x−b2 dx = (b−a) 1(1+2t)(1−t)2dt = b−a . b (x − a) x−b2 dx =

a a−b a−b 0 2 a a−b
(b − a)2 1 t(1 − t)2dt = (b−a)2. The other two integrals can be computed similarly, or be

0 12

guessed using symmetry.

Because of (35), we now see where the f′(a) − f′(b) in (32) comes from.





# 4.15 Adaptive quadrature

The approximate integration methods we have learned so far use equal step sizes. The error of the quadrature over a region depends on the derivative of the function over this region:

(Theorem 2)

bI(f) − Iₙ(f) = a f(ᵐ+1)(t)Kₘ(t)dt.

But function may vary wildly over some parts of its domain and vary more slowly through other parts. By using the information from the integration error formulas, a criterion can be developed for deciding during the calculation what step size is appropriate for a particular subinterval. The idea behind this method, called Adaptive Quadrature, is closely related to the extrapolation ideas we have studied before.

Recall that the Trapezoid Rule S[a,b] on the interval [a, b] satisfies the formula

b f(x)dx = S[a,b] − h3 f′′(c0).

(36)

a 12

for some a &#x3C; c0 &#x3C; b, where h = b − a. Setting c to be the midpoint of [a, b], we could apply the Trapezoid Rule to both half-intervals and, by the same formula, get

b f(x)dx = S[a,c] − h3 f′′(c1) + S[c,b] − h3 f′′(c2)

a 8 12 8 12

= S[a,c] + S[c,b] − h3 f′′(c3).

(37)

Hence S[a,b] − (S[a,c] + S[c,b]) = − h3 f′′(c3) + h3 f′′(c0) ≈ 3 h3 f′′(c3)

4 12 12 4 12

where the approximation f′′(c3) ≈ f′′(c0) has been made.

By subtracting the exact integral out of the equation, we have written the error



ultimately in terms of things we can compute.

For example, S[a,b] − (S[a,c] + S[c,b]) is approximately three times the size of the integration error of the formula S[a,c] + S[c,b] on [a, b]. Therefore, we can check whether the former expression is less than 3*TOL for some error tolerance as an approximate way of checking whether the latter approximates the unknown exact integral within TOL. If the criterion is not met, we can subdivide again. For each half, the required error tolerance goes down by a factor of 2, while the error (for the Trapezoid Rule) should drop by a factor of 2³ = 8, so a sufficient number of halvings should allow the original tolerance to be met with an adaptive composite approach.



# Adaptive quadrature

To approximate within tolerance TOL:

c = a + b$2f (a) + f (b)

S[a,b] = (b − a) 2 b-a

if S[a,][a,][,]|·L borig -aorig

else accept [a,]+[c,] as approximation over [a,]

repeat above recursively for [a, c] and [c,]

end




# Program 5.2 Adaptive Quadrature

Computes approximation to definite integral

Inputs: Matlab function f, interval [a0,b0], error tolerance tol0

Output: approximate definite integral

function int=adapquad(f,a0,b0,tol0)
int=0;
n=1;
a(1)=a0;
b(1)=b0;
tol(1)=tol0;
app(1)=trap(f,a,b);
while n>0 % n is current position at end of the list
c=(a(n)+b(n))/2;
oldapp=app(n);
app(n)=trap(f,a(n),c);
app(n+1)=trap(f,c,b(n));
if abs(oldapp-(app(n)+app(n+1)))&#x3C;3*tol(n)
int=int+app(n)+app(n+1); % success
n=n-1; % done with interval
else % divide into two intervals
b(n+1)=b(n);
b(n)=c; % set up new intervals
a(n+1)=c;
tol(n)=tol(n)/2;
tol(n+1)=tol(n);
n=n+1; % go to end of list, repeat
end
end
function s=trap(f,a,b)
s=(f(a)+f(b))*(b-a)/2;






# Figure 13: Adaptive quadrature applied to f(x) = 1 + sin(e³ˣ)

Tolerance is set to TOL = 0.005.

- (a) Adaptive Trapezoid Rule requires 140 subintervals.
- (b) Adaptive Simpson’s Rule requires 20 subintervals.

The Matlab program works as follows: A list is established of subintervals yet to be processed. The list originally consists of one interval, [a, b]. In general, choose the last subinterval on the list and apply the criterion. If met, the approximation of the integral over that subinterval is added to a running sum, and the interval is crossed off the list. If unmet, the subinterval is replaced on the list by two subintervals, lengthening the list by one, and we move to the end of the list and repeat.

For example, if you run:

int=adapquad(@(x)sin(exp(3x)),-1,1,510^(-5))
when n = 4, a = [-1,0,0.5,0.75], b = [0,0.5,0.75,1], tol = 1.0e-04*[0.25,0.125,0.0625,0.065], app = [0.4456,-0.0330,-0.1296,0.1102]

Of course, the Trapezoid Rule can be replaced by more sophisticated rules. For example, let S[a,b] denote Simpson’s Rule, then:

b f(x)dx = S[a,b] − h³ f(⁴)(c₀).
(38) a for some a &#x3C; c₀ &#x3C; b, where h = (b − a)/2. Setting c to be the midpoint of [a, b], we could apply the Trapezoid Rule to both half-intervals and, by the same formula, get:

b f(x)dx = S[a,c] − h⁵ f(⁴)(c₁) + S[c,b] − h⁵ f(⁴)(c₂)
(39) a 32 90 32 90 = S[a,c] + S[c,b] − h⁵ f(⁴)(c₃).

Hence:

S[a,b] − (S[a,c] + S[c,b]) = h⁵ f(⁴)(c₀) − h⁵ f(⁴)(c₃) ≈ 15h³ f(⁴)(c₃) 90 16 90 16 90 105
where the approximation f(⁴)(c₃) ≈ f(⁴)(c₀) has been made.

Since S[a,b] − (S[a,c] + S[c,b]) is now 15 times the error of the approximation S[a,c] + S[c,b] the integral, we can make our new criterion:

|S[a,b] − (S[a,c] + S[c,b])|
and proceed as before. It is traditional to replace the 15 by 10 in the criterion to make the algorithm more conservative.





# Figure 13

shows an application of Adaptive Simpson’s Quadrature to the same integral. The approximate integral is 2.500 when a tolerance of 0.005 is used, using 20 subintervals, a considerable savings over adaptive Trapezoid Rule Quadrature. Decreasing the tolerance to 0.5 × 10−4 yields 2.5008, using just 58 subintervals.



# 4.16 Gaussian quadrature

Let’s determine the weights A₁, A₂ and two points x₁, x₂ so that

1 −1 f(x)dx ≈ A₁f(x₁) + A₂f(x₂) is as accurate as possible. Because we now have 4 unknowns, we can setup 4 equations with f = 1, x, x², x³. So,

- A₁ + A₂ = 2
- A₁x₁ + A₂x₂ = 0 (40)
- A₁x² + A₂x² = 2/3
- A₁x³ + A₂x³ = 0

The solution is x₁ = −1/√3, x₂ = 1/√3, w₁ = w₂ = 1. This is the two point Gaussian quadrature. One can check that its degree of precision is 3 (we already know from (40) that the degree of precision is at least 3.) But in our previous discussion, we use x₁ = −1 and x₂ = 1 (trapezoidal rule) and the degree of precision is 1.

So, the lesson we learned is that for

b n

I(f) = a f(x)dx ≈ k=1 Aₖ f(xₖ ) = Iₙ(f),

we should let both Aₖ and xₖ (k = 1, .., n) be unknowns (instead of fixing xₖ = a + (k − 1)/(n − 1)) and solve them from I(xℓ) = Iₙ(xℓ) for ℓ = 0, 1, 2, ..., 2n − 1. (We have 2n unknowns and so we set 2n equations.) If we can solve the above equations and obtain Aₖ and xₖ , we can immediately conclude that the degree of precision is at least 2n − 1.

However, we soon recognize that we get a system of nonlinear equations to solve which becomes more and more difficult. (Try n = 3 for yourself.) Is there a systematic approach to find those Aₖ and xₖ ? So, here comes Gauss!




# 4.16.1 Weighted Gaussian quadrature

Let ρ(x) be a weight function on [a, b]. Let {Qₙ}∞ be a system of polynomials with degree of Qₙ equals n. They are orthogonal to each other with respect to the inner product ⟨f, ᵍ⟩ = ∫ab ρfgdx. It means ⟨Qₙ, Qₘ⟩ = 0 when n = m. As Pₘ = span{Q₀, Q₁, ..., Qₘ}, ⟨Qₙ, pₘ⟩ = 0 for any pₘ ∈ Pₘ with m &#x3C; n.

Example: If ρ = 1 and [a, b] = [−1, 1], we have the Legendre polynomial

Qₙ(x) = 1 dⁿ (x² − 1)ⁿ (41)

2ⁿn! dxⁿ

and can prove that (For details, see example 5.14 of the textbook)

1 ∫-11 Qₘ(x)Qₙ(x)dx = 0     m = n

So, deg q ≥ i (why cannot it be &#x3C; i?). But k ≤ i. So deg q = i. □

Given ρ(x), fix one Qₙ. Let x₁, ..., xₙ be the n distinct roots of Qₙ(x). Let w(x) = k=1(x − xk) and ℓₖ (x) = n x − xj = w(x)′

j=1,j=k xk − xj (x − xₖ )w (xₖ )

Set

Aₖ = ρ(x)ℓₖ (x)dx

Then

b n

a ρ(x)f(x)dx ≈ k=1 Aₖ f(xₖ ) (43)

is called weighted Gaussian quadrature.

For ρ = 1, [a, b] = [−1, 1],

1 n






# Gaussian Quadrature

−1 f(x)dx ≈ Σi=1n cif(xi).

The roots of Legendre polynomials and the related weights ci are:

| n |                             | roots i | coefficients c   |
| - | --------------------------- | ------- | ---------------- |
| 2 | -0.5773502691893            | 1       | 1.00000000000000 |
|   | √/3 = 0.57735026918963      | 1       | 1.00000000000000 |
| 3 | -√3/5 = -0.77459666924148   | 5/9     | 0.55555555555555 |
|   | 0 = 0.00000000000000        | 8/9     | 0.88888888888888 |
|   | √3/5 = 0.77459666924148     | 5/9     | 0.55555555555555 |
| 4 | 15+2√30 = -0.86113631159405 | 90-5√30 | 0.34785484513745 |
|   | 15-2√30 = −0.33998104358486 | 90+5√30 | 0.65214515486255 |
|   | 15-2√30 = 0.33998104358486  | 90+5√30 | 0.65214515486255 |
|   | 15+2√30 = 0.86113631159405  | 90-5√30 | 0.34785484513745 |

Example: Approximate ∫-11 e-x² dx using Gaussian quadrature.

Solution: ∫-12

The correct answer to 14 digits is 1.71124878378430.

The n = 2 Gauss quadrature approximation is:

1f(−1/3) + 1f(1/3) ≈ 1.69296344978123.

The n = 3 Gauss quadrature approximation is:

5 f(−3/5) + 8 f(0) + 5 f(3/5) ≈ 1.71202024520191.

To approximate integrals on a general interval [a, b], the problem needs to be translated back to [−1, 1]. For that purpose, we can use the following identity (coming from the substitution t = 2x−(a+b)):

∫ab f(x)dx = (b−a)/2 ∫-11 f((b−a)t + b + a) dt.

Example: Approximate the integral ∫12 ln x dx using Gauss quadrature.

Solution: By (44), ∫21 ln x dx = ∫13 ln t + 3 dt. Now we set f(t) = ln((t + 3)/2) and use the standard roots and coefficients. The result for n = 2 is:

1 ln((−1/3 + 3)/2) + 1 ln((1/3 + 3)/2).






≈ 0.3866. Recall that the exact value is approximately 0.3863.

# Theorem 5

The degree of precision of Gauss quadrature from the n roots of Qₙ is 2n − 1.

# Proof:

(This is Theorem 5.6 of the textbook. It won’t be tested.) Let p ∈ P₂ₙ−₁.

p(x) = q(x)Qₙ(x) + r(x), deg q ≤ n − 1, deg r ≤ n − 1.

Because ab ρ(x)q(x)Qn(x) = 0,

ρ(x)p(x)dx = ρ(x)(q(x)Qₙ(x) + r(x)) = ρ(x)r(x)

n n

= Aₖ r(xₖ ) = Aₖp(xₖ ),

k=1 k=1

where in first equality on the second line, we have used the fact that the degree of precision of Gaussian quadrature is n − 1. Why n − 1? Because Gaussian quadrature is obtained from integrating the interpolating function, with the node points chosen to be the roots of orthogonal polynomials. So, when the polynomial’s degree is ≤ n − 1, it coincide with its interpolating polynomial and the integration is exact.

Now, we want to prove that p cannot be degree higher than 2n − 1: Let f(x) = ( n (x − xi))².

Then

ρ(x)f(x) > 0 while Aₖ f(xₖ ) = 0.

a k






# 4.16.2 Properties of Gauss quadrature

(This part is not required for the exam.)

(uniqueness) b ( ) ( ) ≈ n ˜ (˜ ) ≥

Theorem 6 If a ρ x f x dx k=1 Ak f xk has degree of precision 2n − 1, then this is Gauss quadrature. In particular, this implies 2n − 1 is the maximum degree of precision with n points.

Proof: Let ( ) n ( − ), for ∈ w ˜ x = x x j=1 ˜j then any pₙ−₁ Pₙ−₁, b ( ) ( ) ˜ ( (˜ ) (˜ )) ρw A ˜ x p x dx = w n−1 k ˜ xₖ pₙ−₁ xₖ = 0. a k=1

Therefore, by the uniqueness (for example, uniqueness follows from b(Qn(x) − Q′ (x))² = 0 when the leading coefficient of Q and Q′ are both 1) of nth degree a n orthogonal polynomial, w( ) CQ ( ) for C So, for f ∈ ˜ x = x some constant . x = x k ˜ₖ k = 1, .., n. Then letting Pₙ−₁ in b ( ) ( ) n ˜ (˜ ) ˜ a ρ x f x dx = k=1 Ak f xk and using the Vandermonde matrix, one can prove Aₖ = Aₖ . □

Theorem 7 (positivity) The coefficients of the weighted Gaussian quadrature satisfies Aₖ > 0 for k = 1, ..., n.

Proof: Because Aₖ = b ρℓk (x)dx = b ρℓk (x) j ℓj(x) = b ρ(ℓk (x))². where we have used when k = j, b ρℓk (x)ℓj(x) = b ρ ( − w(ˣ)′ − w(ˣ)′ = 0 a a x xₖ )w (xₖ ) (x xj)w (xj) since w(x) = CQₙ(x). □

Theorem 8 (error formula) If f ∈ C²ⁿ([a, b]), then ∃ξ ∈ (a, b) such that

b ρ(x)f(x) − n Aₖ f(xₖ ) = f(2ⁿ)(ξ) b ρ(x)(w(x))²dx.

a k=1 (2n)! a

Proof: Let p₂ₙ−₁(x) ∈ P₂ₙ−₁ be the Hermite interpolation polynomial of f(x).

p₂ₙ−₁(xₖ ) = f(xₖ ), p′ − (xk ) = f′(xk ), ∀ k = 1, ..., n 2n 1

Then by the property of Hermite interpolation, we know

f(x) − p₂ₙ−₁(x) = f(2ⁿ)(ξ(x)) (w(x))². (2n)!

So, b ρf(x)dx − n Aₖ f(xₖ ) = b ρf(x)dx − b ρp₂n−1(x)dx = f(2n)(η) b ρ(w(x))².

a k=1 a a (2n)! a





# 4.17 Homework 8

1. (Sauer) Page 278, 5.5 Exercises, 1(b,c), 2(b,c), 7, 9
2. (Burden) Page 235, Exercise set 4.7, Q11.



Numerical methods for ODEs

In addition to Sauer’s book, part of the notes are taken from “Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems” by Randall J. LeVeque. It is a long chapter, but except a few examples, §5.14–§5.17 won’t be tested.

We will study how to solve the following ordinary differential equation (ODE) numerically:

u′(t) = f(t, u(t)), u(0) = u₀. (1)

Here are some examples:

1. (Exponential grow or decay) u′(t) = au(t), u(0) = u₀.

It means du = adt, or d ln u = adt. So, ln u = at + C, u = eᵃᵗ⁺C. Using u(0) = u₀ to determine C, we find

u(t) = eatu₀.
2. (Separation of variables) u′(t) = t², u(0) = u₀ > 0.

We can rewrite it as u du = t² dt, which means 1 du² = 1 dt³. So, u² = 2t³ + C for some constant C. Using u(0) = u₀ to determine C = u₀², we get

u(t) = (3u₀² + 2t³)/3.
3. (Integration factor and Duhamel’s principle) u′(t) = a(t)u(t) + b(t), u(0) = u₀.

We multiply e−∫0ta(s)ds on both sides and obtain

d/dt (ue−∫0ta(s)ds) = e−∫0ta(s)dsb(t).

Integrate from 0 to T on both sides. After some manipulation, we find the exact solution is

u = e∫0ta(s)dsu₀ + ∫0te−sa(τ)dτb(s)ds.

In general, we can not find a closed form for the exact solution of (1). For example, we cannot find an explicit formula for the solution of u′ = u² + t², u(0) = u₀. Then, does the solution exist even if we cannot find a closed form of it? From numerical point of view, this is an important question since we should avoid to search for something that does not exist.

The following Picard theorem answers the question that under what condition the solution of:

u′(t) = f(t, u(t)), u(t₀) = u₀. (3)

exists and is unique.



# Theorem 1

Consider problem (3). If f(t, u) is continuous in the region G = {|t − t₀| ≤ a, |u − u₀| ≤ b} and there is a constant L such that for any (t, u₁) ∈ G and (t, u₂) ∈ G,

|ᶠ(t, ᵘ₁) − f(t, ᵘ₂)| ≤ L|ᵘ₁ − u₂|. (4)

Then (3) has a unique solution for t in the interval [t₀ − h, t₀ + h], where h = min a, b with M = max(t,u)∈G |f(t, u)|. M




Proof:

The proof is not required for this module. However, it is included because it is very important for any math major student. For example, the existence of solutions for stochastic differential equations and for stochastic backward differential equations are proved by more or less the same method. It also tells you how to prove the existence of solution by first constructing numerical solutions and then passing to the limit (even though the way of constructing numerical solution in the proof is not practical for real applications).

Define function *un+1(t)* inductively by

*un+1(t) = u0 + ∫ f(t, un(s)) ds.*

with *u0(t) = u0 (a constant function). We will prove un(t) converges uniformly (uniformly with respect to t) on [t0 - h, t0 + h] as n → ∞. The limit is called u. Using the fact that f is continuous and un converges uniformly to u*, one concludes

*u(t) = u0 + ∫ f(t, u(s)) ds.*

Hence *u′ = f(t, u) and u(0) = u0. So, we are left to prove the uniform convergence of un* which follows from the Lipschitz condition (4) and the following identity

*un+1(t) − un(t) = ∫t₀ (f(t, un(s)) − f(t, un−1(s))) ds.*

To be more precise, first note that when we choose *h ≤ a small enough, we have ||uk(s)−u0(t,y)∈G ||f(t, y)|| = hM ≤ b for all k and s ∈ [t0 − h, t0 + h]. Hence when t ∈ [t0 − h, t0 + h], both (t, un−1(s)) and (t, un(s)) remain in the region G. So we can apply the Lipschitz condition of f* to (5) and conclude that

*||un+1(t) − un(t)|| ≤ L ∫t₀ ||un(s) − un−1(s)|| ds.*

We know *||u1(t) − u0(t)|| ≤ M(t − t0).* By induction, we can easily prove that

*||un+1(t) − un(t)|| ≤ M (L(t − t0))n+1 / (n + 1)!*

Hence

*max ||um(t) − un(t)|| ≤ max ||uj(t) − uj−1(t)|| for t ∈ [t0−h,t0+h] and n ≤ j ≤ m*

*≤ M (L(t − t0))j → 0 as m, n → ∞. (Thinking about the tail behavior in the Taylor expansion of eL(t−t0)*)






j (L(t−t₀))j .) Now, you recognize that uₙ is a Cauchy sequence under the norm ∥·∥C₀([t −h,t+h]) j! 0 0 defined as ∥g∥C₀([ₜ₀−h,t₀₊ₕ]) = supₜ∈[ₜ₀−h,t₀₊ₕ] |g(t)|. Hence uₙ’s converge under this norm to some function u. The convergence is uniform convergence. This proves the existence of the solution. The uniqueness proof is skipped. □





# 5.1 System of ODEs

Equation (1) is more general than it appears if we allow u to be a vector. A first-order system has the form

u′ = f₁(t, u₁, · · · , uₙ)

u′ = f₂(t, u₁, · · · , uₙ)

. . .

u′ = fₙ(t, u₁, · · · , uₙ)

Moreover, we can reduce higher order equations to a system of first order equations.

# Example 1

Consider the ODE v′′′(t) = v′(t)v(t) − 2t(v′′(t))², for t > 0. This third order equation requires three initial conditions, typically specified as v(0) = η₁, v′(0) = η₂, v′′(0) = η₃. We can rewrite this as a system of the form (1) by introducing the variables u₁(t) = v(t), u₂(t) = v′(t), u₃(t) = v′′(t). Then the equations take the form

d<u₁>

d<u₂>

f( )

dt u =

dt u₂ = u₃ − 2 = t, u .

u₃ u₁u₂

2tu₃</u₂></u₁>

It is also sometimes useful to note that any explicit dependence of f on t can be eliminated by introducing a new variable that is simply equal to t. In the last example, we can introduce u₄(t) = t so that

u₁

u₂

d =

d<u₂> = u₃ − 2 = f(u)

dt

dt u₃ u₁u₂

2u₃u₄

u₄

1</u₂>

with u(0) = [η₁, η₂, η₃, 0]ᵀ.

The system of ODEs u′ = f(t, u) is linear if

f(t, u) = A(t)u + g(t)

where A(t) ∈ Rᵐ×ᵐ and g ∈ Rᵐ. An important special case is when A(t) = A being a constant matrix. In that situation, we can solve u′ = Au exactly by introducing

eᴮ def

1

2 · · ·

1

n · · ·

= I + B + 2! B + + n! B +

for square matrix B. Then u = eᴬᵗu₀ satisfies u′ = Au since

d eᴬᵗu₀ =

d I + At + t² A² + · · · + tⁿ Aⁿ + · · · u₀

dt

dt 2! n!

= A 0 + I + tA + · · · + tⁿ−¹ Aⁿ−¹ + · · · u₀ = A(eᵗᴬ)u₀ = Au.

Theorem 1 on existence and uniqueness carry over to system of ODEs. We just need to change the condition (4) to its vector value form: There is a constant L such that

∥ᶠ(t, ᵘ₁) − f(t, ᵘ₂)∥∞ ≤ L∥ᵘ₁ − u₂∥∞ (6)

for all (t, u₁) and (t, u₂) in some domain G = {(t, u), |t − t₀| ≤ a, ∥u − u₀∥ ≤ b}.




# Example 2

Consider the pendulum equation

mℓy′′ = −mg sin y.

Let v(t) = y′(t) and u = [y, v]ᵀ. The above equation can be rewritten as

d u = d y = v g = f(u).

dt dt v − ℓ sin(ʸ)

Then

∥ᶠ(ᵘ₁) − f(ᵘ₂)∥∞ = v₁g− v₂ g − ℓ sin(ʸ₁) ⁺ ℓ sin(ʸ₂) ∞ = max |ᵛ₁ − v₂|, g | − sin(ʸ₁) + sin(ʸ₂)|

≤ g ℓ g max( ℓ , 1) max (|v₁ − v₂|, |y₁ − y₂|) = max( ℓ , 1)∥u₁ − u₂∥∞.





# 5.2 Some basic numerical methods

Suppose we want to solve *u′ = f(t, u), u(0) = u₀ for t ∈ [0, T]. Let ∆t = T/N for some integer N and define ti = i∆t. The simplest method is Euler’s method (also called forward Euler’s method), based on replacing u′(tₙ) with D₊Uⁿ = Uⁿ⁺¹−Uⁿ*. This gives the method:

*Uⁿ⁺¹ − Uⁿ = f(Uₙ), n = 0, 1, 2, ..., N − 1.* (7)

Rather than viewing this as a system of simultaneous equations as we did for the boundary value problem before, it is possible to solve this explicitly for *Uⁿ⁺¹ in terms of Uⁿ*:

*Uⁿ⁺¹ = Uⁿ + ∆tf(Uⁿ).* (8)

From the initial data *U⁰ = u₀, we can compute U¹, then U²*, and so on. This is called a time matching method.



# Example 3 Solve

y′ = ty + t³, y(0) = 1 on [0, 1].

Solution: Suppose we choose ∆t = 0.2. we calculate the approximate solution iteratively from

yₙ₊₁ = yₙ + ∆t(tₙyₙ + t³)

| n | tₙ  | yₙ     | y(tₙ)  | eₙ     |
| - | --- | ------ | ------ | ------ |
| 0 | 0.0 | 1.0000 | 1.0000 | 0.0000 |
| 1 | 0.2 | 1.0000 | 1.0206 | 0.0206 |
| 2 | 0.4 | 1.0416 | 1.0899 | 0.0483 |
| 3 | 0.6 | 1.1377 | 1.2317 | 0.0939 |
| 4 | 0.8 | 1.3175 | 1.4914 | 0.1739 |
| 5 | 1.0 | 1.6306 | 1.9462 | 0.3155 |

Because for this particular problem, we can find the exact solution y(t) = 3eᵗ²/² − t² − 2.

The table also shows the error eₙ = |yₙ − y(tₙ)| at each step. If we choose ∆t = 0.1, we get

| n  | tₙ  | y(tₙ)  | eₙ     |
| -- | --- | ------ | ------ |
| 0  | 0.0 | 1.0000 | 0.0000 |
| 1  | 0.1 | 1.0000 | 0.0050 |
| 2  | 0.2 | 1.0101 | 0.0105 |
| 3  | 0.3 | 1.0311 | 0.0170 |
| 4  | 0.4 | 1.0647 | 0.0251 |
| 5  | 0.5 | 1.1137 | 0.0357 |
| 6  | 0.6 | 1.1819 | 0.0497 |
| 7  | 0.7 | 1.2744 | 0.0684 |
| 8  | 0.8 | 1.3979 | 0.0934 |
| 9  | 0.9 | 1.5610 | 0.1269 |
| 10 | 1.0 | 1.7744 | 0.1718 |

Compare the error e₁₀ for the h = 0.1 calculation with the error e₅ for the h = 0.2 calculation.

Note that cutting the step size h in half results in cutting the error at t = 1.0 approximately in



Other one step methods (meaning that Un+1 is determined from Un along.)

- (Backward Euler) Un+1 - Un = f(Un+1) · ∆t
- (Trapezoidal method) Un+1 - Un = 1/2 (f(Un) + f(Un+1)) · ∆t

Note that to use the above two methods, one needs to solve an equation for Un+1. Those types of methods are called implicit methods while forward Euler is called explicit method.

If f is nonlinear, the equation is nonlinear, and one can use Newton’s method. So implicit methods are normally considered to be more expensive.

One may also use multistep method.

- (Midpoint or leapfrog method) Un+1 - Un-1 = f(Un) · 2∆t
- (Second order backward differentiation formula method) 3Un+1 - 4Un + Un-1 = f(Un+1) · 2∆t



# 5.2.1 System of ODEs

Approximation of systems of differential equations can be done as a simple extension of the methodology for a single differential equation.

# Example 4

Apply forward Euler’s Method to the first-order system of two equations:

y′ = y² − 2y₁

y′ = y₁ − y₂ − ty²

with initial condition y₁(0) = 0, y₂(0) = 1.



Solution: Y′ = F(t, Y)

Y = yn+1. Yn+1 = Yn + ∆tF(t , Yn), or, equivalently

yn+1 yn (yn)² - 2yn

yn yn yn - yn - tn(yn)²




# Program 6.2

# Vector version of Euler Method

Input: interval inter, initial vector y0, number of steps n

Output: time steps t, solution y. Example usage: euler2([0 1],[0 1],10);

function [t,y]=euler2(inter,y0,n)
t(1)=inter(1);
y(1,:)=y0;
h=(inter(2)-inter(1))/n;
for i=1:n
t(i+1)=t(i)+h;
y(i+1,:)=eulerstep(t(i),y(i,:),h);
end
plot(t,y(:,1),t,y(:,2));
end

function y=eulerstep(t,y,h)
%one step of the Euler Method
%Input: current time t, current vector y, step size h
%Output: the approximate solution vector at time t+h
y=y+h*ydot(t,y);
end

function z=ydot(t,y)
%right-hand side of differential equation
z(1)=y(2)^2-2y(1);
z(2)=y(1)-y(2)-ty(2)^2;
end

| 1 | 0.9 | 0.8 | 0.7 | 0.6 | 0.5 | 0.4 | 0.3 | 0.2 | 0.1 | 0 |
| - | --- | --- | --- | --- | --- | --- | --- | --- | --- | - |
| 0 | 0.2 | 0.4 | 0.6 | 0.8 | 1   | 1.2 |     |     |     |   |





# 5.2.2 Higher order equations

Example 5 Recall the pendulum equation

mℓy′′ = −mg sin y

which can be converted to a first-order system with y₁ = y, y₂ = y′:

d y₁/dt = y₂g

To solve the equation, we will be given initial condition y₁(0) = y₀ and y₂(0) = v₀ which are the initial position and velocity of the pendulum.

Figure 14: Forward Euler Method applied to the pendulum equation. The curve of smaller amplitude is the angle y₁ in radians; the curve of larger amplitude is the angular velocity y₂. (a) Step size h = 0.01 is too large; energy is growing. (b) Step size h = 0.001 shows more accurate trajectories.



# 5.3 Local truncation errors and one-step errors

We write the difference equation in the form that directly models the derivatives (e.g., in the form (7) rather than (8)) and then insert the true solution of the ODE into the difference equation. We then use Taylor expansion and cancel out common terms.

# Example 6

The local truncation error of the midpoint method is defined by

τⁿ = u(tⁿ⁺¹) − u(tⁿ−¹) − f(u(tₙ))

= u′(tₙ) + 1/6 ∆t²u′′′(tₙ) + O(∆t⁴) − f(u(tₙ))

= 1/6 ∆t²u′′′(tₙ) + O(∆t⁴).

The truncation error is O(∆t²) and so we say the method is second order accurate, although it is not yet clear that the global error will have this behavior. It turns out that we need some form of stability to guarantee that the global error will exhibit the same rate of convergence as the local truncation error. This will be discussed later.

In some literature, a slightly different definition of LTE might be used that is based on the form Uⁿ⁺¹ = Uⁿ−¹ + 2∆tf(Uⁿ) for example, rather than Un+1−Un−1 = f(Un). Denoting this value by Lⁿ, we have

Lⁿ = u(tₙ₊₁) − u(tₙ−₁) − 2∆tf(u(tₙ)) = 1 ∆t³u′′′(tₙ) + O(∆t⁵).

In some textbook, the above Lⁿ, which is 2∆tτⁿ, is called the one-step error since this can be viewed as the error that would be introduced in one time step if the past values Uⁿ, Uⁿ−¹, ... were all taken to be the exact values from u(t). Note that Lⁿ = τⁿ × O(∆t).



# 5.4 Taylor series methods

The forward Euler method can be derived using a Taylor expansion of u(tn+1) about u(tn):

u(tn+1) = u(tn) + ∆tu′(tn) + 1 ∆t²u′′(tn) + · · · .

If we drop all term of order ∆t² and higher, and use the differential equation to replace u′ by f, we obtain

u(tn+1) ≈ u(tn) + ∆tf(tn, u(tn)).

This suggests the forward Euler method. A Taylor series method of higher accuracy can be derived by keeping more terms in the Taylor series. Then we use u′ = f(t, u) to derive formulas for u′′ and etc. For example,

u(tn+1) = u(tn) + ∆tu′(tn) + 1 ∆t²u′′(tn) + O(∆t³)

and

u′ = f(t, u)

u′′ = fu(t, u)u′(t) + ft(t, u) = fu(t, u)f(t, u) + ft(t, u)

where ft = ∂f/∂t and fu = ∂f/∂u. This gives the following numerical method

Un+1 = Un + ∆tf(tn, Un) + 1 ∆t² (fu(tn, Un)f(tn, Un) + ft(tn, Un)) .



# Example 7

Determine the second-order Taylor Method for

y′ = ty + t³, y(0) = 1.

Solution: Since f(t, y) = ty + t³, fₜ = y + 3t², fy = t,

d f(t, y(t)) = fₜ + fyf = y + 3t₂ + t(ty + t₃).

dt

Hence the second-order Taylor method is

yₙ₊₁ = yₙ + ∆t tₙyₙ + t³ + ∆t² yₙ + 3t² + tₙ(tₙyₙ + t³).

Clearly, third and higher order methods will be even more complicated and very messy

expressions must be worked out for each equation. As a result, this approach is not often

used in practice. Hence people try to avoid the explicit evaluation of fu, and that leads to

the Runge-Kutta methods.



# 5.5 Runge-Kutta method

These are one step, but multi-stage method, where intermediate values of the solution and its derivative are generated and used within a single time step.

# Example 8

A two stage explicit Runge-Kutta method is given by

U* = Un + 1 ∆t f(Un)

Un+1 = Un + ∆t f(U*).

In the first stage, an intermediate value is generated that approximates u(tn+1) via Euler’s method. Combine the two steps above, we can rewrite the method as

Un+1 = Un + ∆t f Un + 1 ∆t f(Un).

Viewed this way, this is clearly a one-step method. The local truncation error is defined to be

τn = 1 (u(tn+1) − u(tn)) − f(u(tn)) + 1 ∆t f(u(tn)).

Note that u′ = f(u(t)) implies u′′ = f′u′ = f′f and therefore

f(u(tn)) + 1 ∆t f(u(tn)) = f(u(tn)) + 1 ∆t f′(u(tn)) f(u(tn)) + O(∆t²)

= u′(tn) + 1 ∆t u′′ + O(∆t²).

Hence

τn = 1 ∆t u′(tn) + 1 ∆t² u′′(tn) + O(∆t³) − u′(tn) − 1 ∆t u′′ − O(∆t²) = O(∆t²).




# Example 9

The Runge-Kutta method in the previous example can be extended to the case when f = f(t, u):

U∗ = Uⁿ + 1 ∆tf(tₙ, Uⁿ) 2

Uⁿ⁺¹ = Uⁿ + ∆tf(tₙ + ∆t , U∗). 2






# Example 10

One simple higher order Runge-Kutta method is the four-stage method given by

1. Y = Uⁿ
2. Y = Uⁿ + 1 ∆t f(t , Y )
3. Y = Uⁿ + 1 ∆t f(t + 1 ∆t, Y )
4. Y = Uⁿ + ∆t f(t + 1 ∆t, Y )

Uⁿ⁺¹ = Uⁿ + 1 ∆t f(tₙ, Y ) + 2f(t + 1 ∆t, Y ) + 2f(t + 1 ∆t, Y ) + f(t + ∆t, Y ).

The above method can be proved to be fourth order accurate. The most expensive part of the algorithm is the evaluation of f. When implementing the above algorithm, in each time step, one only needs to evaluate f 4 times instead of 7 times.

If f(t, u) = f(t), this reduced to Simpson’s rule for integrating u′ = f(t) from tₙ to tₙ₊₁.





# Example 11

Solve

y′ = ty + t³, y(0) = 1 on [0, 1] by the 4th order Runge-Kutta method.




# Solution:

function y=rk4(t0,t1,y0,dt)
y=y0;
ddt=dt/2.0;
for t=t0:dt:(t1-dt)
k1=fcn(t,y);
k2=fcn(t+ddt,y+ddtk1);
k3=fcn(t+ddt,y+ddtk2);
k4=fcn(t+dt,y+dtk3);
y=y+(k1+2*k2+2*k3+k4)*dt/6.0;
end
end

function f = fcn(t,y)
f = t.*y+t.^3;
end





# Figure 15: Error as a function of step size for Runge-Kutta of order 4.

For example, abs(rk4(0,1,1,0.2)-(3*exp(0.5)-3)) gives 2.3788e-05. The difference between the proximate solution and the correct solution at t = 1 has slope 4 on a log-log plot, so is proportional to h⁴, for small h.

| steps | step size h | error at t = 1 |
| ----- | ----------- | -------------- |
| 5     | 0.20000     | 2.3788× 10-5   |
| 10    | 0.10000     | 1.4655× 10-6   |
| 20    | 0.05000     | 9.0354× 10-8   |
| 40    | 0.02500     | 5.5983× 10-9   |
| 80    | 0.01250     | 3.4820× 10-10  |
| 160   | 0.00625     | 2.1710× 10-11  |
| 320   | 0.00312     | 1.3491× 10-12  |
| 640   | 0.00156     | 7.2609× 10-14  |





# A general r-stage Runge-Kutta method has the form

r

Y = Uⁿ + ∆t a f(t + c ∆t, Y ),

1 1j n j j

j=1

r

Y = Uⁿ + ∆t a f(t + c ∆t, Y ),

2 2j n j j

j=1

.

.

.

r

Y = Uⁿ + ∆t a f(t + c ∆t, Y ),

r rj n j j

j=1

r

Uⁿ⁺¹ = Uⁿ + ∆t bjf(tₙ + cj∆t, Y ). (10)

j

j=1

and we represent the algorithm using the Butcher tableau:






c₁    a₁₁ · · · a₁ᵣ

.     .       .     .

.     .       .     .

.     .       .     .

cᵣ    aᵣ₁     · · · aᵣᵣ

b₁ · · · bᵣ

For example, the four-stage Runge-Kutta method has the following tableau (entries not shown are all 0):

|   | 0 |   |   |
| - | - | - | - |
| 1 | 1 |   |   |
| 2 | 2 |   |   |
|   | 1 | 0 | 1 |
| 2 | 2 |   |   |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |
| 6 | 3 | 3 | 6 |

Since

tn+1 1

u(tₙ₊₁) = u(tₙ) + f(σ, u(σ))dσ = u(tₙ) + ∆t f(tₙ + σ∆t, y(tₙ + σ∆t))dσ,

tn 0

we can consider the Runge-Kutta method as an approximation of the second integral by a quadrature:

r

Uⁿ⁺¹ = Uⁿ + ∆t bif(tₙ + ci∆t, Y) (11)

i

i=1

with

r

Y = Uⁿ + ∆t a f(t + c ∆t, Y) ≈ u(t + c ∆t). (12)






i ij n j j n i

j=1

Hence we see that we should require

r aij = ci, i = 1, 2, ..., r, (13)

r bj = 1. (14)

An important class of Runge-Kutta methods consists of the explicit methods for which aij = 0 for j ≥ i. For an explicit method, the elements on and above the diagonal in the aij portion of the Butcher tableau are all equal to zero, as, for example, with the four-stage method discussed before. With an explicit method, each of the Yi values is computed using only the previously computed Yj.

Fully implicit Runge–Kutta methods, in which each Yi depends on all the Yj, can be expensive to implement on systems of ODEs. For a system of s equations (where each Yi is in Ys), a system of sr equations must be solved to compute the r vectors Yi simultaneously.

One subclass of implicit methods that are simpler to implement are the diagonally implicit Runge–Kutta methods (DIRK methods) in which Yi depends on Yj for j ≤ i, i.e., aij = 0 for j > i. For a system of s equations, DIRK methods require solving a sequence of r implicit systems, each of size s, rather than a coupled set of sr equations as would be required in a fully implicit Runge–Kutta method. DIRK methods are so named because their tableau has zero values above the diagonal but possibly nonzero diagonal elements.






# Example 12

A second order accurate DIRK method is given by

- Y1 = Un,
- Y2 = Un + 1/4 ∆t f(tn, Y1) + f(tn + 1/2 ∆t, Y2),
- Y3 = Un + 1/3 ∆t f(tn, Y1) + f(tn + 1/2 ∆t, Y2) + f(tn + ∆t, Y3),
- Un+1 = Y3 = Un + 1/3 ∆t f(tn, Y1) + f(tn + 1/2 ∆t, Y2) + f(tn + ∆t, Y3).

This method is known as the TR-BDF2 method. Its tableau is

| 0 | 1 | 1 |
| - | - | - |
| 2 | 4 | 4 |
| 1 | 1 | 1 |
| 3 |   |   |
| 1 |   |   |
| 3 |   |   |

In addition to the conditions (13) and (14), a Runge-Kutta method is second order accurate of

rjbjcj = 1 , (15)

j=1

2

as is satisfied by the method in Example 12. Third order accuracy requires two additional conditions

rjbjc2 = 1 , (16)

j=1

j

3

rirjbiaijcj = 1 . (17)

i=1

j=1

6

Fourth order accuracy requires an additional four conditions on the coefficients, and higher order methods require an exponentially growing number of conditions.






# Runge-Kutta Methods

An r-stage explicit Runge-Kutta method can have order at most r, although for r ≥ 5 the order is strictly less than the number of stages. Among implicit Runge-Kutta methods, r-stage methods of order 2r exist. There typically are many ways that the coefficients aij and bj can be chosen to achieve a given accuracy, provided the number of stages is sufficiently large. Many different classes of Runge-Kutta methods have been developed over the years with various advantages.

The order conditions are quite complicated for higher order methods and an extensive theory has been developed by Butcher for analyzing these methods and their stability properties. For more discussion and details see, for example, J. C. Butcher. *The Numerical Analysis of Ordinary Differential Equations: Runge-Kutta and General Linear Methods*. John Wiley, Chichester, UK, 1987, or the two-volume book by E. Hairer, S. P. Norsett, and G. Wanner.

Using more stages to increase the order of a method is an obvious strategy. For some problems, however, we will also see that it can be advantageous to use a large number of stages to increase the stability of the method while keeping the order of accuracy relatively low. This is the idea behind the so called Runge-Kutta-Chebyshev methods.





# 5.6 Embedded methods and error estimation

Most practical software for solving ODEs does not use a fixed time step but rather adjusts the time step during the integration process to try to achieve some specified error bound. One common way to estimate the error in the computation is to compute using two different methods and compare the results. Knowing something about the error behavior of each method often allows the possibility of estimating the error in at least one of the two results.

A simple way to do this for ODEs is to take a time step with two different methods, one of order p and one of a different order, say, p + 1. Assuming that the time step is small enough that the higher order method is really generating a better approximation, then the difference between the two results will be an estimate of the one-step error in the lower order method. This can be used as the basis for choosing an appropriate time step for the lower order approximation. Often the time step is chosen in this manner, but then the higher order solution is used as the actual approximation at this time and as the starting point for the next time step. Once this is done there is no estimate of the error, but presumably it is even smaller than the error in the lower order method and so the approximation generated will be even better than the required tolerance.

Since the main cost in a Runge-Kutta method is often in evaluating the function f(t, u), it makes sense to reuse function values as much as possible and look for methods that provide two approximations to u(tn+1) of different order based on the same set of function evaluations, by simply taking different linear combinations of the f(Yj, tn + cj ∆t) values in the final stage of the Runge-Kutta method (10). So in addition to the value Un+1 given there, we would like to also compute a value

Un+1 = Un + ∆t ∑j=1r bj f(tn + cj ∆t, Yj).

that gives an approximation of a different order that can be used for error estimation. These are called embedded Runge-Kutta methods and are often displayed in a tableau of the form:

| c1 | a11 | · | · | · | a1r |
| -- | --- | - | - | - | --- |
| .  | .   | . | . | . | .   |
| .  | .   | . | . | . | .   |
| .  | .   | . | . | . | .   |
| cr | ar1 | · | · | · | arr |
|    | b1  | · | · | · | br  |
|    | ˆb1 | · | · | · | ˆbr |





# Runge-Kutta Methods

A very simple example, the second order Runge-Kutta method (9) could be combined with the first order Euler method:

Y1 = Un,
Y2 = Un + 1/2 ∆t f(tn, Y1),
Un+1 = Un + ∆t f(tn + 1/2 ∆t, Y2),
Uˆ n+1 = Un + ∆t f(tn, Y1).

Note that the computation of Uˆ n+1 reuses the f(tn, Y1) obtained before. Also note that Uˆ n+1 − Un+1 ≈ ∆t (f(tn, Y1) − f(tn+1/2, Y2)) ≈ 1/2 ∆t2 u′′(tn), which is approximately the one-step error of Euler’s method.

Most software based on Runge-Kutta methods uses embedded methods of higher order. For example, the ode45 routine in MATLAB uses a pair of embedded Runge-Kutta methods of order 4 and 5 due to Dormand and Prince. Enter type ode45 in the command window in MATLAB for implementation details.

For more about strategies for time step selection, see, for example, L. F. Shampine and M.W. Reichelt, The MATLAB ODE suite. SIAM J. Sci. Comput., 18:1–22, 1997.






# 5.7 Backward Euler revisit and its stability

Recall the backward Euler method for n = 0, 1, 2, ...

yn+1 = yn + ∆t f(tn, yn+1).

What’s the point to waste resources to solve the above nonlinear equation in order to obtain yn+1? The answer is stability.





# Example 13

Apply forward Euler method with ∆t = 0.3 to solve

Solution: y′ = 10(1 − y), y(0) = 0.

So, we get yn+1 = yn + ∆t[10 − 10yn] = 3 − 2yn.

y0 = 0, y1 = 3, y2 = −3, y3 = 9, y4 = −15, y5 = 33, y6 = −63, y7 = 129, · · · .

One can prove that |yn| → ∞. ( ) − −¹⁰ᵗ → → ∞

Please note that the exact solution is y(t) = 1 − e−10t as t → ∞.

The lesson we learned is that if we take large time step, the solution by forward Euler might completely go wrong even though the exact solution is finite and nice.



# Example 14

Apply backward Euler method with ∆t = 0.3 to solve

Solution: y′ = 10(1 − y), y(0) = 0.

yn+1 = yn + ∆t[10 − 10yn+1] ⇒ yn+1 = yn + ∆t = yn + 3.

So, we get a fixed point iteration yn+1 = g(yn) = yn + 3, which converges to 1 since 1 is the fixed point of g and |g′(1)| = 3 &#x3C; 1.

Note that the behavior of the backward Euler solution is similar to that of the exact solution y(t) = 1 − e−10t as t → ∞.

Notice that the explicit Euler method yn+1 = yn + ∆t[10 − 10yn] can be viewed as a fixed-point iteration with g(y) = y(1 − 10∆t) + 10∆t. This iteration will converge to the fixed point at y = 1 as long as |g′(1)| = |1 − 10∆t| &#x3C; 1. Solving this inequality yields 0 &#x3C; ∆t &#x3C; 0.2. For any larger ∆t, the fixed point 1 will repel nearby guesses, and the solution will have no hope of being accurate.




# Example 15

Apply the Backward Euler Method to the initial value problem on [0, 3].

y′ = y + 8y² − 9y³,

y(0) = 1/2

# Solution:

yn+1 = yn + ∆t yn+1 + 8yn² − 9yn³.

Given yn, we solve for yn+1 by Newton’s method, with initial guess yn.





# 1.3

# Backward Euler

y1 Euler

| 0.7 | 0.3 | 0.6 | 1 |
| --- | --- | --- | - |

Figure 16: Comparison of Euler and Backward Euler steps. The differential equation is y′ = 10(1 − y). The forward Euler step overshoots, while the Backward Euler step is more consistent with the system dynamics.

| 1.5 | 1.5 |
| --- | --- |
| 0.5 | 0.5 |

(a) 2 3 00 (b) 2 3

Figure 17: True solution is the dashed curve. The black circles denote the forward Euler method approximation; the blue circles denote Backward Euler. (a) h = 0.3 (b) h = 0.15.



# 5.8 Homework 9

1. (Sauer) Page 291, 6.1 Exercises, 2(a)
2. (Sauer) Page 301, 6.2 Exercises, 4(c). The exact solution is Ce(ᵗ+1)² for any constant C. If you want to learn how to find the exact solution, please read Section 6.1.3 of the textbook.
3. (Sauer) Page 320, 6.4 Exercises, 1(c), 6, 7.



# 5.9 Linear multistep methods

Taylor series and Runge-Kutta methods are one-step methods; the approximation Uⁿ⁺¹ depends on Uⁿ but not on previous values Uⁿ−¹, Uⁿ−², ... . Multistep methods use Uⁿ, Uⁿ−¹, etc. to determine Uⁿ⁺¹.

One-step methods have several advantages over multistep methods:

- The methods are self-starting: from the initial data u₀ the desired method can be applied immediately.
- The time step ∆t can be changed at any point, based on an error estimate, for example.
- The time step can also be changed with a multistep method but more care is required.

On the other hand, one-step methods have some disadvantages. The disadvantage of Taylor series methods is that they require differentiating the given equation and are cumbersome and often expensive to implement. Runge-Kutta methods only use evaluations of the function f, but a higher order multistage method requires evaluating f several times each time step. For simple equations this may not be a problem, but if function values are expensive to compute, then high order Runge-Kutta methods may be quite expensive as well. This is particularly true for implicit methods, where an implicit nonlinear system must be solved in each stage.

An alternative is to use a multistep method in which values of f already computed in previous time steps are reused to obtain higher order accuracy. Typically only one new f evaluation is required in each time step. This leads to the popular class of linear multistep methods.

In general, an r-step linear multistep method (LMM) has the form

r r

αjUn+j = ∆t βjf(tn+j, Un+j). (18)

If βr = 0, then the method (18) is explicit. Note that we can multiply both sides by a constant and have essentially the same method. The normalization αr = 1 is often assumed to fix this scale factor.




# Example 16

The Adams methods have the form

r

Un+r = Un+r-1 + ∆t βjf(Un+j). (19)

These methods all have αr = 1, αr-1 = -1, and αj = 0 for j &#x3C; r - 1. The βj coefficients are chosen to maximize the order of accuracy. If we require βr = 0 so the method is explicit, then the r coefficients β0,..., βr-1 can be chosen so that the method has order r. This can be done by using Taylor expansion of the local truncation error and then choosing the βj to eliminate as many terms as possible. This gives the explicit Bashforth methods.

Another way to derive the Adams-Bashforth methods is by writing

u(tn+r) = u(tn+r-1) + ∫tn+r-1tn+r u′(t)dt = u(tn+r-1) + ∫tn+r-1tn+r f(u(t))dt

and then applying a quadrature rule to this integral to approximate

∫tn+r-1tn+r f(u(t))dt ≈ ∆t ∑j=1r-1 βjf(u(tn+j)).

The quadrature rule can be derived by interpolating f(u(t)) by a polynomial p(t) of degree r - 1 at the points tn, tn+1,...,tn+r-1 and then integrating the interpolating polynomial. For example, if r = 2, we use first order polynomial p1 = fn + (fn+1 - fn)(t - tn).

∫tn+2tn+2 f(t, y(t))dt ≈ ∫tn+2tn+2 p1dt = fn∆t + (fn+1 - fn) &#x26;frac{3∆t2}{2}.

So,

Un+2 = Un+1 + ∆t (3f(tn+1, Un+1) - f(tn, Un)). &#x26;frac{1}{2}

The first few are given below with f def f(n) = tn, U

| # | Scheme            | LTE       |
| - | ----------------- | --------- |
| 1 | Un+1 = Un + ∆t fn | ∆t u′′(ξ) |





# Scheme

# LTE

| steps | Un+2 = Un+1 + ∆t (3fn+1 - fn)                     | \\(\frac{5∆t^2}{12} u^{(3)}(ξ)\\)    |
| ----- | ------------------------------------------------- | ------------------------------------ |
| 3     | Un+3 = Un+2 + ∆t (23fn+2 - 16fn+1 + 5fn)          | \\(\frac{3∆t^3}{8} u^{(4)}(ξ)\\)     |
| 4     | Un+4 = Un+3 + ∆t (55fn+3 - 59fn+2 + 37fn+1 - 9fn) | \\(\frac{251∆t^4}{720} u^{(5)}(ξ)\\) |

Table 7: Adams-Bashforth family

If we allow βᵣ to be nonzero, then we have one more free parameter and so we can donate an additional term in the LTE. This gives an implicit method of order r + 1 called the r-step Adams-Moulton. These methods can again be derived by polynomial interpolation, now using a polynomial of degree r at the points tₙ, tₙ₊₁,...,tₙ₊ᵣ and then integrating the interpolating polynomial.

For example,

u(tₙ₊₁) = u(tₙ) + ∫tₙtₙ₊₁ u′(t)dt = u(tₙ) + ∫tₙtₙ₊₁ f(u(t))dt.

Let fₙ = f(u(tₙ)). Using first order polynomial, p₁ = fₙ + fⁿ⁺¹−ᶠⁿ (t − tₙ). ∫tₙtₙ₊₁ f(u(t))dt ≈ ∆t/2 (fₙ + fₙ₊₁).

So, the 1-step Adams-Moulton method would be

Uⁿ⁺¹ = Uⁿ + ∆t/2 (f(tₙ₊₁, Uⁿ⁺¹) + f(tₙ, Uⁿ)).

This method is also called Crank-Nicolson method or trapezoidal method.




# Steps

| Steps | Scheme                                               | LTE                 |
| ----- | ---------------------------------------------------- | ------------------- |
| 1     | Uⁿ⁺¹ = Uⁿ + ∆ᵗ/2 (f(Uⁿ⁺¹) + fₙ)                      | − ∆ᵗ²/12 u(3)(ξ)    |
| 2     | Uⁿ⁺² = Uⁿ⁺¹ + ∆ᵗ/12 (5f(Uⁿ⁺²) + 8fₙ₊₁ − fₙ)          | − ∆ᵗ⁴/244 u(4)(ξ)   |
| 3     | Uⁿ⁺³ = Uⁿ⁺² + ∆ᵗ/24 (9f(Uⁿ⁺³) + 19fₙ₊₂ − 5fₙ₊₁ + fₙ) | − 19∆ᵗ⁵/720 u(5)(ξ) |

# Table 8: Adams-Moulton family

Example 17 The explicit Nyström methods have the form

Uⁿ⁺ʳ = Uⁿ⁺ʳ−² + ∆t ∑j=0r−1 βjf(Uⁿ⁺ʲ)

with the βj chosen to give order r. The midpoint (or leapfrog) method

Uⁿ⁺¹ = Uⁿ−¹ + 2∆tf(Uⁿ)

is a two step explicit Nyström method. A two step implicit Nyström method is Simpson’s rule

Uⁿ⁺² = Uⁿ + 2∆t/6 (f(Uⁿ⁺²) + 4f(Uⁿ⁺¹) + f(Uⁿ)).





# 5.9.1 Local Truncation Error

For LMMs, it is easy to derive a general formula for the LTE. We have

τ(tn+r) = (1/∆t) ∑j=0r αju(tn+j) − (∆t/r) ∑j=0r βjf(tn+j, u(tn+j)).

So using u′ = f(u),

u(tn+j) = u(tn) + j∆tu′(tn) + 1/2 (j∆t)²u′′(tn) + · · ·

u′(tn+j) = u′(tn) + j∆tu′′(tn) + 1/2 (j∆t)²u′′′(tn) + · · ·

and so on, we obtain

τ(tn+r) = 1/r ∑j=0r αj u(tn) + ∑j=0r (jαj − βj) u′(tn) ∆t + ∑j=0r (1/2 j²αj − jβj) u′′(tn) ∆t + · · ·

+ ∑j=0q-1 (1/q! r jqαj − jq⁻¹βj) u(q)(tn) + · · ·.

The method is consistent if τ → 0 as ∆t → 0, which requires at least the vanishing of the first two terms in this expansion:

∑j=0r αj = 0, and ∑j=0r jαj = βj. (22)

If the first p + 1 terms vanish, then the method will be pth order accurate.



# 5.9.2 Characteristic polynomials

It is convenient at this point to introduce the so-called characteristic polynomials ρ(ξ) and σ(ξ) for the LMM:

ρ(ξ) = ∑j=0r αjξj and σ(ξ) = ∑j=0r βjξj. (23)

Condition (22) can be rewritten as:

ρ(1) = 0 and ρ′(1) = σ(1). (24)



# Example 18 The two-step Adams-Moulton method

Uⁿ⁺² = Uⁿ⁺¹ + ∆t (5f(Uⁿ⁺²) + 8f(Uⁿ⁺¹) − f(Uⁿ))

has characteristic polynomials

ρ(ξ) = ξ² − ξ, σ(ξ) = 1 (5ξ₂ + 8ξ − 1).



# 5.9.3 Starting values

One difficulty with using LMMs if r > 1 is that we need the values U0, U1, .., Ur−1 before we can begin to apply the multistep method. The value U0 is known from the initial data, but the other values are not and typically must be generated by some other numerical method or methods.

Example 19 If we want to use the midpoint method Un+1−Un−1 = f(Un), then we need to generate U1 by some other method before we begin to apply the above method with n = 1. We can obtain U1 from U0 using any one-step method, such as Euler’s method or the trapezoidal method, or a higher order Taylor series or Runge–Kutta method.

Since the midpoint method is second order accurate we need to make sure that the value U1 we generate is sufficiently accurate so that this second order accuracy will not be lost. Our first impulse might be to conclude that we need to use a second order accurate method such as the trapezoidal method rather than the first order accurate Euler method, but this is wrong. The overall method is second order in either case.

This is easiest to explain in terms of the one-step error. The midpoint method has a one-step error that is O(∆t3) and because this method is applied in O(T/∆t) time steps, the global error is expected to be O(∆t2). Euler’s method has a one-step error that is O(∆t2), but we are applying this method only once. If U0 = u(0), then the error in U1 obtained with Euler will be O(∆t2). If the midpoint method is stable, then this error will not be magnified unduly in later steps and its contribution to the global error will be only O(∆t2). The overall second order accuracy will not be affected.

More generally, with an r-step method of order p, we need r starting values U0, U1, .., Ur−1 and we need to generate these values using a method that has a one-step error that is O(∆tp) (corresponding to an LTE that is O(∆tp−1)). Since the number of times we apply this method (r − 1) is independent of ∆t as ∆t → 0, this is sufficient to give an O(∆tp) global error. Of course somewhat better accuracy (a smaller error constant) may be achieved by using a pth order accurate method for the starting values, which takes little additional work.



# 5.9.4 The predictor-corrector methods

One can couple an (explicit) Adams-Bashforth method with an (implicit) Adams-Moulton method of the same order. The idea is to predict Un+1 using an Adams-Bashforth method and then correct its value using an Adams-Moulton method. This is done by using U~n+1 on the right-hand side of the Adams-Moulton method inside the f evaluation so that the Adams-Moulton formula is no longer implicit. For example:

U~n+1 = Un + ∆t f(Un) + f(U~n+1)

It can be shown that this method is second order accurate. It also generates a lower order approximation and the difference between the two can be used to estimate the error.




# 5.10 Backward differentiation formula methods

A very useful class of LMM methods take the form

αᵣUⁿ⁺ʳ + αᵣ−₁Uⁿ⁺ʳ−¹ + · · · + α₁Uⁿ⁺¹ + α₀Uⁿ = ∆tβᵣf(Uⁿ⁺ʳ). (25)

The term on the left are trying to approximate βᵣu′(tₙ₊ᵣ) by a backward difference approximation which, as its name indicates, uses u(tₙ₊ᵣ) and r additional points going backward in time.

It is possible to derive an r-step method that is rth order accurate. The one-step backward differentiation formula (BDF) method is simply the backward Euler method Uⁿ⁺¹ − Uⁿ = ∆tf(Uⁿ⁺¹) which is first order accurate. The other useful BDF methods are below:

| r |    | βᵣ  |      |     |      |     |     |    |
| - | -- | --- | ---- | --- | ---- | --- | --- | -- |
| ₆ | ₅  | ₄   | ₃    | ₂   | ₁    | ₀   |     |    |
|   |    | 2   | 2    |     | -3   | -4  | -1  |    |
| 3 | 6  | 11  | 18   | 9   | 2    |     |     |    |
| 4 | 12 | -25 | -48  |     | -36  | -16 | -3  |    |
| 5 | 60 | 137 | 300  | 300 | 200  | 75  |     | 12 |
| 6 | 60 | 147 | -360 | 450 | -400 | 225 | -72 | 10 |

Personally, I prefer to rewrite (25) as

yₙ₊₁ + a₀yₙ + a₁yₙ−₁ + ... + aᵣyₙ−ᵣ = f(tₙ₊₁, yₙ₊₁).

| Order | b  | a₀  | a₁ | a₂  | a₃ |    |    |
| ----- | -- | --- | -- | --- | -- | -- | -- |
| 1     | 1  | -1  |    |     |    |    |    |
|       | 2  | 2   | -4 | 1   |    |    |    |
|       | 3  | 3   | 3  |     |    |    |    |
| 3     | 6  | -18 | 9  | -2  |    |    |    |
|       | 11 | 11  |    | 11  | 11 |    |    |
| 4     | 12 | -48 | 36 | -16 | 3  |    |    |
|       |    | 25  | 25 |     | 25 | 25 | 25 |

We can use the Newton’s formula to derive the backward differentiation formula for the ODE u′ = f(t, u). Recall that for a function g(t), if we know its value at t = tₙ₊ᵣ, tₙ₊ᵣ−₁, ..., tₙ,






we can define the interpolation polynomial of degree r

pr(t) = g[tn+r] + gtn+r, tn+r−1 + ... + gtn+r, ..., tn · · · (t − tn+r).

Then g(t) − pr(t) = g(r+1)(ξ)(t − tn+r) · · · (t − tn). (26)

for some number ξ that may depend on t. By taking d on both sides of the above equation dt and then plugging in t = tn+r, we get

d g(tn+r) − (g[tn+r, tn+r−1] + ... + gtn+r, ..., tn · · · (tn+r − tn+r−1))

= g(r+1)(ξ)(tn+r − tn+r−1) · · · (tn+r − tn+r−k). (27)

When the step size is uniform, we obtain the backward differentiation formula. In the derivation above, we have used the fact that when g is C²([0, T]), g(r+1)(ξ(t)) in (26) is differentiable in t and its derivative is bounded on [0, T], even though ξ(t) may be not continuous in t. To prove this claim, note that (26) implies

1 g(r+1)(ξ(t)) = f(t) − f(tn+r) with f(t) = g(t) − pr(t)

(r + 1)! (t − tn+r) · · · (t − tn)

and we have inserted an f(tn+r) for free since f(tn+r) = 0. We want to look at the behaviour of (f(t)−f(tn+r)) at tn+r. Using Taylor expansion

f(t) = f(a) + f′(a)(t − a) + ... + f(m)(a)(x − a)m + 1 t f(m+1)(s)(t − s)mds

with a = tn+r and m = 1, we get

1 (r+1) f′(tn+r)(t − tn+r) + t t f′′(s)(t − s)ds

(1)!g (ξ(t)) = ( − ) · · ·n+r − .

r + t tn+r (t tn)

So, we only need to show that h(t) def 1 t f′′( )( − ) differentiable

= t−tn+r tn+r s t s ds is and has bounded derivative at tn+r. This is true since

tt f′′(s)ds (t − tn+r) − tt f′′(s)(t − s)ds

h′(t) = n+r (t − tn+r)² n+r

and t f′′(s)(t − s)ds mean value theorem f′′(θ) t ( − ) f′′(θ)1 ( − )²

tn+r = tn+r t s ds = 2 t tn+r.






We are done.

Here is an application of (27). Take r = 2,

d g(tₙ₊₁) − g(tₙ₊₂) g(tn)−g(tn+1) − g(ᵗⁿ⁺¹)−ᵍ(ᵗⁿ⁺²)

dt g(tⁿ⁺²) −     −∆ᵗ−

+ −∆t          −2∆ᵗ

−∆t            ∆t

= d g(tₙ₊₂) − g(tₙ₊₂)∆ g(tₙ₊₁) + 1 g(tₙ₊₂) − 2g(tₙ₊₁) + g(tₙ)

dt 2 ∆t

= d g(tₙ₊₂) − 3g(tₙ₊₂) − 4g(tₙ₊₁) + g(tₙ)

dt 2∆t

= g(3)(ξ)2∆t².

# 5.11 Homework 10

Based on textbook: Tim Sauer, Numerical Analysis, 2nd edition

1. Page 312, 6.3 Exercises, 1(a), 3(b), 4(b)
2. Page 335, 6.6 Exercises, 1(a)
3. Page 345, 6.7 Exercises, 1(b)

# 5.12 Computer Project 3

1. Sauer, Page 313, 6.3 Computer Problems, 1(a,d)
2. Sauer, Page 336, 6.6 Computer Problems, 1(a)
3. Sauer, Page 346, 6.7 Computer Problems, 5. The exact solution is y = tan(t) for y₀ = 0 and y = tan(t + π) for y₀ = 1.

# 5.13 Stability and convergence

To discuss the convergence of a numerical method for the ODE

u′ = f(t, u), u(0) = η, (28)

we focus on a fixed (but arbitrary) time T > 0 and consider the error ET/∆t = UT/∆t − u(T).

Here we assume we will choose ∆t so that N = T/∆t is an integer. The method converges if E = UT/∆t − u(T) goes to zero as ∆t → 0, i.e.,

∆ → lim UN = u(T). (29)






For an r-step method, we need r starting values. These values will typically depend on ∆t, and to make this clear we will write them as

U0(∆t), U1(∆t), · · · , Ur−1(∆t).

While these will generally approximate u(t) at the times t0 = 0, t1 = ∆t,..., tr−1 = (r − 1)∆t, each of these times approaches 0 as ∆t → 0. So the weakest condition we might put on our starting values is that

limk→0 Um(∆t) = η for m = 0, 1, ..., r − 1. (30)

# Definition 1

An r-step method is said to be convergent if applying the method to any ODE u′ = f(t, u), u(0) = η, with f(t, u) Lipschitz continuous in u, and with any set of starting values satisfying limk→0 Um(∆t) = η for m = 0, 1, ..., r − 1, we obtain

lim∆t→0, N∆t=T UN = u(T) for any fixed time T > 0 at which the ODE has a unique solution.

For a method to be convergent, we can prove that the method must be consistent (i.e., LTE → 0 as ∆t → 0) and also zero-stable, as described later.





# 5.13.1 The test problem

Most of the theory presented below is based on examining what happens when a method is applied to a simple scalar linear equation of the form

u′(t) = λu(t) + g(t) (31)

with initial condition u(0) = η. The solution is given by

u(t) = eλtη + ∫0t eλ(t−τ)g(τ)dτ.




# 5.13.2 One-step methods

If we apply forward Euler method to (30), we obtain

Un+1 = Un + ∆t (λUn + g(tn)).

The LTE is given by

τn = u(tn+1) − u(tn) − (λu(tn) + g(tn))

= u′(tn) + 1/2 ∆tu′′(tn) + O(∆t²) − u′(tn) = 1/2 ∆t u′′(tn) + O(∆t²). (32)

Subtracting this from 0 = Un+1 - Un - (λUn + g(tn)), we obtain (En = Un - u(tn))

∆t

-τn = En+1 - En - λEn.

∆t

Again, this is the same as the numerical scheme but with g replaced by -τ. The above equation can be rewritten as

En+1 = (1 + ∆tλ)En - ∆tτn n-1 - n-1 - n (33)

= (1 + ∆tλ)[(1 + ∆tλ)E ∆tτ ] ∆tτ

= · · · n+1

= (1 + ∆tλ)n+1E0 - ∆t Σm=1n+1 (1 + ∆tλ)n+1-m τm-1.

Note that

for any λ ∈ C. Hence for m = 1 + ∆tλ ≤ 1 + ∆t|λ| ≤ e∆t|λ|

0, 1, 2, ..., n + 1,

|(1 + ∆tλ)n+1-m| ≤ e(n+1-m)∆t|λ| ≤ eT|λ|.

Going back to (33), we have

|En+1| ≤ e|λ|T |E0| + (n + 1)∆t ≤ max |τm-1| ≤ e|λ|T |E0| + T||τ||∞ (34)






1 m≤n+1

where τ = [τ0, τ1, τ2, ..., τn]T. By (32), we know ||τ||∞ ≤ ∆t. If we take U0 = η, E0 = 0.

Hence

|En+1| ≤ C∆t. (35)

Note where stability comes into the picture. The one-step error Ln = ∆tτn introduced in the m-th step contributes the term (1 + ∆tλ)n+1-m Lm-1 to the global error. The fact that (1 + ∆tλ)n+1-m ≤ eT|λ| is uniformly bounded as ∆t → 0 allows us to conclude that each contribution to the final error can be bounded in terms of its original size as a one-step error.





# 5.13.3 Forward Euler method on nonlinear problems

Forward Euler method on u' = f(u) takes the form

Un+1 = Un + ∆tf(Un)

and the truncation error is defined as

τn = u(tn+1) − u(tn) − f(u(tn)) = 1 ∆t u''(tn) + O(∆t²),

just as in the linear case. So u(tₙ₊₁) = u(tₙ) + ∆tf(u(tₙ)) + ∆tτⁿ and Eⁿ = Uⁿ − u(tₙ) satisfies

Eⁿ⁺¹ = Eⁿ + ∆t (f(Uⁿ) − f(u(tₙ))) − ∆tτⁿ. (36)

Now, we assume that f satisfies the Lipschitz condition with Lipschitz constant L, i.e.,

|ᶠ(ᵃ) − f(ᵇ)| ≤ L|ᵃ − b| for any a, b ∈ R.

Then from (36), we obtain

|ᴱⁿ⁺¹| ≤ |ᴱⁿ| + ∆ᵗᴸ|ᴱⁿ| + ∆ᵗ|τⁿ| ≤ (1 + ∆ᵗᴸ)|ᴱⁿ| + ∆ᵗ|τⁿ|

≤ (1 + ∆ᵗᴸ)[(1 + ∆ᵗᴸ)|ᴱⁿ−¹| + ∆ᵗ|τⁿ−¹|] + ∆ᵗ|τⁿ| ≤ · · ·

n+1

≤ (1 + ∆ᵗᴸ)ⁿ⁺¹|ᴱ⁰| + ∆ᵗ m=1(1 + ∆tλ)ⁿ⁺¹−ᵐ |τᵐ−¹|. (37)

Using the same steps as in obtaining (34) and (35), we obtain

|ᴱⁿ⁺¹| ≤ eᴸᵀᵀ∥τ∥∞ = O(∆ᵗ) (38)

for any n satisfying (n + 1)∆t ≤ T.



# 5.13.4 General one-step methods

A general explicit one-step methods takes the form

Un+1 = Un + ∆tΨ(tn, ∆t, Un) (39)

for some function Ψ which depends on f of course. We will assume that Ψ is continuous in ∆t uniformly for (t, u) ∈ R² and Lipshitz continuous in U, with Lipschitz constants L′ that is generally related to the Lipschitz constant of f.




# Example 20

For the two stage Runge-Kutta method *U* = Uⁿ + 1 ∆t f(Uⁿ), Uⁿ⁺¹ = Uⁿ + ∆t f(U**), we have

*Ψ(t, ∆t, u) = f(u) + 1 ∆t f(u).*

If *f is Lipschitz continuous with Lipschitz constant L, then *Ψ* has Lipschitz constant L′ = L + 1 ∆t L².*

If *lim∆ₜ→₀ Ψ(t, ∆t, u) = Ψ(t, 0, u) uniformly for (t, u) ∈ R² and Ψ(t, 0, u(t)) = f(u(t))*, one can prove that one-step method (39) is consistent.

To prove that, take any *tₙ ≤ T, when ∆t → 0, we choose n → ∞ so that tₙ* is fixed,

*τⁿ = u(tₙ + ∆t) − u(tₙ) − Ψ(tₙ, ∆t, u(tₙ)) ∆t*

→ *u′(tₙ) − Ψ(tₙ, 0, u(tₙ)) = u′(tₙ) − f(u(tₙ)) = 0*

Note that by our assumption, the convergence of *τⁿ → 0 is uniformly for n ∈ {0, 1, ..., T/∆t−1}. The τⁿ introduced above allows us to derive (with Eⁿ = Uⁿ − u(tₙ)*)

*Eⁿ⁺¹ = Eⁿ + ∆t (Ψ(tₙ, ∆t, Uⁿ) − Ψ(tₙ, ∆t, u(tₙ))) − ∆t τⁿ.*

With the Lipschitz assumption on Ψ, we obtain

*|Eⁿ⁺¹| ≤ |Eⁿ| + ∆t L′ |Eⁿ| + ∆t |τⁿ|*

and then we can repeat the argument in (37) to obtain

*|Eⁿ⁺¹| ≤ eL′T |E⁰| + T ||τ||∞ → 0*

since *||τ||∞ = max1≤i≤T/∆t−1 τⁱ → 0 as ∆t → 0 and E⁰ = 0.*

Indeed, we have proved Theorem 6.4 in Sauer’s book:





# Theorem 2

Assume that f(t, u) has a Lipschitz constant L for the variable y and that the value u(tₙ) of the solution of the initial value problem

u′ = f(t, u), u(0) = u₀, t ∈ [0, T]

is approximated by Uⁿ from a one-step ODE solver with Lipschitz constant L′ and local truncation error τⁱ (which is related to the exact solution, not the numerical solution). Then

∣ᴱᵏ ∣ def ∣ k − ( )∣ ≤ L′T ∣ 0∣ ∥ ∥

= U u tₖ e E + T τ ∞

for all k ≤ T/∆t.



# 5.14 Zero stability of linear multistep methods

We begin with an example showing a consistent LMM that is not convergent. Except this example, §5.14 won’t be tested in the exam. But the conclusion in Theorem 2 of Dahlquist is famous and should be remembered. §5.15 to §5.17 won’t be tested as well. But for practical purpose, I would suggest you to remember the definition of stability region and how the stability region of Forward Euler method is derived.




# Example 21

The LMM

Uⁿ⁺² − 3Uⁿ⁺¹ + 2Uⁿ = −∆tf(Uⁿ)

has a LTE given by

τⁿ = 1 (u(tₙ₊₂) − 3u(tₙ₊₁) + 2u(tₙ)) + f(u(tₙ)) = 5 ∆tu′′(tₙ) + O(∆t²),

∆t

so the method is consistent and “first order accurate.”

But in fact the global error will not exhibit first order accuracy, or even convergence, in general. This can be seen in a simple example

u′(t) = 0, u(0) = 0

with exact solution u(t) = 0. The numerical scheme takes the form

Uⁿ⁺² − 3Uⁿ⁺¹ + 2Uⁿ = 0. (40)

The following table shows results obtained by applying this method with starting data U⁰ = 0 and U¹ = ∆t. Since U¹(∆t) → 0 as ∆t → 0, this is valid starting data in the context of Definition 1. Similar blowing up behaviour would be seen if we applied this method to an arbitrary equation u′ = f(u) and used any one-step method to compute U¹ from U⁰.

| N  | Uᴺ        |
| -- | --------- |
| 5  | 6.2       |
| 10 | 1023      |
| 20 | 5.4 × 10⁴ |

Table 10: Solution Uᴺ to (40) with U⁰ = 0, u¹ = ∆t and various values of ∆t = 1/N.

The linear difference equation (40) can be solved explicitly for Uⁿ:

Uⁿ = 2U⁰ − U¹ + 2ⁿ U¹ − U⁰. (41)

One can check that the above equation satisfies (40) and also the starting values. Since u(t) = 0, the error is Eⁿ = Uⁿ and we see that any initial errors in U¹ or U⁰ are magnified by a factor of eⁿ in the global error (except in the special case U¹ = U⁰). This exponential growth of the error is the instability that leads to nonconvergence.






# 5.14.1 Solving linear difference equations

We briefly review one solution technique for linear difference equations

r αjUn+j = 0. (42)

We will hypothesize that this equation has a solution of the form

Un = ξn. (43)

for some value of ξ (here ξn is the n-th power). Plugging this into (42) gives

r αjξn+j = 0

j=0

or

r αjξj = 0

j=0

after dividing by ξn. We see that (43) is a solution of (42) if ξ satisfies (44), i.e., if ξ is a root of the polynomial (called characteristic polynomial)

r ρ(ξ) = αjξj.

j=0

Since (42) is linear, any linear combination of solutions is again a solution. If ξ1, .., ξr are distinct roots of ρ(ξ), then a general solution of (42) has the form

Un = c1ξn + c2ξn + · · · + crξn,

where c1, ..., cr are arbitrary constants.






Now, we will look for a particular solution satisfying given initial conditions U0, U1, · · · , Ur−1.

Hence we require c1, ..., cr to satisfy the r × r linear system

c1 + c2 + · · · + cr = U0,
c1ξ1 + c2ξ2 + · · · + crξr = U1,
c1ξr−1 + c2ξr−1 + · · · + crξr−1 = Ur−1.

Example 22 The characteristic polynomial of the difference equation (40) is

ρ(ξ) = ξ² − 3ξ + 2 = (ξ − 1)(ξ − 2)

with roots ξ1 = 1, ξ2 = 2. The general solution has the form Un = c1 + c2en and solving for c1 and c2 from U0 and U1 gives (41).

This example indicates that if ρ(ξ) has any roots that are greater than one in modulus, the method will not be convergent. It turns out that the converse is nearly true: if all the roots have modulus no greater than one, then the method is convergent, with one provision. There must be no repeated roots with modulus equal to one. The next two examples illustrate this.

If the roots are not distinct, say, ξ1 = ξ2 for simplicity, then ξn and ξn are not linearly independent and the Un given by (47), while still a solution, is not the most general solution.

The system (46) would be singular in this case. As shown in the next example, in addition to ξn, there is also a solution of the form nξn and the general solution has the form

Un = c1ξn + c2nξn + c3ξn + · · · + crξn.

If in addition ξ3 = ξ1, then the third term would be replaced by c3n²ξn. Similar modifications are made for any other repeated roots.






# Example 23

Verify that

Uⁿ = c₁ξⁿ + c₂nξⁿ + c₃ξⁿ + · · · + cᵣξⁿ,

(48)

is a general solution to

r αjUⁿ⁺ʲ = 0

(49)

when the characteristic polynomial has the form ρ(ξ) = ∑j=0r αjξj = α0(ξ−ξ1)²(ξ−ξ3) · · · (ξ−ξr) with ξi = ξj when i = j.

Proof: We just need to verify that Uⁿ = c₂nξⁿ is a solution to (49). We need to prove that

r αjc₂(n + j)ξⁿ⁺ʲ = 0

(50)

or equivalently

0 = ∑j=0r αj(n + j)ξj = n ∑j=0r αjξj + ∑j=0r αjjξj.

Since ξ1 is a double root of ρ(ξ), it satisfies ρ(ξ1) = 0 = ρ′(ξ1). Hence

∑j=0r αjξj = 0 and ∑j=1r αjjξj⁻¹ = 0.

Multiplying the last equation by ξ, we obtain ∑j=0r αjjξj = 0. This proves (50).

# Example 24

Applying the consistent LMM

Uⁿ⁺² − 2Uⁿ⁺¹ + Uⁿ = 1 ∆t f(Uⁿ⁺²) − f(Uⁿ)

to the difference equation u′(t) = 0 gives the difference equation

Uⁿ⁺² − 2Uⁿ⁺¹ + Uⁿ = 0.

The general solution is Uⁿ = c₁ + c₂n = U⁰ + n(U¹ − U⁰), again, we see that the solution, and hence the error, grows with n.





# Example 25 Applying the consistent LMM

Un+3 − 2Un+2 + 5 Un+1 − 1 Un = 1 ∆t f(Un)



# Theorem 3 (Dahlquist)

For LMMs applied to the initial value problem for u′(t) = f(t, u(t)),

consistency + zero-stability ⇔ convergence.

The proof can be found in the first volume of the book of Hairer, Norsett, and Wanner. (The proof is definitely not required for the test.)

Condition (24) imply that a consistent LMM always have one root equal to 1. This root is called the principal root. Hence a consistent one-step LMM (such as Euler, backward Euler, trapezoidal) is certainly zero-stable (since ρ(ξ) = ξ − 1). Then the Dahlquist theorem tells us they converge. This gives another proof of what we have proved before that any consistent one-step method (that is a Lipschitz continuous) is convergent.

We can think of zero-stability as meaning “stable in the limit as ∆t → 0.” Although a consistent zero-stable method is convergent, it may have other stability problems that show up if the time step ∆t is chosen too large in an actual computation.




# 5.15 A zero-stable method may perform badly if ∆t is large

Example 27 Consider the ODE

u′(t) = − sin(t), u(0) = 1.

The exact solution is u(t) = cos(t). Suppose we use forward Euler to solve it up to time T = 2. The LTE is

τ(t) = 1 ∆tu′′(t) + O(∆t²) = − 1 ∆t cos(t) + O(∆t²).

Since the function f(t) = − sin(t) is independent of u, it is Lipschitz continuous with Lipschitz constant L = 0, and so the error estimate shows that

|ᴱⁿ⁺¹| ≤ T∥τ∥∞ ≤ 2 1 ∆ᵗ = ∆t.

Suppose we want to compute a solution with |E| ≤ 10−³. Then we should be able to take ∆t = 10−³ and obtain a suitable solution after T/∆t = 2000 time steps. Indeed, calculating using ∆t = 10−³ gives a computed value U²⁰⁰⁰ = −0.415692 with an error E²⁰⁰⁰ = 0.4548 × 10−³.

Example 28 Consider the ODE

u′(t) = λ(u − cos(t)) − sin(t), u(0) = 1

where λ is some constant. The exact solution is u(t) = cos(t). Suppose we take λ = −10 and use forward Euler to solve it up to time T = 2. The LTE remains unchanged: τ(t) = 1 ∆tu′′(t) + O(∆t²) = − 1 ∆t cos(t) + O(∆t²). If we take ∆t = 10−3, we get U²⁰⁰⁰ = −0.416163 with an error E²⁰⁰⁰ = 0.161 × 10−4. We are again successful.

| ∆t       | error        |
| -------- | ------------ |
| 0.001000 | 0.145252E+77 |
| 0.000976 | 0.588105E+36 |
| 0.000950 | 0.321089E−06 |
| 0.000800 | 0.792298E−07 |
| 0.000400 | 0.396033E−07 |

Table 11: λ = −2100. Errors in the computed solution using forward Euler method for different values of the time step ∆t. Note the dramatic change in behavior of the error for ∆t &#x3C; 0.000952.






# Analysis of Forward Euler Method

Suppose we take λ = −2100 and use forward Euler to solve it up to time T = 2. The LTE remain unchanged: τ(t) = 1 ∆tu′′(t)+O(∆t²) = − 1 ∆t cos(t)+O(∆t²). If we take ∆t = 10−3, we get U2000 = −0.2453 × 277 of 277 10 with an error magnitude 10. The computation behaves in an “unstable” manner, with an error that grows exponentially in time.

Since the method is zero-stable and f(t, u) is Lipschitz continuous in u with Lipschitz constant L = 2100, we know the method is convergent. We can use a smaller time step ∆t and obtain Table 11. Clearly something dramatic happens between the value ∆t = 0.00976 and ∆t = 0.000952. For smaller values of ∆t, we get very good result, whereas for larger values of ∆t, there is no accuracy whatsoever.

The equation (58) is a linear equation of the form (31) and so the relation (33) applies:

En+1 = (1 + ∆tλ)En − ∆tτn where τn = τ(tn) from (56). For the case λ = −2100 and ∆t = 10−3, 1 + ∆tλ = −1.1 and so we expect the local error introduced in step m to grow by a factor of (−1.1)n−m by the end of n steps. See (33). After 2000 steps, we expect the truncation error introduced in the first step to have grown by a factor of roughly (−1.1)2000 ≈ 1082, which is consistent with the error actually seen.

For the case λ = −10 and ∆t = 10−3, 1 + ∆tλ = 0.99, causing a decay in the effect of previous errors in each step. This explains why we got a good result or in fact even a better result than the case when λ = 0.

Returning to the case λ = −2100, we expect to observe exponential growth in the error for any value of ∆t greater than −²/λ = 0.00095238 (hence 1 + ∆tλ &#x3C; −1 and recall λ = −2100 &#x3C; 0). This explains what we observed in Table 11.





# 5.16 Stability region

Even though we know a consistent and zero-stable method convergences, its performance is only known to be good when ∆t → 0. The previous example enforces us to consider how to select a practical ∆t (which is a finite number) in real computations.



# Definition 3 (stability region)

It is the subset of the complex plane consisting of those ∆tλ ∈ C for which the numerical method produces bounded solutions when applied to the scalar linear model problem u′ = λu with positive time step ∆t.

When applying a numerical method to solve u′ = f(u) ≈ f(η) + f′(η)(u − η) with initial condition u(0) = η, we should have a rough idea of the size of f′(η) and then we chose ∆t to ensure f′(η)∆t lies inside the stability region.



Why should we only consider the simple model problem

u′(t) = λu(t) (59)




and why should we consider ∆tλ together

and why should it be complex number?

Allowing λ to be complex comes from the fact that in practice we are usually solving a system of ODEs

u′ = Au. (60)

Supposing A ∈ Rⁿ×ⁿ can be diagonalized, A = PΛP−¹. 15 Let v = P−¹u, then (60) can be rewritten as

v′ = Λv, (61)

and hence every component is of the form (59). But λi ∈ C even if we start from a real matrix A.

Maybe (59) seem to be too simple. But the simplicity makes the detailed analysis possible and at the same time the result is still very revealing.






# Example 29

The forward Euler method for (59) is

Un+1 = (1 + ∆tλ)Un. (62)

The amplification factor is (1 + ∆tλ). We recognize that it is the product z = ∆tλ that matters and the stability region is {z ∈ C : |1 + z| ≤ 1}.






# 5.16.1 Stability region for linear multistep methods

Recall the multi-step method

r r

αjUn+ʲ = ∆t βjf(tₙ₊j, Un+ʲ). (63)

j=0 j=0

15One realizes that if P = [p1, p2, ..., pn] and Λ = diag(λ1, ..., λn), then AP = PΛ implies Api = λipi.






# Figure 18: Stability region for

- (a) forward Euler
- (b) backward Euler
- (c) trapezoidal
- (d) midpoint (a segment on imaginary axis)

| Forward Euler | Backward Euler |
| ------------- | -------------- |
| 2             | 1.5            |
| 1             | 1              |
| 0.5           | 0.5            |
| 0             | 0              |
| -0.5          | -0.5           |
| -1            | -1             |
| -1.5          | -1.5           |

(a) $-\frac{3}{2}$ -2 -1 0 1

(b) -2 0 1 2 3

| Trapezoidal | Midpoint |
| ----------- | -------- |
| 2           | 1.5      |
| 1           | 1        |
| 0.5         | 0.5      |
| 0           | 0        |
| -0.5        | -0.5     |
| -1          | -1       |
| -1.5        | -1.5     |

(c) $-2$ -1 0 1 2

(d) $-2$ -1 0 1 2

and recall the characteristic polynomials ρ(ξ) and σ(ξ) for the LMM:

ρ(ξ) = ∑j=0r αjξj and σ(ξ) = ∑j=0r βjξj. (64)

If (63) is applied to u′ = λu, we get αjUn+ j = ∆t and βjλUn+ j = z βjUn+ j.

Once again, only z def ∆ difference = tλ matters. This is a linear equation that we have studied before. Recall that if its characteristic polynomial (which is π(ξ; z) = ρ(ξ) − zσ(ξ))






satisfies the so called root condition, then the solution to the difference equation will remain bounded.

More precisely, the stability region for LMM method (63) is the set of points z ∈ C for which the polynomial of ξ (z is a parameter while ξ is the variable)

π(ξ; z) = ρ(ξ) − zσ(ξ) satisfies the root condition

|ξj| ≤ 1 for j = 1, 2, ..., r, (65)

If ξj is a repeated root, then |ξj| &#x3C; 1. (66)

Here ξj are the roots of π(ξ; z).






# Example 30

If we apply backward Euler to u′ = λu, we get Uⁿ⁺¹ − Uⁿ = ∆tλUⁿ⁺¹ and hence Uⁿ⁺¹ = −1 Uⁿ.

−1 ≤ 1 implies ∆tλ ∈ {ᶻ : |ᶻ − 1| ≥ 1} which in particular includes the whole left complex plane.

Alternative, we can use π(ξ; z) = ρ(ξ) − zσ(ξ) = ξ − 1 − zξ. We obtain ξ₁ = 1/(1 − z). The root condition requires |1 − z| ≥ 1.






# Example 31

For the trapezoidal method Un+1−Un = 1 (f(Un+1) + f(Un)), we have

Un+1 − Un = 1 λ Un+1 + Un

∆t 2

and π(ξ; z) = (ξ − 1) − 1 z(ξ + 1). Hence

ξ1 = (1 + 1 z) / (1 − 1 z).

It can be shown that |ξ1| ≤ 1 ⇔ Re(z) ≤ 0 where Re(z) is the real part of z. Alternatively, Un+1 = (1 + 1z) Un with z = ∆tλ. The amplification factor is (1 + 1z) / (1 − 1z) and we want |(1 + 1z)| ≤ 1.





# Example 32

For the midpoint method *Un+1 - Un-1 = f(Un)*, we have

*Un+1 - Un-1 = λUn / 2∆t*

and *π(ξ; z) = (ξ² - 1) - 2zξ. Hence ξ1,2 = z ± √(z² + 1)*.

It can be shown that if *z is a pure imaginary number of the form z = iα with |α| &#x3C; 1, then |ξ1| = |ξ2| = 1 and ξ1 = ξ2 and hence the root condition is satisfied. For other z*, one can show that the root condition is not satisfied.



# Example 33

Figures 19 and 20 show the stability regions for the r-step Adams-Bashforth and Adams-Moulton methods for various values of r. For r-step method, the polynomial π(ξ; z) has degree r and there are r roots. Determine the values of z for which the root condition is satisfied does not appear simple. However, there is a simple technique called the boundary locus method that is discussed in Section 7.6.1 of the book of LeVeque.



# Stability region of Adams-Bashforth 3 step method

| 1.5 | 1  | 0.5  | 0 | -0.5 | -1 | -1.5 |
| --- | -- | ---- | - | ---- | -- | ---- |
| -2  | -1 | -1.5 |   |      |    |      |




# Stability region of Adams-Bashforth 4 step method

| 1.5 | 1 | 0.5 | 0 | -0.5 | -1 | -1.5 | -2 | $-\frac{3}{4}$ |
| --- | - | --- | - | ---- | -- | ---- | -- | -------------- |





# Stability region of Adams-Bashforth 5-step method

| 1.5 | 1 | 0.5 | 0 | -0.5 | -1 | -1.5 | -2 | $-\frac{1}{2}$ |
| --- | - | --- | - | ---- | -- | ---- | -- | -------------- |

Figure 19: Stability region for some Adams-Bashforth methods. The shaded region just to the left of the origin is the stability region.





# 5.17 A-stability and A(α)-stability

For reasons that we will see when solving time dependent PDEs, it is useful to have a method whose stability region contains the entire left half-plane of the complex plane. Then if the λ in u′ = λu has negative real part, then any time step ∆t would be allowed. For example, we have shown in Examples 30 and 31, backward Euler and trapezoidal methods have this property.



# Definition 4

An ODE method is said to be A-stable if its stability region contains the entire left half-plane {z ∈ C : Re(z) ≤ 0}. For LMMs, it turns out this is quite restrictive. A theorem of Dahlquist states that any A-stable LMM is at most second order accurate, and in fact that the trapezoidal method is the A-stable method with smallest truncation error. Higher order A-stable implicit Runge-Kutta methods do exist, including diagonal implicit Runge-Kutta method. Because of the theorem of Dahlquist, Gear decided to relax this “entire left half-plane” requirement and introduced what he called A(α)-stability.




# Definition 5

Let arg(z) represent the argument of z with arg(z) = π on the negative real axis, and if the wedge π − α ≤ arg(z) ≤ π + α is contained in the stability region, then we say the method is A(α) stable.





# Stability region of Adams-Moulton 2-step method

| 3   | 2  | 1  | 0  | -1 | -2 | -3 |   |   |
| --- | -- | -- | -- | -- | -- | -- | - | - |
| (a) | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 |




# Stability region of Adams-Moulton 3-step method

| 3   | 2  | 1  | 0  | -1 | -2 | -3 |   |
| --- | -- | -- | -- | -- | -- | -- | - |
| (b) | -6 | -5 | -4 | -3 | -2 | -1 | 0 |




# Stability region of Adams-Moulton 4-step method

| 3   | 2  | 1  | 0  | -1 | -2 | -3 |   |   |
| --- | -- | -- | -- | -- | -- | -- | - | - |
| (c) | -6 | -5 | -4 | -3 | -2 | -1 | 0 | 1 |




# Stability region of Adams-Moulton 5-step method

Figure 20: Stability region for some Adams-Moulton methods.

Gear then discovered the backward differentiation methods that we have introduced before (so they are also called Gear’s methods). It turns out that the BDF methods are only zero-stable for r ≤ 6. When r ≤ 6, BDF methods are A(α)-stable for the following value of α:

| r | α     |
| - | ----- |
| 1 | 90°   |
| 2 | 90°   |
| 3 | ≈ 86° |
| 4 | ≈ 73° |
| 5 | ≈ 51° |
| 6 | ≈ 17° |




# 20 Stability region of 1-step BDF method

# 20 Stability region of 2-step BDF method

| 15    | 10 | 5  | 0  | -5 | -10 | -15 |
| ----- | -- | -- | -- | -- | --- | --- |
| $-10$ | 0  | 10 | 20 | 30 |     |     |




# 20 Stability region of 3-step BDF method

# 20 Stability region of 4-step BDF method

| 15       | 10 | 5 | 0 | -5 | -10 | -15 |
| -------- | -- | - | - | -- | --- | --- |
| $--0$ 0  |    |   |   |    |     |     |
| 10 20 30 |    |   |   |    |     |     |




# 20 Stability region of 5-step BDF method

# 20 Stability region of 6-step BDF method

| 15    | 10 | 5  | 0  | -5 | -10 | -15 |
| ----- | -- | -- | -- | -- | --- | --- |
| $-20$ | 0  | 10 | 20 | 30 |     |     |
| $-0$  | 0  | 10 | 20 | 30 |     |     |

Figure 21: Stability region for the BDF methods.




# 6 Numerical Methods in Linear Algebra

In addition to the textbook by Sauer, a standard reference for topics in this chapter is *Numerical Linear Algebra* by Trefethen and Bau. Some parts of the notes are based on this book.





# 6.1 Direct methods for solving linear system of equations

# 6.1.1 Gaussian elimination

Consider the system

3x1 + 5x2 = 9      (1)

6x1 + 7x2 = 4

It can be written as Ax = b in matrix form, or

| 3 | 5 | x1 | = | 9 |
| - | - | -- | - | - |
| 6 | 7 | x2 | = | 4 |

A is called coefficient matrix and b is called right hand side vector. There are three operations that can be applied to a linear system of equations that yield an equivalent system, meaning one that has the same solutions:

1. Swap two equations;
2. Add a multiple of one equation to another;
3. Multiply an equation by a nonzero constant.

For equation (1), we manipulate the augmented matrix [A|b]

| 3 | 5 | | | 9 |
| - | - | - | - |---|
| 6 | 7 | | | 4 |

R2 ← (-2) × R1 + R2

| 3 | 5  | | | 9   |
| - | -- | - | --- |---|
| 0 | -3 | | | -14 |





# Gaussian Elimination

When the coefficient matrix is ‘upper-triangular, we can backsolve for the solution, starting at the bottom. This whole process is called Gaussian elimination.





# 6.1.2 LU decomposition

Note that the process we have done can be characterized as we left multiply

| 3 | 5 |
| - | - |
| 6 | 7 |

by

| -1 | 0 |
| -- | - |
| 2  | 1 |

to obtain

| 3 | 5  |
| - | -- |
| 0 | -3 |

To connect this matrix multiplication to the step R2 R1 + R2, we have to recall how we do the matrix multiplication with row manipulations: The product can be viewed as being computed through two steps

1. 1 0 3 5 = 3 5 which is R1 ← 1 × R1 + 0 × R2, i.e., keep R1 untouched.
2. −* * 3 5 = * * which is R2 ← (−2) × R1 + 1 × R2.

Next, since −1 0 −1 = 1 0 , −1 0 3 5 = 3 5 implies

| 3 | 5 |
| - | - |

=

| 1 | 0 |
| - | - |

3 5.

| 6 | 7 |
| - | - |
| 2 | 1 |

0 −³

So, we have written the coefficient matrix as a product of a lower triangular matrix and an upper triangular matrix. This is called LU factorization. Here a matrix is called lower triangular if its entries above the diagonal are all zeros. Similarly we can define the upper triangular matrix.

So, the LU factorization is a “high-level” algebraic description of Gaussian elimination. Let us look at another example. Before we start, we note that we can generalize




# 1

−1 0 −1 = 1 0 to the following identity for the inverse of a specific kind of matrix (called Gauss matrix)

| 1    | · · · | 0   | 0 | · · · | 0 | 1    | · · · | 0  | 0 | · · · | 0 |
| ---- | ----- | --- | - | ----- | - | ---- | ----- | -- | - | ----- | - |
| .    | .     | .   | . | .     | . | .    | .     | .  | . | .     | . |
| .    | .     | .   | . | .     | . | .    | .     | .  | . | .     | . |
| .    | .     | .   | . | .     | . | .    | .     | .  | . | .     | . |
| Mₖ = | 0     | 1   | 0 | 0     | ⇒ | M−₁= | 0     | 1  | 0 | 0     | . |
| 0    | −βₖ₊₁ | 1   | 0 | k     | 0 | βₖ₊₁ | 1     | 0  | . | .     | . |
| .    | .     | .   | . | .     | . | .    | .     | .  | . | .     | . |
| 0    | · · · | −βₙ | 0 | · · · | 1 | 0    | · · · | βₙ | 0 | · · · | 1 |

Proof: By direct computation using block wise multiplication (see Section A.2 in the book) which means A₁₁ A₁₂ B₁₁ B₁₂ = A₁₁B₁₁ + A₁₂B₂₁ A₁₁B₁₂ + A₁₂B₂₂ A₂₁ A₂₂ B₂₁ B₂₂ A₂₁B₁₁ + A₂₂B₂₁ A₂₁B₁₂ + A₂₂B₂₂ whenever the size matches. □






# Example:

For the following system of equations, apply Gaussian elimination in tableau form to solve it and then find the LU factorization of the associated coefficient matrix A:

| x₁   | + | 2x₂ | − | x₃  | = | 3  |
| ---- | - | --- | - | --- | - | -- |
| −2x₁ | + | x₂  | − | 2x₃ | = | 3  |
| 3x₁  | + | x₂  | + | x₃  | = | −6 |

Solution: This is written in tableau form, and then apply the three operations we have listed before:

155






# 1

2 −¹ | 3

−2 1 −² | 3

3 1 1 | −⁶ − |

R2←(−2)R1+R2 1 2 1 3

→ −⁰ −3 ⁰ | −³

3 1 1 | −6

R3←3R1+R3 1 2 −1 | 3

→ 0 −3 ⁰ | −³

0 7 −2 | 3

R3← 7R2+R3 1 2 −1 | 3

3 − | −

→ 0 3 0 3 .

0 0 −2 | −⁴

Then we solve by backward substitution. So the solution is x3 = 2, x2 = 1, x1 = 3.

Now, we wan to translate the above manipulation into an LU decomposition of the coefficient matrix A. The above manipulation implies

| 1  | 0 | 0  | 1  | 0  | 0 | −1 | 0  | 0  |
| -- | - | -- | -- | -- | - | -- | -- | -- |
| 0  | 1 | 0  | 0  | 1  | 0 | 2  | 1  | 0  |
| 0  | 7 | 1  | 3  | 0  | 1 | 0  | 0  | 1  |
| 1  | 2 | −¹ | 1  | 0  | 0 | 0  | −1 | 1  |
| 2  | 1 | −² | −2 | 1  | 0 | 0  | 1  | 0  |
| −3 | 1 | ¹  | 0  | 0  | 1 | −3 | 0  | 1  |
| 0  | 0 | 1  | 2  | −1 | 2 | 1  | 0  | 0  |
| 0  | 0 | −3 | 0  | 0  | 1 | 0  | 0  | −2 |






# LU Decomposition

This is the LU decomposition.

| 1 | 0 | 0  | 1  | 0 | 0 | 1 | 0  | 0 |
| - | - | -- | -- | - | - | - | -- | - |
| 2 | 1 | −² | =  | 2 | 1 | 0 | 0  |   |
| 1 | 0 | 0  | −3 | 0 | 1 | 0 | −7 | 1 |
| 0 | 0 | −2 | 3  |   |   |   |    |   |

Remark: In the calculation, we have seen 2 1 0 0 1 0 0 1 0 = 0 0 1 −3 0 1 0 −7 1

It can be generalized to the following result:

| −³ | −7 | 1 | 3 |
| -- | -- | - | - |





# Theorem 1

Let (the non-trivial column is the kth column)

| 1  | ·  | · | 0 | 0  | · | · | 0 | ·   | · | 0 |
| -- | -- | - | - | -- | - | - | - | --- | - | - |
| .  | .  | . | . | .  | . | . | . | .   | . | . |
| .  | .  | . | . | .  | . | . | . | .   | . | . |
| .  | .  | . | . | .  | . | . | . | .   | . | . |
| Mₖ | 0  | 1 | 0 |    | 0 | . | . |     |   |   |
| 0  | βᵏ | 1 | 0 | .  |   | . | . | k⁺¹ |   |   |
| .  | .  | . | . | .  | . | . | . | .   | . | . |
| 0  | ·  | · | · | βᵏ | 0 | · | · | 1   |   |   |

Then,

| 1   | ·   | ·     | ·    | ·      | 0  | ·   | ·  | 0 | · | · |
| --- | --- | ----- | ---- | ------ | -- | --- | -- | - | - | - |
| ..  | .   | .     | .    | .      | .  | .   | .  | . | . | . |
| 0   | ·   | ·     | ·    | .      | .  | .   | .  | . | . | . |
| .   | 0   | ·     | .    | .      | .  | .   | .  | . | . | . |
| 0   | ·   | ·     | ·    | 1      | 0  | ·   | ·  | 0 | · | · |
| 0   | ·   | ·     | βᵏ−ʲ | 1      |    | 0   | ·  | · | · | · |
| .   | .   | k−ʲ⁺¹ | .    | .      | .  | .   | .  | . | . | . |
| M   | ·   | ·     | M    | .      | ·  | ·   | ·  | · | · | · |
| k−j | k−1 | k     | ·    | ·      | ·  | ·   | ·  | . | . | . |
| 0   | ·   | ·     | βᵏ−ʲ | βᵏ−ʲ⁺¹ | 1  |     | 0  | 0 | k | − |
| 0   | ·   | ·     | βᵏ   | j      | βᵏ | j+1 | βᵏ | 1 | 0 | 0 |
| .   | .   | k⁺¹   | .    | k⁺¹    | .  | k⁺¹ | .  | . | . | . |
| 0   | ·   | ·     | βᵏ−ʲ | βᵏ−ʲ⁺¹ | ·  |     | βᵏ | 0 | · | · |

Proof: It can be directly checked and the details are omitted. □




# Example:

Find the LU factorization of

| 3 | 1 | 2 |
| - | - | - |
| 6 | 3 | 4 |
| 3 | 4 | 5 |

# Solution:

| 3 | 1              | 2 | add −2 × row 1 to row 2 |   |   |   |
| - | -------------- | - | ----------------------- | - | - | - |
| 6 | 3              | 4 | → →                     | 0 | 1 | 0 |
| 3 | 4              | 5 | add −1 × row 1 to row 3 |   |   |   |
| → | add −3 × row 2 | → | 3                       | 1 | 2 |   |
| 0 | 1              | 0 | .                       | 0 | 0 | 3 |

The above manipulation implies

| 1 | 0  | 0 | 1  | 0 | 0 | 3 | 1 | 2 | 3 | 1 | 2 |   |
| - | -- | - | -- | - | - | - | - | - | - | - | - | - |
| 0 | 1  | 0 | −2 | 1 | 0 | 6 | 3 | 4 | = | 0 | 1 | 0 |
| 0 | −3 | 1 | −1 | 0 | 1 | 3 | 4 | 5 | 0 | 0 | 3 |   |





# 6.1.3 Operation counts

Now, let us count how many floating point operations (flops) are involved in the Gaussian elimination. Floating point operations include addition, subtraction, multiplication and division. For simplicity, we will only count how many multiplication/divisions are required in Gaussian elimination. This counting is important because it directly related to the CPU time of performing one Gaussian elimination. To begin, recall two facts about sum of integers which can be prove by induction.




# Lemma 1

1 + 2 + 3 + 4 + · · · + n = n(n + 1) (5)

1² + 2² + 3² + 4² + · · · + n² = n(n + 1)(2n + 1) . (6)

The following are steps in Gaussian elimination for a full matrix (if a number goes from ∗ to ·, it means its value has been changed.)

| \* | \* | \* | \* | \* |    |
| -- | -- | -- | -- | -- | -- |
| \* | \* | \* | \* | \* |    |
| \* | \* | \* | \* | \* |    |
| \* | \* | \* | \* | \* |    |
| \* | \* | \* | \* | \* |    |
| 0  | ·  | ·  | ·  | ·  |    |
| →  | \* | \* | \* | \* | \* |
| \* | \* | \* | \* | \* |    |
| \* | \* | \* | \* | \* |    |
| \* | \* | \* | \* | \* |    |
| 0  | ·  | ·  | ·  | ·  |    |
| →  | 0  | ·  | ·  | ·  |    |
| 0  | ·  | ·  | ·  | ·  |    |
| 0  | ·  | ·  | ·  | ·  |    |
| \* | \* | \* | \* | \* |    |
| 0  | ·  | ·  | ·  | ·  |    |
| →  | 0  | 0  | •  | •  | •  |
| →  | ·  | ·  | 0  | ⁰  | •  |

(7)

In the first step, we need to multiply the 1st row by − a²¹ and add it to the 2nd row. (We assume a is not zero in this section and later.) This step involves 1 division, n multiplications and n additions. (But following the textbook we ignore addition in our flops counting, because the number of addition/subtractions is very close to the number of multiplication/divisions. See the tutorial problem.) This step is illustrated by the following diagram:

| \* | \* | \* | \* | \* | \* | \*     | \*   | \* | \* |
| -- | -- | -- | -- | -- | -- | ------ | ---- | -- | -- |
| \* | \* | \* | \* | \* | \* | (n+1)f | lops | 0  | ·  |






Repeat this step n − 1 times, we obtain

| \* \* \* \* \*    | \* \* \* \* \* | \* \* \* \* \* |
| ----------------- | -------------- | -------------- |
| \* \* \* \* \* \* |                |                |
| \* \* \* \* \* \* |                |                |
| =                 | \* \* \* \* \* | \* \* \* \* \* |
| \* \* \* \* \* \* |                |                |
| \*                |                |                |

(n+1)(n−1)f lops 0 · · · ·

⇒ 0 · · · ·

0 · · · ·

0 · · · ·

Then we move on to the (n − 1) × (n − 1) sub-matrix formed by · in the last matrix above.

Now, n is reduced to n − 1. So we need ((n − 1) + 1)((n − 1) − 1) flops to reduce the · parts to the (n − 2) × (n − 2) sub-matrix formed by • in (7). Then we move on to the (n − 2) × (n − 2) sub-matrix. ...... We have n − 1 such steps. All together, we need (n + 1)(n − 1) + n(n − 2) + · · · + 4 × 2 + 3 × 1 flops to change a full matrix to an upper triangular matrix. To see how big is the above sum, we write it as n−1(i + 2)i = n−1 i2 + 2 n−1 i = (n − 1)n(2n − 1) + 2 (n − 1)n = n3 + n2 − 5n.

Now, it is easy to see that when n is large, the leading term dominates and the above sum ≈ n³. Now, here is a short cut to obtain ᵗʰⁱˢ n3 without using the formulas from Lemma 1: n−1(i + 2)i ≈ n(x + 2)xdx = x³ + x₂ x=n ≈ n3 + n2 ≈ n3.

This finishes the step of obtaining the upper triangular matrix. But to finish Gaussian elimination, we still need to use backward substitution to solve a system with an upper





Triangular Matrix

∗ ∗ ∗ ∗ ∗ | b₁

0 ∗ ∗ ∗ ∗ | b₂

0 0 ∗ ∗ ∗ | · .

0 0 0 ∗ ∗ | ·

0 0 0 0 ∗ | bₙ

To get xₙ = aᵇⁿ, we need 1 division. To get xₙ−₁ = bⁿ−¹−ᵃⁿ−1,nˣⁿ, we need 1 multiplication and 1 division. ...... To get xₙ−i = bⁿ−ⁱ−(ᵃⁿ−i,n−ⁱ⁺¹ˣⁿ−ⁱ⁺¹⁺···⁺ᵃⁿ−i,nˣⁿ), we need i multiplications and 1 division. (Once again, we ignore addition/subtraction). So, together, we need 1 + 2 + 3 + · · · + n = n(n+1)/2 flops.

The two operation counts, taken together, show that Gaussian elimination is made up of two unequal parts: The relatively expensive elimination step and the relatively cheap back substitution step. If we ignore the lower order terms in the expressions, we find that elimination takes on the order of n³ flops and back substitution takes on the order of n². Here n is the number of the unknowns in the system. We will often use the shorthand terminology of “big-O” to mean “on the order of”, saying that elimination is an O(n³) algorithm and that back substitution is O(n²). This usage implies that the emphasis is on large n, where lower powers of n become negligible by comparison. Overall, Gaussian elimination takes O(n³) + O(n²) = O(n³) operations. In big-O notation, the result of adding different powers of n is that only the highest power remains, since it dominates in the n → ∞ limit.

Operations counts is useful for estimating time required for solving large systems. For example, to estimate the time needed to solve a system of n = 500 equations by Gaussian elimination on a particular computer, we could get a fair guess by solving a system of n = 50 equations and then scaling the CPU time by 10³ = 1000.






# Example:

On a particular computer, back substitution of a 500 × 500 triangular matrix takes 0.1 seconds. Estimate the time needed to solve a general system of 300 equations in 300 unknowns by Gaussian elimination.






# Solution:

CPU time for BS of a 500 × 500 triangular matrix ≈ 500² × 3 × 25

CPU time for GE of a 300 system ≈ 300² × 27 × 100

So, the answer is 2 × 27 × 100 × 0.1 = 7.2 seconds. □

Now, suppose we want to solve Ax = b for different b, but same A. We can apply Gaussian elimination again and again with O(n³) flops each time. Or, we can decompose A = LU only once (assume for the moment this decomposition exists), then when giving a b, we simply solve Ly = b followed by Ux = y, each requires O(n²) flops. Obviously, the latter strategy is more efficient even though it requires more memory.

# Example:

Assume that it takes 1 second to factorize the 300 × 300 matrix A into A = LU. How many problems Ax = b₁, ..., Ax = bₖ can be solved in the next second?

# Solution:

If we know the LU decomposition of A, solving Ax = b requires one back substitution of L and one forward substitution U.

CPU time for solving two 300 × 300 triangular systems of eqns ≈ 300² = 0.01.

CPU time for GE of a 300 × 300 system 300³

So, the answer is 100. □

# Example:

Prove that A = 0 1 does not have an LU decomposition.

# Solution:

Suppose it exists. Then

0 1 = 1 0 b c = b c.

1 1 a 1 0 d ab ac + d

Equating coefficients yields b = 0 and ab = 1, a contradiction. □





# 6.1.4 Error magnification and condition number

We now discuss the two sources of error in Gaussian elimination.

Definition 1 Let xc be an approximate solution of the linear system Ax = b. The residue is the vector r = b − Axc whose size tells how good Ax = b is satisfied. The backward error is the norm of the residue ∥b − Axc∥∞, and the forward error is ∥x − xc∥∞.

Note that ∥a − b∥ is the mathematical way to measure the distance between two subjects a and b. For example, the absolute value ∥x − y∥ is the distance between complex numbers x and y.

# Example:

Find the backward and forward errors for the approximate solution xc = (1, 1)⊤ of the system

| 1 | 1  | x₁ = 3. |
| - | -- | ------- |
| 3 | −4 | ⊤x₂ = 2 |

Solution: The correct solution is x = (2, 1). So, the forward error is ∥x − xc∥∞ = 1. The backward error is ∥b − Axc∥∞ = 3 − (−0.0001)⊤.

# Example:

Find the backward and forward errors for the approximate solution xc = (1, 3) of the system

| 1 | 1 | x₁ = 2. |   |             |
| - | - | ------- | - | ----------- |
| 0 | 0 | 0       | 1 | x₂ = 2.0001 |

Solution: The correct solution is x = (1, 1)⊤. So, the forward error is ∥x − xc∥∞ = 2.0001. The backward error is ∥b − Axc∥∞ = 2. − (1, 1) = 0.0001.

2  2 − 2.0001 = 0.0001.

0  0  0  1  2 ∞

Figure 22 helps to clarify how there can be a small backward error and large forward error at the same time. Even though the approximate solution (−1, 3.0001) is relatively far from the exact solution (1, 1), it nearly lies on both lines. If the lines are far from parallel, then backward and forward errors will be closer in magnitude.



# 3.5

# 3

# 2.5

y=2.0001−1.0001x

y=2−x

# 2

# 1.5

# 1

# 0.5

# 0

# −0.5

# −1

# −0.5

# 0

# 0.5

# 1

# 1.5

# 2

Figure 22: The difference between the lines is exaggerated in the figure. They are actually much closer.




# Definition 2

Given an approximate solution xc, the relative backward error of Ax = b is defined to be ∥b−Axc∥∞ and the relative forward error is ∥x−xc∥∞.

- relative forward error ∥x−xc∥∞

error magnification factor γ = ∥b−Axc∥∞ / ∥b∥∞

Note that γ = ∥b∥∞ ∥x−xc∥∞, where bc = Axc. You want to solve Ax = b where b is the input and x is the output. But because of some measurement error, the b you entered is actually not accurate, and becomes bc. Then you work out an xc so that Axc = bc. So the input error b − bc generates the output error x − xc. That is why γ is called error magnification factor.

Recall that ∥A∥∞ is the maximum absolute row sum, i.e., if A = (aij) ∈ Rⁿ×ⁿ, ∥A∥∞ = maxi=1,...,n ∑j=1ⁿ |aij|.

The condition number of a square matrix A, cond(A), is the maximum possible error magnification factor for solving Ax = b, over all right-hand sides b. Later, we will prove that cond(A) = ∥A∥∞ · ∥A−1∥∞. The proof is not so important but the conclusion is.

# Example:

For the last example, the relative backward error is 0.0001 ≈ 0.00005.

The forward relative error is 1 = 2.0001.

By the definition, the error magnification factor γ for this specific xc is 2.0001 = 40004.0001 / 0.0001.

2.0001

| A   | 1      | 1 |       |
| --- | ------ | - | ----- |
| A−1 | −10000 | 1 | 10001 |






A ∞ = 2.0001 and A ∞ = 20001. So, cond(A) = 2.0001 × 20001 = 40004.0001. The error magnification factor for any other xc in this system will be less than or equal to 40004.0001 (because we will prove γ ≤ cond(ᴬ)). For example, if we ᵗᵃᵏᵉ xc = (2, 2)⊤. Then since x = (1, 1)⊤. ∥ˣ − xc∥∞ = 1. ∥ᴬˣc − b∥∞ = ∥(2, 2.0001)⊤∥∞ = 2.0001. So γ = ∥ᵇ∥∞ ∥ˣ−ˣᶜ∥∞ = 2.⁰⁰⁰¹ 1 = 1. □

Why we introduce cond(A) and γ which are so complicated? Are they useful? Now, suppose we want to solve Ax = b. We are given A and b. But we cannot enter b exactly. The b we used in Gaussian elimination is indeed fl(b) (fl applies to each component of b). So bc = fl(b). We want to see how this error will be amplified. In the following analysis, we try to focus on the effect due to b − bc, but ignore the round off errors that may be produced when storing A and solving Axc = bc. So, we assume A is stored exactly and Axc = bc is solved exactly. Otherwise, things are too complicated to analyze. (We will analyze the round off error in solving Axc = bc in the next subsection.)

Recall that we have stated the fact that |fl(x)−x| ≤ 1 ϵmach. By definition, the ʳᵉˡᵃᵗⁱᵛᵉ backward error is ∥b−Axc∥∞ = ∥ᵇ−ᵇᶜ∥∞. So, the relative backward error in the current case is ∥b−fl(b)∥∞ which is of size 1 ϵmach = 1 2−ᴺ = 2−⁵³ ≈ 1.¹ × 10−¹⁶ (using double precision floating point arithmetic). Recall the definition γ = relative forward error and the theorem (will later) saying that γ ≤ cond(ᴬ). So, relative backward error be proved saying that γ the relative forward error, which by definition is ∥x−xc∥∞, is of size 1 ϵmach × cond(A). In other words, if cond(A) ≈ 10k, we should prepare to ∥x∥∞ of 2 lose k digits accuracy in computing x.

Example: In a previous example, cond(A) ≈ 4 × 10⁴. So, in double precision, we should expect about 16 − 4 = 12 correct digits in the solution x. We can test this by Matlab.

A=[1,1;1.0001,1]; b=[2;2.0001]; xc=A\b; % solving A xc =b by an advanced version of LU fatorization. vpa(xc,16) % displaying 16 digits of xc ans = 1.000000000002221 .9999999999977793
Compared with the correct solution x = (1, 1)⊤, the computed solution has about 11 correct digits, close to our prediction from the condition number.

The Hilbert matrix H, with entries Hij = 1/(i + j − 1), is notorious for its large condition number.

Example: Let H denote the n × n Hilbert matrix. Use Matlab’s \ to compute the solution of Hx = b, where b = H (1, ..., 1)⊤, for n = 10.

n=10; H=hilb(n); cond(H,inf) ans = 3.5354e+013 b=H*ones(n,1); xc=H\b; vpa(xc,16) ans = .9999999988995500 1.000000094005028 .9999980154623497 1.000017912363931




.9999150675502133 1.000232312043433 .9996204783038589

1.000365402573885 .9998087904538157 1.000041929041141

The condition number is about 1013 predicts 16 − 13 = 3 correct digits in the worst case.

There are about 3 correct digits in the computed solution. For n slightly larger than 10, the condition number of the Hilbert matrix is larger than 1016, and no correct digits can be guaranteed in the computed xc.

Even excellent software may have no defense against an ill-conditioned problem. Increased precision helps. However, the condition number of the Hilbert matrix grows fast enough with n to eventually disarm any reasonable finite precision.

Fortunately, the large condition numbers of the Hilbert matrix are unusual. Well-conditioned linear systems of n equations in n unknowns are routinely solved in double precision for n = 104 and larger. However, it is important to know that ill-conditioned problems exist, and that the condition number is useful for diagnosing that possibility.



# Theorem 2

Prove that cond(A) = maxₓ ,b ∥ᵇ∥∞ ∥ˣ−ˣᶜ∥∞ = ∥A∥∞ · ∥A−¹∥∞.

Proof: We know Ax = b and b−bc = b−Axc = A(x−xc). So, ∥x−xc∥∞ = ∥(A−¹)(b−bc)∥∞ ≤ ∥A−¹∥∞∥b − bc∥∞.

On the other hand, b = Ax. So b ∞ = ∥A∥ ∥x∥∞.

So, ∥ᵇ∥∞ ∥ˣ−ˣᶜ∥∞ ≤ ∥A∥∞ · ∥A−¹∥∞.

So, ∥A∥∞ · ∥A−1∥∞ is an upper bound for all error magnification factors. Now, we want to show that this quantity is attainable. Choose x so that ∥A∥∞ = ∥Ax∥∞ = ∥b∥∞ and r such that ∥A−1∥∞ = ∥A−1r∥∞. Set xc = x − A−1r. Then b − bc = A(x − xc) = r. So ∥x − xc∥∞ = ∥Ar∥∞. Thus, ∥b∥∞ ∥x − xc∥∞ = ∥A∥∞ · ∥A−1∥∞. □



# 6.1.5 Swamping

Consider the system of equations

10−20x1 + x2 = 1

x1 + 2x2 = 4

I leave you to check that the exact solution is (x1, x2) = (2 × 1020, 4 − 2 × 1020) ≈ (2, 1).

Now, suppose we use double precision, and use the original Gaussian elimination, we would end up with (x1, x2) = (0, 1). Here is how:

10−20   1     1

1   2     4

R2 − 10−20R1 → 0   2 − 1020   4 − 1020

In IEEE double precision, 2 − 1020 is the same as −1020, due to rounding. Similarly, 4 − 1020 is stored as −1020. Now the bottom equation is −1020x2 = −1020 which leads to x2 = 1. Plugging it into 10−20x1 + x2 = 1, we get x1 = 0.

Now, suppose we first switch the first and second equations, and then do Gaussian elimination:

1   2     4

R2 − 10−20R1

10−20   1     1 → 0   1 − 2 × 10−20   1 − 4 × 10−20

In IEEE double precision, 1 − 2 × 10−20 is stored as 1 and 1 − 4 × 10−20 is stored as 1. So the equations are now

x1 + 2x2 = 4

x2 = 1

It yields the computed solution (x1, x2) = (2.000..., 1.000...) which is correct up to approximately 16 digits.

To explain why the first approach is not good: it is because adding −1020 times the top equation to the bottom equation overpowers the bottom equation. While there were originally two independent equations, after the elimination step, there are essentially two copies of the top equation.

The moral of this example is that multipliers in Gaussian elimination should be kept as small as possible to avoid overpowering. There is a simple modification to the original Gaussian elimination that forces the absolute value of the multiplier to be no larger than 1. This new protocol, which involves judicious row exchanges in the tableau, is called partial pivoting, the topic we will discuss next.



# 165



# 6.1.6 Gaussian elimination with partial pivoting

The form of Gaussian elimination considered so far is often called “naive”, because of two serious difficulties: encountering a zero pivot and swamping. Both can be avoided by changing rows of the coefficient matrix. The partial pivoting protocol asks that before eliminating kth column, the p with k ≤ p ≤ n and largest |apk| (entries in the kth column which lie on or below the diagonal) is located, and pth row and kth row are exchanged if necessary before continuing with the elimination.




# Example:

Apply Gaussian elimination with partial pivoting to solve the system

- −x1 − x2 + 3x3 = −3
- x1 − 2x3 = 1
- 2x1 + 2x2 + 4x3 = 0

# Solution:

This example is written in tableau form as

| −1 | −1 | 3  | −3 |
| -- | -- | -- | -- |
| 1  | 0  | −2 | 1  |
| 2  | 2  | 4  | 0  |

exchange row 1 and row 3

| −1 | −1 | 3  | −3 |
| -- | -- | -- | -- |
| 1  | 0  | −2 | 1  |
| 2  | 2  | 4  | 0  |

add 1 × row 1 to row 2

| 2 | 2 | 4 | 0 |
| - | - | - | - |
| 0 | 1 | 0 | 1 |
| 2 | 2 | 4 | 0 |

add −1 × row 1 to row 3

| 0 | 2 | 1 | 3 |
| - | - | - | - |

exchange row 2 and row 3

| 0 | 2 | 1 | 3 |
| - | - | - | - |
| 0 | 1 | 0 | 1 |

add 1 × row 2 to row 3

| 0 | 0 | 1 | −1 |
| - | - | - | -- |

The equations are now simple to solve. From

- 2x1 + 2x2 + 4x3 = 0
- −2x2 + 1x3 = −3
- 2x3 = −1

we find that x = (1, 1, −1)⊤. □





# 6.1.7 Permutation Matrix

Now, we need to find the mathematical expression of “exchanging two rows”. For that, we need to introduce the permutation matrix.



# Definition 3

A permutation matrix is an n × n matrix consisting of all zeros, except for a single 1 in every row and column.

For example,

| 0 | 0 | 1 | 0 |
| - | - | - | - |
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 |

A permutation matrix P is created by applying arbitrary row exchanges to the identity matrix. For example, the first matrix in (11) can be viewed as applying row exchange (1, 2, 3, 4) → (4, 3, 1, 2) to the 4 × 4 identity matrix.



# Theorem 3

Let P be an n × n permutation matrix formed by a particular set of row changes applied to the identity matrix. Then, for any n × n matrix A, P A is the matrix obtained by applying exactly the same set of row exchanges to A.

The above result is a consequence of the “row manipulation interpretation of matrix multiplication”. For example,

| 0 | 0 | 1 | 0 |
| - | - | - | - |
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 |
| 1 | 0 | 0 | 0 |

is equal to

| a₁₁ | a₁₂ | a₁₃ | a₁₄ | a₃₁ | a₃₂ | a₃₃ | a₃₄ |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a₂₁ | a₂₂ | a₂₃ | a₂₄ | a₄₁ | a₄₂ | a₄₃ | a₄₄ |
| a₃₁ | a₃₂ | a₃₃ | a₃₄ | a₂₁ | a₂₂ | a₂₃ | a₂₄ |
| a₄₁ | a₄₂ | a₄₃ | a₄₄ | a₁₁ | a₁₂ | a₁₃ | a₁₄ |




# 6.1.8 P A = LU factorization

As its name implies, the P A = LU factorization is simply the LU factorization of a exchanged version of A. Under partial pivoting, the rows that need exchanging are not known at the outset, so we must be careful about fitting the row exchange information into the factorization. In particular, we need to keep track of previous multipliers when a row exchange is made. We begin with an example.

# Example: Find the P A = LU factorization of the matrix

| 2 | 1 | 5  |
| - | - | -- |
| 4 | 4 | −⁴ |
| 1 | 3 | 1  |

# Solution:

First, rows 1 and 2 need to be exchanged. It means we need to left-multiply A by P

| 0 | 1 | 0 |
| - | - | - |
| 1 | 0 | 0 |
| 0 | 0 | 1 |

and obtain

| 4 | 4 | −⁴ |
| - | - | -- |
| 2 | 1 | 5  |
| 1 | 3 | 1  |

We will use the permutation matrix P to keep track of the cumulative permutation of rows that have been done along the way. Now, we perform two row operations, namely,

✓✏    −  4        4  4

add − 1 × row ¹ → ✒✑ 2 to row 2

2    −1 ⁷

to eliminate the first column. We have done something new — instead of putting only a zero in the eliminated position, we have made the zero a storage location. Inside the zero at the position, we store the negative of the multiplier that we used to eliminate that position. We do this for a reason. This is the mechanism by which the multiplier will stay with their row, in case future row exchanges are made.




# Next we must make a comparison to choose the second pivot.

We need to exchange the 2nd and 3rd rows of the last matrix. Note that the previous multiplier move along with the row exchange.

| ✓✏ | −  | 4  | 4   | 4 |
| -- | -- | -- | --- | - |
| 1  | ✒✑ | →  | ✓✏2 | ² |
|    | 4  | 1  | ✒✑  |   |
|    | 2  | −1 | ⁷   |   |

To record this permutation, what we need to do is simply exchange the 2nd and 3rd rows of P. So, P becomes P =

| 0 | 1 | 0 |
| - | - | - |
| 0 | 0 | 1 |
| 1 | 0 | 0 |

Then we continue.

| ✓✏ | −  | 4 | 4  | 4         |
| -- | -- | - | -- | --------- |
| 1  | ×  | 1 | ✒✑ | add row 2 |
| →  | ✓✏ | ✓ | ✏  |           |
| 2  | 1  | 5 | 11 | 0         |
| 0  | 0  | 1 | 4  | 4         |
| −⁴ |    | 4 |    |           |

This is the finished elimination. Now we can read off the P A = LU factorization

| 0 | 1 | 0 |
| - | - | - |
| 0 | 0 | 1 |
| 1 | 0 | 0 |

Then we have:

| 2 | 1 | 5  |
| - | - | -- |
| 4 | 4 | −⁴ |
| 4 | 1 | 0  |
| 0 | 0 | 8  |

The entries of L are sitting inside the zeros in the lower triangle of the matrix (below the main diagonal), and U comes from the upper triangle.






# Using the P A = LU factorization to solve a system of equations

Ax = b → P Ax = P b → LUx = P b. So, we first solve for Ly = P b for y and then solve for Ux = y for x.





# 6.1.9 Remark on P A = LU factorization

Recall that in the previous example we have a 3 × 3 matrix A. We need to permute it by P₁, then eliminate the 1st column by left multiplying a matrix M₁. Then we permute it again by P₂, then eliminate the 2nd column by left multiplying a matrix M₂. Finally we obtain an upper triangular matrix U. So, M₂P₂M₁P₁A = U. Our total P is P₂P₁. So, we want to prove P A = LU for some L. Since P² = I, we can write M₂P₂M₁P₁A = U as ((M₂)P₂M₁P₂) (P₂P₁)A = U.

So, P A = (P₂P₁)A = ((M₂)P₂M₁P₂)⁻¹ U = (P₂M₁P₂)⁻¹ M⁻¹U and we can show (P₂M₁P₂)⁻¹ M⁻¹ is L. Note that even M₁ stores the information when we eliminate the first column, it will be permuted by the permutation happening later. That is why when we exchange rows, we need to exchange the whole rows.

The above remark can be extended to n × n matrix A.



Example.

Use the P A = LU factorization to solve the system Ax = b where

A =




# Algorithm of LU factorization of an n × n matrix

A with partial pivoting:

U = A, L = I, P = I. for k = 1 : n − 1
Find µ so that U µ, k is the largest among U k, k , ..., U n, k
U(k, k : n) ↔ U(µ, k : n) (“↔” means interchange two rows)
L(k, 1 : k − 1) ↔ L(µ, 1 : k − 1) (only the low triangular part on the left hand side of the kth column)
P(k, :) ↔ P(µ, :)
if U(k, k) = 0
for j = k + 1 : n
L(j, k) = U(j, k)/U(k, k) (for j = k + 1 : n updates the low triangular part of the kth column)
for ℓ = k : n
end
U(j, ℓ) = U(j, ℓ) − L(j, k)U(k, ℓ)
end
end
end

Note that the matrix L in the k-th step is

1 · · · 0 0 · · · 0
. . . . . . . . . . . . . . . . . . .
L = ∗ ∗ 1 0 0 ∗ ∗
βₖ+1,k 1 0 . . . . . . . . . . . . . . . . . .
∗ · · · βn,k 0 · · · 1

with βj,k = U(j, k)/U(k, k) for j = k + 1, ..., n. In kth step, the kth column of L will be filled in by those βj,k’s. But before we generate and store the βj,k’s, we permute the k-th and µ-th rows of L. However, the permutation does not apply to the full row, but only to the entries lying on the left hand side of the kth column. Obviously, those entries are the β.,.’s generated, stored and permuted during the previous steps.

After the above process, we obtain matrices P, L, U which satisfies P A = LU (proved in our next theorem).

So, if we want to solve Ax = b by Gaussian elimination, mathematically, it is equivalent to say, we first rewrite it as LUx = P b and then solve Ly = P b followed by solving Ux = y.

Here is the Matlab code. The result satisfies P A = LU.

function [L,U,P]=myLU(A)
[m,n]=size(A);
if m~=n
disp(’input matrix must be a square matrix’);
pause; return;
end
p=zeros(n-1,1);
for k=1:n-1






[a,mu]=max(abs(A(k:n,k)));
mu=mu+k-1; % because mu is relative position
p(k)=mu;
if k~=mu
A([k,mu],:)=A([mu,k],:);
end
if abs(A(k,k))>eps
rows=(k+1):n;
A(rows,k)=A(rows,k)/A(k,k);
A(rows,rows)=A(rows,rows)-A(rows,k)*A(k,rows);
end
end
P=eye(n);
for k=1:n-1
if k~=p(k)
P([k,p(k)],:)=P([p(k),k],:);
end
end
L=tril(A);
for k=1:n
L(k,k)=1;
end
U=triu(A);





# 6.1.11 Properties of Gauss transform matrix

To see why the output of the above algorithm satisfies P A = LU, recall the Gauss transform matrix that we have introduced before

| 1 | ·     | · | 0   | 0 | · | · | 0 |
| - | ----- | - | --- | - | - | - | - |
| . | .     | . | .   | . | . | . | . |
| . | .     | . | .   | . | . | . | . |
| . | .     | . | .   | . | . | . | . |
| 0 | 1     | 0 | 0   | . | . | . | . |
| 0 | −βₖ₊₁ | 1 | 0   | . | . | . | . |
| . | .     | . | .   | . | . | . | . |
| . | .     | . | .   | . | . | . | . |
| . | .     | . | .   | . | . | . | . |
| 0 | ·     | · | −βₙ | 0 | · | · | 1 |

Let β(ᵏ) = (0, ..., 0, βₖ₊₁, ..., βₙ)⊤ (called Gauss vector). It is easy to see that Gauss transform matrix has the following property:

Mₖ = I − β(ᵏ)e⊤ (12)

M−¹ = I + β(ᵏ)e⊤. (13)

Mₖ−j · · · Mₖ−₁Mₖ = I − β(ᵏ−ʲ)e⊤ ... − β(ᵏ−1)e⊤ − β(ᵏ)ᵉ⊤, (14)

M−¹ · · · M−¹ M−¹ = I + β(ᵏ−ʲ)e⊤ ... + β(ᵏ−1)e⊤ + β(ᵏ)e⊤. (15)

[Hint: e⊤β(ᵏ) = 0 for any i ≤ k.] Note that if it is not Mₖ−₁Mₖ, but Mₖ Mₖ−₁, the result will have the cross term.



# 6.1.12 The theorem on P A = LU factorization

If A ∈ Rⁿ×ⁿ, then the algorithm of LU factorization with partial pivoting generates Gauss transformation matrices M₁, ..., Mₙ−₁ and permutation matrices E₁, ..., Eₙ−₁ such that

Mₙ−₁Eₙ−₁ · · · M₁E₁A = U (16)

and U is upper triangular. The P generated by the algorithm is P = Eₙ−₁Eₙ−₂ · · · E₁. Here we recall that a permutation matrix is obtained from switching two rows of the identity matrix. So Eᵢ is obtained from switching the i-th row and µ-th row (we always have µ ≥ i) and EᵢB means switching the corresponding two rows of B. In particular, E² = I because it switches back to I. We call a lower triangular matrix unit lower triangular matrix if its diagonal entries are all 1.

Going back to the LU factorization with partial pivoting. Once we get Mₙ−₁Eₙ−₁ · · · M₁E₁A = U, define column vector β(ᵏ) so that Mₖ = I − β(ᵏ)e⊤. Then we construct a unit lower angular matrix L by L k + : n, k = g k + 1) : n) where g = Eₙ−₁ Eₖ₊₁β.

Note that L((k + 1) : n, k) is the entries that lie directly under L(k, k) and Eₖ₊₁β(ᵏ) is a permutation of β(ᵏ). Eₙ−₁ · · · Eₖ₊₁β(ᵏ) means we have to keep permutating β(ᵏ) in the same way how we permute A after β(ᵏ) has been generated. Let P = Eₙ−₁Eₙ−₂ · · · E₁, then we have the following result:



# Theorem 4

P A = LU.

Proof: (the proof is not required for the exam.) Recall (16)

Mₙ−₁Eₙ−₁ · · · M₁E₁A = U

One can easily verify that the above equation can be rewritten as

Mₙ−₁(Eₙ−₁Mₙ−₂Eₙ−₁)(Eₙ−₁Eₙ−₂Mₙ−₃Eₙ−₂Eₙ−₁)(Eₙ−₁Eₙ−₂Eₙ−₃Mₙ−₄Eₙ−₃Eₙ−₂Eₙ−₁) · · · (Eₙ−₁Eₙ−₂Eₙ−₃ · · · E₂M₁E₂ · · · Eₙ−₁)(Eₙ−₁Eₙ−₂ · · · E₂E₁)A = U.

which means

˜ ˜ · · · ˜ A (17)

Mₙ−₁Mₙ−₂ M₁P = U

where ˜ for ≤ −

Mₙ−₁ = Mₙ−₁ and k n 2

˜ · · · · · · − · · · β(ᵏ) ⊤ · · ·

Mₖ = Eₙ−₁ Eₖ₊₁Mₖ Eₖ₊₁ Eₙ−₁ = I Eₙ−₁ Eₖ₊₁ eₖ Eₖ₊₁ Eₙ−₁ = I − g(ᵏ)e⊤Eₖ₊₁ · · · Eₙ−₁.

Since each Ej is a permutation involving row j and a row µ with µ ≥ j, we have Ej(1 : k, 1 : k) = Iₖ ∈ Rᵏ×ᵏ for j = k +1, ..., n − 1, and hence Eₖ₊₁ · · · Eₙ−₁ = Iₖ 0 · · · Iₖ 0 = Iₖ 0.

So e⊤Eₖ₊₁ · · · Eₙ−₁ = e⊤ and 0 ∗ 0 ∗ 0 ∗ k k

˜ − (k) ⊤ · · · − (k) ⊤

Mₖ = I g eₖ Eₖ₊₁ Eₙ−₁ = I g eₖ.




(17) implies P A = ( ˜ −¹ ˜ −¹ · · · ˜ −¹ ) (13) (15), M₁ M₂ Mₙ−₁ U. By and we have n−1 ˜ −¹ ˜ −¹ · · · ˜ −¹ (k) ⊤ M₁ M₂ Mₙ−₁ = I + g eₖ . k=1 The right hand side above is nothing but the L generated by the algorithm. □





# 6.1.13 Uniqueness and avoidance of pivoting

# Theorem 5

If A = LU and A is nonsingular, then the LU factorization is unique and det A = n ∏ uii.

Proof: Consider A = L1U1 = L2U2. Then L−1L1 = U2U−1 is both upper triangle and unit lower triangle, which is I. □

# Tutorial problem

Prove that the inverse of a unit lower triangular matrix is still unit lower triangular.

We state the following theorem but will not present the proof (see Theorem 3.2.1 of “Matrix Computation” by Golub and Van Loan).



# Theorem 6

Given A ∈ Rⁿ×ⁿ. If det A(1 : k, 1 : k) = 0 for k = 1 : n − 1, then A has an LU factorization.

Since symmetric positive definite matrix 16 satisfies det A(1 : k, 1 : k) > 0 for k = 1 : n−1, by the above theorem, we know it has a LU factorization. But the theorem only says it is not zero for the entries on the diagonal that is used to do the Gaussian elimination during the LU factorization. Moreover, we have the following theorem which says that its absolute value is the largest among the rest entries in the same column. We will not prove it but you can find the proof in Theorem 3.4.3 of ”Matrix Computation” by Golub and Van Loan.

16A ∈ Rⁿ×ⁿ is called symmetric positive definite if A = A⊤ and x⊤Ax > 0 whenever x = 0 vector.



# Theorem 7

If A⊤ is strictly diagonal dominant (means aii > ∑j=in aji for all i), then A has an LU factorization and ℓij &#x3C; 1 when i > j. In other words, if the algorithm in Section 6.1.10 is applied, then P = I.



Homework 11
# 6.1.14

1. (Sauer) Page 78, 2.1 Exercises, 4(a)
2. (Sauer) Page 84, 2.2 Exercises, 2(a), 7
3. (Sauer) Page 101, 2.4 Exercises, 4(a)



# 6.2 Iterative methods for linear systems

Suppose we want to solve

3x1 + x2 = 5,

x1 + 2x2 = 5.

We can solve xi from the ith equation and get

x1 = (5 − x2) / 3,

x2 = (5 − x1) / 2.

The above system of equations can be written as ⃗ x = Φ(⃗ x) with ⃗ x =

x1
x2

Then we can try to solve ⃗ x = Φ(⃗ x) by ⃗ xk = Φ(⃗ xk−1) for k = 1, 2, .... with, say, ⃗ x0 =

0
0

This method for solving Ax = b is called Jacobi method and belongs to the so-called iterative methods.

The hope is that if ⃗ xk converges to some vector ⃗ x, then this ⃗ x will satisfy ⃗ x = Φ(⃗ x) and is the solution we are looking for.

Unlike Gauss elimination, which is called direct method, iterative method can give you some useful results even if you terminate before the program returns (i.e. ⃗ xk converges).

Suppose we apply Jacobi iteration to the system

3x1 + x2 = 5,

x1 + 2x2 = 5.

| xk+1 = (5 − xk) / 3 | x0 | 0 | x1 |
| ------------------- | -- | - | -- |
| xk+1 = (5 − xk) / 2 | x0 | 0 | x1 |

Starting from x0 = (0, 0)⊤, we get

x1 = 1 / 3, 1 / 2




# 5

3, 1 / 6, 1 / 9, 1 / 36, .... The iteration converges to the exact solution 1 / 2.

Note that the associated matrix A is strictly diagonal dominant.

If we switch the order of the equations,

- x1 + 2x2 = 5,
- 3x1 + x2 = 5.

xk+1 = (5 − 2xk) / x0 0 x1

xk+1 = (5 − 3xk) / x0 0 x1

Then,

x1 = 5 / 2, 1 / 2, 1 / 2, 1 / 2, .... The iteration actually diverges.

In the first Jacobi iteration

xk+1 = (5 − xk) / 3, if we use the updated xk+1 when putting xk+1, i.e., we use

xk+1 = (5 − xk+1) / 2, we get the so-called Gauss-Seidel method.





# 6.2.1 Jacobi and Gauss-Seidel iterations

Suppose we want to solve Ax = b with A = (aij) and b = (b1, ..., bn)⊤.



# Jacobi iteration

for i = 1, ..., n

xk+1 = (bi - Σj=1i-1 aijxk - Σj=i+1n aijxk) / aii

Let A = L + D + U. Then

Dxk+1 + (L + U)xk = b. (18)

Note that if xk converges to y, then Ay = b by (18). From (18), we have

xk+1 = -D-1(L + U)xk + D-1b.

Let ek = xk - x, then

ek+1 = -D-1(L + U)ek = [-D-1(L + U)]2ek-1 = · · · = [-D-1(L + U)]k e0.

So, Jacobi iteration converges if and only if limk→∞[-D-1(L + U)]k e0 = 0 for any e0, which is equivalent to limk→∞[-D-1(L + U)]k = 0.

We need to study what condition on B ensures B → 0 when k → ∞. It turns out, that condition is ρ(B) &#x3C; 1 by Theorem 5 of Chapter 2. We will introduce ρ(B), which is the spectral radius of matrix B later on.



# Gauss-Seidel iteration

for i = 1, ..., n

xk+1 = (bi - Σj=1i-1 aijxk+1 - Σj=i+1n aijxk) / aii

end

So, (L + D)xk+1 + Uxk = b, xk+1 = -(L + D)-1Uxk + (L + D)-1b.

Gauss-Seidel iteration converges if and only if ρ((L + D)-1U) &#x3C; 1 by Theorem 5.




# Theorem 8 (convergence of Jacobi and Gauss-Seidel iteration)

If A is strictly diagonal dominant17, then ∥G∥∞ ≤ ∥J∥∞ &#x3C; 1 where J = -D-1(L+U) and G = - (L+D)-1U.

# Proof:

(Convergence of Jacobi. This is Theorem 2.10 on Page 107 and 111 of the textbook.)

Define κJ = ∥J∥∞. One can easily verify that κJ = ∥J∥∞ = ∥D-1(L + U)∥∞ = max1≤i≤n Σj=1,...n,j=i aij / aii &#x3C; 1. (19)

(Convergence of Gauss-Seidel. This won’t be tested.) Define E = -D-1L and F = -D-1U, then J = -D-1(L + U) = -I-1(D-1L + D-1U) = E + F and G = -(L + D)-1U = -(D-1L + I)-1D-1U = (I - E)-1F.

Let’s introduce the absolute value of a matrix: |B| = (|bij|) if B = (bij). Let e = (1, 1, ..., 1)⊤ and note that ∥B∥∞ = ∥ |B| e∥∞.

The i-th component of |J| e is Σj=1,...n,j=i aij ≤ κJ by (19).

|J| e ≤ κJe.

Because |J| = |E| + |F|, |F|e ≤ (κJI − |E|) e.

Recall that G = (I− E)-1F. Because E is strictly lower triangle matrix, En = 0, (I− E)-1 = I + E + E2 + ... + En−1. Using this fact, we have

| |n (I − E)-1 ≤ I + |E| + |E|2 + ... + |E|n−1 = (I − |E|)-1 (20) because E = 0.

Therefore |G|e ≤ (I − |E|)-1|F|e ≤ (I − |E|)-1 (κJI − |E|) e ≤ I + (κJ − 1)(I − |E|)-1 e2 n−1 = I + (κJ − 1)(I + |E| + |E| + ... + |E|) e ≤ (I + (κJI − I)) e = κJe.

where we have used κJ − I ≤ 0. This implies ∥G∥∞ ≤ κJ = ∥J∥∞. □





# 6.2.2 Symmetric positive-definite matrices

Definition 4 (see Section 2.6.1 of the textbook) An n × n matrix A is symmetric if A⊤ = A. The matrix A is positive-definite if x⊤Ax > 0 for all vectors x ≠ 0.

From what we have learned in linear algebra, if A is symmetric, then there is an orthogonal matrix Ω and a diagonal matrix Λ = diag(λ₁, · · ·, λₙ) so that A = ΩΛΩ.

Here λi’s are the eigenvalues of A. So, we can write xᵀAx = x⊤ΩΛΩ⊤x = y⊤Λy = λiy², where y = Ω⊤x.

Hence, we have proved that



# Proposition 1

If A is symmetric, then A is positive-definite if and only if all of its values are positive.

Now, we assume A is symmetric positive definite and we want to derive a very efficient method for solving Ax = b. The starting point in the derivation is to consider how we should minimize the function

f(x) = 1⁄2 x⊤Ax − x⊤b.

Because D²f(x) is positive definite, by solving ∇f(x) = 0, one can see that minimizing f and solving Ax = b are equivalent problems.

177



# 6.2.3 Steepest descent

At any point xc, the steepest descent direction −∇f(xc) = b − A xc is also the residue of solving Ax = b

rc = b − A xc.

To minimize f(xc + α rc) = f(xc) − α r⊤ rc + 1/2 α² r⊤ A rc.

α = r⊤ rc/r⊤ A rc. This leads to steepest descent method:

1. Initialize with x0
2. For k = 0, 1, ... until some stopping criteria is satisfied
3. rk−1 = b − A xk−1
4. αk = r⊤ rk−1/r⊤ A rk−1
5. xk = xk−1 + αk rk−1

Note that

r⊤ rk = r⊤ (b − A(xk−1 + αk rk−1)) = r⊤ rk−1 − αk r⊤ A rk−1 = 0.

This indicates that the method is myopic in the sense that it often searches in similar directions to those searched before.



# 6.2.4 Conjugate gradient

In steepest descent method, the sequence x₀, ..., xₖ , ... is found by one-dimensional minimization of f in the direction of the gradient

f(xₖ₊₁) = min f(xₖ + urₖ ) with rₖ = b − Axₖ. (22)

We will now consider

f(xₖ₊₁) = min f(xₖ + ∑j=0k ujpj) with {pj} satisfy p⊤Apj = 0. (23)

Those {pj} are said to be conjugate with respect to A and p0 = b − Ax0.

Note that pi’s are linearly independent (otherwise, assume pk = ∑j=k cjpj and dot it with Apk to see the contradiction.) So, for a problem in Rn, p0, ..., pn−1 will expand the whole Rn and therefore (23) will return the exact solution in at most n steps.

If (23) is true,

0 = ∂f(xk⁺¹) = ∇ᶠ(ˣₖ + ∑j=0k ujpj), pi = A(xk + ∑j=0k ujpj) − b, pi

∂ui = ⟨−rk + uiApi, pi⟩

From the above equation, we know two things: (1) when looking for xk₊₁ = xk + ∑j=0k ujpj, r⊤pi ui =

Remark: We will prove r⊤pk = r⊤rk in Theorem 9. The advantage of using the later is to save one inner product computation per iteration.

The matrix A doesn’t have to be stored explicitly. It suffices to store the product Apk instead. In addition, we only need to store three other vectors xk+1, rk+1 and pk+1. We also need to store the inner product r⊤rk from the previous iteration.

When the conjugate gradient method is applied, n is usually so large that O(n) iterations requires unacceptable amount of work. It is customary to regard the method as a genuinely iterative method with termination based on an iteration maximum kmax and the relative 2-norm of the residue ∥rk∥2. Note that one reason to use 2-norm ∥rk∥2 is because we have already computed it in βk = ∥rk+1∥2/∥rk∥2.

Remark: If rk = b − Axk, (which is true for k = 0) rk+1 = b − Axk − αk Apk = b − Axk+1.

The way used to compute rk+1 saves one computation of Axk+1 since we have already computed Apk. We are only left to verify the following property:



# Theorem 9

p⊤Apj = 0 if i &#x3C; j.




# Proof:

(The proof is not required for the exam.) We will prove the following statement Sk by induction:

1. r⊤pi = 0 for i &#x3C; j ≤ k
2. r⊤pi = r⊤ri for i ≤ k, rk+1 = 0
3. p⊤Apj = p⊤Api = 0 for i &#x3C; j ≤ k

S0 is true because r0 = p0. Suppose Sk is true and we want to show Sk+1 is true.

1. By the definition of αk, r⊤pk = r⊤pk − αkp⊤Apk = 0. Because of Sk - (1)(3), r⊤pj = 0 for any j &#x3C; k.
2. r⊤pk+1 = r⊤(rk+1 + βkpk) = r⊤rk+1.
3. By Sk - (2), αk = 0, otherwise, rk = 0 and we have already converged in the last step and don’t need to go to step k + 1. Then we have:

p⊤Apk = r⊤Apk + βkp⊤Apk = 1/rk (r⊤(rk − rk+1) + βkp⊤Apk).

= 1/αk r⊤(pk − βk-1pk-1 − rk+1) + βkp⊤Apk

= −1/αk r⊤rk+1 + βkp⊤Apk = 0.

In the last step, we have used the definition of αk, βk. For j &#x3C; k,

p⊤Apj = r⊤Apj + βkp⊤Apj = 1/αj r⊤(rj − rj+1).

= 1/αj r⊤(pj − βj-1pj-1 − pj+1 + βjpj) = 0. □

Remark: Notice that we also have r⊤rj = 0 for i &#x3C; j. This is because ri = pi − βi-1pi-1 and Sk - (1).





# 6.2.5 Krylov space and convergence rate of conjugate gradient method

Krylov space *Ki(q, A) is the subspace spanned by the first i vectors of the sequence {Aiq}*i≥₀.

Because *p0 = r0 = b − Ax0, rk+1 = rk − αApk and pk+1 = rk − αk Apk + βpk, by induction, one can prove that rk and pk ∈ span{r0, Ar0, ..., Akr0} def (A) = Kk+1 r0.*

Introduce the norm *∥x∥A = x⊤Ax1/2 and note that if Axe = b, ∥x − xe∥2 = 1/2 x⊤Ax − x⊤b + 1/2 x⊤Axe = f(x) + Const with f defined in (21). So (23) can be rewritten as ∥xk+1 − x∥A = min{∥y − x∥A; y ∈ x0 + Kk+1} (24) where x is the exact solution of Ax = b*.

(The rest analysis, except the statement of Theorem 10, is not required for the exam.)

If we introduce the error *ej = xj − x, then because r0 = −Ae0, any y ∈ x0 + Kk+1 satisfies y − x ∈ x0 − x + Kk+1 = e0 + span{Ae0, ..., Ak+1e0}.*

Therefore, there is a real polynomial *p(t) = 1 + α1t + ... + αk+1tk+1 with y − x = p(A)e0. So (24) means ∥ek+1∥A = min{∥p(A)e0∥A; p ∈ Pk+1} where Pk+1 denotes the set of all real polynomials of degree k + 1 with p(0) = 1. In particular, once k + 1 reaches the degree of the minimal polynomial of A, there is pk+1 so that pk+1(A) = 0.*

Because *A is symmetric positive definite, it can be diagonalized by orthonormal matrix. Denote the eigenvalue and orthonormal eigenvector of A by λ1 ≥ ... ≥ λn > 0 and z1, ..., zn.*

Let *e0 = ∑j=1n βjzj. So ∥e0∥2 = e⊤Ae0 = ∑j=1n λjβj2.*

*∥p(A)e0∥2 = e⊤(p2(A)A)e0 = ∑j=1n p(λj)2λjβj2 ≤ max p(λj)2 ∥e0∥2.*

Therefore *∥ek+1∥A ≤ minp∈Pk+1 maxj |p(λj)| ≤ minp∈Pk+1 maxλ∈[λ1,λn] |p(λ)|* (25)




Because it is min, we can obtain an upper bound of the right hand side of (25) by selecting a specific polynomial (which in fact is optimal). Recall the Chebyshev polynomial

Tk+1(x) = cos((k + 1)(arccos x)), x ∈ [−1, 1]

We need to rescale Tk+1 so that it is defined on [λn, λ1], and then normalized it so that it is in ¯ S. So define Pk+1.

Tk+1 2λ−(λ1+λn)

pk+1(λ) = Tk+1 −(λ1+λn) λ1−λn.

Because maxx |Tk+1(x)| = 1,

maxλ∈[λn,λ1] |pk+1(λ)| = 1 = 1

Tk+1 −(λ1+λn) Tk+1 Cond2(A)+1

λ1−λn Cond2(A)−₁

where Cond2(A) = λ1 = ∥A∥2∥A−1∥2 is the condition number base on 2-norm (see Chapter 2) and we have used the fact that Tk+1 x = Tk+1 x.

To obtain an upper bound of Tk+1 Cond2(A)+1 −1, we use the following property of Tn

Tn z + 2z−1 = zn + z−n

and note that Cond2(A)−1 = z+ with z = √2. So Tk+1 Cond2(A)−1 = z1 + z2.

Hence ∥ek+1∥A ≤ 1 ≤ 2 = 2 Cond2(A) −1 k+1.

∥e0∥A Tk+1 Cond2(A)+1 zk+1 Cond2(A) + 1

Cond2(A)−1





# Theorem 10

Consider conjugate gradient method for Ax = b with A symmetric positive definite. Let Cond2(A) = λmax(A) be the condition number of A. Then

∥xk − x∥A ≤ 2 Cond2(A) − 1 k ∥x0 − x∥A.

Cond2(A) + 1



# 6.2.6 Preconditioned conjugate gradient

This section is provided for your information only and won’t be presented in lecture and won’t be tested at all.

We can write Ax = b as x = (I − A)x + b. A preconditioner P is a matrix that is close to A and is easy to invert. Suppose we have such a P, then we can use P x = (P − A)x + b.

and iterate by P xk+1 = (P − A)xk + b. In each step that goes from xk to xk+1, we have to solve a system P xk+1 = · · · . This is feasible because P can be easily inverted. In the case P = A, this goes back to solving Ax = b in one step. Naturally, one can think of taking P = D or P = L + D where A = L + D + U. They are easy to invert and hopefully can

182

Ax = b (Hence where A = C AC , x Cx C C definite.)

C = ΩΛ−1 definite. Ω is also symmetric positive definite. The game is to choose C so that A is well conditioned and for reasons that will soon emerge, the matrix C2 must also be “easy to invert”.

We apply algorithm in previous Section to (26), we get (relation to Ax = b is put inside [ ])

1. Initialize x = A−1 C Ax C C, r = b - x, r = p = r




2. For k = 0, 1, ... until some stopping criteria is satisfied - α = r A C C A C C

rk = rk + α pk, i.e. x = x + α pk+1

rk+1 = rk - α A pk

Now, it is very clear that we can set p = C-1p C-2 (by solving Mqk := C2qk = rk) and rewrite the above algorithm into a more clever way:

1. Initialize x0, r0 = b − Ax0, solve Mq0 = r0, p0 = q0.
2. For k = 0, 1, ... until some stopping criteria is satisfied
3. αk = r⊤qk / p⊤Apk
4. xk+1 = xk + αkpk
5. rk+1 = rk − αk Apk
6. solve Mqk+1 = rk+1
7. r⊤qk+1 βk = k+1 r⊤qk

Remark: Although the transformation C figured heavily in the derivation, its action is only left through the preconditioner M = C2.

One of the most important preconditioning strategies involves computing an incomplete Cholesky factorization of A. We attempt to find the standard Cholesky factorization A = GG⊤. We approximate G by L where L is a lower triangular matrix and when going through the standard Cholesky factorization, we insist that at any stage, if A(i, j) = 0, then L(i, j) = 0 also. This is done to preserve the sparsity structure of A.

The preconditioner is then taken to be M = LL⊤. On the other hand, we can assume M = C2. Because M is positive semi-definite, we have the existence of such a C. From linear algebra, we know for any matrix C, there is an orthogonal matrix Q and upper triangular matrix R such that C = QR. So, M = R⊤R and therefore R = L⊤ by the uniqueness of Cholesky factorization of M. Then, we see that

A = C-1AC = QL A Q = Q(L-1GG⊤L-⊤)Q.

Hence Cond2 A = Cond2 L GG L-1 as L G and Cond2 BQ = Cond2 B





Cond2(QB) = Cond2(B) for any orthogonal matrix Q (because ∥BQ∥2 = ρ((BQ)⊤BQ) = ρ(Q⊤B⊤BQ) = ρ(B⊤B) = ∥B∥2).



# 6.2.7 Homework 12

1. Based on textbook: Tim Sauer, Numerical Analysis, 2nd edition

Page 115, 2.5 Exercises, 1(c), 2(c)

Page 128, 2.6 Exercises, 1(b), 2(b)

2. (The next problem can be very difficult to some of you. Hence the solution is provided at the end. But you should try it seriously before you read the solution because it can be tested in the exam, as a way for me to tell who should get A and who should get B.)

Suppose you want to solve Ax = b by the Gauss-Seidel iteration with

| A = | | 1 | | α | | - | | - | | α | | 1 |
| --- | --- | --- | --- | --- | --- | --- |---|---|---|---|---|---|

Determine the necessary and sufficient condition for α so that the Gauss-Seidel iteration converges to the exact solution.

Solution: A = L + D + U and (L + D)xk+1 = −Uxk + b. Hence (L + D)ek+1 = −Uek.

Let G = −(L + D)−1U.

| G = | −1 | 0  | −1 | 0 | α |
| --- | -- | -- | -- | - | - |
|     | −1 | 0  | 0  | α | 0 |
|     | 0  | −α | α  | 1 | 0 |
|     | 0  | 0  | α2 |   |   |

It is easy to show that

| Gm = | 0 | −α2m−1 |
| ---- | - | ------ |
|      | 0 | α2m    |

Hence the if and only if condition is |α| &#x3C; 1. Another way is to find the spectral radius of G:

ρ(G) = |α|2 which again leads to the condition |α| &#x3C; 1.



# 6.3 Eigenvalue problem

This is chapter 12 of the textbook.

Given A ∈ Cn×n, a nonzero vector x ∈ Cn is an eigenvector of A and λ is its corresponding eigenvalue if

Ax = λx.

The characteristic polynomial of A ∈ Cn×n is the degree n polynomial

p(z) = det(zI − A),

whose roots are the eigenvalues.

To find the eigenvalues, one obvious approach is to compute all the coefficients of the characteristic polynomial and then compute its roots. But a small error (can be due to machine round off errors) in the coefficients can produce huge errors in the resulting roots. Hence in practice, this is a bad approach.



# 6.3.1 Power iteration and Rayleigh quotient

Suppose A ∈ Cn×n is diagonalizable, i.e there is X = [x1, ..., xn] such that X−1AX = diag(λ1, ..., λn) and

|λ1| > |λ2 ≥ |λ3 ≥ ... ≥ |λn.

Then A[x1, ..., xn] = [x1, ..., xn]diag(λ1, ..., λn) implies Ai = λixi. So, xi’s are indeed the eigenvectors of A. If xi is an eigenvector, for any complex number α, αxi is also an eigenvector associated with the same eigenvalue. So we can assume ∥xi∥2 = 1 for all i.

Given a vector q0 with ∥q0∥2 = 1, the power method produces a sequence of vectors q(k) as follows:

for j = 1, 2, ...
z(k) = Aq(k−1)
q(k) = z(k)/∥z(k)∥2
λ(k) = q(k),*Aq(k)
end



# Proposition 2

Show that q(ᵏ) = Aᵏ q(0)/∥Aᵏ q(0)∥₂.

Proof: First of all, q(ᵏ) = cAᵏ q(0) with c being some constant number. Then, because ∥q(ᵏ)∥ = 1, c = ¹/∥Aᵏ q(0)∥₂.




# Proposition 3

Suppose q(0) = ∑ aixi and suppose a1 = 0. Prove that there is a number αk that could depend on k such that

∥q(ᵏ) − αkx1∥ = O(λ2k/λ1).

(This result is acceptable because multiplying by αk will not change the direction of x1. The vector can be changed by a constant factor.) Moreover, plugging the above estimates into λ(ᵏ) = q(ᵏ),∗Aq(ᵏ), we conclude

∥λ(ᵏ) − λ1∥ = O(λ2k/λ1).

# Proof:

Since q(0) = ∑ aixi,

Ak q(0) = ∑ aiλkixi = a1λk1x1 + ∑ aiλkixi.

Hence

q(ᵏ) = Ak q(0) = a1λk1x1 + O(λ2k)

∥Ak q(0)∥ = ∥a1λk1x1 + ∑ aiλkixi∥

= eiθᵏ∥x1∥ + O(λ2k)

where we have used the following fact for a vector x = 0 and a small perturbation a that goes to zero:

∥x + a∥ − ∥x∥ = O(a).

Then, λ(ᵏ) = q(ᵏ),∗Aq(ᵏ) = eiθᵏ∥x1∥ + O(λ2k)∗A eiθᵏ∥x1∥ + O(λ2k)

= λ1 + O(λ2k/λ1).





# Convergence of Power Method

This proves the convergence of power method. Power method can only find the largest eigenvalue. In addition, the convergence is linear, which means each iteration reduces the error only by a factor λ₂/λ₁. If the largest two eigenvalues are close in magnitude, the convergence will be very slow. Suppose µ is close to an eigenvalue λJ of A, then (λJ − µ)−1 may be much larger than (λi − µ)−1 for i = J. Then, if we apply power method to (A − µI)−1, the process will converge rapidly to qJ. This idea is called inverse iteration (Chapter 12.1.3 of the textbook).

Given a vector q0 with ∥q0∥2 = 1, the inverse iteration produces a sequence of vectors q(k) as follows:

for k = 1, 2, ...
Solve (A − µI)z(k) = q(k−1)
q(k) = z(k)/∥z(k)∥2
λ(k) = q(k),*Aq(k)
end

Remark: One can show that even though the A − µI can be nearly singular, making solving (A − µI)z(k) = q(k−1) ill-conditioned. But if appropriate method (Gauss elimination would work for most matrices A − µI) is used as a solver, the ratio z(k)/∥z(k)∥2 will not be far from the exact ratio. See “Numerical Linear Algebra” by Trefethen &#x26; Bau for more details.

Suppose λJ is the closest eigenvalue to µ and λK is the second closest. Suppose q(0) has some component in the xJ direction, then, by the same proof for the power method,

∥q(k) − αk xJ∥ = O(µ − λJ)k (µ − λK)

We can combine power iteration and the inverse iteration, the resulting method is called Rayleigh quotient iteration (Chapter 12.1.4 of the textbook).

For given a vector q0 with ∥q0∥2 = 1, compute

λ(0) = q(0),*Aq(0)
k = 1, 2, ...
Solve (A − λ(k−1)I)z(k) = q(k−1)
q(k) = z(k)/∥z(k)∥2
λ(k) = q(k),*Aq(k)
end

For your information, when A is real and symmetric and q(0) is close to xJ, one can prove that (see theorem 27.3 of the book of Trefethen and Bau)

∥q(k+1) − ±ˣJ∥ = O(∥q(k) − ±ˣJ∥3)
and λ(k+1) − λJ = O(λ(k) − λJ3).



# 6.3.2 QR factorization and Gram-Schmidt orthogonalization

(Chapter 12.2 of the textbook.) One algorithmic idea in numerical linear algebra that is more important than all the others is the QR factorization. For any matrix A ∈ Cm×n (m ≥ n) A = QR where Q is m × n with orthonormal columns and R is n × n and is upper triangular. R is upper triangular implies span{first k columns of A} = span{first k columns of R}.

In fact, if A = (a1, ..., an) and Q = (q1, ..., qn) with ai qi the column vectors, then

aj − ∑k=1j−1 rkj qk qj = rjj

From (27), or rij qi = aj, it is clear that rij = q*aj with * being the conjugate transpose. r is chosen so i ≤ j ∥ qj ∥2 = 1.

|rjj| = ∥ aj − ∑k=1j−1 rkj qk ∥2.



Example (This is example on Page 213 of the textbook)

Find the QR factorization of

| A | 1 | -4 |
| - | - | -- |
| = | 2 | 3  |
|   | 2 | 2  |

Solution: a1 = 2. r11 = ∥a1∥2 = 3. q1 = a1/r11 = 2/3.

- a2 = 3 - 2/3 = 5/3.

r12 = (q1 a2) q1 = 2/3.

∥r∥22 = v2 = 5. q2 = v2/r22 = 1/3. So, we get

|   |   | 1   | -4   | 1/3 | -4/15 |
| - | - | --- | ---- | --- | ----- |
| 2 | 3 | 2/3 | 1/3  | 0   |       |
| 2 | 2 | 2/3 | 2/15 |     |       |

Here is the pseudo code for the classical Gram-Schmidt iteration, which unfortunately turns out to be unstable because of rounding errors on a computer.

for j = 1 : n
vj = aj
for i = 1 : j − 1
rij = q∗aj
end
vj = vj − rij qi
rjj = ∥vj∥₂
qj = vj/rjj
end

Every matrix has a QR factorization. If it is full rank, it has a unique QR factorization with rjj > 0.

- qq* Given a column vector q, P⊥q := I - qq* is the projection matrix which maps a vector a to (I - qq*)a that is perpendicular to q.

(To see that, verify that q*(I - qq*)a = 0.) If ∥q∥ = q*q, we can ignore the q*q on the denominator.

a q q* ( - I ) q*q a

q q*a q q*q

Note that for each j, the above algorithm projects aj onto a space orthogonal to span{q1, ..., qj−1}. (From (27), we see that aj - ∑k=1j−1 rkj qk ∝ qj ⊥ qk for k ≤ j − 1.) This projection is denoted by Pj. So in the algorithm vj = aj - ∑k=1j−1 rkj qk = Pjaj. Note that vj = aj - ∑k=1 rkj qk = aj - ∑k=1 qk aj qk = ∑k=1 k

Let Qj−1 = (q1, ..., qj−1), then




j−1 P = I − Q − Q∗ = I − q q∗ = (I − q q∗) = P⊥ P⊥ ...P . j j 1 j−1 k k k k qj−1 qj−2 ⊥q₁

k=1 k=(j−1):−1:1

The modified Gram-Schmidt orthogonalization is based on this decomposition of Pj:

Pjaj = (P⊥qj−₁(P⊥qj−₂...(P⊥q₁aj)...)).

Once qi is generated, it will apply P⊥qi to every column of the current matrix. for i = 1 : n

vi = ai end (note: don’t need ai any more)

for i = 1 : n rii = ∥vi∥₂ qi = vi/rii for j = i + 1 : n (note: don’t need vi any more) rij = q∗vj i

end vʲ = vʲ − rⁱʲ qⁱ end In practice, because of the two notes, it is common to let vi overwrite

ai and let qi overwrite vi: for i = 1 : n rii = ∥ai∥₂ ai = ai/rii for j = i + 1 : n rij = a∗aj i

end aʲ = aʲ − rⁱʲ aⁱ end In the end, the aj is the qj we are looking for.

Example: Consider the matrix A = uv⊤ where u, v ∈ Rⁿ are column vectors. Show that

there is a QR decomposition of A. [Hint: Comparing both sides of the following:

QR = (q₁, ..., qₙ)R = uv⊤.

You are only asked to find one such QR decomposition.] Solution: Let u₁ = ∥ u and find n

orthonormal vectors {u₁, ..., uₙ}. Then Q = (u₁, ..., uₙ) u∥2 ∥ᵘ∥₂ᵛ 0 and R = 0 . . . . 0

# 6.3.3 QR algorithm without shifts

From now on, we will consider the simple case of finding the eigenvalue of A which is real

and symmetric. Here is the QR algorithm without shifts, very simple: Pure QR algorithm

A(0) = A for k = 1, 2, ... Q(ᵏ)R(ᵏ) = A(ᵏ−1) A(ᵏ) = R(ᵏ)Q(ᵏ) end

Note that

A(ᵏ) = R(ᵏ)Q(ᵏ) = Q(ᵏ),⊤A(ᵏ−1)Q(ᵏ). (28)

Remark: In practice, the algorithm need several modifications, including (1) reducing to

tridiagonal/Hessenberg form (2) Instead of A(ᵏ), a shifted matrix A(ᵏ) − µ(ᵏ)I is factored at

each step, while µ(ᵏ) is some eigenvalue estimate. (3) whenever an eigenvalue is found,

break A(ᵏ) into submatrices and apply QR algorithm on each submatrix. We will gradually

introduce those improvements.

We have the following convergence results of the above algorithm, whose proof will not be

given (see Theorem 28.4 in Trefethen and Bau), but we will explain the idea behind this

algorithm in the next subsection.





# Theorem 11

Let the pure QR algorithm be applied to a real symmetric matrix A ∈ Rm×m whose eigenvalues satisfies λ1 > λ2 > ... > λm and whose corresponding eigenvector matrix Q has all nonsingular leading principle submatrices. Then as k → ∞, A(k) converges linearly with constant β = maxj λj+1 to diag(λ1, ..., λm) and Q(1)Q(2) · · · Q(k) (with the sign of its columns adjusted as necessary) converges at the same rate to Q.

# Example:

Let A = QR be a QR decomposition of the matrix A = uv⊤. Show that the matrix RQ is already an upper triangular matrix and find all the eigenvalues of A.

∥u∥2v ∥u∥2v⊤u1 ∥u∥2v⊤u2 · · · ∥u∥2v⊤un

| 0 | 0               | 0 | 0 | 0 |
| - | --------------- | - | - | - |
| 0 | u1, u2, ..., un | 0 | 0 | 0 |
| . | .               | . | . | . |
| . | .               | . | . | . |

So, the eigenvalues are v⊤u, 0, 0, ..., 0 with n - 1 zeros.

The eigenvectors are u1, ..., un.



# 6.3.4 Why the QR algorithm works and its relation to block power iteration

This subsection will not be tested in the exam.

We will relate the QR algorithm to another methods called block power iteration and simultaneous iteration, whose behaviors are more obvious. When reading the following proof/explanation, please keep in mind that there are three key steps to study the convergence of QR method:

1. Q(ᵏ) → Q(ᵏ) where Q comes from the QR factorization used in block power iteration and Q = [q₁, ..., qₘ] is the eigenvector matrix.
2. Q(ᵏ) = Q(ᵏ) where Q comes from QR factorization used in simultaneous iteration.
3. A(ᵏ) = A(ᵏ) where A is defined QᵀAQ which hence converges to diag(λ₁, ..., λₘ).



# Block Power Iteration

Let’s start from the so called block power iteration: Let V(0) be an m × m initial matrix V(0) = (v(0), ..., v(0)) with v(0) the column vector.

V(ᵏ) = Aᵏ V(0) = (v(ᵏ), ..., v(ᵏ)). (29)

Let’s do a QR factorization of V(ᵏ):

Q(ᵏ) R(ᵏ) = V(ᵏ). (30)

Let q₁, ..., qₘ be the eigenvector of A and v(0) = Σi=1m aij qi.

Then v(ᵏ) = Σi=1m λᵏ aij qi.

Because of the assumption |λ₁| > |λ₂| > ... > |λₘ|, v(ᵏ) ≈ span{q₁}, v(ᵏ) ≈ span{q₁, q₂}, ..., vm ≈ span{q₁, ..., qₘ}. Hence one can expect that Q(ᵏ) should converge to Q = (q₁, ..., qₘ). (31)

So, the following convergence result seems to be reasonable (we skip the proof which can be found in Theorem 28.1 of the book of Trefethen and Bau).



# Theorem 12

Consider the iteration (29)–(30) with the same assumption of Theorem 11. We further suppose all the leading principle submatrices of Q⊤V(0) are nonsingular (Q is defined (31)).

Then as k → ∞, the columns of the matrices Q(ᵏ) converges linearly to the eigenvectors of A:

∥q(ᵏ) − ±qj∥ ≤ Cβk for some constant C independent of k.

As k → ∞, the vectors v(ᵏ), ..., v(ᵏ) in the iteration (29)–(30) all converge to multiples of the same dominant eigenvector of A. Thus, although the space they span converges to something useful, these vectors constitute a highly ill-conditioned basis of that space.

The remedy is simple, one must orthonormalize at each step. Thus we will not construct V(ᵏ) as defined above, but a different sequence of matrices Z(ᵏ) with the same column space.




# Simultaneous Iteration

Let Q(0) = I for k = 1, 2, ...

Z(ᵏ) = Q(ᵏ−1) A

Q(ᵏ) R(ᵏ) = Z

end

From the above algorithm, we have

Q(k) = ZR(k) = QR

A2 Q(k-2) R(k-1) = Q R R (by induction)

= Q R R R Ak Q(0) ×

= Q R R R = product of some upper triangular matrices.

So the column spaces of Q(k) equal to the column space of Ak Q(k) [Q(k) Q(k-1) · · · Q(1)]

(32) = Q R R R.

Recall that in (30), we already have

Q(k) R(k) = V = V A(0)

So, if V(0) Q(k) R = V = Q R R R = 0, it is easy to prove that QR factorization is unique under the additional assumption that diagonal entries of R are positive. We will keep the diagonal entries of R be positive when computing the QR factorization. Note that if T1 and T2 are an upper triangular matrix with positive diagonal entries, so is T1 T2. So both R(k) [Q(k) Q(k-1) · · · Q(1)] (32) and R R R in are upper triangular matrices with positive diagonal entries. By the uniqueness of QR factorization, Q(k) = Q.

Hence we can apply Theorem 12 and conclude that Q(k) will converge to the Q defined in (31).

Now, define

A(k) = Q(k) A Q(k)⊤

(33) Since Q(k) converges to Q, A(k) converges to λ1, ..., λn. This shows the convergence of the simultaneous iteration. Now, we want to relate QR algorithm to the simultaneous






# Iteration and Convergence of QR Algorithm

Consider the pure QR algorithm that generates {A(k), Q(k), R(k)}, and the simultaneous iteration that generates {Q(k), R(k)}. Define A(k) by Then A(k) = A(1) A(2).

# Theorem 13

We prove by induction. The case k = 0 is trivial because A(0) = A = A. Suppose it is true for ≤ k − 1. Ak, consider the following two equations that follow from their associated algorithms:

R(k) = Q(k) Q(k)⊤ A(k-1)

R(k) = Q = Q A = Q Q A

(34) and (35) give two QR factorizations of the same matrix A(k-1) (after algorithm), Q, by the uniqueness requiring rjj > 0 in the we have

R(k) = R Q = Q Q Q ... Q

Next, by (28)

A(ᵏ) (k),⊤A(k−1) (k) (k),⊤ ˆ(k−1) (k) (k),⊤ ˆ(k−1),⊤ ˆ(ᵏ−1) (k) = Q Q = Q A Q = Q Q AQ

Q

Q(ᵏ),⊤ Q(1)...Q(ᵏ−1) ⊤ A Q(1)...Q(ᵏ−1) Q(ᵏ) ˆ(ᵏ),⊤A ˆ(ᵏ) = = Q Q

ˆ(ᵏ) = A.

The second equality is by induction. The third equality is by definition. The last equality is by definition (33). □





# 6.3.5 Real Schur decomposition and the QR algorithm

Although the pure (or unshifted) QR is an improved version of Power Iteration, the conditions required by Theorem 11 are strict, a couple of improvements are needed to make this eigenvalue finder work more generally—for example, in the case of nonsymmetric matrices. One problem, which also occurs for symmetric matrices, is that unshifted QR is not guaranteed to work in the case of a tie for dominant eigenvector. An example of this is

A = 0 1, 1 0

which has eigenvalues 1 and −1. Another form of “tie” occurs when the eigenvalues are complex. For example,

A = −0 1, 1 0

Nothing in the definition of the unshifted QR algorithm allows for the computation of complex eigenvalues. Furthermore, unshifted QR does not make use of the trick of Inverse Power Iteration. We found that Power Iteration could be speeded up considerably with this trick, and we want to find a way to apply the idea to our new implementation. These refinements are applied next, after introducing the goal of the QR algorithm, which is to reduce the matrix A to its real Schur form.

You may have learned the following theorem in linear algebra




# Theorem 14 (Schur decomposition)

For every matrix A ∈ Cⁿ×ⁿ, there is a unitary matrix Q and an upper-triangular T so that

A = QT Q∗.

# Proof:

We prove by induction on the dimension of A. Let x be any eigenvector of A, with corresponding eigenvalue λ and ∥x∥₂ = 1. Starting from x, formulate a unitary matrix U with x being its first column. One can check that

U∗AU = λ B .

0 C

By the inductive hypothesis, there exists a Schur decomposition C = V T V∗. Now define

Q = U 1 0

0 V

Q is a unitary matrix and satisfies

Q∗AQ = λ BV

0 T

But if we only deal with real numbers, we have to allow 2× 2 blocks on the main diagonal.





# Theorem 15 (Real Schur decomposition)

If A ∈ Rⁿ×ⁿ, then there exists an orthogonal Q ∈ Rⁿ×ⁿ such that

A = Q R₁₁ R₁₂ · · · R₁ₘ

0 R₂₂ · · · R₂ₘ Q⊤.

0 0 · · · Rₘₘ

where each Rii is either a 1 × 1 real number or a 2 × 2 real matrix (in the latter case det(xI − Rii) has two complex conjugate roots).




Proof:

Let k be the number of complex conjugate pairs of eigenvalues of A ∈ Rn×n. We prove by induction on k. If λ = γ + iµ is a complex eigenvalue, then there exist vectors y, z ∈ Rn×1 so that A(y + iz) = (γ + iµ)(y + iz).

By equating the real and complex parts on both sides, we get

| A       | \[y, z] |   |
| ------- | ------- | - |
| \[y, z] | γ       | µ |
| −µ      | γ       |   |

So span(y, z) is a 2-dimensional, real invariant subspace18 of A. By Gram-Schmidt, we can find v1 ⊥ v2, ∥v1∥2 = ∥v2∥ = 1, and span(v1, v2) = span(y, z). Extend them to B = {v1, v2, · · · , vn} which is an orthonormal basis of Rn. Define U = [v1, v2, v3, · · · , vn] which is real and orthogonal. Av1, Av2 ∈ span(v1, v2) implies that

| A | U   |   |
| - | --- | - |
| U | R11 | B |
| 0 | C   |   |

By the inductive hypothesis, there exists a real Schur decomposition C = V T V⊤. Now define

| Q | =    |   |
| - | ---- | - |
| U | I2×2 | 0 |
| 0 | V    |   |





# QR Algorithm and Shifted QR Algorithm

Q is a real orthogonal matrix and satisfies

Q⊤AQ = R11BV.

The full QR algorithm iteratively moves an arbitrary matrix A toward its Schurization by a series of similarity transformations. We will proceed in two stages. First we will install the inverse power iteration idea with shifts and add the idea of deflation to develop the shifted QR algorithm. Then we will develop an improved version that allows for complex eigenvalues.

The shifted version is straightforward to write. Each step consists of applying the shift, completing a QR factorization, and then taking the shift back. In symbols,

A0 − sI = Q1R1

A1 = R1Q1 + sI.

Note that A1 and A0 have the same eigenvalues because A1 − sI = R1Q1 = Q⊤(A0 − sI)Q1 = Q⊤A0Q1 − sI.

What are good choices for the shift s? This leads us to the concept of deflation for eigenvalue calculations. We will choose the shift to be the bottom right entry of the matrix Ak. This will cause the iteration, as it converges to real Schur form, to move the bottom row to a row of zeros, except for the bottom right entry. After this entry has converged to an eigenvalue, we deflate the matrix by eliminating the last row and column. Then we proceed to find the rest of the eigenvalues.

The following is the Matlab implementation. At each step, we apply a shifted QR step, and then check the bottom row. If all entries are small except the diagonal entry ann, we declare that entry to be an eigenvalue and deflate by ignoring the last row and last column for the rest of the computation.

% Program 12.6 Shifted QR Algorithm, preliminary version
function lam=shiftedqr0(a)
tol=1e-14;
m=size(a,1);
lam=zeros(m,1);
n=m;
while n>1
while max(abs(a(n,1:n-1)))>tol
mu=a(n,n); % define shift mu
[q,r]=qr(a-mueye(n));
a=rq+mu*eye(n);
end
lam(n)=a(n,n); % declare eigenvalue
n=n-1; % decrement n
a=a(1:n,1:n); % deflate
end
lam(1)=a(1,1); % 1x1 matrix remains



# 12.7 Shifted QR Algorithm, general version

One can try for example

lam=shiftedqr0([3,2;1,4])

lam = 2.000 5.000

Finally, to allow for the calculation of complex eigenvalues, we must allow for the existence of 2 × 2 blocks on the diagonal of the real Schur form. The improved version of the shifted QR algorithm given in Program 12.7 tries to iterate the matrix to a 1 × 1 diagonal block in the bottom right corner; if it fails (after a user-specified number of tries), it declares a 2 × 2 block, finds the pair of eigenvalues, and then deflates by 2. This improved version will converge to real Schur form for most, but not all, input matrices.

Computes real and complex eigenvalues of square matrix

Input: matrix a

Output: eigenvalues lam

function lam=shiftedqr(a)
tol=1e-14;kounttol=500;
m=size(a,1);lam=zeros(m,1); n=m;
while n>1
kount=0;
while max(abs(a(n,1:n-1)))>tol &#x26;&#x26; kount<kounttol ...="" end="" &#x3C;="" code=""></kounttol>
One can try

lam=shiftedqr([3,2,1;1,4,2;-3,-4,1])

lam = 3.1173 - 2.6974i 3.1173 + 2.6974i 1.7654 + 0.0000i

Even in its general form, the shifted QR algorithm fails for the following example:

0 0 0 1
0 0 -1 0
0 1 0 0
-1 0 0 0

Matrices like this one, with a repeated complex eigenvalue, may not be moved into real Schur form by shifted QR. The extra assistance needed for these more difficult examples is to replace A by a similar matrix in upper Hessenberg form,



# 6.3.6 Household reflection

Given A = [x₁, x₂, ..., xₙ], we want to find a symmetric orthogonal matrix F so that F A = [F x₁, F x₂, .., F xₙ] is something like

. . . • . . . . . .

F A = 0 F x₂ F x₃ F x₄ . . . . . . . 0 . . . . . . 0 . . . . . .

For any x ∈ Rⁿ, if F is orthogonal, ∥x∥² = x⊤x = (F x)⊤(F x) = ∥F x∥². So, for w = F x to become [•, 0, .., 0]⊤, we must have

w = F x = [±∥x∥₂, 0, 0, ...]⊤ = ±∥x∥₂e₁. (36)



# 6.3.7 Reduction to Hessenberg matrices

How can we find an explicit form of F? Take + sign for the moment. Notice that ∥x∥₁e₁ is the vector on the first axis. Let v = ∥x∥₂e₁ − x. Let H being the hyperplane (passing zero) perpendicular to v. So, H is the plane right in the middle between x and w = F x = ∥x∥₂e₁. Then F x is the reflection of x respect to the plane H. We know (I − vv⊤ )a is the projection of a onto H. So, we go exactly twice as far in the same direction to get reflection. So, F x = (I − 2 vv⊤ )x.

It is easy to verify that this F is symmetric and orthogonal. Recall that in (36) we can select from ±. For numerical stability, it is desirable to reflect x to the vector ±∥x∥₂e₁ that is not too close to x itself. So, we take −sign(x₁)∥x∥₂e₁ where x₁ is the first component of x. So, v = −sign(x₁)∥x∥₂e₁ − x. Because we only need v⊤v and vv⊤, we take v = sign(x₁)∥x∥₂e₁ + x.

Comparing the following two ways to do Householder reflector in order to put as many zeros into a matrix as possible while preserving its eigenvalues.

Bad approach:

| \*  | \* | \* | \* | \* | ×  | × | ×        | × | × |
| --- | -- | -- | -- | -- | -- | - | -------- | - | - |
| \*  | \* | \* | \* | \* | ⊤  | 0 | ×        | × | × |
| A = | \* | \* | \* | \* | \* | → | Q₁ A =   | 0 | × |
| \*  | \* | \* | \* | \* | 0  | × | ×        | × | × |
| \*  | \* | \* | \* | \* | 0  | × | ×        | × | × |
| \*  | \* | \* | \* | \* | •  | • | •        | • | • |
| ⊤   | •  | •  | •  | •  | •  | → | Q₁ AQ₁ = | • | • |
| •   | •  | •  | •  | •  | •  | • | •        | • | • |

Good approach: Let Q = 1 0.

| 1   | ˜  | 0  | Q₁ |    |    |    |        |    |    |
| --- | -- | -- | -- | -- | -- | -- | ------ | -- | -- |
| \*  | \* | \* | \* | \* | \* | \* | \*     | \* | \* |
| \*  | \* | \* | \* | \* | ⊤  | ×  | ×      | ×  | ×  |
| A = | \* | \* | \* | \* | \* | →  | Q₁ A = |    | 0  |





Certainly the 2nd approach can be continue until we get the Hessenberg form.

# Definition 5

A matrix H = (hij) is called upper Hessenberg if hij = 0 when i > j + 1, i.e., it looks like

| \* | \* | \* | \* | \* |    |    |
| -- | -- | -- | -- | -- | -- | -- |
| \* | \* | \* | \* | \* |    |    |
|    |    | 0  | \* | \* | \* |    |
|    | 0  | 0  | \* | \* |    |    |
|    |    | 0  | 0  | 0  | \* | \* |

The above “Good approach” shows that we can have the following result:

# Theorem 16

For any A ∈ Rn×n, there is an orthogonal matrix Q and an upper Hessenberg matrix H so that A = QHQ⊤.





# Example

Put 3 5 −⁵ into upper Hessenberg form.




# Solution:

This is the Example on Page 241 of the textbook, but we pickup a different sign for w. Let x = [3, 4]⊤. v = sign(x₁)∥x∥₂e₁ + x = [8, 4]⊤. The Householder reflector

| H₁ = I − vv⊤ | −0.⁶ | −0.⁸ |
| ------------ | ---- | ---- |
| 2 v⊤v =      | −0.8 | 0.⁶  |

Therefore,

| H₁x = | \[− 0]⊤ | 5,   |      |
| ----- | ------- | ---- | ---- |
| 1     | 0       | 0    |      |
| H₁A = | 0       | −0.⁶ | −0.⁸ |
| 0     | −0.8    | 0    | −5   |
| 0     |         | 0    | −4   |
|       | 4       |      |      |

and

| A = H₁AH₁ = | −⁵ | −0.6 | 4.² |
| ----------- | -- | ---- | --- |
|             | 0  | −0.8 | 5.⁶ |

By the way, the above result, even though different from the one in the textbook, is the same as the one produced by the following Matlab code

% Program 12.8 Upper Hessenberg form
% Input: matrix a
% Output: Hessenberg form matrix a and reflectors v
% Usage: [a,v]=hessen(a) yields similar matrix a of
% Hessenberg form and a matrix v whose columns hold
% the v’s defining the Householder reflectors.
function [a,v]=hessen(a)
[m,~]=size(a);
v=zeros(m,m);
for k=1:m-2
x=a(k+1:m,k);
v(1:m-k,k)=-sign(x(1)+eps)norm(x)eye(m-k,1)-x;
v(1:m-k,k)=v(1:m-k,k)/norm(v(1:m-k,k));
a(k+1:m,k:m)=a(k+1:m,k:m)-2v(1:m-k,k)v(1:m-k,k)’a(k+1:m,k:m);
a(1:m,k+1:m)=a(1:m,k+1:m)-2a(:,k+1:m)v(1:m-k,k)v(1:m-k,k)’;
end
hessen([2 1 0;3 5 -5;4 0 0])
ans =
2.0000 -0.6000 -0.8000
-5.0000 -0.6000 4.2000
0 -0.8000 5.6000

Thus, we finally have a complete method for finding all eigenvalues of an arbitrary square matrix A. The matrix is first put into upper Hessenberg form with the use of a similarity transformation (Program 12.8), and then the shifted QR algorithm is applied (Program 12.7). The Matlab eig command provides accurate eigenvalues based on this progression of calculations.





# 6.3.8 Least square solution to linear systems of equations

In some cases, the number of equations we want to solve is greater than the number of unknowns we are looking for. We can not find a solution that satisfies all the equations. For example

| 1 | −⁴ x₁ | −³   |
| - | ----- | ---- |
| 2 | 3 x₂  | = 15 |
| 2 | 2     | 9    |

We write the above equation as Ax = f even though we cannot find such an x so that Ax = f. The idea is to find x so that the distance between the two vectors Ax and f are as small as possible. Here we assume A ∈ Rᵐ×ⁿ, x ∈ Rⁿ×¹ and f ∈ Rᵐ×¹.

We can define the distance between two vectors a = (a₁, ..., aₘ)⊤ and b = (b₁, ..., bₘ)⊤:

m

dist(a, b) = ∥a − b∥₂ = ∑j=1m (aj − bj)².

The x that minimizes ∥Ax − f∥₂ (or equivalently, minimizes ∥Ax − f∥²) is called the least square solution of Ax = b. We recognize ∥a∥² = m ∑j=12 aj² = a⊤a.

Hence

∥Ax − f∥² = (Ax − f)⊤(Ax − f) = (x⊤A⊤ − f⊤)(Ax − f) = x⊤(A⊤A)x − 2x⊤A⊤f + f⊤f.

where we have used the fact that f⊤Ax = (x⊤A⊤f)⊤ = x⊤A⊤f since x⊤A⊤f is a scalar.



# Theorem 17

The x which minimizes ∥Ax − f∥² should satisfy

A⊤Ax = A⊤f.

(The above equation is called the normal equations for least squares).

Proof: ∇x (∥Ax − f∥²) = 0. It is easy to check that the gradient is 2(A⊤A)x − 2A⊤f, hence we obtain (39). □



# Proposition 4

Suppose A ∈ Rm×n (m ≥ n) and rank(A) = n. Prove that A⊤Ax = b has a solution and the solution is unique.

Proof: For finite dimensional system Bx = b, existence and uniqueness are equivalent (both related to det(B) = 0). So, we only need to show uniqueness. If A⊤Ax = 0 for some x = 0, then (Ax)⊤(Ax) = 0. So Ax = 0 ∈ Rm which implies that the column vectors of A are linearly dependent. It contradicts to the assumption that A has rank n which means A has n linearly independent columns or rows. □




# Example 1

Use the normal equations to find the least square solutions of (37). (This is example on Page 192 of the textbook.)





# Solution:

A⊤A =
| 9 | 6  |
| - | -- |
| 6 | 29 |

A⊤f =
| 45 | 75 |
| -- | -- |

So x = [3.8, 1.8]⊤. □




# Example 2

(least squares and Rayleigh quotient) Given any matrix A ∈ Rn×n and vector u ∈ Rn, what is the least square solution to ux = Au?





Solution:

u⊤ux = u⊤Au. x = u⊤Au is the Rayleigh quotient.

u⊤u



# Proposition 5

(QR factorization and least squares) Let A ∈ Rm×n (m ≥ n) has rank n. Suppose we want to solve A⊤Ax = A⊤b. Suppose there is a QR factorization of A: A = QR where Q ∈ Rm×n and R ∈ Rn×n. Prove that x satisfies Rx = Q⊤b. Since R is a triangular matrix, Rx = Q b can be easily solved by backward substitution.




Proof:

Recall that n = rank(QR) ≤ min(rank(Q), rank(R)) = min(n, rankR). Hence rankR = n. Hence the n × n matrix R is invertible.

A⊤Ax = A⊤b becomes R⊤Q⊤QRx = R⊤Q⊤b. Note that Q⊤Q = I ∈ Rn×n. So R⊤Rx = RQ⊤b. Since R⊤ ∈ Rn×n is invertible, the previous equation implies Rx = Q⊤b.






Remark:

Please note the difference between the above method and the one on Page 217 of the textbook. In the textbook, they use full QR factorization, while our QR factorization is the reduced QR factorization in the textbook.

The condition number of A⊤A in the normal equation is about square of that of A. As mentioned on Page 196 and Page 217 of the textbook, the advantage of using QR approach to solve least squares problem is to avoid A⊤A which is more ill-conditioned comparing with the original A.





# Example 3

(This is the Example on Page 217 of the textbook) Solve the least square problem

| 1 | −4 | x1 | −3 |    |
| - | -- | -- | -- | -- |
| 2 | 3  | x2 | =  | 15 |
| 2 | 2  |    |    | 9  |

Solution: Recall that from a previous example, we have the QR decomposition

| 1 | −4 | 1/3 | −14/15 | 3    | 2 |   |
| - | -- | --- | ------ | ---- | - | - |
| 2 | 3  | =   | 2/3    | 1/3  | 0 | 5 |
| 2 | 2  |     | 2/3    | 2/15 |   |   |

Hence we just need to solve

| 3 | 2 | x1 | = | 1/3    | 1/3 | 2/3  | ⊤  | −3 | 15 |
| - | - | -- | - | ------ | --- | ---- | -- | -- | -- |
| 0 | 5 | x2 | = | −14/15 | 1/3 | 2/15 | 15 | =  | 9  |

The solution is x1 = 3.8 and x2 = 1.8.



# 6.3.9 Homework 13

1. (Sauer) Page 538, 12.1 Exercises, 2(a), 9
2. (Sauer) Page 547, 12.2 Exercises, 1, 3, 4
3. Compute by hand the QR decomposition of

| 4  | 3  | 1 |
| -- | -- | - |
| −5 | −3 | 0 |
| 3  | 2  | 1 |

(Fitting models to data) Let (t₁, f₁), ..., (tₘ, fₘ) be a set of points in the plane. Given a fixed class of model y = g(t), such as all lines y = at + b, or all parabolas y = a + bt + ct², we want to locate the specific instance of the model that "best fits" the data points. The least square fitting means we want to select the parameters of the model (e.g. the (a, b) in the line model or the a, b, c in the parabola so that f - g(t)² is minimized. Derive the general formula for a and b if our model is y = at + b. The solution is provided for you to check your answer.

Solution: Let F(a, b) = ∑i=1m (fi - ati - b)². Then we should have ∂ₐF(a, b) = 0 and ∂bF(a, b) = 0. Solving the resulting system of equations, we obtain

a = (∑i ti fi - m t̄ f̄) / (∑i ti² - m t̄²), b = f̄ - a t̄.





# 6.3.10 Computer Project 4

1. Read the reality check on Page 549 of the textbook. Write your own power method code and use it to compute the eigenvector of the G-matrix, given the A-matrix on page 550, with initial vector q(0) = [1, 0, 0, ..., 0]⊤. [4 marks]





# 2.

Write your own pure (unshifted) QR algorithm code by directly calling the QR position function in Matlab. Use it to find all the eigenvalues of

| 4 | 3  | 1 | -7 |
| - | -- | - | -- |
| 3 | -3 | 0 | -8 |
| 1 | 0  | 1 | -8 |

[4 marks]

Explain why the pure QR method does not work for

| 4  | 3  | 1 |
| -- | -- | - |
| -5 | -3 | 0 |
| 3  | 2  | 1 |

[2 marks]



# 7 Least Squares, Trigonometric Interpolation and FFT

# 7.1 Fitting models to data

This is from Sections 4.1.2, 4.2.2 of Sauer. Let (t₁, f₁), ..., (tₘ, fₘ) be a set of points in the plane. Given a fixed class of model y = g(t), such as all lines y = at + b, or all parabolas y = a + bt + ct², we want to locate the specific instance of the model that “best fits” the data points. The least square fitting means we want select the parameters of the model (e.g. the (a, b) in the line model or the (a, b, c) in the parabola model) so that ∥ ⃗ − (⃗ ∥² m | − |² f f t)² = ∑i=1m fi g(ti) is minimized.



# Example 1

Find the straight line that best fit the 4 data points (−1, 1), (0, 0), (1, 0), (2, −2).




# Solution:

Let the line be g(t) = at + b. We need to solve

| A | f  |    |
| - | -- | -- |
| 1 | −1 | 1  |
| 1 | 0  | 0  |
| 1 | 1  | 0  |
| 1 | 2  | −2 |

We cannot find a solution to make Ax = f. So, we take one step back and are satisfied if we can find x so that the ∥ · ∥₂ distance between Ax and f are minimized. We can either use ∇ₓ∥ᴬˣ − f∥² = 0 or notice Ax − f ⊥ column space of A since Ax is the best approximation to f in the column space of A. Either way, we get the normal equation A⊤A = A⊤f with

| A⊤A | A⊤f |    |
| --- | --- | -- |
| 4   | 2   | −1 |
| 2   | 6   | −5 |

So x = (A⊤A)−1A⊤f = (¹, −9)⊤.





# Example 2

Find the parabola that best fit the 4 data points (−1, 1), (0, 0), (1, 0), (2, −2).



Solution:

The model is g = a + bt + ct². Substitution of the data points into the model yields, we see that we need to solve

| A | 1 | -1 | 1 |
| - | - | -- | - |
| 1 | 0 | 0  |   |
| 1 | 1 | 1  |   |
| 1 | 2 | 4  |   |

We have:

| f | 1  |
| - | -- |
|   | 0  |
|   | 0  |
|   | -2 |

One can check that we cannot find x = (a, b, c) that satisfies the above 4 equations. We know the x satisfies A⊤Ax = A⊤f which is

|   | 4 | 2 | 6  | a | -¹ |
| - | - | - | -- | - | -- |
|   | 2 | 6 | 8  | b | -⁵ |
|   | 6 | 8 | 18 | c | -⁷ |

The solution is (a, b, c) = 9 , − 13 , − 1 . □

Note that the exponential model y = c₁eᶜ²ᵗ cannot be directly fit by least squares cause c₂ does not appear linearly in the model equation. To overcome the difficulty, we use ln y = ln c₁ + c₂t. Similarly, for y = c₁tᶜ², we use ln y = ln c₁ + c₂ ln t.



# Example 3

The number of transistors on Intel central processing units since the early 1970s is given in the table that follows. Fit the model y = c₁eᶜ²ᵗ to the data.

| CPU         | year | transistors |
| ----------- | ---- | ----------- |
| 4004        | 1971 | 2,250       |
| 8008        | 1972 | 2,500       |
| 8080        | 1974 | 5,000       |
| 8086        | 1978 | 29,000      |
| 286         | 1982 | 120,000     |
| 386         | 1985 | 275,000     |
| 486         | 1989 | 1,180,000   |
| Pentium     | 1993 | 3,100,000   |
| Pentium II  | 1997 | 7,500,000   |
| Pentium III | 1999 | 24,000,000  |
| Pentium 4   | 2000 | 42,000,000  |
| Itanium     | 2002 | 220,000,000 |
| Itanium 2   | 2003 | 410,000,000 |




Solution:

The model is rewritten as

ln y = k + c₂t.

k + 33c₂ = ln 410000000

The matrix equation is Ax = b and the normal equation A⊤Ax = A⊤b is

| 13  | 235  | k = 176.90   |
| --- | ---- | ------------ |
| 235 | 5927 | c₂ = 3793.23 |

which has solution k ≈ 7.197 and c₂ ≈ 0.3546. Hence c₁ = ek ≈ 1335.3. The exponential curve y = 1335.3e0.3546t is shown in Figure along with the data. The doubling time for the law is ln 2/c₂ ≈ 1.95 years. Gordon C. Moore, cofounder of Intel, predicted in 1965 that over the ensuing decade, computing power would double every 2 years.

Figure 2: Semilog Plot of Moore’s Law. Number of transistors on CPU chip versus year.




# 7.2 Least squares approximation of a function

It turns out least squares idea can also be used to approximate a given function on an entire interval. (So, we are given a function instead of a discrete data set.)






# Example 4

Following the outlined steps to find the least square polynomial approximation of the form

P(x) = ax² + b on the interval [0, 1] for the function f(x) = √(1 − x²) and then use the result to approximate the value of √0.21.





# 7.3 Least square fitting with trigonometric functions

This is from Section 4.2.1 of Sauer. Periodic data call for periodic model. Outside air temperatures, for example, obey cycles on numerous time scales. As a first example, hourly temperatures data are fit to sines and cosines.



# Example 5

Fit the recorded temperatures in Washington DC on January 1, 2001, as listed in the following table to a periodic model *y = c₁ + c₂ cos(2πt) + c₃ sin(2πt)*

| Time (t) | Temperature (°F) |
| -------- | ---------------- |
| 0:00     | 30               |
| 1:00     | 29               |
| 2:00     | 28               |
| 3:00     | 27               |
| 4:00     | 26               |
| 5:00     | 25               |
| 6:00     | 24               |
| 7:00     | 25               |
| 8:00     | 28               |
| 9:00     | 30               |
| 10:00    | 32               |
| 11:00    | 34               |
| 12:00    | 36               |
| 13:00    | 38               |
| 14:00    | 40               |
| 15:00    | 42               |
| 16:00    | 43               |
| 17:00    | 41               |
| 18:00    | 39               |
| 19:00    | 37               |
| 20:00    | 35               |
| 21:00    | 33               |
| 22:00    | 31               |
| 23:00    | 30               |

| time of day | t | temp. (C) |
| ----------- | - | --------- |
| 12 mid.     | 0 | −2.²      |
| 3 am        | 1 | −2.⁸      |
| 6 am        | 1 | −4        |
| 9 am        | 3 | −8        |
| 12 noon     | 1 | 2         |
| 3 pm        | 5 | 8         |
| 6 pm        | 3 | −4        |
| 9 pm        | 7 | −8        |

Solution: Substituting the data into the model *y = c₁ + c₂ cos(2πt) + c₃ sin(2πt)* results in the following inconsistent system of linear equations.




c₁ + c₂ cos(2π0) + c₃ sin(2π0) = −2.2

c₁ + c₂ cos(2π(1/8)) + c₃ sin(2π(1/8)) = −2.8

c₁ + c₂ cos(2π(1/4)) + c₃ sin(2π(1/4)) = −6.1

c₁ + c₂ cos(2π(7/8)) + c₃ sin(2π(7/8)) = 1.1

which can be put into the form of Ax = f with

| 1 | 1    | 0    | −2.² |
| - | ---- | ---- | ---- |
| 1 | √₂/₂ | √₂/₂ | −2.⁸ |
| 1 | 0    | 1    | −6.¹ |

A =

| 1 | −√₂/₂ | √₂/₂ |   | − | ----- | ----- |   | 1 | √−1 | 0 |   | 1 | −2/2 | −√₂/₂ |
| - | ----- | ---- | - | - | ----- | ----- | - | - | --- | - | - | - | ---- | ----- |
| 1 | 0     | −1   |   | 1 | √₂/₂  | −√₂/₂ |   |   |     |   |   |   |      |       |

So, we cannot find a solution x to satisfy Ax = f. Again, by minimizing ∥Ax − f∥², we obtain the normal equations A⊤Ax = A⊤f:

| 8 | 0 | 0 | c₁ | −15.⁶    |
| - | - | - | -- | -------- |
| 0 | 4 | 0 | c₂ | 2.9778   |
| 0 | 0 | 4 | c₃ | −10.²³⁷⁶ |

So we obtain (c₁, c₂, c₃) = (−1.95, −0.7445, −2.5594) and the best version of the model, in the sense of least squares, is

y = −1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt).





# Example 6 Fit the temperature data to the improved model

y = c₁ + c₂ cos 2πt + c₃ sin 2πt + c₄ cos 4πt.




# 1

0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1 0 0.2 0.4 0.6 0.8 1

# Figure 3:

Left: Plot of Example 5 (y = −1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt)). Right: Plot of Example 6 (y = −1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt)).

Solution: The system of equations is now

c₁ + c₂ cos(2π0) + c₃ sin(2π0) + c₄ cos(4π0) = −2.2

c₁ + c₂ cos(2π(1/8)) + c₃ sin(2π(1/8)) + c₄ cos(4π(1/8)) = −2.8

c₁ + c₂ cos(2π(1/4)) + c₃ sin(2π(1/4)) + c₄ cos(4π(1/4)) = −6.1

c₁ + c₂ cos(2π(7/8)) + c₃ sin(2π(7/8)) + c₄ cos(4π(7/8)) = 1.1

or Ax = b with

| A = | 1    | 1    | 0    | 1    |
| --- | ---- | ---- | ---- | ---- |
| b = | −2.2 | 1    | √₂/₂ | √₂/2 |
|     | 0    | −2.8 | 1    | 0    |
|     | 1    | −1   | −6.1 |      |

The normal equation is

| 8 | 0 | 0 | 0 | c₁ = −15.6   |
| - | - | - | - | ------------ |
| 0 | 4 | 0 | 0 | c₂ = −2.9778 |
| 0 | 0 | 4 | 0 | c₃ = 10.2376 |
| 0 | 0 | 0 | 4 | c₄ = 4.5     |

The solutions are c₁ = −1.95, c₂ = −0.7445, c₃ = −2.5594, and c₄ = 1.125. □

Now, if we compare Figure 1 with Figure 3, we see that if we use polynomial to do the least square fitting, when we increase the degree of the polynomial, all coefficients change. But if we use trig function and increase the number of trig functions included in the model, the old coefficients stay the same. For the current case, it is obvious that this is because the columns of A are orthogonal. We will further explain and extend this to more general cases in our last chapter (Trig interpolation and fast Fourier transform).





# 7.4 Discrete Fourier transform

This is from Section 10.1 of the textbook. Here is a key identity that we will need later to simplify our computations of the Discrete Fourier Transform (DFT).




# Lemma 1

Let ω = e−i 2π where n is an integer, n > 1. Then

1 + ω + ω² + · · · + ωn−¹ = 0. (2)

Proof: Geometrically, this identity is obvious since its left hand side is the resultant force at the origin, which obviously is zero by the symmetry. To prove it mathematically is also simple. Using the formula that 1 + r + r² + · · · + rk = (1−rk+1) / (1−r),

1 + ω + ω² + · · · + ωn−¹ = 1 − ωn = 0. □

1 − ω

A similar method of proof shows that

1 + ω² + ω⁴ + · · · + ω2(n−1) = 0

1 + ω³ + ω⁶ + · · · + ω3(n−1) = 0

− 2(−1) (−1)( · · · · · · 1 + ωn 1 + ωn−1) = 0.

The next one is different:

1 + ωn + ω2n + · · · + ωn(n−1) = 1 + 1 + 1 + · · · + 1 = n.

This information is collected into the following Lemma






# Lemma 2

Let ω = e−i 2π where n is an integer, n > 1 and let k be an integer. Then

| n−1 | ωjk | = n | if k/n is an integer |
| --- | --- | --- | -------------------- |
| j=0 |     | 0   | otherwise.           |






# Definition 1

The Discrete Fourier Transform (DFT) of x = [x0, x1, ..., xn−1]⊤ is the dimensional vector y = [y0, y1, ..., yn−1]⊤ defined by (ω = e−ⁱ²π/n)

yk = √n ∑j=0n−1 xjωjk. (4)






# Theorem 1 (inverse DFT)

With the y defined by (4), i.e, y = 1 n−1 x ωjk for k = 0, ..., n − 1,

k n−1 k √n j=0 j

1 −jk

xₖ = √n j=0 yjωjk.






# Proof:

When y = 1n−1 x ωℓj and when k = 0, ..., n − 1,

j ~√~n ℓ=0 ℓ

1n−1 −jk 1n−1 −jk 1n−1 ℓj 1n−1 n−1 j(ℓ−k)

√ₙ j=0 ωj yj = √n j=0 ωℓ √ₙ ℓ=0 xℓωj = n ℓ=0 xℓ j=0 ω = xₖ.

In the last step, we have used the fact that ℓ − k ∈ {−n + 1, −n + 2, ..., n − 1} and (3). So, all the terms in n−1 vanish except when ℓ = k. □






# Now introduce the Fourier matrix

| ω0 | ω0   | ω0      | · · · | ω0          |         |
| -- | ---- | ------- | ----- | ----------- | ------- |
| ω0 | ω1   | ω2      | · · · | ωn−1        |         |
| 1  | ω0   | ω2      | ω4    | · · ·       | ω2(n−1) |
| √n | ω0   | ω3      | ω6    | · · ·       | ω3(n−1) |
| .  | .    | .       | .     | .           | .       |
| .  | .    | .       | .     | .           | .       |
| .  | .    | .       | .     | .           | .       |
| ω0 | ωn−1 | ω2(n−1) | · · · | ω(n−1)(n−1) |         |

and note that ω−jk = ωjk (the conjugate). We realize that we can write (4) as y = Fnx. For example, with k = 2 in (4), y = 1/nn−1x ωj2 = 1/√n (ω0x + ω2x + · · · + ω2(n−1)x).

Similarly, we can write (5) as x = Fny. So, the inverse of matrix Fn is its conjugate matrix Fn. Or equivalently, FnFn = I. Now, consider x = F−1y = Fny = Fny.

Since Fn and Fn are symmetric, FnFn = I implies F⊤Fn = I.

Then ∥Fnx∥² = Fnx⊤Fnx = x⊤F⊤Fnx = x⊤x = ∥x∥².

Thus the magnitude of the vector x is unchanged upon DFT.





# Example 7

Find the DFT of the vector *x* = [1, 0, −1, 0]⊤.




# Solution:

n = 4. ω = e-i2π/4 = -i. Applying the DFT, we obtain

| y0 | 1 | 1  | 1  | 1  |    |    |    |    |    |
| -- | - | -- | -- | -- | -- | -- | -- | -- | -- |
| y1 | 1 | 1  | ω  | ω2 | ω3 | 0  |    |    |    |
| y2 |   |    | =  | √4 | 1  | ω2 | ω4 | ω6 | -1 |
| y3 | 1 | ω3 | ω6 | ω9 | 0  |    |    |    |    |

=

| 1 | 1 | -i | -1 | i | 0  |    |   |
| - | - | -- | -- | - | -- | -- | - |
|   | 2 | 1  | -1 | 1 | -1 | -1 | 0 |
| 1 | i | -1 | -i | 0 | 1  |    |   |

□






# Proposition 1

Let y = (y₀, ..., yₙ−₁)⊤ be the DFT of x = (x₀, ..., xₙ−₁)⊤ where xj’s are real numbers. Prove (1) y₀ is real and (2) yₙ−ₖ = yₖ for k = 1, ..., n − 1.

Proof: y = 1 (x + x + · · · + x ) ∈ R.

0 ~~√~~n 0 1 n−1

ω = e−ⁱ²π/n. Hence ω−ʲᵏ = ωʲᵏ and ωʲⁿ = 1

yₙ−ₖ = √n Σj=0n−1 xjωj(n−k) = √n Σj=0n−1 xjωjk = √n Σj=0n−1 xjωjᵏ

where in the last step, we have used the fact that xj ∈ R. Finally, we recognize that the last expression is exactly yₖ.





# 7.5 Fast Fourier Transform

From the matrix vector multiplication form, we see that the DFT applied to an n-vector requires O(n²) operations. In 1965, Cooley and Tukey found a way to accomplish the DFT in O(n log n) operations in an algorithm called the fast Fourier transform (FFT). The popularity of the FFT for data analysis followed immediately. The field of signal processing converted from primarily analog to digital largely due to this algorithm. We will explain their method and how its superiority to the naive DFT through an operation count.

We will show how to compute z = Mₙx recursively, where Mₙ = √nFₙ. To complete the DFT requires dividing by √n, or y = Fₙx = z/√n.

We start by showing how the n = 4 case works, to get the main idea across. The general case will then clear. For n = 4, ω = e−ⁱ²π/⁴ = −i. The z = Mₙx is

| z₀ | 1 | 1  | 1  | 1  | x₀ |
| -- | - | -- | -- | -- | -- |
| z₁ | 1 | ω  | ω² | ω³ | x₁ |
| z₂ | 1 | ω² | ω⁴ | ω⁶ | x₂ |
| z₃ | 1 | ω³ | ω⁶ | ω⁹ | x₃ |

It can be rewritten as

z₀ = ω⁰x₀ + ω⁰x₂ + w⁰ ω⁰x₁ + ω⁰x₃

z₁ = ω⁰x₀ + ω²x₂ + w¹ ω⁰x₁ + ω²x₃

z₂ = ω⁰x₀ + ω⁴x₂ + w² ω⁰x₁ + ω⁴x₃

z₃ = ω⁰x₀ + ω⁶x₂ + w³ ω⁰x₁ + ω⁶x₃.

Using the fact that ω⁴ = 1, we can rewrite the above equations as

z₀ = (ω⁰x₀ + ω⁰x₂) + w⁰ ω⁰x₁ + ω⁰x₃

z₁ = (ω⁰x₀ + ω²x₂) + w¹ ω⁰x₁ + ω²x₃

z₂ = (ω⁰x₀ + ω⁰x₂) + w² ω⁰x₁ + ω⁰x₃

z₃ = (ω⁰x₀ + ω²x₂) + w³ ω⁰x₁ + ω²x₃.

Note that each term in parentheses in the top two lines is repeated verbatim in the bottom two lines. Let µ = ω² and define

u₀ = µ⁰x₀ + µ⁰x₂




u₁ = µ⁰x₀ + µ¹x₂

and

v₀ = µ⁰x₁ + µ⁰x₃

v₁ = µ⁰x₁ + µ¹x₃

Both u = (u₀, u₁)⊤ and v = (v₀, v₁)⊤ are essentially DFTs with n = 2. More precisely,

u = M₂ x₀ and v = M₂ x₁. We can write the original M₄x as

| x₂                   | x₃ |
| -------------------- | -- |
| z₀ = u₀ + ω⁰v₀ (7)   |    |
| z₁ = u₁ + ω¹v₁ (8)   |    |
| z₂ = u₀ + ω²v₀ (9)   |    |
| z₃ = u₁ + ω³v₁. (10) |    |

In summary, the calculation of the DFT(4) has been reduced to a pair of DFT(2) plus 7 extra multiplications and additions (step (7)–(10)).

Ignoring the 1/√n for a moment, DFT(n) can be reduced to computing two DFT(ⁿ )s plus 2n − 1 extra operations (n − 1 multiplication and n additions). For example, when n = 32,

z₀ = ω⁰×⁰x₀ + ω⁰×²x₂ + · · · + ω⁰×³⁰x₃₀ + w⁰ (ω⁰×⁰x₁ + ω⁰×²x₃ + · · · + ω⁰×³⁰x₃₁)

z₁ · = ω¹×⁰x₀ + ω¹×²x₂ + · · · + ω¹×³⁰x₃₀ + w¹ (ω¹×⁰x₁ + ω¹×²x₃ + · · · + ω¹×³⁰x₃₁)

| z · · 15×0 | 15×2   | · · · | 15×30 |         |
| ---------- | ------ | ----- | ----- | ------- |
| 15         | ( 15×0 | 15×2  | · · · | 15×30 ) |

15 = ω x₀ + ω x₂ + + ω x₃₀ + w ω x₁ + ω x₃ + + ω x₃₁

z₁₆ = ω¹⁶×⁰x₀ + ω¹⁶×²x₂ + · · · + ω¹⁶×³⁰x₃₀ + w¹⁶ (ω¹⁶×⁰x₁ + ω¹⁶×²x₃ + · · · + ω¹⁶×³⁰x₃₁)

z₁₇ · = ω¹⁷×⁰x₀ + ω¹⁷×²x₂ + · · · + ω¹⁷×³⁰x₃₀ + w¹⁷ (ω¹⁷×⁰x₁ + ω¹⁷×²x₃ + · · · + ω¹⁷×³⁰x₃₁)

| z · · 31×0 | 31×2   | · · · | 31×30 |         |
| ---------- | ------ | ----- | ----- | ------- |
| 31         | ( 31×0 | 31×2  | · · · | 31×30 ) |

31 = ω x₀ + ω x₂ + + ω x₃₀ + w ω x₁ + ω x₃ + + ω x₃₁






Note that ω³² = 1. Let µ = ω². Let

u₀ = µ⁰x₀ + µ⁰x₂ + · · · µ⁰x₃₀

u₁ = µ⁰x₀ + µ¹x₂ + · · · µ¹⁵x₃₀

· · · 0 15 · · · 15×15

u₁₅ = µ x₀ + µ x₂ + µ x₃₀

and

v₀ = µ⁰x₁ + µ⁰x₃ + · · · µ⁰x₃₁

v₁ = µ⁰x₁ + µ¹x₃ + · · · µ¹⁵x₃₁

· · · 0 15 · · · 15×15

v₁₅ = µ x₁ + µ x₃ + µ x₃₁.

Then

z₀ = u₀ + ω⁰v₀

z₁ = u₁ + ω¹v₁

z · · · 15 15 = u₁₅ + ω v₁₅

z₁₆ = u₀ + ω¹⁶v₀

z₁₇ = u₁ + ω¹⁷v₁

z · · · 31 31 = u₁₅ + ω v₁₅

A careful count of the additions and multiplications necessary yields the next theorem





# Theorem 2

Let n be a power of 2. Then the fast Fourier transform of size n can be completed in n(2 log₂ n − 1) + 1 additions and multiplications, plus a division by √n.

Proof: Ignore the division by √n, which is applied at the end. The result is equivalent to say that the DFT(2ᵐ) can be completed in 2ᵐ(2m − 1) + 1 additions and multiplications. We proceed by induction: For m = 1, DFT(2) takes two additions and one multiplication:

y₀ = u₀ + 1v₀, y₁ = u₀ + ωv₀.

Suppose this formula is true for DFT(2ᵐ). Then DFT(2ᵐ⁺¹) takes two DFT(2ᵐ)’s, which take 2(2ᵐ(2m − 1) + 1) operations plus 2(2ᵐ⁺¹) − 1 extras. The total number of operations is 2(2ᵐ(2m − 1) + 1) + 2(2ᵐ⁺¹) − 1 = 2ᵐ⁺¹(2(m + 1) − 1) + 1. □



# 7.6 Trigonometric interpolation

This is from Section 10.2 of the textbook. What does the DFT actually do? In this section, we present an interpretation of the output vector y of the Fourier Transform as interpolating coefficients for evenly spaced data.

The following is Corollary 10.8 of the textbook. The Pₙ in (11) will be called an order n trigonometric function.



# Theorem 3

For an even integer n, let *tj = c + j(d − c)/n for j = 0, ..., n − 1 and let x = (x0, ..., xn−1)⊤ denote a vector of n real numbers. Define y = a + bi = Fnx where Fn is the DFT matrix, a = (a0, ..., an−1)⊤ ∈ Rn×1, b = (b0, ..., bn−1)⊤ ∈ Rn×1*. Then the function

*Pn(t) = √n a + √n ∑k=1n−1 ak cos(2πk(d − c)) − bk sin(2πk(d − c))*

*√n(t − c) + 2 cos(nπ(d − c)/n)*

satisfies *Pn(tj) = xj for j = 0, ..., n − 1*.



# Example 8

Let [c, d] = [0, 1] and n = 8. Let x = (−2.2, −2.8, −6.1, −3.9, 0, 1.1, −0.6, −1.1)⊤. Find the trigonometric interpolant.




# Solution:

The Fourier transform output, accurate to four decimal places, is

| −5.5154           | −1.0528          | 3.6195  |
| ----------------- | ---------------- | ------- |
| 1.5910            | −1.1667i         | −0.5028 |
| −0.2695           | −0.7778          |         |
| −0.5028 + 0.2695i | 1.5910 + 1.1667i | −1.0528 |
| −3.6195           |                  |         |

According to the formula (11), the interpolating function is

P₈(t) =

| −5.5154                   | −1.0528             | 3.6195                 |
| ------------------------- | ------------------- | ---------------------- |
| √₈                        | + √₂                | cos(2πt) − √₂ sin(2πt) |
| 1.5910                    | −1.1667 √₂ cos(4πt) | − √₂ sin(4πt)          |
| −0.5028                   | −0.2695             | −0.7778                |
| √₂ cos(6πt) − √₂ sin(6πt) | + √₈ cos(8πt)       |                        |

= − 1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt) + 0.825 sin(4πt) − 0.3555 cos(6πt) + 0.1906 sin(6πt) − 0.2750 cos(8πt). (12)

The plot of P₈(t) is shown in Figure 4. □

Now, we want to prove Theorem 3. For that purpose, we need the following result:





# Theorem 4 (DFT interpolation theorem)

Given an interval [c, d] and positive integer n, let

tj = c + j(d − c)/n for j = 0, ..., n − 1 and let x = (x0, ..., xn−1)⊤ denote a vector of n numbers.

Define y = a + bi = Fnx where Fn is the DFT matrix, y = (y0, ..., yn−1)⊤ ∈ Cn×1, a = (a0, ..., an−1)⊤ ∈ Rn×1, b = (b0, ..., bn−1)⊤ ∈ Rn×1. Then the complex function

Q(t) =
1
√n
<sum>
k=0
n−1
i2πk(t−c)/(d−c)
yk e
</sum>

satisfies Q(tj) = xj for j = 0, ..., n − 1. Furthermore, if xj’s are real, the real function

P(t) =
1
√n
<sum>
k=0
n−1
t − c
t − c
ak cos 2πk
d − c
− bk sin 2πk
d − c
</sum>

satisfies P(tj) = xj for j = 0, ..., n − 1.

217




# Figure 4: Trigonometric interpolation.

| t   | f    |
| --- | ---- |
| 0   | −2.2 |
| 1/8 | −2.8 |
| 2/8 | −6.1 |
| 3/8 | −3.9 |
| 4/8 | 0    |
| 5/8 | 1.1  |
| 6/8 | −0.6 |
| 7/8 | −1.1 |






# Proof:

Let ω = e−ⁱ²π/N. Then

1 n−1 −k j 1 n−1 i2πkj/n

xj = √n Σk=0n−1 yₖ ω−k = √n Σk=0n−1 yₖ ei2πkj/n

1 n−1 i2πk(tj − c)/(d − c)

= √n Σk=0n−1 yₖ ei2πk(tj − c)/(d − c) = Q(tj).

It is obvious that P(t) defined by (14) is the real part of Q(t). Taking real part on both sides of Q(tj) = xj, we get P(tj) = xj. □






# Proof of Theorem 3:

First, since x is real, by Proposition 1, y = Fₙx satisfies y₀ ∈ R, yₖ = yₙ−ₖ for k = 1, ..., n − 1. This means b₀ = 0, aₖ = aₙ−ₖ, bₖ = −bₙ−ₖ. When n is even, the last equation implies bₙ = −bₙ, hence bₙ = 0.

Second, (see Figure 5)

e−i²πkᵗj−ᶜ = ei²π(ⁿ−ᵏ) tj−ᶜ for j = 1, ..., n − 1 because ei²πn tj−ᶜ = ei²πj = 1. Therefore cos 2πk tj−ᶜ = cos 2π(n − k)tj−ᶜ and sin 2πk tj−ᶜ = − sin 2π(n − k)ᵗʲ−ᶜ. Plugging in t = tj in (14), we obtain

P(tj) = √n k=0n−1 aₖ cos 2πk d − c − bₖ sin 2πk d − c

1 n tj − c tj − c

√n an cos 2π2 d − c − bn sin 2π2 d − c

1 n−1 tj − c tj − c

√n k=ₙ₊₁ aₖ cos 2πk d − c − bₖ sin 2πk d − c

Using the equations we have obtained before, bn term vanishes and the last term can be rewritten as

1 n−1 tj − c tj − c

√ₙ k=ₙ₊₁ an−ₖ cos 2π(n − k) d − c − bn−ₖ sin 2π(n − k) d − c






n−1

1 2 tj − c tj − c = √n ℓ=1 aℓ cos 2πℓ d − c − bℓ sin 2πℓ d − c.

In the end, we recall the fact that b₀ = 0, a₀ cos 2π0 tʲ−ᶜ = a₀. Hence P(tj) = Pₙ(tj) with the Pₙ defined by (11). □

1 1

0.5 cos(2π t) 0.5

cos(2π 7 t)

0 0

−sin(2π t)

−0.5 −0.5 sin(2π 7 t)

−10 0.2 0.4 0.6 0.8 1 −10 0.2 0.4 0.6 0.8 1

Figure 5: e−ⁱ²πkᵗʲ−ᶜ = eⁱ²π(ⁿ−ᵏ) tʲ−ᶜ for n = 8, k = 1. d = 1. c = 0. {ᵗ } = d−c d−c j {0, 1/8, 2/8, ..., 7/⁸}. Left: Real part. Right: Imaginary part.

19In fact we also have sin 2π n tʲ−c = 0 for j = 0, ..., n − 1.

2 d−c

219






# Example 9

Let [c, d] = [0, 1] and n = 4. Let x = (1, 0, −1, 0)⊤. Find the trigonometric interpolant.

Solution: From the example of last section, we know the DFT of x is y = (0, 1, 0, 1)⊤. From (11), we know

P₄(t) = a⁰ + (a₁ cos(2πt) − b₁ sin(2πt)) + a² cos(4πt) = cos(2πt). □

By the way, by (14), we know

P(t) = 1 (a₀ + a₁ cos(2πt) + a₂ cos(4πt) + a₃ cos(6πt)) = 1 cos(2πt) + 1 cos(6πt).

2 2

The plots of P(t) and P₄(t) are shown in Figure 6.

| 1/2 cos(2 π s) + 1/2 cos(6 π s) |     |     |     |     |   |      |      |      |      |    |
| ------------------------------- | --- | --- | --- | --- | - | ---- | ---- | ---- | ---- | -- |
| 1                               | 0.8 | 0.6 | 0.4 | 0.2 | 0 | −0.2 | −0.4 | −0.6 | −0.8 | −1 |
| 0                               | 0.2 | 0.4 | 0.6 | 0.8 | 1 |      |      |      |      |    |

Figure 6: Trigonometric interpolation. 1 cos(2πt) + 1 cos(6πt) (solid line) and cos(2πt) (dashed line).





# 7.7 Orthogonality and interpolation

# Theorem 5

Let f₀(t), ..., fₙ−₁(t) be functions of t and t₀, ..., tₙ−₁ be real numbers. Assume that the n × n matrix

| A =                     | f₀(t₀)   | f₀(t₁)   | · · · | f₀(tₙ−₁)   |
| ----------------------- | -------- | -------- | ----- | ---------- |
|                         | f₁(t₀)   | f₁(t₁)   | · · · | f₁(tₙ−₁)   |
| . . . . . . . . . . . . |          |          |       |            |
|                         | fₙ−₁(t₀) | fₙ−₁(t₁) | · · · | fₙ−₁(tₙ−₁) |

is a real n × n orthogonal matrix (i.e., A⊤A = I). If y = Ax, then the function

n−1

F(t) =

The proof that A is an orthogonal matrix is Lemma 10.10 of the textbook. The proof is straightforward. One way to prove it is to express cos(2πjk/n) as (ei²πjk/n + e−i²πjk/n)/2 and write everything in terms of ω = e−i²π/n. Then apply (3). Since the calculations are long and tedious, and is not required for the exam, we will present it in a separate subsection (the next subsection) which also explains how come we can “find” such an orthogonal matrix. □

As the conditions for Theorem 5 are satisfied, we can apply the theorem and obtain the interpolation function (with coefficient y = Ax = (y₀, ..., yₙ−₁)⊤)

F(t) = √n y₀ + 12 n y₁ cos 2π(t − c) − d − c + n y₂ sin 2π(t − c) + 2 y₃ cos 4π(t − c) + 2 y₄ sin 4π(t − c) + · · · 1n √n yₙ−₁ cos nπ(t − c) (24)

for the points (tₗ, xₗ), in agree with the Pₙ(t) in (11).




# Example 11

Use the basis functions of the last example (Example 10) to interpolate the data points x = [−2.2, −2.8, −6.1, −3.9, 0, 1.1, −0.6, −1.1] from Example 8.

# Solution:

| 1  | 1  | · · ·   | 1     | −2.8 | −1.4889  | −6.1    | −5.1188 |
| -- | -- | ------- | ----- | ---- | -------- | ------- | ------- |
| 2  | 1  | cos 2₈  | cos 8 | −3.9 | 2.2500   |         |         |
| n  | .  | .       | .     | .    | 0.0      | 1.6500  |         |
| .  | .  | .       | .     | .    | 1.1      | −0.7111 |         |
| √2 | √2 | cos (π) | · · · | √2   | cos (7π) | −0.6    | 0.3812  |

The formula (24) given the interpolation function

P(t) = −5.5154 + 2 cos(2πt) − 2 sin(2πt) + 2.2500 cos(4πt) + 1.6500 sin(4πt) − 2 − 0.7111 + 2 cos(6πt) + 2 sin(6πt) + √8 cos(8πt) = − 1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt) + 0.825 sin(4πt) − 0.3555 cos(6πt) + 0.1906 sin(6πt) − 0.2750 cos(8πt). (25)

in agreement with (12). □

Now we have another approach to find the trigonometric interpolation function.





# 7.8 Orthogonal matrix and eigenvectors related to DFT

Materials presented in this subsection try to give you the idea how people come up with the matrix A in (23) (see (26)). Since they are some advanced topics, they are not required for the exam. First, suppose it is God-given, let us prove that it is an orthogonal matrix:

| A = | 1      | 1       | · · · | 1       |
| --- | ------ | ------- | ----- | ------- |
|     | √2     | √2      | √2    |         |
| 1   | cos 2π | · · ·   | cos   | 2π(n−1) |
|     | √2     | √2      | √2    |         |
| 0   | sin 2π | · · ·   | sin   | 2π(n−1) |
| n   | .      | .       | n     | .       |
| .   | .      | .       | .     | .       |
| 1   | 1      | cos (π) | · · · | 1       |
|     | √2     | √2      | √2    |         |

Hint: One way to prove it is to express cos(2πjk/n) as (ei2πjk/n + e−i2πjk/n)/2 and write everything in terms of ω = e−i2π/n. Then apply the following equation that we have proved before:

n−1 ωjk = n when k = 0, ±n

j=0 0 when k = ±1, ..., ±(n − 1).

Proof: Note that the first row is 1 (1, 1, 1, 1, · · · , 1, 1) and the last row is 1 (1, −1, 1, −1, · · · , 1, −1). Clearly, these two rows have unit length.

So, we are left to prove:

cos² 2πk0 + cos² 2πk1 + · · · + cos² 2πk(n − 1) = n (27)

sin² 2πk0 + sin² 2πk1 + · · · + sin² 2πk(n − 1) = n (28)

cos 2πk0 cos 2πm0 + cos 2πk1 cos 2πm1 + · · · + cos 2πk(n − 1) cos 2πm(n − 1) = 0 n when k = m




(29) sin 2πk0 sin 2πm0 + sin 2πk1 sin 2πm1 + · · · + sin 2πk(n − 1) sin 2πm(n − 1) = 0

n when k = m

(30) cos 2πk0 sin 2πm0 + cos 2πk1 sin 2πm1 + · · · + cos 2πk(n − 1) sin 2πm(n − 1) = 0

n when k = m

(31) From the hint, we know that when k = ±1, · · · ± (n − 1),

∑j=0n−1 e−i2πjk/n = ∑j=0n−1 cos(2πjk/n) − i ∑j=0n−1 sin(2πjk/n) = 0.

(32) 223

Using cos²(θ) = 1−cos(2θ), (27) ⇔ cos 2π2k0 + cos 2π2k1 + · · · + cos 2π2k(n−1) = 0

which is true as k = 1, ..., n − 1 (see the real part of (32) with k replaced by 2k). So, we have proved (27).

Since sin²(θ) + cos²(θ) = 1, (27) ⇔ (28). So, we have proved (28).

For identities (29)–(31), let us prove (31) as an example. The proofs of the other two are the same. Note that (31) ⇔ ∑j=0n−1 cos(2πkj/n) sin(2πkj/n) = 0. Let ω = e−i2π/n. Then

cos(2πkj/n) = ei2πkj/n + e−i2πkj/n = ω−kj + ωkj and sin(2πkj/n) = ei2πkj/n − e−i2πkj/n = ω−kj − ωkj.

Also note that k = 0, 1, ..., 2 and m = 1, 2, ..., 2

∑j=0n−1 cos(2πkj/n) sin(2πmj/n) = n−1 ω−kj + ωkj ω−mj − ωmj

= 1/n−1 ∑j=02i ω−(k+m)j − ω(m−k)j + ω(k−m)j − ω(k+m)j = 0.

In the last step we have used −(n − 1) ≤ ±k ± m ≤ n − 1 and we have applied the identity in the hint. □

But the above proof does not answer the question that how people can come up with such a complicated orthogonal matrix A. Now, here is where it comes from:

A is orthogonal means its rows are perpendicular to each other.





From some advanced linear algebra course, we learned (or will learn) the following fact:

Suppose vi is eigenvector of a symmetric matrix B with eigenvalue λi (i = 1, 2), which means Bvi = λivi for i = 1, 2. If λ1 = λ2, then we know v1 ⊥ v2, i.e., v1⊤v2 = 0. The reason is very simple: λ1 v1⊤v1 = (Bv1)⊤v1 = v1⊤B⊤v1 = v1⊤(Bv1) = λ1 v1⊤v1. Hence v1 v2 = 0, i.e., v1 ⊥ v2.

It turns out that



# Proposition 2

The rows of A in (23) are eigenvectors of the following n × n matrix D with different eigen values.

| −²  | −¹  | −   | −¹  |
| --- | --- | --- | --- |
| 1   | 2   | 1   |     |
| −1  | ²   | −¹  |     |
| ... | ... | ... | ... |
| −   | −1  | ²   | −¹  |

Therefore, by the aforementioned result, the rows of A are perpendicular to each other.

We will postpone the proof of Proposition 2 for the moment, but try to answer a more interesting question: how come we can find such a strange matrix D?

All those things can be viewed as starting from the simple identities

d² cos(kπt) = −(kπ)² cos(kπt), d² sin(kπt) = −(kπ)² sin(kπt).

(34)

224



Recall that we have learned the three point centered-difference formula (5):

u(t + h) − 2u(t) + u(t − h) =



# 7.9 Revisit of the least square fitting with trigonometric functions

Let us go back to trigonometric functions. Theorem 3 showed how the DFT makes it easy to interpolate n evenly space data points on [0, 1] by trigonometric function of the form

Pₙ(t) = √n + √n ∑k=1n/2−1 (aₖ cos(2kπt) − bₖ sin(2kπt)) + √² cos(nπt). (37)

Recall Examples 5 and 6 shown in Figure 3. Examples 5 and 6 contain less terms than (37) and are least squares approximation. Examples 11 and Example 8 contain more terms and are exact interpolation. All four examples use the same data. We have already explained why Example 5 and Example 6 share the same the constant term, cos(2πt) term and sin(2πt) terms. When we add more and more terms, least squares approximation becomes interpolation. So, it is not very surprising to see that the four examples always share the same coefficients for common terms.

In general, we have the following result:



# Theorem 6 (Orthogonal Function Least Squares Approximation Theorem)

Let m ≤ n be integers, and assume that data (t₀, x₀), ..., (tₙ−₁, xₙ−₁) are given. Set y = Ax, where A =

| f₀(t₀)   | f₀(t₁)   | · · · | f₀(tₙ−₁)   |
| -------- | -------- | ----- | ---------- |
| f₁(t₀)   | f₁(t₁)   | · · · | f₁(tₙ−₁)   |
| .        | .        | .     | .          |
| .        | .        | .     | .          |
| .        | .        | .     | .          |
| fₙ−₁(t₀) | fₙ−₁(t₁) | · · · | fₙ−₁(tₙ−₁) |

The interpolation function with basis functions f₀(t), ..., fₙ−₁(t) is

Fₙ(t) = ∑k=0n−1 yₖ fₖ(t), (38)

and the best least squares approximation, using only the functions f₀(t), ..., fₘ−₁(t) is

Fₘ(t) = ∑k=0m−1 yₖ fₖ(t). (39)

Proof: By Theorem 5, F(t) = ∑k=0n−1 yₖ fₖ(t) satisfies F(tj) = xj for j = 0, ..., n − 1. For least square approximation, we are looking for G(tj) = xj for j = 0, ..., n − 1. Our "hope" that G(tj) = xj (j = 0, ..., n − 1) can be written as

x = A⊤c

where c = (c0, ..., cm−1) and A =

| f₀(t₀)   | f₀(t₁)   | · · · | f₀(tₙ−₁)   |
| -------- | -------- | ----- | ---------- |
| f₁(t₀)   | f₁(t₁)   | · · · | f₁(tₙ−₁)   |
| .        | .        | .     | .          |
| .        | .        | .     | .          |
| .        | .        | .     | .          |
| fₘ−₁(t₀) | fₘ−₁(t₁) | · · · | fₘ−₁(tₙ−₁) |

is the matrix of the first m rows of A. The normal equation is AₘA⊤c = Aₘx.




The condition that A is an orthogonal matrix implies that A⊤A = I, or, equivalently, A has pairwise orthonormal columns. So, Aₘ also has pairwise orthonormal columns. Hence AₘA⊤ = I ∈ Rm×m. So, c = Aₘx, which is nothing but the first m entries of the vector y = Ax. □

We apply the above theorem to the trigonometric function case. Given n data points, to find the best least squares trigonometric function with m &#x3C; n terms fitting the data, it suffices to compute the actual interpolant with n terms and keep only the desired m terms. From the statement of the theorem, we note that the order was not relevant. The desired m terms may not be the m lowest frequency terms. We could have specified any subset of the basis functions. The least squares solution is found simply by dropping all terms in (38) that are not included in the subset. The version (39) is a “low-pass” filter, assuming that the lower index functions go with lower “frequencies”; but by changing the subset of basis functions kept, we can pass any frequencies of interest simply by dropping the undesired coefficients.






# Example 12

Fit the temperature data by least squares trigonometric functions of orders 4 and 6.

| time of day | 12 mid. | 3 am | 6 am | 9 am | 12 noon | 3 pm | 6 pm | 9 pm |
| ----------- | ------- | ---- | ---- | ---- | ------- | ---- | ---- | ---- |
| t           | 0       | 1    | 1    | 3    | 1       | 5    | 3    | 7    |
| temp. (C)   | −2.²    | −2.⁸ | −4   | −8   | 2       | 8    | −4   | −8   |
|             | 8       | 6.1  | 3.9  | 0.0  | 1.1     | 0.6  | 1.1  |      |

Figure 7: Least square trigonometric fits for the temperature data. Fits for m = 4 (solid line) and 6 (dashed line) are shown.

Solution: We know the interpolation polynomial is (see either (25) or (12))

P₈(t) = − 1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt) + 0.825 sin(4πt) − 0.3555 cos(6πt) + 0.1906 sin(6πt) − 0.2750 cos(8πt).

So, the least squares models of orders 4 and 6 are

P₄(t) = − 1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt)

P₆(t) = − 1.95 − 0.7445 cos(2πt) − 2.5594 sin(2πt) + 1.125 cos(4πt) + 0.825 sin(4πt) − 0.3555 cos(6πt).

The results are shown in Figure 7. For trigonometric interpolation P₈, we can think of the least squares approximation P₄ or P₆ as ”filtering out” the high frequencies (e.g., cos(8πt) etc.).






# Example 13

Let *tj = j/100, aj = j, bj = −j, for j = 0, 1, 2, ..., 99*. Define

*f(t) = ∑k=099 (ak cos (2πkt) + bk sin (2πkt))*. (40)

Denote *f(tj) by yj for j = 0, ..., 99. Determine the values of cℓ, dₘ for ℓ = 0, ..., 5, m = 1, ..., 4*, so that

*P(t) = c0 + ∑k=14 (ck cos (2πkt) + dk sin (2πkt)) + c5 cos(10πt) is the least squares approximation to the data points (tj, yj) for j = 0, ..., 99. [Hint: Recall for any integer k and for any j = 0, ..., 99, cos(2π(100 − k)tj) = cos(2πktj), sin(2π(100 − k)tj) = −sin(2πktj), and sin (2π50tj) = 0]*

# Solution:

We have 100 data points, but 200 functions. We need to find an interpolation function using 100 functions. So, we use the fact that for any integer *k, cos 2(100 − k)πtj = cos 2kπtj, sin 2(100 − k)πtj = − sin 2kπtj, and sin (2π50tj) = 0*. Now, define

*g(t) = a0 + ∑k=149 (ak cos (2πkt) + bk sin (2πkt)) + (a50 cos (2π50t) + b50 sin (2π50t)) + ∑k=5199 (ak cos (2π(100 − k)t) − bk sin (2π(100 − k)t)) has the same value of f(t) when t = tj for j = 0, ..., 99*.

So, by the orthogonal matrix approach, the least square approximation is *a0 + ∑k=14 ((ak + a100−k) cos (2πkt) + (bk − b100−k) sin (2πkt)) + (a5 + a100−5) cos (2π5t)*. So,

(*c0, c1, c2, c3, c4, c5) = (a0, a1+a99, a2+a98, a3+a97, a4+a96, a5+a95) = (0, 100, 100, 100, 100, 100)*

and (*d1, d2, d3, d4) = (b1 − b99, b2 − b98, b3 − b97, b4 − b96) = (98, 96, 94, 92).*





# 7.10 Discrete cosine transform

This part is taken from Section 11.1 of the textbook. Let n be a positive integer. The one-dimensional discrete cosine transform of order n is defined by the n × n matrix C

| 1             | 1              | · · · | 1                   |
| ------------- | -------------- | ----- | ------------------- |
| √2            | √2             | √2    | √2                  |
| cos π/2n      | cos 3π/2n      | · · · | cos (2n−1)π/2n      |
| cos 2π/2n     | cos 6π/2n      | · · · | cos 2(2n−1)π/2n     |
| ·             | ·              | ·     | ·                   |
| ·             | ·              | ·     | ·                   |
| cos (n−1)π/2n | cos (n−1)3π/2n | · · · | cos (n−1)(2n−1)π/2n |

The discrete cosine transform (DCT) of x = (x₀, ..., xₙ−₁)⊤ is the n-dimensional vector y = (y₀, ..., yₙ−₁)⊤ given by y = Cx. This definition is the same as Matlab’s dct. Unlike the case of our DFT and Matlab’s fft, there is no √n difference on the factor between our DCT and Matlab’s dct.

Note that C is a real orthogonal matrix (C⊤C = I). The orthogonality of C follows from the fact that the rows of C are the unit eigenvectors of the real symmetric n × n matrix

| -1 | -1 | -1 |
| -- | -- | -- |
| 1  | 2  | 1  |
| -1 | -1 | -1 |

Note that the matrix in Proposition 2 corresponds to eigenvalue problem − d²₂ u = λu on [0, 1], u in periodic on [0, 1] while the current one corresponds to eigenvalue problem λu on [0, 1], u′(0) = u′(1) = 0.

The proof that C is orthogonal is similar to the proof of Proposition 2: Suppose we divide the interval [0, 1] into n intervals and define tj be the middle point of the jth interval for j = 1, ..., n. So, tj = 2ʲ−¹. We recognize the (k + 1)th row of C is cos(kπt) evaluated at t1, ..., tn.

Let v = (cos(2ⁿ), cos(kπt1), ..., cos(kπtn))⊤. Claim that Dvk = −2 + 2 cos(kπh)vk.

These are n equations. Except the first and the last equations, the others are all due to the identity (35). By introducing t0 = −1/(2n) and tn+1 = 1 + 1/(2n) and note that Suppose vi is eigenvector of a⊤symmetric matrix A with eigenvalue λi (i = 1, 2). It means Avi = λivi for i = 1, 2. If λ1 = λ2, then λ1v1v2 = (Av1)⊤v2 = v2⊤A⊤v2 = v2⊤(Av2) = λ2v2⊤v2. Hence v1⊥v2.




cos(kπt₁) = cos(kπt₀) and cos(kπtₙ) = cos(kπtₙ₊₁), we can derive the first and last equations in (43). In this way, we have proved that vi ⊥ vj when i = j, i, j = 0, ..., n − 1.

To see why we have the coefficients in C, we simply recall

1 = 1 cos(kπt)2dt ≈ n cos(kπtj)2h (Riemann sum).

It turns out the ≈ above is exactly =. Why? You can directly verify it:

n






# 1.5

0.5

0

−0.5

−1

−1.5

0.5 1 1.5 2 2.5 3 3.5 4

Figure 8: DCT interpolation with P(t) = 1 0.9239 cos(2ᵗ + 1)π + cos(2(2ᵗ + 1)π) − 0.3827 cos(3(2ᵗ + 1)π).

So

P₄(t) = √2 (0.9239 cos((2t + 1)π/8) + cos((2(2t + 1)π)/8) − 0.3827 cos((3(2t + 1)π)/8).

The interval on which we are looking for interpolation is [0, n] in the previous example where n is the number of data points.

Now, we want to draw a connection between DCT and the interpolation on a fixed interval [c, d] with tj = c + 2ʲ⁺¹ (d − c) for j = 0, ..., n − 1. Note that in our previous discussion, we set t = j (d − c).

In some sense, we always cut c, d into n sub-intervals. In the previous cases, we use the left end point of an interval but now we want to switch to the middle point of an interval.

Let

- f₀(t) = 1/n
- f₁(t) = 2 cos(π(t − c)/(d − c))
- f₂(t) = 2 cos(2π(t − c)/(d − c))
- f₃(t) = 2 cos(3π(t − c)/(d − c))
- · · ·
- fₙ₋₁(t) = 2 cos((n − 1)π(t − c)/(d − c))






The above fj’s can be compared with the fj’s in (16)–(22). Note that fₖ (tj) = 2 cos kπ(tj−c) = 2 cos kπ(2j+1). So C = (fₖ (tj)) for k, j = 0, ..., n − 1. Note that for the same C, we have demonstrated two different ways to choose tj and fj so that C = (fₖ (tj)). Can you write down the fj and tj we used in Theorem 7?

With our choice of fj in (45)–(49), by Theorem 5, we have the following result:





# Theorem 8

For an even integer n, let *tj = c + 2j + 1 (d − c) for j = 0, ..., n − 1 and let x = (x0, ..., xn−1)⊤ denote a vector of n real numbers. Define Cx as the DCT matrix. Then the function y = Cx*

*Qn(t) = √n + √n Σk=1n−1 yk cos( (t − c) kπ / (d − c) ) (50) satisfies Qn(tj) = xj for j = 0, ..., n − 1*.




# Example 15

Use the DCT to interpolate the points (¹ , 1), (³ , 0), (⁵ , −1), (⁷ , 0).

Solution: Recall dct([1,0,-1,0])=[0, 0.9239, 1, -0.3827]. So,

Q₄(t) = √2 (0.9239 cos(πt) + cos(2πt) − 0.3827 cos(3πt)). □

| 1.5 | 1   | 0.5 | 0   | −0.5 | −1 | −1.5 |
| --- | --- | --- | --- | ---- | -- | ---- |
| 0.2 | 0.4 | 0.6 | 0.8 | 1    |    |      |

Figure 9: DCT interpolation with Q₄(t) = √2 (0.9239 cos(πt) + cos(2πt) − 0.3827 cos(3πt))

Similarly to our previous section, we can develop the least squares approximation theorem for data fitting of the type (44) or (50). It is elaborated in Section 11.1.2.

Figure 10: The 2D-DCT can be used to interpolate function values on a square grid, such as pixel values of an image.





# 7.11 Two-dimensional DCT

This is from Section 11.2 of the textbook. The two-dimensional Discrete Cosine Transform is simply the one-dimensional DCT applied in two dimensions, one after the other.

The 2D-DCT is the one-dimensional DCT applied successively to both horizontal and vertical directions. Consider the matrix X consisting of the values xij, as in Figure 10. Each column of CXT corresponds to a fixed si. To do a 1D-DCT in the s-direction means moving across the rows; so, again, transposing and multiplying by C yields C(CXT)T = CXCT.




# Definition 2

The two-dimensional Discrete Cosine Transform (2D-DCT) of the n × n matrix X is the matrix Y = CXT, where C is defined in (41). The inverse 2D-DCT is X = CTY C.

If Matlab’s dct is available, the command Y=dct(dct(X')') computes the 2D-DCT with two applications of the 1D-DCT.

To write a useful expression for the interpolating function, recall the definition of C in (41)

Cij = 2 ai cos(i(2j + 1)π / (2n)) for i, j = 0, 1, · · · , n − 1, where ai = 1/√2 if i = 0, 1 if i = 1, · · · , n − 1.

Then

xij = ∑k=0n−1 ∑l=0n−1 CTkℓykℓClj = ∑k=0n−1 ykℓakaℓ cos(k(2i + 1)π) cos(l(2j + 1)π.

Hence we have proved the following theorem






# Theorem 9 (2D-DCT Interpolation Theorem)

Let X = (xij) be a matrix of n2 real numbers.

Let Y = ykℓ be the two-dimensional Discrete Cosine Transform of X. Define a0 = 1 and ak = 1 for k > 0. Then the real function

Pn(s, t) = 2n−1   ykℓakaℓ cos k(2s + 1)π cos l(2t + 1)π.

satisfies Pn(i, j) = xij for i, j = 0, · · · , n − 1.






# Example 16

Find the 2D Discrete Cosine Transform of the data in

| 1 | 1 | 1 | 1 |
| - | - | - | - |
| 3 |   | 1 |   |
| 1 | 0 | 0 | 1 |
| 2 |   | 1 |   |
| 1 | 0 | 0 | 1 |
| 1 | 1 | 1 | 1 |
| 0 | 0 | 1 | 2 |
| 3 |   |   |   |

Then find its interpolation function and discuss its least squares approximations.

| 1             | 1           | 1  | 1           |
| ------------- | ----------- | -- | ----------- |
| \~~√\~~2 π | \~~√\~~2 | 3π | \~~√\~~2 |
| 5π            | \~~√\~~2 | 7π |             |

Solution: C = 2 cos 8 cos 8 cos 8 cos 8.

| 4     | cos 2π | cos 6π  | cos 10π | cos 14π |
| ----- | ------ | ------- | ------- | ------- |
| 38    | 8      | 8       | 8       |         |
| cos π | cos 9π | cos 15π | cos 21π |         |
| 8     | 8      | 8       | 8       |         |

1 1 1 1 3 0 1 0

CXC⊤ = C 1 0 0 1 C⊤ = 0 0 0 0.

| 1 | 0 | 0  | 1 |
| - | - | -- | - |
| 1 | 0 | −1 | 0 |
| 1 | 1 | 1  | 1 |
| 0 | 0 | 0  | 0 |

234

P₄(s, t) = 4 2 y⁰⁰ + √2 y⁰² cos 8 + √2 y₂₀ cos 8 + y₂₂ cos 8 cos 8

= 4 + 2√2 cos 8 + 2√2 cos 8 − 2 cos 8 cos 8.






# Least squares approximations with the 2D-DCT

Least squares approximations with the 2D-DCT are done in the same way as with the 1-DCT. For example, implementing a low-pass filter would mean simply deleting the “high-frequency” components, those whose coefficients have larger indices, from the interpolating function. For the current case, the best least squares fit to the basis functions cos i(2t + 1)π cos j(2s + 1)π for i + j ≤ 2 is given by dropping all terms that do not satisfy i + j ≤ 2. In this case, the only nonzero “high-frequency” term is the i = j = 2 term, leaving P₂(s, t) = 4 + 2√2 cos 8 + 2√2 cos 8.

# The 16 values of P₂(i, j) are as follows

|   | 1    | 2    | 3    |      |
| - | ---- | ---- | ---- | ---- |
| 0 | 1.25 | 0.75 | 0.75 | 1.25 |
| 1 | 0.75 | 0.25 | 0.25 | 0.75 |
| 2 | 0.75 | 0.25 | 0.25 | 0.75 |
| 3 | 1.25 | 0.75 | 0.75 | 1.25 |





# 7.12 Image compression

The concept of orthogonality, as represented in the Discrete Cosine Transform, is crucial to performing image compression. Images consist of pixels, each represented by a number (or three numbers, for color images). The convenient way that methods like the DCT can carry out least squares approximation makes it easy to reduce the number of bits needed to represent the pixel values, while degrading the picture only slightly, and perhaps imperceptibly to human viewers.

Figure 11 shows a grayscale rendering of a 256 × 256 array of pixels. The grayness of each pixel is represented by one byte, a string of 8 bits representing 0 = 00000000 (black) to 255 = 11111111 (white). We can think of the information shown in the figure as a 256 × 256




# Figure 11: Grayscale image.

(a) Each pixel in the 256 × 256 grid is represented by an integer between 0 and 255.

(b) Crude compression–each 8 × 8 square of pixels is colored by its average grayscale value. An array of integers. Represented in this way, the picture holds 256² = 2¹⁶ = 64K bytes of information.

Matlab imports grayscale or RGB (Red-Green-Blue) values of images from standard image formats. For example, given a grayscale image file picture.jpg, the command x = imread('picture.jpg'); puts the matrix of grayscale values into the double precision variable x. If the JPEG file is a color image, the array variable will have a third dimension to index the three colors. We will restrict attention to gray scale to begin our discussion; extension to color is straightforward.

An m × n matrix of grayscale values can be rendered by Matlab with the commands imagesc(x); colormap(gray) while an m × n × 3 matrix of RGB color is rendered with the imagesc(x) command alone. A common formula for converting a color RGB image to gray scale is

Xgray = 0.2126R + 0.7152G + 0.0722B.

Figure 11(b) shows a crude method of compression, where each 8 × 8 pixel block is replaced by its average pixel value. The amount of data compression is considerable–there are only 32² = 2¹⁰ blocks, each now represented by a single integer–but the resulting image quality is poor. Our goal is to compress less harshly, by replacing each 8 × 8 block with a few integers that better carry the information of the original image.

To begin, we simplify the problem to a single 8× block of pixels, as shown in Figure 12, Row-1-(a). The block was taken from the center of the subject’s left eye in Figure 11. Figure 12, Row-1-(b) shows the one-byte integers that represent the grayscale intensities of the 64 pixels. In Figure 12, Row-1-(c), we have subtracted 256/2 = 128 from the pixel numbers.






Figure 12

(b)=(c)+128. First row: (a) Grayscale view of an 8 × 8 block; (b) Grayscale pixel values; (c) Grayscale pixel values minus 128. Second row: (a) Filtered image; (b) Grayscale pixel values, after transforming and adding 128; (c) Inverse transformed data.

to make them approximately centered around zero. This step is not essential, but Sauer claims that better use of the 2D-DCT will result because of this centering. My understanding is that if we do not subtract 128, it would make the constant term in the 2D-DCT too large compared with other coefficients. But the quantization matrix discussed in Section 11.2.3 on Quantization (which we will skip and leave you to read if you are interested in) is based on the assumption that the sizes of those coefficients are compatible. Subtracting 128 allows us to directly use the quantization matrix proposed by the JPEG standard.

To compress the 8 × 8 pixel block shown, we will transform the matrix of grayscale pixel values, which is Row-1-(c) in Figure 12,

| -18 | 40   | 48   | 54   | 42   | 31  | 6   | 17 |
| --- | ---- | ---- | ---- | ---- | --- | --- | -- |
| 38  | 40   | 36   | 33   | 37   | 43  | 31  | 13 |
| -26 | -94  | -106 | -103 | -90  | -17 | 18  | 31 |
| -21 | -79  | 2    | 31   | -126 | -99 | -11 | 36 |
| -33 | -57  | 25   | 79   | -113 | -98 | -6  | 22 |
| 16  | -107 | -128 | -109 | -128 | -98 | 4   | 7  |
| 35  | 1    | -45  | -61  | -59  | -21 | 11  | 31 |

We calculate the 2D-DCT of X to be

| Y = (Y ) = C XC⊤ = |      |      |      |     |     |     |     |
| ------------------ | ---- | ---- | ---- | --- | --- | --- | --- |
| -121               | -661 | 27   | -65  | 27  | 98  | 7   | -25 |
| 200                | 22   | -124 | 34   | -36 | -62 | 5   | 6   |
| 113                | 43   | -32  | 55   | -25 | -75 | -21 | 12  |
| -10                | 35   | -69  | -131 | 28  | 54  | -4  | -24 |
| -14                | -18  | 16   | 1    | -5  | -27 | 14  | -6  |
| -124               | -74  | 47   | 60   | -1  | -16 | -8  | 13  |
| -81                | 35   | -57  | -54  | -7  | 6   | 1   | -16 |
| 16                 | 11   | 5    | -15  | 11  | 12  | -1  | 9   |

after rounding to the nearest integer for simplicity.

The compression strategy we try will be a form of low-pass filtering. As discussed in the last section, least squares approximation with the 2D-DCT is just a matter of dropping terms from the interpolation function P₈(s, t). For example, we can cut off the contribution of






functions with relatively high spatial frequency by setting all Yk l = 0 for k + l ≥ 7 (recall that we continue to number matrix entries as 0 ≤ k, l ≤ 7). After low-pass filtering, the transform coefficients are

| −¹²¹ | −661 | 27   | −65 | 27   | 98  | 7 | 0 |
| ---- | ---- | ---- | --- | ---- | --- | - | - |
| 200  | 22   | −124 | 34  | −³⁶  | −62 | 0 | 0 |
| 113  | 43   |      | −32 | 55   | −25 | 0 | 0 |
| Y    | −10  | 35   | −⁶⁹ | −131 | 0   | 0 | 0 |
| low  | −¹⁴  | −18  | 16  | 0    | 0   | 0 | 0 |
| −¹²⁴ | −74  | 0    | 0   | 0    | 0   | 0 | 0 |
|      | 81   | 0    | 0   | 0    | 0   | 0 | 0 |

To reconstruct the image, we apply the inverse 2D-DCT as CTY C8low 8 and get the grayscale pixel values shown in Figure 12, Row-2-(a). We can see that the image in Row-2-(a) is similar to the original in Row-1-(a), but different in detail.

How much have we compressed the information from the 8× 8 block? The original picture can be reconstructed (losslessly, except for the integer rounding) by inverse transforming the 2D-DCT Y in (51) and adding back the 128. In doing the low-pass filtering by setting all Y = 0 for k + l ≥ 7, we have cut the storage requirement to 1+2+3+···+7 = 7 of the original amount, while retaining most of the qualitative visual aspects of the 8×8 block.

Interested readers are referred to Section 11.2.3 and Section 11.3 for further compression techniques.

% https://www.mathworks.com/help/images/discrete-cosine-transform.html

I = imread(’Lenna.png’); % color image I = 0.2126I(:,:,1)+0.7152I(:,:,2)+0.0722I(:,:,3); % gray scale % Note that the above I is already uint8 type (which is quite unexpected). % In fact, both K = uint8(0) + 1.1 and K = uint8(1)0.77 are 1 and uint8. % So, uint8(1)0.77 &#x3C; 0.95 is false while 10.77 &#x3C; 0.95 is true

% I = imread(’barbara.png’); % gray image

figure(2) subplot(2,2,1) imshow(I); hold on; title(’original image’);

T = dctmtx(8); % dctmtx returns Discrete cosine transform matrix dct = @(block_struct) T * block_struct.data * T’; % 2d-dct






% B = blockproc(A,[m n],fun) processes the image A by applying the function
% fun to each distinct block of size [m n] and concatenating the results
% into the output matrix, B.
% if I is not conveted to double precision, blockproc will complain and say
% that MTIMES (*) is not fully supported for integer classes.
I = double(I);
B = blockproc(I,[8 8],dct);

for mask_choice = 1:3
switch mask_choice
case 1
mask = [1 1 1 1 0 0 0 0 1 1 1 0 0 0 0 0 1 1
0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
case 2
mask = [1 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
otherwise
mask = [1 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0];
end
B2 = blockproc(B,[8 8],@(block_struct) mask .* block_struct.data);
invdct = @(block_struct) T’ * block_struct.data * T; % inverse 2d-dct
I2 = blockproc(B2,[8 8],invdct);
subplot(2,2,mask_choice+1)
imshow(uint8(I2));
hold on;
title([’mask choi =’,num2str(mask_choice)]);
end







# 7.13 Homework 14

1. (Sauer) Page 198, 4.1 Exercises, 9(c), 12.
2. (Sauer) Page 481, 10.2 Exercises, 1(b,c).
3. (Sauer) Page 491, 10.3 Exercises, 1(b,c).
4. (Sauer) Page 500, 11.1 Exercises, 3(c,d), 4(c,d).
5. (Sauer) Page 512, 11.2 Exercises, 2(c,d), 3(c,d).





# Boundary Value Problems

A general second-order boundary value problem (BVP) asks for a solution of

y′′(t) = f(t, y, y′), y(a) = yₐ, y(b) = yb. (1)

In the above equation, boundary conditions for the solution y(t) at a and b are prescribed. This is different from the pendulum equation y′′ = − g sin(y), which are also a second-order differential equation. In the latter case, we are given with the initial position and velocity y(0) = y₀ and y′(0) = v₀, and it is hence called initial value problem (IVP).

Figure 13: Comparison of initial value problem (IVP) and boundary value problem (BVP).

To aid your intuition, consider a projectile, which satisfies the second-order differential equation y′′(t) = −g as it moves, where y is the projectile height and g is the acceleration of gravity. Specifying the initial position and velocity uniquely determines the projectile’s motion, as an initial value problem. On the other hand, a time interval [a, b] and the positions y(a) and y(b) could be specified. The latter problem, a boundary value problem, also has a unique solution in this instance.




# Example 1

It is easy to verify that *y(t) = t sin t* is a solution of the boundary value problem

*y′′(t) = −y + 2 cos t, y(0) = 0, y(π) = 0*.





# Example 2

Show that

y′′(t) = −y, y(0) = 0, y(π) = 1 has no solution.

# Solution:

The differential equation has a two-dimensional family of solutions, generated by the linearly independent solutions cos t and sin t. All solutions of the equation must have the form y(t) = a cos t + b sin t. Substituting the first boundary condition, 0 = y(0) = a implies that a = 0 and y(t) = b sin t. The second boundary condition 1 = y(π) = b sin π = 0 gives a contradiction. There is no solution, and existence fails.




# Example 3

Show that

y′′(t) = −y, y(0) = 0, y(π) = 0

has infinitely many solutions.

# Solution:

Check that y(t) = k sin t for every real number k is a solution.





# 8.1 Shooting method

Define F(s) = difference between yb and y(b), where y(t) is the solution of the IVP with y(a) = ya and y′(a) = s. Then, the boundary value problem is reduced to solving the equation F(s) = 0. An equation solving method we learned before, say, the bisection method, may now be used to solve F(s) = 0. This is called the shooting method for solving the BVP.




# Example 4

Apply the Shooting Method to the boundary value problem

y′′ = 4y, y(0) = 1, y(1) = 3.

Solution: Write the differential equation as a first order system in order to use Matlab’s ode45 IVP solver:

y′ = v
v = 4y

function z=F(s)
a=0;
b=1;
yb=3;
ydot=@(t,y) [y(2);4*y(1)];
[t,y]=ode45(ydot,[a,b],[1,s]);
z=y(end,1)-yb; % end means last entry of solution y
end

Then, call sstar=fzero(@F,[-1,0]) and get sstar = -0.4203.

# Example 5

Apply the Shooting Method to the boundary value problem

y₁ ′ = (4 − 2y₂)/t³ , y₁(1) = 0, y₂(2) = 0. y₂ −ᵉʸ¹

Solution: If the initial condition y₂(1) were present, this would be an initial value problem. We will apply the Shooting Method to determine the unknown y₂(1), using Matlab routine ode45.

function z=F(s)
a=1;
b=2;
yb=0;
ydot=@(t,y) [(4-2*y(2))/t^3;-exp(y(1))];
[t,y]=ode45(ydot,[a,b],[0,s]);
z=y(end,2)-yb; % end means last entry of solution y
end

Then, s = fzero(@F,[0 2]) returns s = 1.5000. Using ode45 with initial values y₁(1) = 0 and y₂(1) = 1.5 results in the solution depicted in the following figure.

a=1;
b=2;
yb=0;
ydot=@(t,y) [(4-2*y(2))/t^3;-exp(y(1))];
[t,y]=ode45(ydot,[a,b],[0,s]);
figure;
plot(t,y)

1.6

1.4

1.2

1

0.8

0.6

0.4

0.2

0

1 1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2





245



# 8.2 Finite difference methods

The fundamental idea behind finite difference methods is to replace derivatives in the differential equation by discrete approximations, and evaluate on a grid to develop a system of equations.

Recall

y′(t) = y(t + h) − y(t − h) − h² y′′′(c)

and

y′′(t) =




# Example 7 Solve the BVP

y′′(t) = y − y², y(0) = 1, y(1) = 4 using finite difference method.

Solution: h = 1/(n + 1). y₀ = 1, yₙ₊₁ = 3. For i = 1, ..., n,

yi+1 − 2yi + yi−₁ − yi + y₂ = 0.

h² i

This leads to the system of equations for Y = (y₁, · · · , yₙ)ᵀ:

AY − h²Y + h²Y² = b

where Y = (y², · · · , y²)ᵀ,

| A | -2  | 1   | 0   | ... | 0   | 0   |     |     |
| - | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | -2  | ... | 0   | 0   | -1  |     |     |     |
|   | 0   | 1   | ... | ... | 0   | 0   |     |     |
|   | ... | ... | ... | ... | 0   | 0   | 0   |     |
|   | 0   | 0   | 0   | ... | ... | ... | 1   | 0   |
|   | ... | ... | 0   | 0   | 0   | ... | -2  | 1   |
|   | 0   | 0   | 0   | 0   | 1   | -2  | ... | ... |

We can solve the nonlinear system of equations by Newton’s methods:

Y = Y − [A − h²I + 2h²diag(Y )]⁻¹(AY − h²Y + h²(Y )² − b)

In each step, we need to solve JS = AY − h²Y + h²(Y )² − b and then subtract S from Y to obtain Y, where

J = [A − h²I + 2h²diag(Y )]

| J | 2h²y² − 2 − h² | 1   | 0              | ... | 0   | 0   |   |   |
| - | -------------- | --- | -------------- | --- | --- | --- | - | - |
|   | 1              | 1   | 2h²y² − 2 − h² | ... | 0   | 0   |   |   |
| 2 | ...            | ... | 0              | 1   | 0   |     |   |   |
|   | ...            | ... | ...            | ... | 0   | 0   | 0 |   |
|   | 0              | 0   | 0              | ... | ... | ... | 1 | 0 |





| 2h²y² − 2 − h² | 1 | 0 | ... | 0   | 0              |                |   |
| -------------- | - | - | --- | --- | -------------- | -------------- | - |
| 0              | 0 | 0 | ... | ... | 2h²y² − 2 − h² | 1              | n |
| 0              | 0 | 0 | ... | 0   | 1              | 2h²y² − 2 − h² | n |




# 4.5

| 4   | 3.5 | 3   | 2.5 | 2   | 1.5 | 1   | 0   |     |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | - |
| 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1 |





# Program 7.1 Nonlinear Finite Difference Method for BVP

Uses Multivariate Newton’s Method to solve nonlinear equation

Inputs: interval inter, boundary values bv, number of steps n

Output: solution w

Example usage: w=nlbvpfd([0 1],[1 4],40)

function w=nlbvpfd(inter,bv,n)
a=inter(1);
b=inter(2);
ya=bv(1);
yb=bv(2);
h=(b-a)/(n+1); % h is step size
w=zeros(n,1); % initialize solution array
for i=1:20 % loop of Newton step
w=w-jac(w,inter,bv,n)\f(w,inter,bv,n);
end
plot([a a+(1:n)*h b],[ya w’ yb]); % plot w with boundary data
end

function y=f(w,inter,bv,n)
y=zeros(n,1);
h=(inter(2)-inter(1))/(n+1);
y(1)=bv(1)-(2+h^2)w(1)+h^2w(1)^2+w(2);
y(n)=w(n-1)-(2+h^2)w(n)+h^2w(n)^2+bv(2);
for i=2:n-1
y(i)=w(i-1)-(2+h^2)w(i)+h^2w(i)^2+w(i+1);
end
end

function a=jac(w,inter,bv,n)
a=zeros(n,n); % WARNING: should use sparse matrix when n is large!
h=(inter(2)-inter(1))/(n+1);
for i=1:n
a(i,i)=2*h^2*w(i)-2-h^2;
end
for i=1:n-1
a(i,i+1)=1;
a(i+1,i)=1;
end
end






# Example 8 Solve the BVP

y′′(t) = y′ + cos y, y(0) = 0, y(π) = 1 using finite difference method.

Solution: h = π/(n + 1). y₀ = 0, yₙ₊₁ = 1. For i = 1, ..., n,

yi+1 − 2yi + yi−₁ − yi+1 − yi−₁ − cos yi = 0.

h² 2h

This leads to the system of equations for Y = (y₁, · · · , yₙ)ᵀ:

AY − h² cos(Y) = b

where cos(Y) = (cos(y₁), · · · , cos(yₙ))ᵀ,

|       | -2 | 1     | -h  | 0  | ...   | 0     | 0 |   |   |
| ----- | -- | ----- | --- | -- | ----- | ----- | - | - | - |
| 1 + h | -2 | 2     | ... | 0  | 0     | 0     |   |   |   |
| 2     | h  | ...   | ... | 0  |       |       |   |   |   |
| 0     |    | 1 + 2 | 0   | 0  | 0     | 0     |   |   |   |
|       |    |       | .   | .  | .     | .     | . | . | . |
| A =   | .  | .     | .   | .  | .     | .     |   |   |   |
| 0     | 0  | 0     | .   | .  | .     | 1 − h | 0 |   |   |
| .     | .  |       | 2   | -0 | h     |       |   |   |   |
| 0     | 0  | 0     | -2  | ¹  | -h    | 1 + 2 |   |   |   |
| 0     | 0  | 0     | ... | 0  | 1 + h | -²²   |   |   |   |

We can solve the nonlinear system of equations by Newton’s methods:

Y = Y − [A + h²diag(sin(Y ))]−¹(AY − h² cos(Y ) − b)

k+1 k k k k

In each step, we need to solve JS = AY − h² cos(Y ) − b and then ˢᵘᵇᵗʳᵃᶜᵗ S from Y to obtain Y ,

where J

k k k

k=1

J = [A + h²diag(sin(Y ))]






| -2    | ⁺             | h² sin(ʸ₁) | ¹               | -h | 0     | ...   | 0 | 0          |   |    |
| ----- | ------------- | ---------- | --------------- | -- | ----- | ----- | - | ---------- | - | -- |
| h     | -2            | 2          | ...             | 0  | 0     | 0     |   |            |   |    |
| 1 + 2 | 2 + h sin(y₂) | ...        |                 | 0  | 0     | 0     |   |            |   |    |
| 0     | 1 + h         | ...        | 0               | 0  | 0     |       |   |            |   |    |
| .     | .             | .          | .               | .  | .     | .     |   |            |   |    |
| =     | .             | .          | .               | .  | .     | .     |   |            |   |    |
| 0     | 0             | 0          | .               | .  | .     | 1 − h | 0 |            |   |    |
|       |               |            |                 |    |       | .     | . | -2         | 2 | -h |
| 0     | 0             | 0          | 2 + h sin(yₙ−₁) | 1  | 2     |       |   |            |   |    |
| 0     | 0             | 0          | ...             | 0  | 1 + h | -2    | ⁺ | h² sin(ʸₙ) |   |    |

Graph Data
1
0.8
0.6
0.4
0.2
0
-0.2
-0.4
-0.6
-0.8

0 0.5 1 1.5 2 2.5 3 3.5 call w=nlbvpfd([0 pi],[0 1],40) with f and jac redefined as follows

function y=f(w,inter,bv,n)
y=zeros(n,1);
h=(inter(2)-inter(1))/(n+1);
hh=h^2;
Iph2=1+h/2;
Imh2=1-h/2;
y(1)=-2w(1)+Iph2bv(1)+Imh2w(2)-hhcos(w(1));
y(n)=Iph2w(n-1)-2w(n)-hhcos(w(n))+Imh2bv(2);
for j=2:n-1
y(j)=-2w(j)+Iph2w(j-1)+Imh2w(j+1)-hhcos(w(j));
end

function a=jac(w,inter,bv,n)
a=zeros(n,n); % W
WARNING: should use sparse matrix when n is large!
h=(inter(2)-inter(1))/(n+1);
hh=h^2;
for i=1:n
a(i,i)=-2+hh*sin(w(i));
end
Iph2=1+h/2;
Imh2=1-h/2;
for i=1:n-1
a(i,i+1)=Imh2;
a(i+1,i)=Iph2;
end






# Homework 15

# Based on textbook: Tim Sauer, Numerical Analysis, 2nd edition

1. Page 363, 7.2 Computer Problem (but turn it into an Exercise), 2(a). Choose n = 2. Like in Example 6, find the numerical solution [y₁, y₂] manually and compare yi with the exact solution values y(ti) for i = 0, 1, 2, 3. (You might be asked to perform the same calculations in the exam.)





# 8.4 Computer Project 5

1. Page 354, 7.1 Computer Problems, 1(b)
2. Page 363, 7.2 Computer Problems, 4(b)




# 8.5 Error estimation of finite difference method for Poisson

tion in 1-D

The subsequent discussions mainly follow the textbook “Finite Difference Methods for Ordinary and Partial Differential Equations: Steady-State and Time-Dependent Problems” by Randall J. LeVeque.

Consider

u′′(x) = f(x) (2)

on interval [a, b] with u(a) = α and u(b) = β. To simplify the notation, we will assume a = 0 and b = 1 from now on.

We will attempt to compute a grid function consisting of values U₀, U₁,... Uₘ, Uₘ₊₁, where Uj is our approximation to the solution u(xj). Here xj = jh and h = m1 + 1 is the mesh width, the distance between grid points. From the boundary condition, we know that U₀ = α and Uₘ₊₁ = β, and so we have m unknown values U₁, ..., Uₘ to compute. If we replace u′′(x) in (2) by the centered difference approximation

D²Uj = 1 (Uj−₁ − 2Uj + Uj+1),

h²

then we obtain a set of m algebraic equations

1 (Uj−₁ − 2Uj + Uj+1) = f(xj) for j = 1, 2, ..., m. (3)

h²

Note that the first equation (j = 1) involves the value U₀ = α and the last equation (j = m) involves the value Uₘ₊₁ = β. We have a linear system of m equations for the m unknowns, which can be written in the form

AU = F, (4)

where U is the vector of unknowns U = [U₁, U₂, ..., Uₘ]ᵀ and

A =






# Tridiagonal Linear System

This tridiagonal linear system is nonsingular and can be easily solved for U from any right hand side F.

How well does U approximate the function u(x)? If we let U be the vector of true values

u(x₁)
u(x₂)
U = .
.
.
u(xₘ)

then the error vector E defined by

E = U − U

contains the errors at each grid point. Our goal is to obtain a bound on the magnitude of this vector E, showing that it is O(h²) as h → 0. To measure the magnitude of this vector we must use some norm, for example, the max-norm

∥E∥∞ = max |Ej| = max |Uj − u(xj)|.
1 ≤ j ≤ m 1 ≤ j ≤ m

We hope to show that ∥E∥∞ = O(h²).

Other norms are often used to measure grid functions, either because they are more appropriate for a given problem or simply because they are easier to bound since some mathematical techniques work only with a particular norm. Other norms that are frequently used include the 1-norm

∥E∥₁ = h Σj=1m |Ej|

and the 2-norm

∥E∥₂ = (h Σj=1m |Ej|²)1/2.





Note the factor of h that appears in these definitions.



# 8.5.1 Local truncation error

Now we want to estimate the error in our finite difference solution to BVP obtained by solving the system (4). The technique we will use is absolutely basic to the analysis of finite difference methods in general. It involves two key steps. We first compute the local truncation error (LTE) of the method and then use some form of stability to show that the global error can be bounded in terms of the LTE.

The global error simply refers to the error U − U that we are attempting to bound. The LTE refers to the error in our finite difference approximation of derivatives and hence is something that can be easily estimated using Taylor series expansions, as we have seen in Chapter on numerical ODEs. Stability is the magic ingredient that allows us to go from these easily computed bounds on the local error to the estimates we really want for the global error. Let’s look at each of these in turn.

252



# 8.5.2 Local truncation error

The LTE is defined by replacing Uj with the true solution u(xj) in the finite difference formula, which for the current case, is (3). In general, the true solution u(xj) won’t satisfy this equation exactly and the discrepancy is the LTE, which is denoted by τj

τj = 1 (u(xj−₁) − 2u(xj) + u(xj+1)) − f(xj) (5)

h² for j = 1, 2, ..., m. Of course in practice we don’t know what the true solution u(x) is, but if we assume it is smooth, then by the Taylor series expansions,

τj = u′′(xj) + 1 h2u(4)(xj) + O(h4) − f(xj).

As u is the exact solution, it satisfies u′′ = f. Hence

τj = 1 h2u(4)(xj) + O(h4).

Although u(4) is in general unknown, it is some fixed function independent of h, and so τj = O(h2) as h → 0.

Let τ = [τ1, τ2, ...τm] , then τ = A ˆ − U F.



# 8.5.3 Global error

Since E = U − ˆ A ˆ − AU − U, τ = U F, 0 = F, we obtain

AE = −τ.

This is simply the matrix form of the system of equations

1 (Ej−₁ − 2Ej + Ej+1) = −τ(xj) for j = 1, 2, ..., m (6)

h²

with the boundary condition E0 = Em+1 = 0.

The key observation is that the global error E satisfies a set of finite difference equations that has exactly the same form as our original difference equations for U except that the right-hand side is given by −τ rather than F.

From this it should be clear why we expect the global error E to be roughly the same magnitude as the local error τ. We can interpret (6) as a discretization of the ODE

e′′(x) = −τ(x), for 0 ≤ x1≤ 21 (4) (7)

with boundary condition e(0) = e(1) = 0. Since τ ≈ 12 h u (x), integrating twice shows that the global error should be roughly

e(x) ≈ − 1 h²u′′(x) + 1 h₂ (u′′(0) + x(u′′(1) − u′′(0)))

12 12

and hence the error is expected to be O(h²). (Please check that the right hand sides vanishes at x = 0, 1.)



# 8.5.4 Stability

The above argument is not completely convincing because we are relying on the assumption that solving the difference equations (6) gives a decent approximation to the solution of the differential equation (7). Since it is exactly this assumption we are trying to prove, the reasoning is rather circular. Instead, let’s look directly at the discrete system (6), which we will rewrite in the form

AhEh = −τh,

where the superscript h indicates that we are on a grid with mesh spacing h. This serves as a reminder that these quantities change as we refine the grid. In particular, the matrix Ah is an m × m matrix with h = 1/(m + 1) so that its dimension is growing as h → 0.

Let Ah⁻¹ be the inverse of this matrix. Then

Eh = − Ah⁻¹ τh

and taking norms gives

∥Eh∥ = ∥ Ah⁻¹ τh∥ ≤ ∥ Ah⁻¹ ∥∥τh∥.

We know that ∥τh∥ = O(h²) and we are hoping the same will be true for ∥Eh∥. It is clear what we need for this to be true: we need ∥ Ah⁻¹ ∥ to be bounded by some constant independent of h as h → 0:

∥ Ah⁻¹ ∥ ≤ C for all h sufficiently small.

Then we will have ∥Eh∥ ≤ C∥τh∥ which implies that ∥Eh∥ goes to zero at least as fast as ∥τh∥. This motivates the following definition of stability for linear BVPs.



# Definition 1

Suppose a finite difference method for a linear BVP gives a sequence of matrix equations of the form AhUh = Fh, where h is the mesh width. We say that the method is stable if (Ah)⁻¹ exists for all h sufficiently small (for h &#x3C; h₀, say) and if there is a constant C, independent of h, such that

∥ Ah⁻¹ ∥ ≤ C for all h &#x3C; h₀.



# 8.5.5 Consistency

We say that a method is consistent with the differential equation and boundary conditions if this simply says that ∥τh∥ → 0 as h → 0. of ∥ h∥ we have a sensible discretization the problem. Typically τ = O(hp) for some integer p > 0, and then the method is certainly consistent.



# 8.5.6 Convergence

A method is said to be convergence if ∥Eh∥ → 0 as h → 0. Combing the ideas introduced before, we arrive at the conclusion that

consistency   ⇒          (10)

stability = convergence.

This is easily proved by

∥Eh∥ ≤ ∥Ah⁻¹∥∥τh∥ ≤ C∥τh∥ → 0 as h → 0.

Although this has been demonstrated only for the linear BVP, in fact most analyses of finite difference methods for differential equations follow this same two-tier approach, and the statement (10) is sometimes called the fundamental theorem of finite difference methods. In fact, as our above analysis indicates, this can generally be strengthened to say that

O(hp) local truncation error   ⇒        O(p)

stability = h global error.

Consistency (and the order of accuracy) is usually the easy part to check. Verifying stability is the hard part. Even for the linear BVP just discussed it is not at all clear how to check the condition (9) since these matrices become larger as h → 0. For other problems it may not even be clear how to define stability in an appropriate way. As we will see, there are many definitions of “stability” for different types of problems. The challenge in analyzing finite difference methods for new classes of problems often is to find an appropriate definition of “stability” that allows one to prove convergence using (10). For nonlinear PDEs this frequently must be tuned to each particular class of problems and relies on existing mathematical theory and techniques of analysis for this class of problems.

Whether or not one has a formal proof of convergence for a given method, it is always good practice to check that the computer program is giving convergent behavior, at the rate expected. Appendix A in the textbook contains a discussion of how the error in computed results can be estimated.



# 8.5.7 Stability and convergence in the 2-norm

Recall that ∥A∥₂ = ρ(ATA) and when A is symmetric, ∥A∥₂ = ρ(A) = max1≤p≤m λp where λp refers to the pth eigenvalue of A.

The eigenvalues of A−1 are simply the inverses of the eigenvalues of A, so ∥A−1∥₂ = ρ(A−1) = max1≤p≤m λ−1 = min1≤p≤m λp.

We claim that the m eigenvalues of A in our finite difference method for u′′ = f are given by

λp = 2 (cos(pπh) − 1)   (11)

for p = 1, 2, ..., m with the corresponding eigenvectors given by

up = (up, up, ..., up) = [sin(pπh), sin(2pπh), ..., sin(mpπh)]T. (12)

The claim can be easily proved if one notice that

(A<up)j = 1 (sin((j − 1)pπh) − 2 sin(jpπh) + sin((j + 1)pπh)) h²</u

= 1 (2 sin(jpπh) cos(pπh) − 2 sin(jpπh)) h²

= λpup.j

The above derivative is also true for j = 1 and j = m since sin((1 − 1)pπh) = 0 = sin((m + 1)pπh).

It is easy to see that ∥A−1∥2 = (min ∑p=1m λp)−1 ∑p=1m λp = λ1.

By Taylor expansion, we can verify that

λ1 = 2 (cos(πh) − 1) = −π2 + O(h2).

So

∥A−1∥2 = 1 ≤ C (13)



and

∥Eh∥2 ≤ ∥(Ah)−1∥2∥τh∥2 ≤ Ch2. (14)

From now on, we use C to denote a general constant (which means it does not depend on h) whose value may change from line to line.



# 8.5.8 Max-norm estimates

In general, we can relate two different norms




# Theorem 1

Let ∥ · ∥α and ∥ · ∥β represent two different vector norms on ℝN, then there exists two constants C1 and C2 such that

C1∥x∥α ≤ ∥x∥β ≤ C2∥x∥α for all x ∈ ℝN. It is easy to verify that the vector norms defined by ∥x∥p = ∥(x1, ..., xN)∥p = (∑i=1N |xi|p)1/p satisfy

1. h∥x∥∞ ≤ ∥x∥1 ≤ Nh∥x∥∞,
2. √h∥x∥∞ ≤ ∥x∥2 ≤ √Nh∥x∥∞,
3. √h∥x∥2 ≤ ∥x∥1 ≤ √Nh∥x∥2.

Suppose we want to bound ∥E∥∞ = max |Ej|. By Theorem 1, we know

∥ᴱ∥∞ ≤ √ₕ∥ᴱ∥2 ≤ Ch

However, this does not show the second order accuracy that we hope to have. To show that ∥ᴱ∥∞ = O(h2), one can explicitly calculate the inverse of A and then show that ∥ᴬ−1∥∞ = O(1) and hence

∥ᴱh∥∞ ≤ ∥(ᴬh)−1∥∞∥τh∥∞ ≤ Ch2. (15)

We skip the proof (which can be found in Section 2.11 of the book by LeVeque) because we will present the proof for the 2-D case which can be applied to the current 1-D case.





# 8.5.9 How to handle Neumann boundary conditions

Now, we consider u′′ = f on [0, 1] with u′(0) = σ and u(1) = β. Now, our unknowns are [U₀, U₁, ..., Uₘ] and we need one more equation in addition to the m equations in (3). We can have, for example, the following three options:

1. U₁−U₀ = σ. The local truncation error is O(h).
2. 3U₀−4U₁+U₂ = σ. The local truncation error is O(h²).
3. First introduce an extra U₋₁. Then set 1 (U₁ − U₋₁) = σ and U₋₁−2U₀+U₁ = f(x₀). By eliminating U₋₁, we get 1 h 0 = σ + 2 f(x₀). The local truncation error is O(h²).

(a) Sample solution u′′ = f(x) = eˣ with u′(0) = σ = 0 and u(1) = β = 3. The solid line is the true solution. The plus sign shows a solution on a grid with 20 points using U₁−U₀ = σ. The circle shows the solution on the same grid using U₁−U₀ = σ + h f(x₀).

(b) A log-log plot of the max-norm error as the grid is refined is also shown for each case.



# 8.6 Poisson equation in 2-D

Consider the two-dimensional (2-D) Poisson equation with Dirichlet boundary condition

∆u def ∂²u ∂²u f( ) ( ) ∈ (16)

= ∂x₂ + ∂y₂ = x, y , x, y D,

u(x, y) = g(x, y), (x, y) ∈ ∂D. (17)

Here D = {(x, y), 0 &#x3C; x &#x3C; a, 0 &#x3C; y &#x3C; b} is a rectangle. Define the mesh points as the points of intersection of the straight lines xi = i∆x, i = 0, 1, ..., m + 1, and yj = j∆y, j = 0, 1, ..., n + 1. Here (m + 1)∆x = a and (n + 1)∆y = b.

| yj+2 |   | yj+2 |    |    |    |     |   |
| ---- | - | ---- | -- | -- | -- | --- | - |
| yj+1 | 1 | yj+1 | 1  | 4  | +1 |     |   |
| yj   | 1 | -4   | 1  | yj | 4  | -20 | 4 |
| yj-1 | 1 | yj-1 | 1  | 4  | 1  |     |   |
| yj-2 |   | yj   | -2 |    |    |     |   |

(a) $xi- 2$ xi+1 i+2$ (b) i$

xi-1xi $xi 2$ xi-1$ xi+1xi+2

Figure 15: Portion of the computational grid for ∆u = f in 2D. (a) 5 point stencil. (b) 9 point stencil.




# 8.6.1 The 5-point stencil for the Laplace operator

Let ui,j represent an approximation to u(xi, yj) and let fi,j = f(xi, yj). The five-point difference approximation to (16) at the point (i, j) is

1 2 (ui+1,j − 2ui,j + ui−1,j) + 1 2 (ui,j+1 − 2ui,j + ui,j−1) = fi,j.

∆x ∆y

For simplicity of notation we will consider the special case where a = b, ∆x = ∆y = h, and m = n, although it is easy to handle the general case. We can rewrite the above equation as

1 (ui+1,j + ui−1,j + ui,j+1 + ui,j−1 − 4ui,j) = fi,j.

(18)





# 8.6.2 Ordering the unknowns

Let

u[1] u₁j

u = u[2], where u[ʲ] = u₂j (19) . . . . . . u[ᵐ] umj

and let

B =
\[
\begin{bmatrix}
I &#x26; 0 &#x26; 0 &#x26; \cdots &#x26; 0 \\
-4 &#x26; 1 &#x26; 0 &#x26; \cdots &#x26; 0 \\
I &#x26; B &#x26; I &#x26; 0 &#x26; \cdots &#x26; 0 \\
1 &#x26; -4 &#x26; 1 &#x26; 0 &#x26; \cdots &#x26; 0 \\
\end{bmatrix}
\]

A =
\[
\begin{bmatrix}
1 &#x26; 0 &#x26; I &#x26; B &#x26; \cdots &#x26; 0 \\
\end{bmatrix}
\]
with B =
\[
\begin{bmatrix}
0 &#x26; 1 &#x26; -4 &#x26; 1 &#x26; \cdots &#x26; 0 \\
\end{bmatrix}
\]
(20) . . . . . . . . . . . . h² . . . . . . . . . . . . . . . . . . . .

. . . . 0 0 &#x26; \cdots &#x26; I &#x26; B &#x26; I &#x26; 0 &#x26; 0 &#x26; \cdots &#x26; 1 &#x26; -4 &#x26; ¹ &#x26; 0 &#x26; 0 &#x26; \cdots &#x26; 0 &#x26; I &#x26; B &#x26; 0 &#x26; 0 &#x26; \cdots &#x26; 0 &#x26; 1 &#x26; -4

where B ∈ Rᵐ×ᵐ and A ∈ Rᵐ²×ᵐ². Our numerical scheme (18) can be written as

Au = b (21)

with appropriate right hand side b.

Another possibility, which has some advantages when solving Au = b, is to use the black ordering shown in Figure 16. This ordering is significant because all four neighbours of red grid points are black points, and vice versa, and it leads to a matrix equation with the structure

D H ured = fred (22) Hᵀ D ublack fblack



# Example 9 (This is Example 8.8 in Sauer’s book)

Apply the Finite Difference Method with m = n = 5 to approximate the solution of the Laplace equation ∆u = 0 on [0, 1] × [1, 2] with the following Dirichlet boundary conditions:

- u(x, 1) = ln(x² + 1)
- u(x, 2) = ln(x² + 4)
- u(0, y) = 2 ln y
- u(1, y) = ln(y² + 1)




# Solution:

% Program 8.5 Finite difference solver for 2D Poisson equation
% with Dirichlet boundary conditions on a rectangle
% Input: rectangle domain [xl,xr]x[yb,yt] with MxN space steps
% Output: matrix w holding solution values
% Example usage: w=poisson(0,1,1,2,4,4)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%
% WARNING: when N is large, should use sparse matrix !!!
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%
function w=poisson2d(xl,xr,yb,yt,M,N)
f=@(x,y) 0; % define input function data
g1=@(x) log(x.^2+1); % define boundary values
g2=@(x) log(x.^2+4); % Example 8.8 is shown
g3=@(y) 2log(y);
g4=@(y) log(y.^2+1);
m=M+1;n=N+1;
mn=mn;
h=(xr-xl)/M;
h2=h^2;
k=(yt-yb)/N;
k2=k^2;
x=xl+(0:M)*h; % set mesh values
y=yb+(0:N)*k;
A=zeros(mn,mn);
b=zeros(mn,1);
for i=2:m-1 % interior points
for j=2:n-1
A(i+(j-1)*m,i-1+(j-1)*m)=1/h2;
A(i+(j-1)*m,i+1+(j-1)*m)=1/h2;
A(i+(j-1)*m,i+(j-1)*m)=-2/h2-2/k2;
A(i+(j-1)*m,i+(j-2)*m)=1/k2;
A(i+(j-1)*m,i+j*m)=1/k2;
b(i+(j-1)*m)=f(x(i),y(j));
end
end
for i=1:m % bottom and top boundary points
j=1;
A(i+(j-1)*m,i+(j-1)*m)=1;
b(i+(j-1)*m)=g1(x(i));
j=n;
A(i+(j-1)*m,i+(j-1)*m)=1;
b(i+(j-1)*m)=g2(x(i));
end
for j=2:n-1 % left and right boundary points
i=1;
A(i+(j-1)*m,i+(j-1)*m)=1;
b(i+(j-1)*m)=g3(y(j));
i=m;
A(i+(j-1)*m,i+(j-1)*m)=1;
b(i+(j-1)*m)=g4(y(j));
end
v=A\b; % solve for solution in v
labeling
w=reshape(v(1:mn),m,n); % translate from v to w
mesh(x,y,w')

| 5   | 1.8 | 1.6 | 1.4     | 10 | 1.2 | 1   | 0.8 | 15  | 0.6 | 0.4 | 0.2 | 20  | 0r  | 1.8 |
| --- | --- | --- | ------- | -- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 250 | 5   | 10  | nz=6115 | 20 | 25  | 1.6 | 1.4 | 1.2 | 1   | 0   | 0.2 | 0.4 | 0.6 | 0.8 |

Figure 17: (a) spy(A). (b) Solution.





# 8.6.3 Accuracy and stability

Let u(x, y) be the exact solution. The local truncation error τij at the (i, j) grid point is defined in the obvious way,

τij = 1 (u(xi+1, yj) + u(xi−1, yj) + u(xi, yj+1) + u(xi, yj−1) − 4u(xi, yj)) − f(xi, yj), (23) h²

and by splitting this into the second order difference in the x- and y-directions it is clear from previous results that

τij = 1 h² ∂4u(xi, yj) + ∂4u(xi, yj) + O(h4).

For this linear system of equations, the global error Eij = uij − u(xi, yj) then solves

AhEh = −τh (24)

just as in one-dimension. We add superscript h in A to stress its dependence on h. The method will be globally second order accurate in some norm provided that it is stable, i.e., that ∥(Ah)−1∥ is uniformly bounded as h → 0. In the 2-norm this is again easy to check for this simple problem, since we can explicitly compute the spectral radius of the matrix, as we did in one dimensional case.

The eigenvalues and eigenvectors of A can now be indexed by two parameters p and k corresponding to wave numbers in the x- and y-directions for p, k = 1, 2, ..., m. The (p, q) eigenvector up,q has the m² elements.

Here ∆²U = ∆(∆U) = uxxxx + 2uxyy + uyyyy. The above equation means that the exact solution satisfies

Ui−1,j−1 + Ui+1,j−1 + Ui−1,j+1 + Ui+1,j+1 + 4Ui,j−1 + 4Ui,j+1 + 4Ui−1,j + 4Ui+1,j − 20Ui,j

6h² = f + 1 h²∆f + O(h4).

This leads to the following modified nine-point scheme which is a 4th order approximation of (16).

ui−1,j−1 + ui+1,j−1 + ui−1,j+1 + ui+1,j+1 + 4ui,j−1 + 4ui,j+1 + 4ui−1,j + 4ui+1,j − 20ui,j

6h² = fi,j + 1 (fi−1,j + fi+1,j + fi,j−1 + fi,j+1 − 4fi,j)

= 1 (fi−1,j + fi+1,j + fi,j−1 + fi,j+1 + 8fi,j).




Related stencil is shown in Figure 15. The above scheme can be used when we only know fi,j which is f evaluated at (xi, yj). If we know the whole f, we can also evaluate ∆f directly and use f(xi, yj) + h² ∆f(xi, yj) on the right hand side.

# 8.6.5 Maximum norm estimates

This subsection will not be covered in the lecture and will not be tested. In (16)–(17), denote the set of mesh points in D by D and those on C def ∂D C G ∪ C h = by h. Let h = Dh h be the set of all mesh points in G def ∪ C = D.

Introduce the five-point difference operator L defined by

Lui,j = 1 (ui+1,j + ui−₁,j + ui,j₊₁ + ui,j−₁ − 4ui,j), (i, j) ∈ Dₕ.

The difference equations approximating (16)–(17) can be written as

Lui,j = fi,j, (i, j) ∈ Dₕ,

ui,j = gi,j, (i, j) ∈ Cₕ.

Our problem is to express, if possible, the discretization error ei,j = Ui,j − ui,j at the (i, j)th mesh point of Dₕ in terms of h. Here Ui,j = U(xi, yj). Define the local truncation error Ti,j = LUi,j − fi,j.

Then the error satisfies

Lei,j = Ti,j.

Assuming U ∈ C⁴(D) and using Taylor expansion, one can prove that

Ti,j = 1 h² ∂⁴U + ∂⁴U,

12 ∂x⁴ ξ,yj ∂y⁴ xi,η

where xi−₁ &#x3C; ξ &#x3C; xi+1 and yi−₁ &#x3C; η &#x3C; yi+1. Let






M = max max ∂⁴U, max ∂⁴U.

G ∂x⁴ G ∂y⁴

Then max |Lei,j| ≤ 1 h2M.

Dh 6

Applying Theorem 2 (to be presented) and using the fact that ei,j = 0 for (i, j) ∈ Cₕ, we know

max |ei,j| ≤ 1 (a2 + b2)h2M.

Dh 24

To prove Theorem 2, we need the following Lemma:





# Lemma 1

The simply connected open-bounded domain D with closed boundary curve C is covered with a square mesh defined by the lines *xi = ih, yj = jh, i, j = 0, ±1, ±2, .... The set of mesh points interior to D is denoted by Dₕ and the set on C by Cₕ. The function wi,j defined on Dₕ ∪ Cₕ is such that Lwi,j ≥ 0 for all (i, j) ∈ Dₕ where L is defined by (27). Prove that max wi,j ≤ max wi,j*.

*Dh Ch*




# Proof:

For any point p ∈ Dₕ, denotes its surrounding points by n, s, e, w. Then the assumption implies Lwₚ = (wₙ + wₛ + wₑ + ww − wₚ)/h² ≥ 0

wₚ ≤ 1 (wₙ + wₛ + wₑ + ww).

Now, we assume (34) is not true. Then, there is a p ∈ Dₕ so that wₚ ≥ wi,j ∀(i, j) ∈ Dₕ and wₚ > wi,j ∀(i, j) ∈ Cₕ. Equation (35) implies wₚ ≤ 1 (wₙ + wₛ + wₑ + ww) ≤ wₚ and therefore wₙ = wₛ = wₑ = ww = wₚ. By choosing p as the point say, n, and repeating the argument, we finally can prove that wi,j = wₚ for all points Dₕ and Cₕ. This contradicts the assumption wₚ > wi,j ∀(i, j) ∈ Cₕ. □






# Theorem 2

If v is any function defined on the set of mesh points Gₕ = Dₕ ∪ Cₕ in the rectangular region 0 ≤ x ≤ a, 0 ≤ y ≤ b, then

max |v| ≤ max |v| + 1 (a² + b²) max |ᴸᵛi,j|.

Dh Ch 4 (i,j)∈Dₕ

Proof: Define φi,j by

φi,j = 1 (x² + y²) = 1 (i² + j²)h².

4 i j 4

Clearly 0 ≤ φi,j ≤ 1 (a² + b²) ∀(i, j) ∈ Gh. One can easily check that

Lφi,j = 1.

Let N = max Dh |L vi,j| and define

w+ = v + Nφ, w− = −v + Nφ.

We then obtain

Lw± = ±L vi,j + N ≥ 0.

Since Nφ ≥ 0 and because of Lemma 2,

max(±vi,j) ≤ max w± ≤ max w± ≤ 1 (a² + b²)N + max ±vi,j.

Dh Dh i,j Ch i,j 4 Ch

So we conclude

max |vi,j| ≤ max |vi,j| + 1 (a² + b²) max |L vi,j|. □

Dh Ch 4 Dh





# 8.7 Heat equations in 1-D

We now begin to study finite difference methods for time-dependent partial differential equations (PDEs), where variations in space are related to variations in time. We begin with the heat equation (or diffusion equation)

∂tu = ν∂2u + f(x, t) in [0, 1],

(37)

with initial condition

u(x, 0) = η(x)

and boundary condition

u(0, t) = g0(t) and u(1, t) = g1(t).

Here ν is a positive constant.

Let xi = ih and tn = nΔt with h = m−1 being the mesh spacing and Δt being the time step. Let Un ≈ u(xi, tn) represent the numerical approximation at grid point xi, tn.

One natural discretization of (37) would be (Forward Euler + centered difference D2Un = Ui − 2Un + Ui ≈ ∂xu(xi, tn))

h2

Un+1 − Un = Un − 2Un + Un

i Δt i = ν i−1 h2 i+1 + f(xi, tn).

(38)




# 18

(a) (b)

$+$

tn

$j- 1$ j$ $j+1$

Figure 18: Stencils for the methods (38) and (40).

This is an explicit method since we can compute each $U^{n+1}$ explicitly in terms of the previous data:

$U^{n+1} = U^{n} + \nu \Delta t \frac{U^{n}{i-1} - 2U^{n}{i} + U^{n}_{i+1}}{h^2} + \Delta t f(x_i, t_n).$ (39)

Figure 18 shows the stencil of this method.

Another method, which is more useful, is the Crank-Nicolson method (Adams-Moulton 2)

$\frac{U^{n+1}{i} - U^{n}{i}}{\Delta t} = \frac{\nu}{2} \frac{U^{n}{i-1} - 2U^{n}{i} + U^{n}{i+1}}{h^2} + \frac{U^{n+1}{i-1} - 2U^{n+1}{i} + U^{n+1}{i+1}}{h} + f(x_i, t_{n+1}).$ (40)

It can be rewritten as

$U^{n+1} = U^{n} + \nu \Delta t \frac{U^{n}{i-1} - 2U^{n}{i} + U^{n}{i+1}}{2h^2} + U^{n+1}{i-1} - 2U^{n+1}{i} + U^{n+1}{i+1} + \Delta t f(x_i, t_{n+2}).$ (41)

or

$-r U^{n+1}{i-1} + (1 + 2r) U^{n+1}{i} - r U^{n+1}{i+1} = r U^{n}{i-1} + (1 - 2r) U^{n}{i} + r U^{n}{i+1} + \Delta t f(x_i, t_{n+2}).$ (42)

with $r = \nu \Delta t$. This is an implicit method and gives a tridiagonal system of equations to solve for all the values $U_j^{n+1}$ simultaneously.

The following is the code from Sauer’s book.

% Program 8.4 Crank-Nicolson method
% with Dirichlet boundary conditions
% input: space interval [xl,xr], time interval [yb,yt],
% number of space steps M, number of time steps N
% output: solution w
% Example usage: w=heatcn(0,1,0,1,10,10)
function w=heatcn(xl,xr,yb,yt,M,N)
f=@(x) sin(2pix).^2;
l=@(t) 0t;
r=@(t) 0t;






# Diffusion Coefficient Calculation

D=1; % diffusion coefficient

h=(xr-xl)/M; k=(yt-yb)/N; % step sizes

sigma=Dk/(hh); m=M-1; n=N;

WARNING: a and b should be spare matrix when m is large

a=diag(2+2sigmaones(m,1))+diag(-sigma*ones(m-1,1),1);

a=a+diag(-sigma*ones(m-1,1),-1); % define tridiagonal matrix a

b=diag(2-2sigmaones(m,1))+diag(sigma*ones(m-1,1),1);

b=b+diag(sigma*ones(m-1,1),-1); % define tridiagonal matrix b

lside=l(yb+(0:n)k); rside=r(yb+(0:n)k);

w(:,1)=f(xl+(1:m)*h)’; % initial conditions

for j=1:n

sides=[lside(j)+lside(j+1);zeros(m-2,1);rside(j)+rside(j+1)];

w(:,j+1)=a(bw(:,j)+sigmasides);

end

w=[lside;w;rside];

x=xl+(0:M)h; t=yb+(0:N)k;

mesh(x,t,w’);

view (60,30); axis([xl xr yb yt -1 1])

| 0.5 | 0.5 | 0   | -0.5 | -0.5 | -1  | 0   | 0   | 0.2 | 0.4 | 0.6 | 0.8 |
| --- | --- | --- | ---- | ---- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0.2 | 0.4 | 0.6  | 0.8  | 0.2 | 0.4 | 0.6 | 0.8 | 0   | 0.2 | 0.4 |
| 0.6 | 0.8 | 0   | 0.2  | 0.4  | 0.6 | 0.8 |     |     |     |     |     |





# Figure 19:

(a) w=heatcn(0,1,0,1,10,10).

(b) w=heatcn(0,1,0,1,50,50).



# 8.7.1 Local truncation error and order of accuracy

We can define the local truncation error as usual—we insert the exact solution u(x, t) of the PDE into the finite difference equation and determine by how much it fails to satisfy the discrete equation.

Example 10 The local truncation error of the method (38) is

τiⁿ = u(xi, tn+1) − u(xi, tn) − ν u(xi−1, tn) − 2u(xi, tn) + u(xi+1, tn) − f(xi, tn).

∆t h²

Although we don’t know u(x, t) in general, if we assume it is smooth and use Taylor series expansions about u(x, t), we find that

τiⁿ = ∂tu(xi, tn) + ∆t ∂2u(xi, tn) + 1 ∂3u(xi, tn) + · · ·

2 t 6 t

− ν ∂2u(xi, tn) + h² ∂4u(xi, tn) + · · · − f(xi, tn)

x 12 x

= ∆t ∂2u(xi, tn) − h² ν∂4u(xi, tn) + O(∆t² + h4).

2 t 12 x

In the last step, we have used the fact that u satisfies (37).

This method is said to be second order accurate in space and first order accurate in time since the truncation error is O(∆t + h²). The Crank-Nicolson method is centered in both space and time, and an analysis of its local truncation error shows that it is second order accurate in both space and time,

τiⁿ = O(∆t² + h²)

A method is said to be consistent if τiⁿ → 0 as ∆t, h → 0. Just as in the other cases we have studied (boundary value problems and initial value problems for ordinary differential equations (ODEs)), we expect that consistency, plus some form of stability, will be enough.



to prove that the method converges at each fixed point (X, T) as we refine the grid in both space and time. Moreover, we expect that for a stable method the global order of accuracy will agree with the order of the local truncation error, e.g., for Crank-Nicolson we expect that

Un − u(X, T) = O(∆t2 + h2)

as ∆t, h → 0 when ih = X and n∆t = T are fixed. For linear PDEs, the fact that consistency plus stability is equivalent to convergence is known as the Lax equivalence theorem and is discussed later after an introduction of the proper concept of stability. As usual, it is the definition and study of stability that is the hard (and interesting) part of this theory.




# 8.7.2 Method of lines discretizations

To understand how stability theory for time-dependent PDEs relates to the stability theory we have already developed for time-dependent ODEs, it is easiest to first consider the so called method of lines (MOL) discretization of the PDE. In this approach we first discretize in space alone, which gives a large system of ODEs with each component of the system corresponding to the solution at some grid point, as a function of time. The system of ODEs can then be solved using one of the methods for ODEs that we have previously studied. This approach is also often called a semidiscrete method, since we have discretized in space but not yet in time.

For example, we might discretize the heat equation (9.1) in space at grid point xi by

U′(t) = ν (Ui−₁(t) − 2Ui(t) + Ui+1(t)) + f(xi, t)
i h²
for i = 1, ..., m, where prime now means differentiation with respect to time. We can view this as a coupled system of m ODEs for the variables Ui(t), which vary continuously in time along the lines shown in Figure 20.

Figure 20: Method of lines interpretation. Ui(t) is the solution along the line forward in time at the grid point xi

This system can be written as

U′(t) = AU + g(t) (43)
where

| -2 | ¹  | f(x1, t) | + 12 g0(t) |
| -- | -- | -------- | ---------- |
| 1  | -2 | ¹        | f(x2, t)   |
| ν  | 1  | -2       | 1          |
| h² | .  | .        | .          |
| 1  | -2 | ¹        | f(xm−1)    |
| 1  | -² | f(xm)    | + 12 g1(t) |






This MOL approach is sometimes used in practice by first discretizing in space and then applying a software package for systems of ODEs. There are also packages that are specially designed to apply MOL. This approach has the advantage of being relatively easy to apply to a fairly general set of time-dependent PDEs, but the resulting method is often not as efficient as specially designed methods for the PDE.

As a tool in understanding stability theory, however, the MOL discretization is extremely valuable. We know how to analyze the stability of ODE methods applied to a linear system of the form (43) based on the eigenvalues of the matrix A, which now depend on the spatial discretization. If we apply an ODE method to discretize the system (43), we will obtain a fully discrete method which produces approximations Uⁿ ≈ Ui(tₙ) at discrete points in time which are exactly the points (xi, tₙ) of the grid that we shown in the stencil plot.

For example, applying Euler’s method Uⁿ⁺¹ = Uⁿ + ∆tf(Uⁿ) to this linear system results in the fully discrete method (38). Applying instead the trapezoidal method Un+1−Un = 1 (f(Un) + f(Un+1)) results in the Crank-Nicolson method (40). Applying a higher order linear multistep or Runge-Kutta method would give a different method, although with the spatial discretization (43) the overall method would be only second order accurate in space.

Replacing the right hand side of (43) with a higher order approximation of ∂²u(xi, t) and then using a higher order time discretization would give a more accurate method.





# 8.7.3 Stability theory

We now investigate the stability of schemes like (38) or (40). After diagonalization and substitution, (43) can be rewritten as (A = ΩᵀΛΩ, V = ΩU, g Ω (0) Ω (0)) = g, Vt = Ut = V′ = ΛV + g.

As Λ = diag(λ1, ..., λm) is a diagonal matrix, the computation of each component of V is decoupled. Similar to what we have done for the Poisson equation in 1-D, we can obtain λp = 2ν (cos(pπh) − 1) for p = 1, 2, 3, ..., m, where h = 1/(m + 1). Those eigenvalues are negative and the one farthest from the origin is λm ≈ −4ν/h². If we apply a numeric method for ODE to U′ = AU + g, we require −4ν∆t/h² ∈ S which is the stability region of the numeric method.



# Example 11

If we use forward Euler (38), we must require |1 + λₚ∆t| ≤ 1 for each value λₚ. Hence we require −2 ≤ −4ν∆t/h² ≤ 0. This limits the time step allowed to ν∆t ≤ 1/h².

This is a severe restriction: the time step must decrease at the rate of h² as we refine the grid, which is much smaller than the spatial width h when h is small.



# Example 12

If we use the trapezoidal method, we obtain the Crank–Nicolson discretization (40). The trapezoidal method for the ODE is absolutely stable in the whole left half-plane and the eigenvalues λₚ are always negative. Hence the Crank-Nicolson method is stable for any time step ∆t > 0. Of course it may not be accurate if ∆t is too large. Generally we must take ∆t = O(h) to obtain a reasonable solution, and the unconditional stability allows this.



# 8.7.4 Stiffness of the heat equation

Now, we assume ν = 1 for simplicity. Recall that for the A in (43), its eigenvalues

λₚ = 2 (cos(pπh) − 1)

h²

lie on the negative real axis with one fairly close to the origin λ₁ ≈ −π² for all h, while the largest in magnitude is λₘ ≈ −4/h². Because of λₘ, to use Euler method, we need a very small time step ∆t ≤ h²/2. But for the (vₘ, λₘ) pair in V′ = ΛV, it satisfies

d vₘ = λₘvₘ ≈ − 4 vₘ

dt h²

and therefore vₘ(t) ≈₂ vₘ(0)ᵉ−⁴t/h² which decays to zero very very fast. On the other hand, v₁(t) ≈ v₁(0)e−π t decays much slower. So, after a while, v₁ component is the main component in V that you can see while vₘ component is barely visible. Even though v₁ is the main component, it puts very little restriction on the time step you can take. It is the “invisible” component that limits the time step you can take.

If for a system of ODE U′ = AU, A has a wide range of eigenvalues, we say U′ = AU is a very stiff system. Stiffness is a reflection of the very different time scales present in the solution to the heat equation. High frequency spatial oscillations in the initial data will decay very rapidly due to rapid diffusion over very short distances, while smooth data decay much more slowly since diffusion over long distances takes much longer.



# 8.7.5 Convergence

We now address the question of convergence at a fixed point (X, T):

lim Uⁿ = u(X, T).

h→0, ∆t→0, jh=X, n∆t=T j

For simplicity, we will assume that ∆t and h are related by some fixed rules, e.g., ∆t = 0.4h² so that we can speak of convergence as ∆t → 0.

When applied to solve ∂ₜu = ν∂²u + f, the forward Euler and Crank-Nicolson methods we have studied so far can be written in the form

Uⁿ⁺¹ = B(∆t)Uⁿ + bⁿ(∆t) (44)

for some B(∆t) ∈ Rᵐ×ᵐ and some vector bⁿ(∆t) ∈ Rᵐ. For example, for forward Euler,

B(∆t) = I + ∆tA

where A = ν² tridiag(1, −2, 1). For Crank-Nicolson,

B(∆t) = I − ∆t A⁻¹ I + ∆t A



# Figure 21

Solutions to the heat equation at three different times (columns) shown for three different sets of initial conditions (rows). In the top row u₁(x, t₀) consists of only a low wave number, which decays slowly. The middle row shows data consisting of a higher wave number, which decays more quickly. The bottom row shows data u₃(x, t₀) that contains a mixture of wave numbers. The high wave numbers are most rapidly damped (an initial rapid transient), while at later times only the lower wave numbers are still visible and decaying slowly.



# Definition 2

A linear method of the form (44) is Lax-Richtmyer stable if, for each time T, there is a constant CT > 0 such that

∥ᴮ(∆ᵗ)ⁿ∥ ≤ CT for all ∆t > 0 and integers n for which n∆t ≤ T.



# Theorem 3 (Lax equivalence theorem)

A consistent linear method of the form (44) is convergent if and only if it is Lax-Richtmyer stable.

Proof: We only prove that stability implies convergence. The proof of the other direction can be found in most textbooks on functional analysis and is not required for this course. The numerical solution satisfies

Un+1 = BUn + bn.

Let ( un = u(xi, tn) ) and ( un = [un, \ldots, un]T ). By the definition of local truncation error ( τn ), we have [ un+1 = B un + bn + Δt τn. ] where ( τn = [τn, \ldots, τn]T ). Let ( En = Un - un ), then [ En+1 = B En - Δt τn. ]

Hence after ( N ) time steps, [ EN = BN E0 - Δt ∑n=1N BN-n τn-1, ] from which we obtain [ |EN| ≤ |BN| |E0| + Δt ∑n=1N |BN-n| |τn-1|. ]

If the method is Lax-Richtmyer stable, then for ( N Δt ≤ T ), [ -|EN| ≤ CT |E0| + T C \max1 ≤ n ≤ N |τn| → 0 ] as ( Δt → 0 ) for ( N Δt ≤ T ), provided the method is consistent (i.e., ( \max1 ≤ n ≤ N |τn-1| → 0 ) and we use appropriate initial data (i.e., ( |E0| → 0 ) as ( Δt → 0 )).




# Example 13

For the heat equation, the matrix ( A ) from ( U' = AU + g ) and the matrix ( B ) from ( U^{n+1} = B U^n + b^n ) are both symmetric. Recall that the 2-norm of a symmetric matrix is equal to its spectral radius. The eigenvalues of ( A ) are ( \lambda^A = 2\nu (\cos(p \pi h) - 1) ) with ( p = 1, 2, \ldots, m ).

[ B = I + \Delta t A, \quad \nu \Delta t \leq 1 \quad \Rightarrow \quad |B| \leq 1. ] Under the condition ( h^2 \leq \frac{2}{\Delta t} ), ( \lambda_p = 1 + \Delta t \lambda_p ) for all ( p ). Hence ( B^2 \leq 1 ). So the method is Lax-Richtmyer stable and hence convergent under this restriction on the time step.

Similarly, the matrix ( B ) for the Crank-Nicolson method is symmetric and has eigenvalues [ 1 + \frac{\Delta t \lambda^A}{2}, \quad 1 - \frac{\Delta t \lambda^A}{2} ] and so the Crank-Nicolson method is stable in the 2-norm for any ( \Delta t > 0 ). For the methods considered so far we have obtained ( |B| \leq 1 ). This is called strong stability. But note that this is not necessary for Lax–Richtmyer stability.

If there is a constant ( \alpha ) so that a bound of the form [ |B(\Delta t)| \leq 1 + \alpha \Delta t, ] for ( n \Delta t \leq T ), [ |B(\Delta t)^n| \leq e^{\alpha n \Delta t} \leq e^{\alpha T}. ]

Note that the matrix ( B(\Delta t) ) depends on ( \Delta t ), and its dimension grows as ( \Delta t, h \to 0 ). The general theory of stability in the sense of uniform power boundedness of such families of matrices is often nontrivial.





# 8.7.6 von Neumann analysis

We now introduce von Neumann analysis which is a useful technique to determine the time step size in order to get stability. To apply the von Neumann analysis to ∂ₜu = ν∂²u + f, we assume f = 0 and consider periodic boundary condition on [0, 1].



# Lemma 2

Let i = √−1. Given v = (v₀, v₁, ..., vM), define its discrete fourier transform (DFT)

v̂ₖ = √(1/(M + 1)) Σj=0M vj e−2πikj/(M+1)   k = 0, ..., M.

Then

vj = √(1/M) Σk=0M v̂k e2πikj/(M+1)   j = 0, ..., M.

Moreover, ∥v∥2 = ∥v̂∥2 with v2 = v2 and v̂ = v̂2. Formula (47) is called the inverse discrete fourier transform (iDFT). Note that v₀ = vM+1 for any vj defined by (47).




# Proof:

√(1/(M + 1)) Σk=0M v̂k e2πikj/(M+1) = 1/(M + 1) Σl=0M Σk=0M vl e−2πikl/(M+1) e2πikj/(M+1)

= 1/(M + 1) Σl=0M vl Σk=0M e−2πikl/(M+1) e2πikj/(M+1)

Note that Σk=0M e2πik(j−l)/(M+1) = M + 1 if l = j and = 1−e2πi(M+1)(j−l)/(M+1) = 0 if l ≠ j. Hence

√(1/(M + 1)) Σk=0M v̂k e2πikj/(M+1) = vj.

Moreover,

∥v̂∥² = Σk=0M v̂k v̂k = 1/(M + 1) Σj=0M Σl=0M vj e−2πikj/(M+1) e2πikl/(M+1)

= 1/(M + 1) Σj,l vj vl = v². □






Remark:

Whether or not you multiply an h = 1/(M + 1) to the square of the 2-norm of a vector of length M + 1 does not change ∥v∥2 = ∥v̂∥2 since this h appears on both sides.






# Consider the forward Euler scheme for ∂ₜu = ν∂²u

Uⁿ⁺¹ = Uⁿ + ν∆t (Uⁿ − 2Uⁿ + Uⁿ ), j = 0, ..., m (48)

with periodic boundary condition Uⁿ⁺¹ = Uⁿ⁺¹ . (Recall homework 1 for how to deal with periodic boundary conditions.) From the knowledge of FFT and iFFT, we know given any vector Uⁿ = (Uⁿ, Uⁿ, ..., Uⁿ ), 0 1 m

Uⁿ = √ 1/m Σk=0m + 1 Uᵏ ej 2πikx for (49) j = 0, 1, ..., m,

for some ˆ n (49), Plugging into (48), we get

m ˆ n⁺¹ − ˆ n − ν∆t Σk=0m (2πikh)² Uₖ ej 2πikx = 0, j = 0, ..., m.

So the left hand side is the iDFT of 0. By the uniqueness of the iDFT, all the coefficients must vanish. Hence

ˆ n⁺¹ = Q ˆ n, Q = 1 + ν∆t/h² πkh

Q is called the symbol or amplification factor of the discrete operator on the right hand side of (48). If ∥ ˆ n⁺¹∥ ≤ ∥ ˆ n∥, then U ² ≤ U ². By Lemma 2, this implies U ² ≤ U ².

Note that Q ≤ 1 and we want to make sure Q ≤ 1. We then see that Q ≤ 1 is guaranteed if ν∆t ≤ 1/h².





# 8.8 Homework 16

1. (Sauer) Page 392, 8.1 Exercises, 4, 6

Please note that if one wants to solve ∆u = f with appropriate boundary condition on a general multi-dimensional region Ω, the finite difference method that we have learned so far fails. To solve PDEs on general multi-dimensional regions, people have invented finite element methods. You are encouraged to read Sections 7.3.2 and 8.3.2 to learn the basics of finite element methods.