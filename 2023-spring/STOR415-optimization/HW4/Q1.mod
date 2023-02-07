var x1 >=0; # valves from supplier 1
var x2 >=0; # valves from supplier 2
var x3 >=0; # valves from supplier 3

minimize cost: 5*x1+4*x2+3*x3;  

subject to c1: 0.4*x1+0.3*x2+0.2*x3 >= 500;  
subject to c2: 0.4*x1+0.35*x2+0.2*x3 >= 300; 
subject to c3: 0.2*x1+0.35*x2+0.6*x3 >= 300; 
subject to c4: x1 <= 700; 
subject to c5: x2 <= 700; 
subject to c6: x3 <= 700; 