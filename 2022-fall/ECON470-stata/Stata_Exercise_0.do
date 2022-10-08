*点击左上角file然后选择import你需要的任何file类型*

* Q1 *
ci means bwght mage cigs, level(90)
summarize
* summarize才可以看std.dev，ci means看的是sampling distribution的std.dev也就是std.err

histogram bwght, percent normal title("Relative Frequency of Birth Weight (Jimmy Zheng)") ytitle("") xtitle("Birth Weight(g)") text(7 1600 "Normal Distribution" "Density Curve", box margin(l+1 r+1 t+1 b+1)) 

kdensity bwght, normal title("Distribution of Birth Weight and a Normal Distribution (Jimmy Zheng)", size(*0.7)) ytitle("") xtitle("Birth Weight(g)")

egen bwght_mean = mean(bwght)
egen bwght_sd = sd(bwght)

ksmirnov bwght = normprob((bwght-bwght_mean)/bwght_sd) 
*inspect Combined K-S: the p-value < 0.01, so we reject the null of normality*

ttest bwght = 3430, level(99)
ttest bwght = 3430, level(95)
ttest bwght = 3430, level(90)

graph twoway scatter bwght cigs, title("Mother's Cig. Consumption and Infant Birth Weigh (Jimmy Zheng)", size(*0.8)) xtitle("Mother's Cig. Consumption") ytitle("Infant Birth Weight")

pwcorr cig meduc bwght, sig
* Add sig will display p-values correspondingly*

* Q2 *
gen t = _n
tsset t
tsline IPI, title("U.S. Monthly Industrial Production Index (Jimmy Zheng)", size(*0.85)) xtitle("Month") ytitle("Industrial Production Index (IPI)")

gen g_ipi = log(IPI)-log(IPI[_n-1])

tsline g_ipi, title("The Growth of U.S. Monthly Industrial Production Index (IPI) (Jimmy Zheng)", size(*0.7)) xtitle("Month") ytitle("The Growth of IPI")

ci means g_ipi, level(95)

ttest g_ipi = 0.003, level(95)

gen ln_y = log(IPI)
regress ln_y t
predict trend
predict cycle, resid
tsline ln_y trend, title("The Growth of U.S. Monthly Industrial Production Index (IPI) and Predicted Trend Line (Jimmy Zheng)", size(*0.585)) xtitle("Month") ytitle("The Growth of IPI")
tsline cycle, title("The Growth Cycle of U.S. Monthly Industrial Production Index (IPI) (Jimmy Zheng)", size(*0.7)) xtitle("Month") ytitle("The Growth Cycle of IPI")



