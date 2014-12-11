args <- commandArgs(trailingOnly = TRUE)
data <- read.csv(args[1])

plot_colors <- c("blue", "blue", "red", "red", "forestgreen", "forestgreen", "black", "black")

png(args[2], 1024, 720)
par(mar=c(5.5,4.5,2,1))
matplot(data[,1],data[,-1],type="l",col=plot_colors,lty=c(1,2),ylab='Percent Errors on Testing Set',xlab=ifelse(length(grep("1_instances",args[1]))>0,'Number of Training Examples, Uses Crossvalidation','Number of Training Examples'), lwd=c(2,1), cex.lab=2, cex.axis=2, cex.main=2, cex.sub=2)

# add a legend
legend("topright", c("Linear Test ","Linear Training", "Polynomial Test", "Polynomial Training", "Radial Test", "Radial Training", "Sigmoid Test", "Sigmoid Training"), lty=c(1,2), cex=2.0, col=plot_colors, lwd=2, bty="n")

