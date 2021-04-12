require(knitr)
#library(devtools)

require(lmerTest)

# Danielle's standard packages
library(dplyr)
library(tidyverse)
library(ggplot2)
library(ggthemes)
library(stringr)
library(relaimpo)
library(gridExtra)
library(knitr)
library(lme4)
library(png)
library(jpeg)
library(ggpubr)

library(estimatr)
library(sandwich)
library(margins)

cbbPalette <- c("#0072B2","#56B4E9")


setwd("~/Dropbox/Research/Tattoos/Article")



################################################################################
###################### Comprehension ###########################################
################################################################################


####### Read in comprehension data & catch cheaters ##################

### English comprehension data ###
dat.comprehension_eng <- read.delim("../Data_eng/Comprehension_eng/Comprehension_forcedchoice_eng/data-eng-comp-nodups.txt",sep="\t")
dat.comprehension_eng$language <- "Eng"
dat.comprehension_eng$usernum <- paste(dat.comprehension_eng$usernum,"_eng_comp",sep="")

length(levels(as.factor(dat.comprehension_eng$usernum)))
#49

#View(dat.comprehension_eng)

### Spanish comprehension data ###
dat.comprehension_spa <- read.delim("../Data_spa/Comprehension_sp/Comprehension_forcedchoice_sp/data-spa-comp-nodups.txt",sep="\t")
dat.comprehension_spa$language <- "Spa"
dat.comprehension_spa$usernum <- paste(dat.comprehension_spa$usernum,"_spa_comp",sep="")

length(levels(as.factor(dat.comprehension_spa$usernum)))
#48


### Russian comprehension data ###
dat.comprehension_rus <- read.delim("../Data_ru/Comprehension_ru/output-ru/data-ru-comp-nodups.txt",sep="\t")
dat.comprehension_rus$language <- "Rus"
dat.comprehension_rus$usernum <- paste(dat.comprehension_rus$usernum,"_rus_comp",sep="")

length(levels(as.factor(dat.comprehension_rus$usernum)))
#52

#View(dat.comprehension_rus)

dat.comprehension_per <- read.delim("../Data_per/Comprehension_per/data-per-comp-nodups.txt",sep="\t")
dat.comprehension_per$language <- "Per"
dat.comprehension_per$usernum <- paste(dat.comprehension_per$usernum,"_per_comp",sep="")

length(levels(as.factor(dat.comprehension_per$usernum)))
#46

#View(dat.comprehension_per)

dat.comprehension_ar <- read.delim("../Data_ar/Comprehension_ar/data-ar-comp-nodups.txt",sep="\t")
dat.comprehension_ar$language <- "Ar"
dat.comprehension_ar$usernum <- paste(dat.comprehension_ar$usernum,"_ar_comp",sep="")

length(levels(as.factor(dat.comprehension_ar$usernum)))
#39

#View(dat.comprehension_ar)

### Join them all together ###
dat.comprehension <- dplyr::bind_rows(dat.comprehension_eng, dat.comprehension_spa, dat.comprehension_rus,dat.comprehension_per,dat.comprehension_ar)

#View(dat.comprehension)

dat.comprehension$language <- factor(dat.comprehension$language, levels = c("Ar","Per","Rus","Spa","Eng"))

#summary(dat.comprehension)

dat.comprehension$expected <-
    recode(dat.comprehension$expected,  
           arm = "arm_shoulder", back = "back", leg = "leg_knee", 
           either = "either",
           arm_shoulder = "arm_shoulder",
           leg_knee = "leg_knee",
           .default = "NA_character_")

dat.comprehension$expected <- as.character(dat.comprehension$expected)
dat.comprehension$choice <- as.character(dat.comprehension$choice)

#View(dat.comprehension)

dat.comprehension <-
  dat.comprehension %>%
  mutate(
    unexpectedchoice = as.numeric(!(expected==choice)&!(expected=="either"))
  )  %>%
  group_by(usernum) %>%
      mutate(total_unexpected = sum(unexpectedchoice),
             total_answers = n(),
             ) %>%
  ungroup() 

table(dat.comprehension$total_answers)

dat.comprehension[dat.comprehension$total_answers==13,]$usernum


summary(as.factor(dat.comprehension$total_unexpected))

dat.cheaters <- 
  dat.comprehension %>%
    filter(total_unexpected>0)

table(dat.cheaters$language,dat.cheaters$usernum)

### List of the chaters: ###
levels(as.factor(dat.cheaters$usernum))

### Remove the cheaters ###
dat.comprehension <- 
  dat.comprehension %>%
  filter(total_unexpected==0,total_answers==12)

## Not sure why this is necessary, if it is: ###
#dat.comprehension$expected <- as.factor(dat.comprehension$expected)
#dat.comprehension$choice <- as.factor(dat.comprehension$choice)

length(levels(as.factor(dat.comprehension$usernum[dat.comprehension$language=="Eng"])))
#44
length(levels(as.factor(dat.comprehension$usernum[dat.comprehension$language=="Spa"])))
#48


length(levels(as.factor(dat.comprehension$usernum[dat.comprehension$language=="Rus"])))
#49
length(levels(as.factor(dat.comprehension$usernum[dat.comprehension$language=="Per"])))
#38
length(levels(as.factor(dat.comprehension$usernum[dat.comprehension$language=="Ar"])))
#32


dat.comprehension$condname <- dat.comprehension$cond

