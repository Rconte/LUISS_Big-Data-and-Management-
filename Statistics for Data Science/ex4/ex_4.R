head(clouds)
typeof(clouds)
ncol(clouds)
nrow(clouds)
names(clouds)
summary(clouds)

#Average
mean(clouds$time)
mean(clouds$sne)
mean(clouds$cloudcover)
mean(clouds$prewetness)
mean(clouds$rainfall)

summary(clouds$time)
summary(clouds$sne)
summary(clouds$cloudcover)
summary(clouds$prewetness)
summary(clouds$rainfall)

hist(clouds$time, col = 'green')
hist(clouds$sne, col = 'red')
hist(clouds$cloudcover, col = 
      'purple')
hist(clouds$prewetness, col = 'grey')
hist(clouds$rainfall, col = 'yellow')


boxplot(clouds$time, col = 'green', horizontal = TRUE)
boxplot(clouds$sne, col = 'red',horizontal = TRUE)
boxplot(clouds$cloudcover, col = 
       'purple',horizontal = TRUE)
boxplot(clouds$prewetness, col = 'grey',horizontal = TRUE)
boxplot(clouds$rainfall, col = 'yellow',horizontal = TRUE)

?boxplot
rainbox <- boxplot(clouds$rainfall ~ clouds$seeding, data = clouds, col = 'Blue', horizontal = TRUE, main = 'Guarino libero', xlab = 'Rainfall', ylab = 'Seeding', legends.text = 'Amount of Rain')
?pairs

rainbox
outlier <- rainbox$out

?hist
numclouds <- clouds[,2:7]
numclouds <- numclouds[-5]

pair_clouds <- pairs(numclouds)
?aggregate
aggregate(clouds$rainfall ~ clouds$seeding, FUN = 'mean')
aggregate(clouds$rainfall ~ clouds$seeding, FUN = 'sd')
aggregate(clouds$rainfall ~ clouds$seeding, FUN = 'median')

library(corrplot)

cor_clouds <- cor(numclouds)
corrplot(cor_clouds)

clouds_frm <- clouds$rainfall ~ clouds$seeding + clouds$seeding:(clouds$sne + clouds$cloudcover + clouds$prewetness + clouds$echomotion) + clouds$time
Xstar <- model.matrix(clouds_frm, data = clouds)
Xstar
attr(Xstar,'contrasts')
library(caret)
idx  <- createDataPartition(clouds$rainfall, p = 0.8, list = FALSE)
idx
tr_clouds <- clouds[idx,]
te_clouds <- clouds[-idx,]
?lm
rain_fit = lm(clouds_frm, tr_clouds)
summary(rain_fit)
plot(rain_fit)
coef(rain_fit)
vcov_rain <- vcov(rain_fit)
diag(vcov_rain)


lm(formula = clouds_frm, data = tr_clouds)
plot(clouds$sne~clouds$seeding)
?predict
pred_tr <- predict(rain_fit, tr_clouds)
pred_tr

pred_te <- predict(rain_fit,te_clouds)
pred_te

my_rmse = function(truth,pred){
  out = sqrt(mean((truth - pred)^2))
  return(out)
}

my_rmse(tr_clouds$rainfall, pred_tr)
my_rmse(te_clouds$rainfall, pred_te)

?caret::train()


?caret::trainControl()

ctrl = trainControl(method = 'cv', number = 10)



