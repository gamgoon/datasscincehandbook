import sklearn.datasets
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression, Lasso
from sklearn.preprocessing import normalize
from sklearn.metrics import r2_score

diabetes = sklearn.datasets.load_diabetes()
# print("---------------------------")
# print(diabetes['data'])
# print("---------------------------")
# print(diabetes['target'])
X, Y = normalize(diabetes['data']), diabetes['target']
# print("---------------------------")
# print(X)
# print("---------------------------")
# print(Y)
# print("---------------------------")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.8)
# print(X_train)
# print("---------------------------")
# print(X_test)
# print("---------------------------")
# print(Y_train)
# print("---------------------------")
# print(Y_test)
# print("---------------------------")
linear = LinearRegression()
linear.fit(X_train, Y_train)
preds_linear = linear.predict(X_test)
corr_linear = round(pd.Series(preds_linear).corr(pd.Series(Y_test)), 3)
rsquared_linear = r2_score(Y_test, preds_linear)

print("선형 계수:")
print(linear.coef_)
plt.scatter(preds_linear, Y_test)
plt.title("선형 회귀 결과. 상관관계 = %f R^2 점수 = %f" % (corr_linear, rsquared_linear))
plt.xlabel("예측값")
plt.ylabel("실루엣")
plt.plot(Y_test, Y_test, 'k--')
plt.show()

lasso = Lasso()
lasso.fit(X_train, Y_train)
preds_lasso = lasso.predict(X_test)
preds_lasso = round(pd.Series(preds_lasso).corr(pd.Series(Y_test)), 3)
corr_lasso = round(pd.Series(preds_lasso).corr(pd.Series(Y_test)), 3)
rsquared_lasso = round(r2_score(Y_test, preds_lasso), 3)

print("라소 계수:")
print(lasso.coef_)
plt.scatter(preds_lasso, Y_test)
plt.title("라소 회귀 결과. 상관관계= %f R^2 점수 = %f" % (corr_lasso, rsquared_lasso))
plt.xlabel("예측값")
plt.ylabel("실젯값")

plt.plot(Y_test, Y_test, 'k--')
plt.show()