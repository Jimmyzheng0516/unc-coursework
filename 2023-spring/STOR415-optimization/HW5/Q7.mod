param n;
param m;

param A {i in 1..m, j in 1..n}; 
param b {i in 1..m};

var z;
var y {j in 1..m};
var x {j in 1..n};

minimize residual: z;

subject to cons1 {i in 1..m}: 
z >= y[i];

subject to cons2 {i in 1..m}: 
z >= -y[i];

subject to cons3 {i in 1..m}:
b[i] - sum {j in 1..n} A[i,j]*x[j] = y[i];