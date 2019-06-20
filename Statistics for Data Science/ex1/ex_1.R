?read.table
?read.delim

?stringr
youraw <- read.delim('you.tsv',stringsAsFactors = FALSE)

str(youraw)
ncol(youraw) #num of columns
nrow(youraw) #num of rows


names(youraw) #name of cols
youraw[7,5] #position (7,5)
youraw[2,] # second row??

youclean <- youraw
names(youclean) <- c("where", "prev.life", "good.prob", "good.stat",
                     "good.R", "other.lan")
names(youclean)
str(youclean)
typeof(youclean$other.lan)
str(youclean$other.lan)
?str_split


library(stringr) #### PERICOLO
tolower(youclean$other.lan)
x <- str_split(youclean$other.lan,'[[:punct:]]')
z <- tolower(x)

<- lan1[lan1 == ' '] <- NA
head(youclean, n = 6)
z<- subset(youclean, (other.lan == 'no') | (other.lan == 'No') |(other.lan == 'nO'))

z
youclean$where
typeof(youclean$where)
youclean$where <- as.factor(youclean$where)
typeof(youclean$where)

?save()

save(youraw,youclean, file = 'you.Rdata')