dat.comprehension$condname <-
  recode(dat.comprehension$condname, 
         target_f1_4 = "Big toe vs. ring toe",
         target_f1_5 = "Big toe vs. pinky toe",
         target_f4_5 = "Ring toe vs. pinky toe",
         target_h1_4 = "Thumb vs. ring finger",
         target_h1_5 = "Thumb vs. pinky finger",
         target_h4_5 = "Ring finger vs. pinky finger",
         .default = "Filler"
  )

dat.comprehension <-
  dat.comprehension %>%
  filter(!(condname == "Filler")) %>%
  droplevels()

summary(dat.comprehension)

dat.comprehension <-
  dat.comprehension %>%
    mutate(
      condpluschoice = paste(cond,choice,sep="__")
  )

dat.comprehension$condpluschoice <- as.factor(dat.comprehension$condpluschoice)

dat.comprehension$outcome <- as.character(dat.comprehension$condpluschoice)

#View(dat.comprehension)

dat.comprehension$outcome <-  
    recode(dat.comprehension$outcome,
         target_f1_4__big_toe = "0",
         target_f1_4__ring_toe = "1",
         target_f1_5__big_toe = "0",
         target_f1_5__pinky_toe = "1",
         target_f4_5__pinky_toe = "1",
         target_f4_5__ring_toe = "0",
         target_h1_4__ring_finger = "1",
         target_h1_4__thumb = "0",
         target_h1_5__pinky = "1",
         target_h1_5__thumb = "0",
         target_h4_5__pinky = "1",
         target_h4_5__ring_finger = "0",
         .default = "NA_character_")

dat.comprehension$outcome <- as.numeric(dat.comprehension$outcome)




####### Plot comprehension data ##################

### Plot a single item (example) ###

gg_df.h1_4.eng <- 
  dat.comprehension %>%
  filter(condname=="Thumb vs. ring finger",language=="Eng") %>%
  group_by(condname,language) %>%
  do(tidy(lm_robust(outcome ~ 1, data = .)))

gg_df.h1_4.eng

ggplot(gg_df.h1_4.eng, aes(condname, estimate)) +
  geom_point() +
  coord_flip() +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0) +
  geom_hline(yintercept = 0.5, color = "#F8766D") +
  ylim(low=0,high=1) +
  ylab("Thumb vs. ring finger (n=45)") +
  xlab("") +
  theme(legend.position = "none",
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())
  #ggtitle("She has a tattoo on her finger",paste("n = ",nsubjects.eng," native English speakers (Prolific)",sep=""))

#ggsave("plots/__English-h1_4.png", width = 6, height = 1)

gg_df.f1_4.eng <- 
  dat.comprehension %>%
  filter(condname=="Big toe vs. ring toe",language=="Eng") %>%
  group_by(condname,language) %>%
  do(tidy(lm_robust(outcome ~ 1, data = .)))


ggplot(gg_df.f1_4.eng, aes(condname, estimate)) +
  geom_point() +
  coord_flip() +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0) +
  geom_hline(yintercept = 0.5, color = "red") +
  ylim(low=0,high=1) +
  ylab("Big toe vs. ring toe (n=45)") +
  xlab("") +
  theme(legend.position = "none",
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank())
  #ggtitle("She has a tattoo on her finger",paste("n = ",nsubjects.eng," native English speakers (Prolific)",sep=""))

#ggsave("plots/__English-f1_4.png", width = 6, height = 1)


### Plot all data ###

for (condition in dat.comprehension$condname) {
  gg_df <- 
    dat.comprehension %>%
    filter(condname==condition) %>%
    group_by(condname,language) %>%
    do(tidy(lm_robust(outcome ~ 1, data = .)))
  
  ggplot(gg_df, aes(language, estimate)) +
    geom_point() +
    coord_flip() +
    geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0) +
    geom_hline(yintercept = 0.5, color = "red") +
    ylim(low=0,high=1) +
    #ylab("Finger: Pinky finger (left) vs. thumb (right)") +
    ylab(condition) +
    xlab("") +
    theme(legend.position = "none")  
  
  ggsave(paste("plots/",condition,".png",sep=""),    # The directory to save the file in
         width = 6, # The width of the plot in inches
         height = 1.5)
}


  
dat.pvalues <- 
    dat.comprehension %>%
    group_by(condname,language) %>%
    summarize(prop = sum(outcome), total = n()) %>%
    rowwise %>%
    mutate(tst = list(broom::tidy(prop.test(prop, total)))) %>%
    tidyr::unnest(tst)

#dat.pvalues

dat.pvalues$adjusted <- p.adjust(dat.pvalues$p.value,method="fdr")

dat.pvalues$language <- factor(dat.pvalues$language, levels(as.factor(dat.comprehension$language)))

#View(dat.pvalues)

for (condition in dat.pvalues$condname) {
  dat.pvalues.sub <- dat.pvalues %>%
    filter(condname == condition)
  
  ggplot(dat.pvalues.sub, aes(language, estimate)) +
    geom_point() +
    coord_flip() +
    geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0) +
    geom_hline(yintercept = 0.5, color = "red") +
    ylim(low=0,high=1) +
    #ylab("Finger: Pinky finger (left) vs. thumb (right)") +
    ylab(condition) +
    xlab("") +
    theme(legend.position = "none")  
  
  ggsave(paste("plots/",condition,".png",sep=""),    # The directory to save the file in
         width = 6, # The width of the plot in inches
         height = 1.5)
}

#View(dat.pvalues)
library(xtable)

xtable(dat.pvalues[c("language","condname","estimate","p.value","adjusted")],booktabs = TRUE)




################################################################################
###################### Production ##############################################
################################################################################


