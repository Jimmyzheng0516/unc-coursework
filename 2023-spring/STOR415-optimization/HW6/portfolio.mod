param n; # number of stocks
param m; # number of scenarios

param R {i in 1..m, j in 1..n};
param P {i in 1..m};
param delta;

var r {i in 1..m};
var d {i in 1..m};
var x {j in 1..n} >=0;

minimize ADR: sum{i in 1..m} P[i]*d[i];

subject to cons1: sum{i in 1..m} P[i]*r[i] >= delta;
subject to cons2: sum{j in 1..n} x[j] = 1;
subject to cons3 {i in 1..m}: sum{j in 1..n} R[i,j]*x[j] = r[i];
subject to cons4 {i in 1..m}: d[i] >= 0;
subject to cons5 {i in 1..m}: d[i] >= -r[i];

