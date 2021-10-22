setwd("~/Dropbox/Tattoos/Data_eng/Comprehension_eng/Comprehension_forcedchoice_eng/")
dat.eng.comp <- read.delim("data-eng-comp.txt","\t")
summary(dat.eng.comp)

dat.h1_4 <- dat.eng.comp[dat.eng.comp$cond=="target_h1_4",]
summary(dat.h1_4$choice)

dat.h1_5 <- dat.eng.comp[dat.eng.comp$cond=="target_h1_5",]
summary(dat.h1_5$choice)