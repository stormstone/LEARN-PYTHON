rm(list=ls())
setwd('F:/data')
data <- read.csv('gjc_zd_(有实际站点).csv',header = T, stringsAsFactors = F)
zd1 <- table(data$实际站点)
head(zd1)
zd <- as.data.frame(zd1)
colnames(zd) <- c('上车站点','上车人数')
zd$线路名称 <- '68路线'
data1 <- cbind(zd$线路名称,zd$上车站点,zd$上车人数)

file <- list.files()
shuju <- list.files(file[which(file == 'gjc')])
dir <- paste('./',file[which(file == 'gjc')],'/',shuju,sep = '')
d <- length(dir)

nun <- function(data){
  gjc <- data.frame('线路名称'=0,'上车站点'=0,'上车人数'=0)
  a <- unique(data$实际站点)
  for(i in 1 :length(a)){
    data1 <- data[which(data$实际站点== a[i]),]
    gjc[i,1] <- '68路线'
    gjc[i,2] <- a[i]
    gjc[i,3] <- length(data1[,1])
  }
  return(gjc)
}
lujing <- c('./aa/a.csv','./aa/b.csv','./aa/c.csv',
            './aa/d.csv','./aa/e.csv')
for(j in 1:d){
  da <- read.csv(dir[j],stringsAsFactors = F)
  ad <- nun(da)
  write.csv(ad,lujing[j],row.names = F)
}
rm(list = ls())
setwd('F:/data')
data <- read.csv('gjc_qz.csv',header = T,stringsAsFactors = F)
head(data)
pro <- read.csv('poisson_pro.csv',header = T,stringsAsFactors = F)
head(pro)
pro <- pro[,-1]
pro$sum <- 0
OD <- data.frame()

for(i in 1:nrow(data)){
  for(j in 1:nrow(data)){
    if(i < j){
      pro$sum[i] <- sum(pro[i,]*data[,4])
      p <- (pro[i,j]*data[j,4])/pro$sum[i]
      OD[i,j] <- round(p*data[i,3])
    }
    else{
      OD[i,j] <- 0
    }
  }
}
m=length(OD)
for(i in 1:m){
  OD[m+1,i] <- sum(OD[c(1:m),i])
}
# 第二次循环是矩阵已经变化，所以要限定“c(1:m)”
n=nrow(OD)
for(j in 1:n){
  OD[j,n] <- sum(OD[j,c(1:n-1)])
}

data <- data.frame(c1=c(1,2,2,3),c2=c(2,5,4,6))
attach(data)
c1
detach(data)
c1
find.package()

require(utils)

summary(women$height)   # refers to variable 'height' in the data frame
attach(women)
summary(height)         # The same variable now available by name
height <- height*2.54 
find("height")
summary(height)         # The new variable in the workspace
rm(height)
summary(height) 
height <<- height*25.4  # Change the copy in the attached environment
find("height")
summary(height)         # The changed copy
detach("women")
summary(women$height)   # unchanged
gc()
install.packages('rpart')
library(rpart)
head(kyphosis)
a <- kyphosis
detach(kyphosis)
attach(kyphosis)
fit <- rpart(Kyphosis~Age+Number+Start)
#加复杂系数限制模型
fit2 <- rpart(Kyphosis~Age+Number+Start,control = rpart.control(cp = 0.05))
par(mfrow = c(1,1),xpd = NA)
plot(fit,main = '不加复杂系数限制')
text(fit)
plot(fit2,main = '加复杂系数限制')
text(fit2,use.n = TRUE)
library(party)  #加载party包
ctree.model <- ctree(Kyphosis~Age+Number+Start,kyphosis)
plot(ctree.model,type='simple')

data<-read.csv("./gps/gps_20140609.csv",header = T)
which(duplicated(data))
aa<-c[which(duplicated(data)),]

e<- as.data.frame.array()
cadd <- function(x) Reduce("+", x, accumulate = TRUE)
cadd(seq_len(7))

a<- list(c(1,2),c(2,3))
b<-as(a,'matrix')
c<-as.data.frame(b)
class(a)
b <- as.data.frame(a,col.names=(c('xx','yy')))
f <- as.array(a)
class(f)
d<-as.list(f)
g<-unlist(f)
b[1]
b[[1]][1]
c <- as.list(b)
class(c)
c <-unlist(c)
d <- as.data.frame(a)
as.character(b)
require(arules)
detach(b)
library(splines)
pkg <- "package:splines"

detach(pkg, character.only = TRUE)
detach(package:splines)
