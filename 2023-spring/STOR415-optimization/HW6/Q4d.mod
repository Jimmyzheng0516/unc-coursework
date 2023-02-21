param n;

param p {i in 1..n};
param f {i in 1..n-1};
param c;

var x {i in 1..n} >= 0;
var s {i in 1..n} >= 0;

minimize z: sum{i in 1..n} p[i]*x[i];

subject to cons1 {i in 2..n}:
s[i] = s[i-1] + x[i] - f[i-1];

subject to cons2 {i in 1..n}:
s[i] <= c;

subject to cons3: x[1] = 0;
subject to cons4: x[n] = 0;
subject to cons5: s[1] = c;

