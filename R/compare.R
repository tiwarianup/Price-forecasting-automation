args =  commandArgs(TRUE)
date1 = "22022015"
#date2 = args[2]

library(XLConnect)
# DD & DNH to be added

incData = readWorksheetFromFile('C:/Users/sayanigupta/Downloads/open_access.xlsx', sheet=1)

dataFrame = data.frame(incData$state, as.Date(incData$report_date, format = "%Y-%m-%d"), incData$stoa)

colnames(dataFrame) = c("State", "Date","Stoa")

flCha = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_CHANDIGARH_", date1, ".csv", sep="")
flDel = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_DELHI_", date1, ".csv", sep="")
flHar = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_HARYANA_", date1, ".csv", sep="")
flHim = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_HP_", date1, ".csv", sep="")
flJam = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_JK_", date1, ".csv", sep="")
flPun = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_PUNJAB_", date1, ".csv", sep="")
flRaj = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_RAJASTHAN_", date1, ".csv", sep="")
flUp = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_UP_", date1, ".csv", sep="")
flUk = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_UTTARANCHAL_", date1, ".csv", sep="")
flGuj = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_GUVNL_", date1, ".csv", sep="")
flMp = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_MPSEB_", date1, ".csv", sep="")
flMah = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_MSEB_", date1, ".csv", sep="")
flCht = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_CSEB_", date1, ".csv", sep="")
flGoa = paste("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/STOA_GOA_", date1, ".csv", sep="")

#flCha , flDel , flHar , flHim , flJam , flPun , flRaj , flUp , flUk , flGuj , flMp , flMah , flCht , flGoa

dataCha = read.csv(flCha)
dataDel = read.csv(flDel)
dataHar = read.csv(flHar)
dataHim = read.csv(flHim)
dataJam = read.csv(flJam)
dataPun = read.csv(flPun)
dataRaj = read.csv(flRaj)
dataUp  = read.csv(flUp)
dataUk  = read.csv(flUk)
dataGuj = read.csv(flGuj)
dataMp  = read.csv(flMp)
dataMah = read.csv(flMah)
dataCht = read.csv(flCht)
dataGoa = read.csv(flGoa)

# Comparison of STOA for Chandigarh Data
compCha1 = dataCha$STOA
compCha2 = dataFrame[(dataFrame$State == "CHANDIGARH") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compCha3 = compCha2$Stoa
diffCha = abs(compCha1 - compCha3)

# Comparison of STOA for Delhi Data
compDel1 = dataDel$STOA
compDel2 = dataFrame[(dataFrame$State == "DELHI") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compDel3 = compDel2$Stoa
diffDel = abs(compDel1 - compDel3)

# Comparison of STOA for Haryana Data
compHar1 = dataHar$STOA
compHar2 = dataFrame[(dataFrame$State == "HARYANA") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compHar3 = compHar2$Stoa
diffHar = abs(compHar1 - compHar3)

# Comparison of STOA for Himachal Pradesh Data
compHim1 = dataHim$STOA
compHim2 = dataFrame[(dataFrame$State == "HP") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compHim3 = compHim2$Stoa
diffHim = abs(compHim1 - compHim3)

# Comparison of STOA for Jammu Kashmir Data
compJam1 = dataJam$STOA
compJam2 = dataFrame[(dataFrame$State == "JK") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compJam3 = compJam2$Stoa
diffJam = abs(compJam1 - compJam3)

# Comparison of STOA for Punjab Data
compPun1 = dataPun$STOA
compPun2 = dataFrame[(dataFrame$State == "PUNJAB") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compPun3 = compPun2$Stoa
diffPun = abs(compPun1 - compPun3)

# Comparison of STOA for Rajasthan Data
compRaj1 = dataRaj$STOA
compRaj2 = dataFrame[(dataFrame$State == "RAJASTHAN") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compRaj3 = compRaj2$Stoa
diffRaj = abs(compRaj1 - compRaj3)

# Comparison of STOA for Uttar Pradesh Data
compUp1 = dataUp$STOA
compUp2 = dataFrame[(dataFrame$State == "UTTAR PRADESH") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compUp3 = compUp2$Stoa
diffUp = abs(compUp1 - compUp3)

# Comparison of STOA for Uttarakhand Data
compUk1 = dataUk$STOA
compUk2 = dataFrame[(dataFrame$State == "UTTARAKHAND") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compUk3 = compUk2$Stoa
diffUk = abs(compUk1 - compUk3)

# Comparison of STOA for Gujarat Data
compGuj1 = dataGuj$STOA
compGuj2 = dataFrame[(dataFrame$State == "GUJARAT") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compGuj3 = compGuj2$Stoa
diffGuj = abs(compGuj1 - compGuj3)


# Comparison of STOA for Madhya Pradesh Data
compMp1 = dataMp$STOA
compMp2 = dataFrame[(dataFrame$State == "MADHYA PRADESH") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compMp3 = compMp2$Stoa
diffMp = abs(compMp1 - compMp3)

# Comparison of STOA for Maharashtra Data
compMah1 = dataMah$STOA
compMah2 = dataFrame[(dataFrame$State == "MAHARASHTRA") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compMah3 = compMah2$Stoa
diffMah = abs(compMah1 - compMah3)

# Comparison of STOA for Chattisgarh Data
compCht1 = dataCht$STOA
compCht2 = dataFrame[(dataFrame$State == "CHATTISGARH") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compCht3 = compCht2$Stoa
diffCht = abs(compCht1 - compCht3)

# Comparison of STOA for Goa Data
compGoa1 = dataGoa$STOA
compGoa2 = dataFrame[(dataFrame$State == "GOA") & (dataFrame$Date == as.Date(date1, format="%d%m%Y")), ]
compGoa3 = compGoa2$Stoa
diffGoa = abs(compGoa1 - compGoa3)

compDf = data.frame(diffCha, diffDel, diffHar, diffHim, diffJam, diffPun, diffRaj, diffUp, diffUk, diffGuj, diffMp, diffMah, diffCht, diffGoa)

colnames(compDf) = c("Chandigarh", "Delhi", "Haryana", "Himachal Pradesh", "Jammu-Kashmir", "Punjab", "Rajasthan", "Uttar Pradesh", "Uttarakhand", "Gujarat", "Madhya Pradesh", "Maharashtra", "Chattisgarh", "Goa")

setwd("D:/D Drive data/PSPCL/STEP/Exchange Price Projection/All States/SYSTEM/Bilateral/Comparison")
filename = paste("Comparison_", date1, ".csv", sep="")
write.csv(compDf, filename)
