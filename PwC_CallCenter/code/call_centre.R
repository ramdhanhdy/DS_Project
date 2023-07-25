library(lubridate)
library(ggplot2)
library(dplyr)
library(ggstatsplot)
library(plotly)
library(htmlwidgets)
library(gridExtra)


# Set a global theme for all plots
theme_set(theme_light() + theme(panel.grid.major = element_blank(), panel.grid.minor = element_blank()))

call_data <- read.csv('Call-Center-Dataset.csv') %>%
  rename('Answered' = 'Answered..Y.N.',
         'Speed_of_answer_in_seconds' = 'Speed.of.answer.in.seconds',
         'Satisfaction_rating'='Satisfaction.rating') %>%
  mutate(Date = as.Date(Date),
         Year = year(Date),
         Month = month(Date),
         Weekday = wday(Date, label=TRUE),
         Weekday = factor(Weekday, 
                          levels = c("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"),
                          ordered = TRUE),
         Hour = hour(hms(Time)), 
         Time_Category = cut(Hour, breaks=c(-Inf, 6, 12, 18, Inf), 
                             labels=c("Midnight", "Morning", "Afternoon", "Evening")))

call_data_year <- call_data %>%
  group_by(Year, Month) %>%
  summarise(call_volume = n(),
            answered_calls = sum(Answered=='Y'),
            unanswered_calls = sum(Answered=='N'),
            answer_rate = answered_calls/call_volume,
            resolved_calls = sum(Resolved=='Y'),
            unresolved_calls = sum(Resolved=='N'),
            resolve_rate = resolved_calls/call_volume,
            Satisfaction_rating = mean(Satisfaction_rating),
            AvgTalkDuration_seconds = median(AvgTalkDuration_seconds))

call_data_agent <-  call_data %>%
  na.omit() %>%
  filter(AvgTalkDuration_seconds!=0) %>%
  group_by(Agent) %>%
  summarise(AvgSatisfaction = median(Satisfaction_rating),
            AvgTalkDuration_seconds = mean(AvgTalkDuration_seconds),
            AvgAnsSpeed = mean(Speed_of_answer_in_seconds),
            ResolutionRate = mean(Resolved == 'Y'),
            CallVolume = n())

call_data_agent_week <- call_data %>%
  na.omit() %>%
  filter(AvgTalkDuration_seconds!=0) %>%
  group_by(Weekday, Agent) %>%
  summarise(AvgSatisfaction = median(Satisfaction_rating),
            AvgTalkDuration_seconds = mean(AvgTalkDuration_seconds),
            AvgAnsSpeed = mean(Speed_of_answer_in_seconds),
            ResolutionRate = round(mean(Resolved == 'Y'), 2),
            CallVolume = n())



# Summary
total_calls <- nrow(call_data)
answered_calls <- nrow(filter(call_data, Answered == 'Y'))
unanswered_calls <- nrow(filter(call_data, Answered == 'N'))
resolved_calls <- nrow(filter(call_data, Answered == 'Y'))
unresolved_calls <- nrow(filter(call_data, Answered == 'N'))

## Agent Performance
# Duration by Agent
boxplot_agents <- ggplot(call_data, aes(x = AvgTalkDuration_seconds, y = Agent, fill = Agent)) +
  geom_boxplot() +
  scale_fill_hue(direction = 1) +
  labs(title = "Call Duration by Agent",
       x = "Average Duration (seconds)",
       y = "Agent",
       fill = "Agent")

# Agent-wise Calls
p_call_qty <- ggplot(call_data, aes(x=Agent)) +
  geom_bar(fill="steelblue") +
  labs(title = "Call Volume by Agent",
       x = "Agent",
       y = "Number of Calls")

# Agent Resolution Rate
p_resolution_rate <- call_data_agent %>%
  ggplot(aes(x=Agent, y=ResolutionRate)) +
  geom_bar(stat="identity", fill="steelblue") +
  labs(title = "Resolution Rate by Agent",
       x = "Agent",
       y = "Resolution Rate")

