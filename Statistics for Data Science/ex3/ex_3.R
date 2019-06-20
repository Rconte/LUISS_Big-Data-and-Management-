typeof(hubble)
summary(hubble)
names(hubble)
ncol(hubble)
nrow(hubble)

mean(hubble$x)
mean(hubble$y)

sd(hubble$x)
sd(hubble$y)

median(hubble$x)
median(hubble$y)

cov(hubble$x,hubble$y)

hist(hubble$x)
barplot(hubble$x, hubble$y, beside = TRUE, col = 2, legend.text = 'x')
?boxplot
boxplot(hubble$x, hubble$y, horizontal = TRUE ,col = 'Blue')
plot(hubble$x,hubble$y, xlab = 'x', ylab = 'y', col = 'Red')
hubble_corr <- cor(hubble[,2:3]) # posso anche mettere -1 
library(corrplot)
corrplot((hubble_corr))

library(caret)
?createDataPartition
set.seed(1234)
idx <- createDataPartition(hubble$y, p = 0.8, list = FALSE)
hubble[idx,2:3]
hubble[-idx,2:3]


tr_hubble = hubble[idx,2:3]
tr_hubble
te_hubble = hubble[-idx,2:3]
te_hubble
?lm
hubblefit <- lm(forumula = y ~ x-1  , data = tr_hubble  )
hubblefit
plot(hubble$x,hubble$y, xlab = 'x', ylab = 'y', col = 'Red')
?plot
?abline

coeff <- summary(hubblefit)$coefficients[2]
coeff
bind <- cbind(0,coeff)
bind
abline(bind, ltw = 2, col = 'Blue')
print(hubblefit)

summary(hubblefit)
plot(hubblefit)
?predict

prediction <- predict(hubblefit, te_hubble)
hubble_hat <- predict(hubblefit, te_hubble)
head(prediction)

par(mfrow = c(2,1))

with(tr_hubble,
     {plot(x,y,pch = 21, bg = 'lightblue', cex = .7,
           main = 'Hubble Training set')
       abline(hubblefit, col = 'blue')
       }
     )
with(te_hubble,{
  plot(x,y,pch = 21, bg = 'green',cex = .7,
       main = 'Hubble test set')
  lines(x,hubble_hat, col = 'red')
})
my_rmse = function(truth,pred){
  out =sqrt(mean((truth-pred)^2))
  return(out)
}


my_rmse(tr_hubble$y,prediction)



age_of_the_universe = (1/coeff)/(3.09 * 1019)
age_of_the_universe
  
age_of_the_universe2 = 1/coeff
age_of_the_universe2
#scrivere a brutti quanti anni ha il suo universo..
?lm
hubble_fit_quad <- lm(y~poly(x, degree = 2, raw = TRUE)-1, data = tr_hubble)
hubble_fit_quad
coef(hubble_fit_quad)
quadratic=hubble_fit_quad$coefficients[1]*tr_hubble$x+hubble_fit_quad$coefficients[2]*(tr_hubble$x)^2
quadratic

with (tr_hubble,
      {
        plot(x,y, pch=21, bg="blue", cex=.7,
             main= "Quadratic Hubble")
        lines(x,quadratic,col="red")
      }
)
