import statsmodels.api as sm
x = [0,1,2,0,1,2]
#calculate autocorrelations
sm.tsa.acf(x)