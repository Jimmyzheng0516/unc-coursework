param n;  
param m; 
param A {i in 1..m, j in 1..n}; 
param b {i in 1..m};           
param c {j in 1..n};        
var x {j in 1..n} >=0;
minimize cost:  sum {j in 1..n} c[j] * x[j];
subject to cons {i in 1..m}:
sum {j in 1..n} A[i,j]*x[j] >= b[i];