####### Read in English, Spanish, & Russian Production Data and join DFs ##################
prod_eng <- read.csv("../Data_eng/Production_eng/Prod_eng_encrypted.csv")
#View(prod_eng)
names(prod_eng)
prod_eng$Language = "English"
prod_eng$Display_Utt <- prod_eng$Normal_Utt
prod_eng$Normal_Utt_latinized <- prod_eng$Normal_Utt

length(levels(as.factor((prod_eng$participant.id))))
#24


prod_eng$Condition <-
  recode(prod_eng$Condition,
         Target_H1 = "target_h1", Target_H4 = "target_h4", Target_H5 = "target_h5",
         Target_F1 = "target_f1", Target_F4 = "target_f4", Target_F_5 = "target_f5")


eng.counts <-
  prod_eng %>%
  filter(str_detect(Condition,"^target")) %>%
  mutate(Normal_Utt_latinized = Normal_Utt) %>%
  group_by(Condition) %>%
  summarize(length(unique(Normal_Utt_latinized)))
eng.counts

eng.counts$language = "English"

#demographic_prod_eng <- read.csv("../Data_eng/Production_eng/demographic_prod_eng.csv")
#demographic_prod_eng <- demographic_prod_eng %>%
#  rename(participant.id = participant_id)
#names(demographic_prod_eng)
#demog_joined_prod_eng <- left_join(prod_eng, demographic_prod_eng, by = c("participant.id"))

prod_spa <- read.csv("../Data_spa/Production_sp/Production_spa_encrypted.csv")
#View(prod_spa)
names(prod_spa)
prod_spa$Language = "Spanish"
prod_spa$Display_Utt <- prod_spa$Normal_Utt
prod_spa$Normal_Utt_latinized <- prod_spa$Normal_Utt

length(levels(as.factor((prod_spa$participant.id))))
#23

summary(prod_spa)

spa.counts <-
  prod_spa %>%
  group_by(Condition) %>%
  summarize(length(unique(Normal_Utt_latinized)))
spa.counts

spa.counts$language = "Spanish"


prod_rus <- read.delim("../Data_ru/Production_ru/production_ru_annotated_encrypted.tsv",sep="\t")
#View(prod_rus)
names(prod_rus)

prod_rus <-  rename(prod_rus, 
       participant.id = Prolific_ID ,
       Condition = cond)

prod_rus$Language = "Russian"
prod_rus$Display_Utt <- paste(prod_rus$Normal_Utt_latinized," (",prod_rus$Normal_Utt_gloss,")",sep="")

summary(prod_rus)

rus.counts <-
  prod_rus %>%
  group_by(Condition) %>%
  summarize(length(unique(Normal_Utt_latinized)))
rus.counts

rus.counts$language = "Russian"



length(levels(as.factor((prod_rus$participant.id))))
#32

prod_per <- read.delim("../Data_per/Production_per/production_per_annotated_encrypted.tsv",sep="\t")
#View(prod_per)
names(prod_per)
prod_per$Language = "Persian"
prod_per$Display_Utt <- paste(prod_per$Normal_Utt_latinized," (",prod_per$Normal_Utt_gloss,")",sep="")


per.counts <-
prod_per %>%
  group_by(Condition) %>%
  summarize(length(unique(Normal_Utt_latinized)))
per.counts

per.counts$language = "Persian"


length(levels(as.factor((prod_per$participant.id))))
#23

prod_ar <- read.delim("../Data_ar/Production_ar/production_ar_annotated_encrypted.tsv",sep="\t")
#View(prod_ar)
names(prod_ar)
prod_ar$Language = "Arabic"
prod_ar$Display_Utt <- paste(prod_ar$Normal_Utt_latinized," (",prod_ar$Normal_Utt_gloss,")",sep="")

length(levels(as.factor((prod_ar$participant.id))))
#25

table(prod_ar$Condition,prod_ar$Normal_Utt_latinized)

ar.counts <- 
prod_ar %>%
  group_by(Condition) %>%
  summarize(length(unique(Normal_Utt_latinized))) 

ar.counts

ar.counts$language = "Arabic"

prod.counts <- 
dplyr::bind_rows(eng.counts, spa.counts, rus.counts, per.counts, ar.counts)

names(prod.counts) <- c("Condition","Count","Language")
names(prod.counts)

prod.counts <- 
prod.counts %>%
  mutate(
    Digit = factor(
      Condition,
      levels = c(
        "target_h1",
        "target_h4",
        "target_h5",
        "target_f1",
        "target_f4",
        "target_f5"
      ),
      labels = c(
        "Thumb",
        "Ring Finger",
        "Pinky Finger",
        "Big Toe",
        "Ring Toe",
        "Pinky Toe"
      )
    ))


ggplot(data=prod.counts,aes(x=Language,y=Count,fill=Digit)) + 
  geom_bar(stat="identity",position=position_dodge() ) +
  ylab("Number of distinct expressions used for digit") +
  theme_bw() +
  theme(text = element_text(size = 14)) 





########## Combine production data and do same stuff to it all ####################

production_combined <- dplyr::bind_rows(prod_eng, prod_spa, prod_rus, prod_per, prod_ar)
#View(production_combined)



