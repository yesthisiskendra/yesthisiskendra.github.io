
setwd('/Users/kendraosburn/browserJournal')
df <- read.csv('bh_0819_sm_date.csv')
library(dplyr)

#UNIQUE LANDINGS BY YEAR
landings_by_year <- df %>% 
  group_by(year) %>%
  count()

#UNIQUE WEBSITES BY YEAR
unique_by_year <- df %>% 
  group_by(year) %>%
  summarise(Unique_Elements = n_distinct(site))


#UNIQUE LANDINGS BY MONTH & YEAR
landings_by_month <- df %>% 
  group_by(month, year) %>%
  count()

#UNIQUE WEBSITES BY MONTH & YEAR
unique_by_month <- df %>% 
  group_by(month, year) %>%
  summarise(Unique_Elements = n_distinct(site))

#UNIQUE WEBSITES BY MONTH & YEAR
unique_by_day <- df %>% 
  group_by(month, year, day) %>%
  summarise(n = n_distinct(site)) %>%
  arrange(desc(n))

