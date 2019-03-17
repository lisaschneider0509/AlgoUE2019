library(ggplot2)
library(gridExtra)

hanoi_data <- read.csv("Hanoi.csv", header = TRUE, sep = ",")


hanoi <- ggplot(data = hanoi_data, 
                    aes(x = hanoi_data$Disks, 
                        y = hanoi_data$Runntime))
hanoi <- hanoi + 
  geom_line() + 
  theme_light() + 
  labs(title = "Towers of Hanoi", 
       x = "disk number",
       y = "runntime (s)") +
  theme(plot.title = element_text(hjust = 0.5, face = "bold"), 
        plot.subtitle = element_text(hjust = 0.5, size = 13),
        axis.title.x = element_text(size = 13), axis.title.y = element_text(size = 13), 
        legend.position = "bottom") 
hanoi