production_combined$Condition <-
    recode(production_combined$Condition,
           target_h1 = "Target_H1", target_h4 = "Target_H4", target_h5 = "Target_H5",
           target_f1 = "Target_F1", target_f4 = "Target_F4", target_f5 = "Target_F5",
           Target_H1 = "Target_H1", Target_H4 = "Target_H4", Target_H5 = "Target_H5",
           Target_F1 = "Target_F1", Target_F4 = "Target_F4", Target_F_5 = "Target_F5",
           Filler_Arm = "Filler_Arm", Filler_Shoulder = "Filler_Shoulder", Filler_Knee = "Filler_Knee",
           Filler_Calf = "Filler_Calf", Filler_Forearm = "Filler_Forearm", Filler_Back = "Filler_Back",
           .default = "NA_character_")

production_combined$IsTarget <- 
    recode(production_combined$Condition,
           "Target_H1" = TRUE, 
           "Target_H4" = TRUE,
           "Target_H5" = TRUE,
           "Target_F1" = TRUE, 
           "Target_F4" = TRUE,
           "Target_F5" = TRUE,
           .default = FALSE)

production_combined <- 
  production_combined %>% filter(IsTarget==TRUE) %>%
  droplevels()

production_combined <-
  production_combined %>%
  mutate(
    digit = factor(
      Condition,
      levels = c(
        "Target_H1",
        "Target_H4",
        "Target_H5",
        "Target_F1",
        "Target_F4",
        "Target_F5"
      ),
      labels = c(
        "Thumb",
        "Ring Finger",
        "Pinky Finger",
        "Big Toe",
        "Ring Toe",
        "Pinky Toe"
      )
    )
  ) %>%
  filter(!is.na(digit)) #holdover from pre-IsDigit days but no harm

#View(production_combined)

production.summary.spec <- 
  production_combined %>%
  group_by(Language,digit) %>%
  mutate(N_subjects = n()) %>%
  group_by(Language, digit, N_subjects, Display_Utt, Specificity) %>%
  summarize(my_count = n()) %>%
  mutate(my_prop = my_count / N_subjects * 100)

View(production.summary.spec)




# gg_eng_df_mydigit <- 
#   production_combined %>%
#   filter(Language=="English") %>%
#   filter(digit=="Ring Finger") %>%
#   droplevels()
# 
# g_eng_mydigit <- ggplot(gg_eng_df_mydigit, aes(y = my_prop, x = fct_reorder(Display_Utt, as.numeric(Specificity)), fill = as.factor(Specificity))) +
#   geom_col() +
#   # geom_text(data = summary_eng_df_mydigit,
#   #           aes(label = label),
#   #           hjust = "left",
#   #           nudge_y = 0.5) +
#   theme_bw() +
#   ylim(0,100) +
#   theme(
#     legend.position = "none",
#     strip.background = element_blank(),
#     strip.text = element_blank(),
#     panel.grid.minor.x = element_blank(),
#     axis.text.y = element_text(size = 20),
#     axis.title=element_text(size=22),
#     axis.title.x=element_blank(),
#     axis.text.x=element_blank(),
#     axis.ticks.x=element_blank(),
#     axis.title.y = element_blank(),
#     plot.title = element_text(size = 20)
#   ) +
#   coord_flip()+ 
#   labs(title = "English", size = 35)  +
#   scale_fill_manual(values=cbbPalette)
# 
# g_eng_mydigit 


plot_digit <- function(dig,language) {
  gg_df_mydigit <- 
    production.summary.spec %>%
    filter(digit==dig) %>%
    droplevels() %>%
    filter(Language==language) %>%
    droplevels()
  
  gg_df_mydigit$Specificity <- factor(gg_df_mydigit$Specificity,levels=c(1,0))
  
  g_mydigit <- ggplot(gg_df_mydigit, aes(y = my_prop, x = fct_reorder(Display_Utt, as.numeric(Specificity)), fill = as.factor(Specificity))) +
    geom_col() +
    # geom_text(data = summary_eng_df_mydigit,
    #           aes(label = label),
    #           hjust = "left",
    #           nudge_y = 0.5) +
    theme_bw() +
    ylim(0,100) +
    theme(
      legend.position = "none",
      strip.background = element_blank(),
      strip.text = element_blank(),
      panel.grid.minor.x = element_blank(),
      axis.text.y = element_text(size = 16),
      axis.title=element_text(size=18),
      axis.title.x=element_blank(),
      axis.text.x=element_blank(),
      axis.ticks.x=element_blank(),
      axis.title.y = element_blank(),
      plot.title = element_text(size = 16)
    ) +
    coord_flip()+ 
    #labs(title = "", size = 35)  +
    scale_fill_manual(values=cbbPalette)
  
    g_mydigit 
}


plot_digit("Pinky Toe","English")

plot_digit("Pinky Toe","Persian")

plot_digit("Big Toe","Russian")



numutts_for_digit <- function(dig,lg) {
  gg_df_mydigit <- 
    production.summary.spec %>%
    filter(digit==dig) %>%
    droplevels() %>%
    filter(Language==lg) %>%
    droplevels()
  
  return(length(levels(as.factor(gg_df_mydigit$Display_Utt))))
}


