*点左上角“File“然后import你想要的data格式”*

putexcel set Stata_Hw_1_table, replace

*Q1*
reg MORT INC_PC ALC_PC TOB_PC POV ED_HS ED2_COLL HEALTH_PC PHYS URBAN AGED
putexcel A2 = etable

*Q4*
test HEALTH_PC PHYS

*Q5*
gen ln_alc = log(ALC_PC)
gen ln_inc = log(INC_PC)
gen ln_tob = log(TOB_PC)
gen ln_mort = log(MORT)

reg MORT ln_inc ln_alc ln_tob POV ED_HS ED2_COLL HEALTH_PC PHYS URBAN AGED
putexcel A20 = etable

reg ln_mort ln_inc ln_alc ln_tob POV ED_HS ED2_COLL HEALTH_PC PHYS URBAN AGED
putexcel A38 = etable

* Export Regression Results
putexcel set report.xlsx, replace
putexcel A13 = etable

putdocx begin
putdocx table results = etable
putdocx save report1, replace
