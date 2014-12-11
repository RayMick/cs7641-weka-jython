# KNN Errors
args <- commandArgs(trailingOnly = TRUE)
data <- read.csv(args[1])
cross = args[2]
print(cross)

plot_colors <- c("black")

png(args[2], 1024, 720)
par(mar=c(4.5,4.5,2,1))
matplot(data[,1],data[,2],type="l",col=plot_colors,lty=1,ylab='Time to Train Model (seconds)',xlab=ifelse(length(grep("1_instances",args[1]))>0,'Number of Training Examples, Uses Crossvalidation','Number of Training Examples'), lwd=2, cex.lab=2, cex.axis=2, cex.main=2, cex.sub=2, font.lab=1)
