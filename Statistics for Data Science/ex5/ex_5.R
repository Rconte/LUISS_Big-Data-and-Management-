california_price <- read.csv('california_price.csv')
head(california_price)

summary(california_price)
names(california_price)


ncol(california_price)
nrow(california_price)

california_corr <- cor(california_price)
california_corr
library(corrplot)
corrplot(california_corr)
library(caret)
?createDataPartition()

idx <- createDataPartition(california_price$median_house_value, p = 0.7, list = FALSE)
idx

y = california_price$median_house_value 
X = california_price[,-29]
head(X)

tr_california <- california_price[idx,]

te_california <- california_price[-idx,]

X_tr <- tr_california[,-29]
X_te <- te_california[,-29]
y_tr <- tr_california[29]
y_te <- tr_california[29]

y_tr

dim(y_tr)

?train

ctrl <- trainControl( method = 'cv', number = 10)

california_fit <- train(median_house_value ~ . , data = tr_california, method = 'lm', trControl = ctrl)
summary(california_fit)
names(california_fit)
coef(california_fit$finalModel)

library(glmnet)
X_tr <- as.matrix(X_tr)
X_te <- as.matrix(X_te)
y_tr <- as.matrix(y_tr)
y_te <- as.matrix(y_te)

fitglmnet <- glmnet(X_tr, y_tr, alpha = 0 )
class(fitglmnet)
par(mfrow = c(3,1))
plot(fitglmnet,xvar = 'lambda', label = TRUE)

?cv.glmnet
 cv <- cv.glmnet(X_tr,y_tr)
names(cv) 

optimal_lambda <-cv$lambda.min
optimal_lambda

#plot(,optimal_lambda) vaffanculo

fitglmnet2 <- glmnet(X_tr, y_tr, alpha = 1 )
fitglmnet2
plot(fitglmnet2,xvar = 'lambda', label = TRUE)
fitglmnet3 <- glmnet(X_tr, y_tr, alpha = 0.9 )
plot(fitglmnet3,xvar = 'lambda', label = TRUE)

rmse1<-RMSE(predict(california_fit,X_tr),y_tr)
rmse1
rmse2<-RMSE(predict(fitglmnet),X_tr)
rmse2

