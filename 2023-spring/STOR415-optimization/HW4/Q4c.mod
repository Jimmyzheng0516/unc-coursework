param n;

param c {j in 1..n};
param d {j in 1..n};

var x {i in 1..n} >=0;
var s {i in 0..n} <=4000, >= 0;

minimize cost: sum {j in 1..n} c[j]*x[j];

subject to init1: s[0]=2000;
subject to init2: s[n]=0;

subject to cons{i in 1..n}: 
s[i-1]+x[i] = s[i]+d[i];