# Plot resolution rate by agent throughout the week
p_resolution_rate2 <-  call_data_agent_week %>%
                          ggplot(aes(x = Weekday, y = ResolutionRate, group = Agent, color = Agent)) +
                          geom_line(size = 1) +
                          labs(title = "Resolution Rate by Agent Throughout the Week",
                               x = "Day of the Week",
                               y = "Resolution Rate") +
                          theme(legend.position = "bottom") +
                          facet_wrap(~Agent)

# Average Speed of Answer
p_ans_speed<- call_data_agent %>%
  ggplot(aes(x=Agent, y=AvgAnsSpeed)) +
  geom_bar(stat="identity", fill="steelblue") +
  labs(title = "Average Speed of Answer by Agent",
       x = "Agent",
       y = "Average Speed of Answer (seconds)")

## Call Details Section

# Call Volume Over Time
p_call_otime <- call_data %>%
  count(Hour) %>%
  ggplot(aes(x=Hour, y=n)) +
  geom_line(color="steelblue") +
  labs(title = "Call Volume Throughout the Day",
       x = "Hour of Day",
       y = "Number of Calls")

# Call Volume Over Days of the Week
p_call_odow <- call_data %>%
  mutate(Weekday = wday(Date, label = TRUE)) %>% # Extract day of week
  count(Weekday) %>%
  ggplot(aes(x=Weekday, y=n)) +
  geom_bar(stat="identity", color="steelblue", fill="steelblue", alpha=0.5) +
  geom_line(aes(group=1), color="red", size=1) + # add line plot
  labs(title = "Call Volume Throughout the Week",
       x = "Day of Week",
       y = "Number of Calls")

# Topic Distribution
p_topic_pie <- ggplot(call_data, aes(x="", fill=Topic)) +
  geom_bar(width = 1) +
  coord_polar("y", start=0) +
  theme_void() +
  labs(fill="Topic", 
       title="Distribution of Call Topics")


# Get overall median
rate_topic_median <- median(call_data$Satisfaction_rating, na.rm = TRUE)
call_data_topic <- call_data %>%
  group_by(Topic) %>%
  summarise(MedianSatisfaction = median(Satisfaction_rating, na.rm = TRUE)) %>%
  mutate(Topic = reorder(Topic, MedianSatisfaction))  # reorder factors based on the median
topic_for_label <- call_data_topic$Topic[which.max(call_data_topic$MedianSatisfaction)]

# Plot Satisfaction Rate by Topic
ggplot(call_data_topic, aes(x = Topic, y = MedianSatisfaction, fill=MedianSatisfaction)) +
  geom_bar(stat = "identity") + # add color
  scale_fill_gradient(low = "navyblue", high = "royalblue2") +
  geom_hline(yintercept = rate_topic_median, linetype="dashed", 
             color = "red", size=1) + # add horizontal line
  annotate("text", x = topic_for_label, y = rate_topic_median, label = "Global Median", 
           vjust = 12, hjust = -0.1, color = "darkred") +
  coord_flip() + # make the chart horizontal
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(title = "Median Satisfaction Rate by Topic",
       x = "Topic",
       y = "Median Satisfaction Rating")


# Call Duration Distribution
p_duration_dist <- call_data %>%
  select(AvgTalkDuration_seconds) %>%
  na.omit() %>%
  filter(AvgTalkDuration_seconds!=0) %>%
  ggplot(aes(x=as.numeric(AvgTalkDuration_seconds))) +
  geom_histogram(fill="steelblue") +
  labs(title = "Call Duration Distribution",
       x="Call Duration (seconds)",
       y="Frequency")

## Customer Satisfaction

# Overall Satisfaction Rating
mean(call_data$Satisfaction_rating, na.rm = TRUE)

# Satisfaction Rating Over Time
p_rating_time <- call_data %>%
                  select(Satisfaction_rating, Time) %>%
                  mutate(Hour = lubridate::hour(hms(Time))) %>%
                  na.omit() %>%
                  group_by(Hour) %>%
                  summarise(AvgSatisfaction = mean(Satisfaction_rating, na.rm = TRUE)) %>%
                  ggplot(aes(x=Hour, y=AvgSatisfaction)) +
                    geom_col(fill="steelblue", alpha=0.5) +
                    geom_line(color="red", size=1) +
                    scale_x_continuous(breaks = unique(call_data$Hour)) +
                    labs(title = "Satisfaction Rating by Hours",
                         x="Hour of Day",
                         y="Average Satisfaction Rating")