plot_language <- function (lg) {
    
    h1_plot <- plot_digit("Thumb",lg)
    h4_plot <- plot_digit("Ring Finger",lg)
    h5_plot <- plot_digit("Pinky Finger",lg)
    
    f1_plot <- plot_digit("Big Toe",lg)
    f4_plot <- plot_digit("Ring Toe",lg)
    f5_plot <- plot_digit("Pinky Toe",lg)
    
    numutts_h1 <- numutts_for_digit("Thumb",lg)
    numutts_h4 <- numutts_for_digit("Ring Finger",lg)
    numutts_h5 <- numutts_for_digit("Pinky Finger",lg)
    
    numutts_f1 <- numutts_for_digit("Big Toe",lg)
    numutts_f4 <- numutts_for_digit("Ring Toe",lg)
    numutts_f5 <- numutts_for_digit("Pinky Toe",lg)
    
    total_numutts = numutts_h1 + numutts_h4 + numutts_h5 +
      numutts_f1 + numutts_f4 + numutts_f5
    
    vscale_factor <- 1.5
    vmargin <- 1
    
    plot_height <- vmargin + vscale_factor*total_numutts
    
    height_vec <- c(numutts_h1,numutts_h4, numutts_h5,numutts_f1,numutts_f4,numutts_f5) + 1
    print(height_vec)
    
    ggarrange(h1_plot,h4_plot,h5_plot,
              f1_plot,f4_plot,f5_plot,
              #heights = numutts*3,
              heights = height_vec,
              #heights = c(2,3,4,3,7,6),
              ncol = 1, nrow = 6, align = "v")
 }


plot_language("English")

#ggsave("plots/production/English_production.png",height=(2+3+4+3+7+6)/3,width=10)
 
plot_language("Spanish")
  
#ggsave("plots/production/Spanish_production.png",height=(9+8+7+7+7+13)/3,width=10)
 
plot_language("Russian")

#ggsave("plots/production/Russian_production.png",height=(5+5+4+4+6+9)/3,width=15)
 
plot_language("Persian")
 
#ggsave("plots/production/Persian_production.png",height=(8+7+7+5+6+4)/3,width=15)
 
plot_language("Arabic")
 
#ggsave("plots/production/Arabic_production.png",height=(8+10+13+14+9+12)/3,width=15)
 
 
########## Summarize by utterance/image pair ####################

#View(production_combined)


production.summary <- 
  production_combined %>%
  group_by(Language,digit,Normal_Utt_latinized) %>%
  tally()

production.summary$digit<- tolower(str_replace_all(production.summary$digit," ","_"))


production.summary$Normal_Utt_latinized <- tolower(str_replace_all(production.summary$Normal_Utt_latinized," ","_"))

production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized," ","_")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ñ","n")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ā","a")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ū","u")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ĭ","i")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ṣ","s")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ẓ","z")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"ī","i")
production.summary$Normal_Utt_latinized <- str_replace_all(production.summary$Normal_Utt_latinized,"'","h")


#View(production.summary)

write.csv(production.summary,"../modelling/production_summary.csv")

#production.summary.eng <- production.summary %>% filter(Language == "English")
#View(production.summary.eng)
#write.csv(production.summary.eng,"../modelling/production_summary_English.csv")

#production.summary.spa <- production.summary %>% filter(Language == "Spanish")
#View(production.summary.spa)

#production.summary.rus <- production.summary %>% filter(Language == "Russian")
#View(production.summary.rus)

#production.summary.per <- production.summary %>% filter(Language == "Persian")
#View(production.summary.per)

#production.summary.ar <- production.summary %>% filter(Language == "Arabic")
#View(production.summary.ar)





######################## Modelling ############################



#to install rwebppl
#install.packages("devtools")
#devtools::install_github("mhtess/rwebppl")
require("rwebppl")

execute_model <- function(alpha,beta,epsilon,speakertype,role,input,body_region,lg) {
  model_data <- list(alpha,beta,epsilon,speakertype,role,input,body_region,lg)
  model <- webppl(program_file="../Modelling/model.wppl", 
                  data = model_data, 
                  data_var = "model_data",
                  packages = "webppl-csv lodash")
  return(model)
}

# sample values to use for testing
test_alpha <- 1 #how much accuracy matters (higher => more)
test_beta <- 2.5      #how much cost matters (higher => more)
test_epsilon <- 0.025   #fake count for unattested utterances so they're not impossible ("smoothing")
test_speakertype <- "plain"  #use production probabilities
#speakertype options: "empirical", "plain" ("frequency" not implemented)
#default uses flat priors and cost only



#test runs for the speaker
test_result <- execute_model(test_alpha,test_beta,test_epsilon,"plain",
                             "speaker","ring_toe","foot","English")
test_result

test_result <- execute_model(test_alpha,test_beta,test_epsilon,"plain",
                             "speaker","big_toe","foot","English")
test_result


#test runs for the listener
test_result2 <- execute_model(2,test_beta,0.0001,"empirical",
                             "listener","finger","h1_4","English")
test_result2

test_result3 <- execute_model(test_alpha,test_beta,test_epsilon,test_speakertype,
                              "listener","palets_nogi","f4_5","Russian")
test_result3
length(test_result3$support)

test_result4 <- execute_model(2,test_beta,test_epsilon,"plain",
                              "listener","toe","f1_4","English")
test_result4

execute_model(2,test_beta,test_epsilon,"plain",
              "speaker","ring_toe","foot","English")


execute_model(2,1,test_epsilon,"plain",
              "speaker","ring_toe","foot","English")


betas_to_try 

#helper function for collecting data
#in case probability is 1 for one option

choose_other <- function(winner,cond) {
  if (cond=="h1_4") {
      if (winner=="thumb")  { return("ring_finger") }
      if (winner=="ring_finger") { return("thumb") }
  }
  if (cond=="h1_5") {
    if (winner=="thumb")  { return("pinky_finger") }
    if (winner=="pinky_finger") { return("thumb") }
  }
  if (cond=="h4_5") {
    if (winner=="ring_finger")  { return("pinky_finger") }
    if (winner=="pinky_finger") { return("ring_finger") }
  }
  if (cond=="f1_4") {
    if (winner=="big_toe")  { return("ring_toe") }
    if (winner=="ring_toe") { return("big_toe") }
  }
  if (cond=="f1_5") {
    if (winner=="big_toe")  { return("pinky_toe") }
    if (winner=="pinky_toe") { return("big_toe") }
  }
  if (cond=="f4_5") {
    if (winner=="ring_toe")  { return("pinky_toe") }
    if (winner=="pinky_toe") { return("ring_toe") }
  }
  return(NULL)
}
#choose_other("thumb","h1_4")


