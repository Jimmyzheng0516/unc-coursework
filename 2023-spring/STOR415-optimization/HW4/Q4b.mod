var x1 >=0; 
var x2 >=0; 
var x3 >=0; 
var x4 >=0;
var x5 >=0;
var x6 >=0;
var s0 >=0;
var s1 >=0;
var s2 >=0;
var s3 >=0;
var s4 >=0;
var s5 >=0;
var s6 >=0;

minimize cost: 0.75*x1+0.72*x2+0.9*x3+0.95*x4+0.92*x5+0.85*x6;  

subject to c1: 2000+x1 = 5000+s1;  
subject to c2: s1+x2 = 8000+s2; 
subject to c3: s2+x3 = 10000+s3; 
subject to c4: s3+x4 = 11000+s4; 
subject to c5: s4+x5 = 9000+s5; 
subject to c6: s5+x6 = 7000+s6; 
subject to c7: s1 <= 4000; 
subject to c8: s2 <= 4000; 
subject to c9: s3 <= 4000; 
subject to c10: s4 <= 4000; 
subject to c11: s5 <= 4000; 
subject to c12: s0 = 2000;
subject to c13: s6 = 0;
 