global_median <- median(call_data$Satisfaction_rating, na.rm = TRUE)

agent_for_label <- call_data_agent$Agent[which.max(call_data_agent$AvgSatisfaction)]

p_rating_agent <- ggplot(call_data_agent, aes(x=Agent, y=AvgSatisfaction)) +
        geom_col(aes(fill = AvgSatisfaction)) +
        scale_fill_gradient(low = "steelblue", high = "lightblue") +
        coord_flip() +
        geom_hline(aes(yintercept = global_median),
                   color = "darkred", 
                   linetype = "dashed", 
                   size = 1) +
        annotate("text", x = agent_for_label, y = global_median, label = "Global Median", 
                 vjust = 12, hjust = -0.1, color = "darkred") +
        labs(title = "Satisfaction by Agent",
             x="Agent",
             y="Average Satisfaction Rating")




# Select the necessary columns
data_for_plot <- call_data_agent[, c("Agent", "AvgSatisfaction", "AvgTalkDuration_seconds", "AvgAnsSpeed", "ResolutionRate", "CallVolume")]

# Convert Agent to factor
data_for_plot$Agent <- as.factor(data_for_plot$Agent)

# Create the parallel coordinate plot
ggparcoord(data = data_for_plot, columns = 2:6, groupColumn = 1, scale = "globalminmax") +
  theme_minimal() +
  labs(title = "Parallel Coordinate Plot for Call Center Metrics",
       x = "Metrics",
       y = "Scaled Values") +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

# Create Agent Groups
call_data$AgentGroup <- case_when(
  call_data$Agent %in% c("Stewart", "Martha", "Becky", "Jim") ~ "HighPerformers",
  call_data$Agent %in% c("Greg", "Diane", "Dan") ~ "LowPerformers",
  TRUE ~ "Other"
)

p_rating_hour2 <- call_data %>%
                    select(Satisfaction_rating, Hour, AgentGroup) %>%
                    na.omit() %>%
                    group_by(Hour, AgentGroup) %>%
                    summarise(AvgSatisfaction = mean(Satisfaction_rating, na.rm = TRUE)) %>%
                    ggplot(aes(x=Hour, y=AvgSatisfaction, color=AgentGroup)) +
                      geom_line(size=1) +
                      scale_x_continuous(breaks = unique(call_data$Hour)) +
                      labs(title = "Satisfaction Rating by Hour and Agent Group",
                           x="Hour of Day",
                           y="Average Satisfaction Rating") +
                      theme(legend.position="bottom")


p_norm_rate <- call_data %>%
                  select(Satisfaction_rating, Hour, AgentGroup) %>%
                  na.omit() %>%
                  group_by(Hour, AgentGroup) %>%
                  summarise(NormalizedSatisfaction = sum(Satisfaction_rating) / n()) %>%
                  ggplot(aes(x=Hour, y=NormalizedSatisfaction, color=AgentGroup)) +
                  geom_line(size=1) +
                  scale_x_continuous(breaks = unique(call_data$Hour)) +
                  labs(title = "Normalized Satisfaction Rating by Hour and Agent Group",
                       x="Hour of Day",
                       y="Normalized Satisfaction Rating") +
                  theme(legend.position="bottom")
                   

call_data %>%
  na.omit() %>%
  mutate(Weekday = wday(Date, label = TRUE)) %>%
  group_by(Weekday, AgentGroup) %>%
  summarise(NormalizedSatisfaction = mean(Satisfaction_rating, na.rm = TRUE)) %>%
  ggplot(aes(x=Weekday, y=NormalizedSatisfaction, color=AgentGroup)) +
  geom_line(size=1, aes(group = AgentGroup)) +
  labs(title = "Agent Performance Over the Week",
       x="Day of the Week",
       y="Normalized Satisfaction Rating") +
  theme(legend.position="bottom")