# Now run through all of the calls we want to make

# First set up the values we want to look at


alpha_values <- c(0.5,1,1.5,2) #values of alpha to try
beta_values <- c(0,0.5,1,1.5,2,2.5,3,3.5,4)    #values of beta to try
epsilon_values <- c(0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4)  #values of epsilon to try, relevant for empirical speaker
speakertype_options <- c("plain","empirical")
#we can't run "frequency" speakertype until we have frequencies for the new utterances
roles <- c("listener") #speaker, listener
languages <- c("English","Spanish","Persian","Arabic","Russian")
#Russian is busted because the frequency=>probability of "palets nogi" is 0 for both big toe and pinky toe
body_regions <- c("hand","foot")
hand_digits <- c("thumb","ring_finger","pinky_finger") 
foot_digits <- c("big_toe","ring_toe","pinky_toe") 
hand_conditions <- c("h1_4","h1_5","h4_5")
foot_conditions <- c("f1_4","f1_5","f4_5")

utterances <- data.frame(language = c("English","Spanish","Arabic","Persian","Russian"),
                         finger = c("finger","dedo","isbah","angusht","palets"),
                         toe = c("toe","dedo_del_pie","isbah_qadm","angushte_pa","palets_nogi"))

results <- data.frame() #initialize before running for loop
for (lg in languages) {
  for (role in roles) {
    for (alpha in alpha_values) {
      for (speakertype in speakertype_options) {
        epsilons_to_try = epsilon_values
        if (!(speakertype=="empirical")) {
          epsilons_to_try = c("NA")
        }
        for (epsilon in epsilons_to_try) {
          
          betas_to_try <- beta_values
          if (speakertype=="empirical") {
            betas_to_try <- c("NA")
          }
          for (beta in betas_to_try) {
            
            for (body_region in body_regions) {   
              result <- NULL
              if (role=="speaker") {
                if (body_region=="hand") {
                  for (digit in hand_digits) {
                    result <- execute_model(alpha,beta,epsilon,speakertype,
                                            role,digit,body_region,lg)    
                    result$alpha <- alpha
                    result$beta <- beta
                    result$epsilon <- epsilon
                    result$speakertype <- speakertype
                    result$role <- role
                    result$input <- digit
                    result$cond <-body_region
                    result$language <- lg
                    
                    results <- rbind(results, result)
                  }
                }
                else { #body_region is foot
                  for (digit in foot_digits) {
                    result <- execute_model(alpha,beta,epsilon,speakertype,
                                            role,digit,body_region,lg)    
                    result$alpha <- alpha
                    result$beta <- beta
                    result$epsilon <- epsilon
                    result$speakertype <- speakertype
                    result$role <- role
                    result$input <- digit
                    result$cond <-body_region
                    result$language <- lg
                    
                    results <- rbind(results, result)
                  }
                }
                
              } #end speaker
              
              else { #role is listener we assume
                if (body_region=="hand") {
                  utterance <- utterances[utterances$language==lg,]$finger[1]
                  for (condition in hand_conditions) {
                    result <- execute_model(alpha,beta,epsilon,speakertype,
                                            role,utterance,condition,lg)
                    
                    #if the probability assigned to one option is 1
                    #then we have to add a 0 probability for the other option
                    if (length(result$support)==1) {
                      winner <- result$support
                      loser <- choose_other(winner,condition)
                      result <- rbind(result,c(loser,0))
                    }
                    #note the above will generally be unnecessary if we are using smoothed counts
                    #i.e. epsilon > 0
                    
                    result$alpha <- alpha
                    result$beta <- beta
                    result$epsilon <- epsilon
                    result$speakertype <- speakertype
                    result$role <- role             
                    result$input <- utterance
                    result$cond <- condition
                    result$language <- lg
                    
                    results <- rbind(results, result)
                  }
                }
                else { #body_region is foot we assume
                  utterance <- utterances[utterances$language==lg,]$toe[1]
                  for (condition in foot_conditions) {
                    result <- execute_model(alpha,beta,epsilon,speakertype,
                                            role,utterance,condition,lg)
                    
                    #if the probability assigned to one option is 1
                    #then we have to add a 0 probability for the other option
                    if (length(result$support)==1) {
                      winner <- result$support
                      loser <- choose_other(winner,condition)
                      result <- rbind(result,c(loser,0))
                    }
                    
                    result$alpha <- alpha
                    result$beta <- beta
                    result$epsilon <- epsilon
                    result$speakertype <- speakertype
                    result$role <- role             
                    result$input <- utterance
                    result$cond <- condition
                    result$language <- lg
                    
                    results <- rbind(results, result)
                  }
                }
              } #end listener
            }
          } 
        }
      }
    }
  }
}

View(results)
#write.csv(results,"full-modelling-results.csv")




results.plain <- filter(results,speakertype=="plain")
View(results.plain)

results.empirical <- filter(results,speakertype=="empirical")
View(results.empirical)

results.all <- rbind(results.plain,results.empirical)
#results <- results.all

