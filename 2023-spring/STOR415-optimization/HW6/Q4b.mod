var x1 >= 0;
var x2 >= 0;
var x3 >= 0;
var x4 >= 0;
var x5 >= 0;
var s1 >= 0;
var s2 >= 0;
var s3 >= 0;
var s4 >= 0;
var s5 >= 0;

minimize cost: 2.19*x2 + 1.95*x3 + 2.45*x4;

subject to c1: s2 = s1 + x2 - 11;
subject to c2: s3 = s2 + x3 - 6;
subject to c3: s4 = s3 + x4 - 9;
subject to c4: s5 = s4 - 10;
subject to c5: s1 <= 13;
subject to c6: s2 <= 13;
subject to c7: s3 <= 13;
subject to c8: s4 <= 13;
subject to c9: s5 <= 13;
subject to c10: s1 = 13;
subject to c11: x1 = 0;
subject to c12: x5 = 0;
