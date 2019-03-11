library(ggplot2)
library(gridExtra)

fib_data <- read.csv("fibonacci.csv", header = TRUE, sep = ",")


plot(data$size, data$time, type = "l")
lines(data$size, data$efficient, type = "l", col = "red")
legend("topright", 
       legend = c(data$inefficient, data$efficient), 
       title = "Efficient vs. inefficient Fibonacci", 
       xlab = "fibonacci position", 
       ylab = "Time (s)")

fibonacci <- ggplot(data = fib_data, 
                    aes(x = data$size, 
                        y = data$time, 
                        group = data$function., 
                        color = data$function.))
fibonacci <- fibonacci + 
  geom_line() + 
  theme_light() + 
  
  

fibonacci
