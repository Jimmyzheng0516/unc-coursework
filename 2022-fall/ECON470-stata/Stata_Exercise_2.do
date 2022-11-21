*点左上角“File“然后import你想要的data格式”*

*Q2*

gen work = (WAGE>0)

gen ed_par = (ED_mom + ED_dad)/2

*Q3*

graph twoway scatter WAGE ED, title("Education and Female Wage(Jimmy Zheng)", size(*0.8)) xtitle("Education Level") ytitle("Wage")

*Q4*

reg WAGE AGE ED CHILD_6 WAGE_h AGE_h ed_par 
display e(ll) 
* display e(ll) shows the log-likelihood for OLS

tobit WAGE AGE ED CHILD_6 WAGE_h AGE_h ed_par, ll(0)

heckman WAGE AGE ED CHILD_6 WAGE_h AGE_h ed_par, select(work= AGE ED CHILD_6 HOURS_h)

*Q5*

probit  WAGE AGE ED CHILD_6 WAGE_h AGE_h ed_par
mfx

*Q7*

probit  work AGE ED CHILD_6 HOURS_h
estimates store U
probit work AGE ED
estimates store R
lrtest U R

*Export*
putdocx begin
putdocx table results = etable
putdocx save report1, replace
