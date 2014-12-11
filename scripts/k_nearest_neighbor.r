# KNN Errors
args <- commandArgs(trailingOnly = TRUE)
rmse <- read.csv(args[1])

plot_colors <- c(rgb(r=0.0,g=0.0,b=0.9), "red", "forestgreen","black","purple")

png(args[2], 1024, 720)
par(mar=c(4,4.5,2,1))
matplot(rmse[,1],rmse[,-1],type="l",col=plot_colors,lty=1,ylab='RMSE',xlab='K', lwd=2, cex.lab=2, cex.axis=2, cex.main=2, cex.sub=2, font.lab=1)

# add a legend 
legend("topright", c("Linear Euclidian","Linear Manhattan","KDTree Euclidian","Ball Euclidian","Cover Euclidian"), cex=2, col=plot_colors, lty=1, lwd=2, bty="n")