comprehension_summary <- 
  dat.comprehension %>%
  group_by(condname,language) %>%
  do(tidy(lm_robust(outcome ~ 1, data = .)))


model.listener <- results.all %>%
  filter(role=="listener") %>%
  droplevels() %>%
  mutate(
    rightone = as.numeric((cond=="h1_4"&support=="ring_finger")|
                            (cond=="h1_5"&support=="pinky_finger")|
                            (cond=="h4_5"&support=="pinky_finger")|
                            (cond=="f1_4"&support=="ring_toe")|
                            (cond=="f1_5"&support=="pinky_toe")|
                            (cond=="f4_5"&support=="pinky_toe")
    )
  )  %>%
  filter(rightone==1) #just use the probability of the one on the right
model.listener$condname <- model.listener$cond
model.listener$condname <-
  recode(model.listener$condname, 
         f1_4 = "Big toe vs. ring toe",
         f1_5 = "Big toe vs. pinky toe",
         f4_5 = "Ring toe vs. pinky toe",
         h1_4 = "Thumb vs. ring finger",
         h1_5 = "Thumb vs. pinky finger",
         h4_5 = "Ring finger vs. pinky finger",
         .default = ""
  )
model.listener$language <- recode(model.listener$language, 
                                  "English"="Eng","Spanish"="Spa","Persian"="Per","Arabic"="Ar","Russian"="Rus")


merged <- merge(comprehension_summary,model.listener,by=c("condname","language"))
#levels(as.factor(merged$condname))
merged$condname <- factor(merged$condname,levels=c("Thumb vs. ring finger","Thumb vs. pinky finger","Ring finger vs. pinky finger",
                                                   "Big toe vs. ring toe","Big toe vs. pinky toe","Ring toe vs. pinky toe"
))


View(merged)

#testing
#myalpha = 1
#mybeta = 2
#myspeakertype = "plain"
#myepsilon = "NA"
#mymerged <- merged %>% filter(epsilon==myepsilon,alpha==myalpha,
#        beta==mybeta,
#        speakertype==myspeakertype
#        )
#summary(mymerged)
#summary(merged)
#eval <- summary(lm_robust(estimate ~ as.numeric(prob), data = mymerged))
#eval$adj.r.squared
#names(eval)

alpha_values_tried <- levels(as.factor(results.all$alpha))
alpha_values_tried

beta_values_tried <- levels(as.factor(results.all$beta))
#remove NS
beta_values_tried
beta_values_tried <- beta_values_tried[-length(beta_values_tried)] 
beta_values_tried

epsilon_values_tried <- levels(as.factor(results.all$epsilon))
epsilon_values_tried
epsilon_values_tried <- epsilon_values_tried[-length(epsilon_values_tried)] 
epsilon_values_tried

speakertype_options_tried <- levels(as.factor(results.all$speakertype))
speakertype_options_tried

evals <- data.frame() #initialize before running for loop
for (myalpha in alpha_values_tried) {
  for (myspeakertype in speakertype_options) {
    epsilons_to_try <- epsilon_values_tried
    if (!(myspeakertype=="empirical")) {
      epsilons_to_try <- c("NA")
    }
    print(myspeakertype)
    print(epsilons_to_try)
    for (myepsilon in epsilons_to_try) {
      
      betas_to_try <- beta_values
      if (myspeakertype=="empirical") {
        betas_to_try <- c("NA")
      }
      for (mybeta in betas_to_try) {

        mymerged <- filter(merged, alpha==myalpha,
                           beta==mybeta,
                           speakertype==myspeakertype,
                           epsilon==myepsilon)
        #print(summary(mymerged))
         
        if (length(mymerged$condname)>0) {
          
          eval <- summary(lm_robust(estimate ~ as.numeric(prob), data = mymerged))
          
          myeval <- data.frame(myspeakertype)
          myeval$alpha <- myalpha
          myeval$beta <- mybeta
          myeval$epsilon <- myepsilon
          
          myeval$adj.r.squared <- eval$adj.r.squared
          myeval$r.squared <- eval$r.squared
          
          evals <- rbind(evals, myeval)
          
        }         
      }
    }
  }
}


View(evals)

evals.plain <- filter(evals, myspeakertype=="plain")
View(evals.plain)
evals.plain$alpha <- as.factor(evals.plain$alpha)
evals.plain$beta <- as.numeric(evals.plain$beta)

#Negative R^2 values correspond to residual errors larger than the total sum of squares and can easily happen in no-intercept regressions

max(evals.plain$adj.r.squared)

evals.plain.optimal <- filter(evals.plain,adj.r.squared >= max(evals.plain$adj.r.squared)
)
summary(evals.plain.optimal)


evals.plain.optimal


textx <- as.numeric(evals.plain.optimal$beta[1])
texty <- as.numeric(evals.plain.optimal$adj.r.squared[1]) + 0.08
ggplot(data=evals.plain,aes(x=beta,y=adj.r.squared)) +
  geom_point(aes(color=alpha)) +
  geom_line(aes(color=alpha)) +
  geom_point(data=evals.plain.optimal,aes(x=beta,y=adj.r.squared),shape=1,size=2,color="black") +
  ylim(c(-0.1,1)) +
  ylab("Adjusted R^2") +
  #scale_colour_manual(values = grey.colors(4,rev=TRUE)) +
  theme_bw() +
  theme(text = element_text(size = 16)) +
  theme(legend.position = "none") +
  annotate("text",x=textx,y=texty,label="optimal (R^2 = 0.22):\nalpha = 1, beta = 2.5",size=5)



