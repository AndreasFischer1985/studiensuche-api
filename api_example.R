#----------------
# Simple Example
#----------------

install.packages(c("devtools","rjson","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="5aee2cfe-1709-48a9-951d-eb48f8f73a74"
clientSecret="3309a57a-9214-40db-9abe-28b1bb30c08c"
postData=list( "grant_type"="client_credentials","client_id"=clientId,"client_secret"=clientSecret) 
token_request=httr::POST(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        body=postData,encode="form",
        config=httr::config(connecttimeout=60))
token=httr::content(token_request, as='parsed')$access_token
url="https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?smo=1;2;3;4;5"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))
data_request
data=httr::content(data_request)
maxPage=round(data[["maxErgebnisse"]]/20)
completeData=lapply(1:maxPage,function(i){
        print(i);
	httr::content(httr::GET(url=paste0(url,"&pg=",i), httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        	config=httr::config(connecttimeout=60)))
})

data$facetten[[5]] # Angebote je Region
data$facetten[[2]] # Angebot je Studienform


#---------------------------------
# Plotte angebote nach smo und sfo
#---------------------------------

sfo=0:6
urls=paste0("https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?smo=1;2;3;4;5&sfo=",sfo)
datalist=lapply(urls,function(url)
	httr::content(httr::GET(url=url, httr::add_headers(.headers=c("OAuthAccessToken"=token)),
        config=httr::config(connecttimeout=60))))
ty=sapply(1:length(datalist),function(i)sapply(datalist[[i]]$facetten[[7]]$auswahl,function(x)x$trefferAnzahl))
rownames(ty)=sapply(datalist[[1]]$facetten[[7]]$auswahl,function(x)x$label)
rownames(ty)=paste0(gsub("&shy;","-\n",rownames(ty)),"\n(n=",rowSums(ty),")");
colnames(ty)=c(
"auf Anfrage","Vollzeitstudium","Teilzeitstudium","Wochenendveranstaltung","Fernstudium","Selbststudium","Blockstudium")
x=t(ty[-1,])
x=x[order(rowSums(x),decreasing=T),order(colSums(x))]

dev.new();par(bg = 'white')
qqBaseX::flowerplot(x,circle=.01,reverseLegend=T)
title(main="Duale Studienangebote nach Studienform",adj=0,line=2,font.main=2)
title(main="\ngemäß Kursnet Studiensuche",adj=0,line=1,font.main=1)
title(sub=paste0("Stand: ",format(Sys.Date(),"%d.%m.%Y")),adj=1,cex.sub=0.7,line=1)
title(sub="Mach dir selbst ein Bild! Unter https://github.com/bundesAPI/studiensuche-api",adj=1,cex.sub=0.7,line=2)
qqBaseX::saveDevs()
