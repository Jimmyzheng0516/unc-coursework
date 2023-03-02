param n;

param srate;
param startcash;
param rev {i in 1..n};
param exp {i in 1..n};

var b {i in 0..n} >=0;
var c {i in 1..n+1} >=0;
var D; # difference in total revenue and total expense
var I; # total interest payment

minimize z: sum{i in 1..n} srate*b[i];

subject to cons1: b[0] = 0;
subject to cons2: c[1] = startcash;
subject to cons3 {i in 2..n+1}: 
c[i] = c[i-1] + rev[i-1] + b[i-1] - exp[i-1] - (1+srate)*b[i-2];

# the following constraints are used in Question 4
subject to cons4: 
D = sum{i in 1..n}rev[i] - sum{i in 1..n}exp[i];
subject to cons5:
I = sum{i in 1..n}srate*b[i];


