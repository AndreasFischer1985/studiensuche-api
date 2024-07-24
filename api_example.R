#----------------
# Simple Example
#----------------

install.packages(c("devtools","rjson","httr"))
devtools::install_github("AndreasFischer1985/qqBaseX")
clientId="infosysbub-studisu"

url="https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?smo=1;2;3;4;5"
data_request=httr::GET(url=url, httr::add_headers(.headers=c("X-API-Key"=clientId)),
        config=httr::config(connecttimeout=60))
data_request
data=httr::content(data_request)
maxPage=round(data[["maxErgebnisse"]]/20)
completeData=lapply(1:maxPage,function(i){
        print(i);
	httr::content(httr::GET(url=paste0(url,"&pg=",i), httr::add_headers(.headers=c("X-API-Key"=clientId)),
        	config=httr::config(connecttimeout=60)))
})