# Plot for Average Satisfaction
plot_satisfaction <- ggplot(agent_data, aes(x=CallVolume, y=AvgSatisfaction)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "cadetblue3", linetype='dotted') +
  labs(title = "Call Volume vs Average Satisfaction",
       x = "Call Volume",
       y = "Average Satisfaction")

# Plot for Average Talk Duration
plot_duration <- ggplot(agent_data, aes(x = CallVolume, y = AvgTalkDuration)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "darkolivegreen", linetype='dotted') +
  labs(title = "Call Volume vs Average Talk Duration",
       x = "Call Volume",
       y = "Average Talk Duration")

# Plot for Average Answer Speed
plot_speed <- ggplot(agent_data, aes(x = CallVolume, y = AvgAnsSpeed)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "darkorange", linetype='dotted') +
  labs(title = "Call Volume vs Average Answer Speed",
       x = "Call Volume",
       y = "Average Answer Speed")

# Plot for Resolution Rate
plot_resolution <- ggplot(agent_data, aes(x = CallVolume, y = ResolutionRate)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "darkred", linetype='dotted') +
  labs(title = "Call Volume vs Resolution Rate",
       x = "Call Volume",
       y = "Resolution Rate")

# Combine plots
grid.arrange(plot_satisfaction, plot_duration, plot_speed, plot_resolution, ncol = 2)



ggplotly(p_resolution_rate2) %>%
  saveWidget(file='p_resolution_rate2.html')


ply1 <- ggplotly(plot_satisfaction)
ply2 <- ggplotly(plot_duration)
ply3 <- ggplotly(plot_speed)
ply4 <- ggplotly(plot_resolution)


subplot(ply1, ply2, ply3, ply4, nrows=2) %>%
  saveWidget(file='p_corr_comparisons.html')


# Test correlation between AvgTalkDuration_seconds and AvgSatisfaction
correlation_satisfaction <- cor.test(call_data$AvgTalkDuration_seconds, call_data$AvgSatisfaction)

# Test correlation between AvgTalkDuration_seconds and AvgAnsSpeed
correlation_speed <- cor.test(call_data$AvgTalkDuration_seconds, call_data$AvgAnsSpeed)

# Test correlation between AvgTalkDuration_seconds and ResolutionRate
# correlation_resolution <- cor.test(call_data$AvgTalkDuration_seconds, call_data$ResolutionRate)

# Print results
print(correlation_satisfaction)
print(correlation_speed)
print(correlation_resolution)


# Plot for Average Satisfaction
plot_satisfaction <- ggplot(call_data_agent, aes(x=AvgTalkDuration_seconds, y=AvgSatisfaction)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "cadetblue3", linetype='dotted') +
  labs(title = "Talk Duration vs Average Satisfaction",
       x = "Average Talk Duration (seconds)",
       y = "Average Satisfaction")

# Plot for Average Answer Speed
plot_speed <- ggplot(call_data_agent, aes(x = AvgTalkDuration_seconds, y = AvgAnsSpeed)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "darkorange", linetype='dotted') +
  labs(title = "Talk Duration vs Average Answer Speed",
       x = "Average Talk Duration (seconds)",
       y = "Average Answer Speed")

# Plot for Resolution Rate
plot_resolution <- ggplot(call_data_agent, aes(x = AvgTalkDuration_seconds, y = ResolutionRate)) +
  geom_text(aes(label = Agent), check_overlap = TRUE, size = 2.5) +
  geom_smooth(method = lm, se = FALSE, color = "darkred", linetype='dotted') +
  labs(title = "Talk Duration vs Resolution Rate",
       x = "Average Talk Duration (seconds)",
       y = "Resolution Rate")

# Combine plots
grid.arrange(plot_satisfaction, plot_speed, plot_resolution, ncol = 2)

# Fit a robust linear model
robust_model <- rlm(ResolutionRate ~ AvgTalkDuration_seconds, data = call_data_agent)

# Print the model summary
summary(robust_model)

# # Save ggplotly as widget in file test.html
# saveWidget(ggplotly(p_rating_agent), file = "test.html");
# # Save ggplotly as widget in file test.html
# saveWidget(ggplotly(p_rating_time), file = "p_rating_time.html");
# saveWidget(ggplotly(p_rating_time), file = "p_rating_time.html")
