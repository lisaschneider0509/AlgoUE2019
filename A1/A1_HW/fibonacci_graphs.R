library(ggplot2)
library(gridExtra)

fib_data <- read.csv("fibonacci.csv", header = TRUE, sep = ",")


fibonacci <- ggplot(data = fib_data, 
                    aes(x = data$size, 
                        y = data$time, 
                        group = data$function., 
                        color = data$function.))
fibonacci <- fibonacci + 
  geom_line() + 
  theme_light() + 
  labs(title = "Efficient vs. inefficient fibonacci", 
       x = "fibonacci size",
       y = "time (s)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"), 
        plot.subtitle = element_text(hjust = 0.5, size = 13),
        axis.title.x = element_text(size = 13), axis.title.y = element_text(size = 13), 
        legend.position = "bottom") + 
  scale_color_manual(values = c("black", "red"), name = "Fibonacci function")
  

fibonacci