evals.empirical <- filter(evals, myspeakertype=="empirical")
#evals.empirical <- evals.toshow
evals.empirical$alpha <- as.factor(evals.empirical$alpha)
evals.empirical$epsilon <- as.numeric(evals.empirical$epsilon)

max(evals.empirical$adj.r.squared)

evals.emp.optimal <- filter(evals.empirical,adj.r.squared >= max(evals.empirical$adj.r.squared))
evals.emp.optimal

alphasubset <- levels(evals.plain$alpha)

alphasubset


evals.empirical.alphasubset <- filter(evals.empirical, alpha %in% alphasubset)

textx <- as.numeric(evals.emp.optimal$epsilon[1])
texty <- as.numeric(evals.emp.optimal$adj.r.squared[1]) + 0.08
ggplot(data=evals.empirical.alphasubset,aes(x=epsilon,y=adj.r.squared)) +
  geom_point(aes(color=alpha)) + #first alpha=transparency; second=rationality param
  geom_line(aes(color=alpha)) +
  geom_point(data=evals.emp.optimal,aes(x=epsilon,y=adj.r.squared),shape=1,size=3,color="black") +
  ylim(0,1) +
  #ylab("Adjusted R^2") +
  ylab("") +
  theme_bw() +
  theme(text = element_text(size = 16))  +
  annotate("text",x=textx,y=texty,label="optimal (R^2 = 0.64):\nalpha=1, epsilon=0.25",size=5)

#heatmap version (looks ok for this model but not the other one)
#ggplot(data=evals.empirical,aes(epsilon,alpha,fill=adj.r.squared)) + 
#  geom_tile() +
#  geom_point(data=evals.emp.optimal,aes(x=epsilon,y=alpha),shape=8,color="yellow") +
#  labs(fill = "Adjusted R^2")


#alpha=1 is more or less optimal for empirical
#and optimal for plain
#and it's simple and common so might as well use it for both

#epsilon=0.1 is close to optimal for empirical
#beta=2.5 is optimal for plain

chosenmodel.empirical <- filter(merged,
                                speakertype=="empirical",
                                alpha==1,
                                epsilon==0.1)


chosenmodel.plain <-  filter(merged,
                             speakertype=="plain",
                             alpha==1,
                             beta==2.5)

#these are the two models we will plot
chosen.merged <- rbind(chosenmodel.empirical,chosenmodel.plain)

#plot model results vs. empirical estimates by condition

chosen.merged %>%
  ggplot(aes(x=language, y = as.numeric(prob),color=speakertype,shape=speakertype,alpha=speakertype)) +
  geom_hline(yintercept=0.5,color="red") +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high), width = 0,color="grey") + 
  geom_point(aes(x=language, y=estimate),color="black",shape=16) +
  geom_point() +
  scale_shape_manual(values=c(17, 15)) +
  scale_alpha_manual(values=c(1,1)) +
  scale_color_manual(values=c("blue","cyan3")) +
  #scale_x_discrete(limits=c("Spa","Eng")) +
  ylim(0,1) +  
  ylab("Probability of B (in A vs. B)") +
  xlab("") +
  theme_bw() +
  coord_flip() +
  facet_wrap(~condname,ncol=3) 


# get R squared values for both models

summary(lm_robust(estimate ~ as.numeric(prob), data = chosenmodel.empirical))
# Multiple R-squared:  0.6508 ,	Adjusted R-squared:  0.6384  

summary(lm_robust(estimate ~ as.numeric(prob), data = chosenmodel.plain))

#Multiple R-squared:  0.2479 ,	Adjusted R-squared:  0.2211 

summary(chosen.merged)


# Renaming model names for graphs.
chosen.merged$speakertype <- recode(chosen.merged$speakertype,
                             empirical = "production",
                             plain = "complexity")


chosen.merged %>%
  mutate(condition = condname) %>%
  ggplot(aes(x=as.numeric(prob), y = estimate)) +
  geom_abline(intercept=0, slope=1, linetype="dotted",color="grey") +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high,color=language), width = 0) + 
  geom_point(aes(color=language,shape=condition)) +
  theme_bw() +
  xlim(0,1) +
  ylim(0,1) +
  geom_smooth(method='lm',size=0.5,se=FALSE) +
  facet_wrap(~language*speakertype) +
  #facet_wrap(~speakertype) +
  ylab("observed frequency of B (in 'A vs. B')") +
  xlab("model probability of B (in 'A vs. B')") +
  theme(text = element_text(size = 14)) 



chosen.merged %>%
  mutate(condition = condname) %>%
  ggplot(aes(x=as.numeric(prob), y = estimate)) +
  geom_abline(intercept=0, slope=1, color="grey", linetype="dotted") +
  geom_errorbar(aes(ymin = conf.low, ymax = conf.high,color=language), width = 0) + 
  geom_point(aes(color=language,shape=condition)) +
  theme_bw() +
  xlim(0,1) +
  ylim(0,1) +
  geom_smooth(method='lm',size=0.5,se=FALSE) +
  facet_wrap(~speakertype) +
  ylab("observed frequency of B (in 'A vs. B')") +
  xlab("model probability of B (in 'A vs. B')") +
  theme(text = element_text(size = 14)) 


chosen.merged.bylg <- 
  chosen.merged %>%
  group_by(language,speakertype) %>%
  summarize(rsquared = summary(lm_robust(estimate ~ as.numeric(prob)))$adj.r.squared)

chosen.merged.bylg

xtable(chosen.merged.bylg)

