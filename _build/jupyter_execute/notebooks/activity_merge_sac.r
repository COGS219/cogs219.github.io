library(tidyverse)

responses <- read.csv("https://psych750.github.io/data/iconicity_sample.csv")
demographics <- read.csv("https://psych750.github.io/data/iconicity_sample_demographics.csv")


responses %>% arrange(subj_code) %>% head

demographics %>% head


left_join(convert_gender,demographics) %>% head


library(psychTools)
convert_gender =read.clipboard.csv(sep="\t")

convert_gender

responses %>% group_by(word) %>% summarize(mean_resp=mean(key,na.rm=TRUE)) %>% head

responses %>% group_by(subj_code) %>% mutate(median_RT = median(rt)) %>% head(25)

responses %>% 
   group_by(subj_code) %>% 
   mutate(scaled_resp_by_subj = scale(key),num_ratings_by_subj=n()) %>% 
   group_by(word) %>% 
   mutate(scaled_resp_by_word = scale(key),num_ratings_for_word=n()) %>% 
   tail(20)



iris %>% head

iris %>%
  group_by(Species) %>% 
  summarise(across(1:4, mean))

iris %>%
  group_by(Species) %>% 
  summarise(across(where(is.numeric), mean)) # select all the numeric columns

iris %>%
  group_by(Species) %>% 
  summarise(across(contains("Length"), mean)) # select all the columns whose name contains Length

iris %>% select_if(is.numeric) %>% cor


library(broom)
iris %>% group_by(Species) %>% 
    do(tidy( 
      lm(Sepal.Length ~ Petal.Length, data = .)))

library(gapminder)
gapminder %>% head

gapminder %>% group_by (year) %>% 
    summarize(lifeExp=mean(lifeExp)) %>% 
    filter(year==min(year) | year==max(year))

gapminder %>% group_by(country) %>% 
    do(tidy( 
      lm(lifeExp ~ year, data = .))) %>% 
      filter(term=="year") %>% 
      select(country,estimate) %>%
      arrange(-estimate)

gapminder %>% group_by(country,year) %>% 
    summarize(lifeExp=mean(lifeExp)) %>% 
    filter(country=="Oman" | country=="Zimbabwe") %>% 
    filter(year==min(year) | year==max(year))
