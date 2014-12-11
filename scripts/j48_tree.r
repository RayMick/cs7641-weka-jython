# rmse vs
args <- commandArgs(trailingOnly = TRUE)
print(args)
data <- read.csv(args[1])
png(args[2], 1024, 720)
par(mar=c(4,4.5,2,1))
plot(data$cf, data$rmse, ylab='RMSE', xlab='Confidence Factor', type='l', lwd=2, cex.lab=2, cex.axis=2, cex.main=2, cex.sub=2, font.lab=1)
