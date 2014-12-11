# KNN Errors
args <- commandArgs(trailingOnly = TRUE)
data <- read.csv(args[1])
cross = args[2]
print(cross)

plot_colors <- c("blue", "blue", "red", "red", "forestgreen", "forestgreen", "black", "black")

png(args[2], 1024, 720)
par(mar=c(4.5,4.5,2,1))
matplot(data[,1],data[,-1],type="l",col=plot_colors,lty=c(1,2),ylab='Percent Errors on Testing Set',xlab=ifelse(length(grep("1_instances",args[1]))>0,'Number of Training Examples, Uses Crossvalidation','Number of Training Examples'), lwd=c(2,1), cex.lab=2, cex.axis=2, cex.main=2, cex.sub=2, font.lab=1)

# add a legend 
legend("topright", c("Test Set","Train Set"), lty=c(1,2), cex=2, col=plot_colors, lwd=2, bty="n")
