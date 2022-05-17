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
url="https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?smo=5"
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


#------------------------------------------------------------------
# Get clientID & clientSecret from https://web.arbeitsagentur.de/studiensuche/suche
#------------------------------------------------------------------
# GET /studiensuche/suche HTTP/1.1
# Host: web.arbeitsagentur.de
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Accept-Language: de,en-US;q=0.7,en;q=0.3
# Accept-Encoding: gzip, deflate, br
# DNT: 1
# Connection: keep-alive
# Upgrade-Insecure-Requests: 1
# Pragma: no-cache
# Cache-Control: no-cache
#------------------------------------------------------------------

getCredentials=function(
    url="https://web.arbeitsagentur.de/studiensuche/suche",
    verbose=T
    ){ 
    if(verbose) print("\nTrying to get credentials...\n")
    get_request=httr::GET(
        url=url,
        config=httr::config(connecttimeout=60)
        )
    x=as.character(httr::content(get_request)) 
    clientId=print(gsub("(.* '|',)","",qqBaseX::matchAll(x,"clientId: (.*?),")))
    clientSecret=print(gsub("(.* '|',)","",qqBaseX::matchAll(x,"clientSecret: (.*?),")))
    if(verbose){
        print(paste("URL: ", url))
        print(paste("Credentials unchanged?", clientId=="5aee2cfe-1709-48a9-951d-eb48f8f73a74" & clientSecret=="3309a57a-9214-40db-9abe-28b1bb30c08c"))
    }
    return(list(
        clientId=gsub("(.* '|',)","",qqBaseX::matchAll(x,"clientId: (.*?),")),
        clientSecret=gsub("(.* '|',)","",qqBaseX::matchAll(x,"clientSecret: (.*?),")),
        clientCookies=get_request$cookies$value,
        data=get_request
    ))
}


#------------------------------------------------------------------
# Get token from https://rest.arbeitsagentur.de/oauth/gettoken_cc
#------------------------------------------------------------------
# POST /oauth/gettoken_cc HTTP/1.1
# Host: rest.arbeitsagentur.de
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0
# Accept: application/json, text/plain, */*
# Accept-Language: de,en-US;q=0.7,en;q=0.3
# Accept-Encoding: gzip, deflate, br
# Content-Type: application/x-www-form-urlencoded
# Content-Length: 127
# Origin: https://web.arbeitsagentur.de
# DNT: 1
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
#------------------------------------------------------------------

getToken=function(
    url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
    clientId="1c852184-1944-4a9e-a093-5cc078981294",
    clientSecret="777f9915-9f0d-4982-9c33-07b5810a3e79",
    clientCookies=NULL,
    verbose=T
    ){
    if(verbose) print("\nTrying to get token...\n")
    postHeaders=c(
        "Host"="rest.arbeitsagentur.de",
        "User-Agent"="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept"="application/json, text/plain, */*",
        "Accept-Language"="de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding"="gzip, deflate, br",
        "Content-Type"="application/x-www-form-urlencoded",
        "Content-Length"="127",
        "Origin"="https://web.arbeitsagentur.de",
        "DNT"="1",   
        "Connection"="keep-alive",
        "Pragma"="no-cache",
        "Cache-Control"="no-cache"
    )
    if(!is.null(clientCookies)) postHeaders=c(postHeaders,"Cookie"=clientCookies)
    postData=list( 
        "grant_type"="client_credentials",
        "client_id"=clientId,
        "client_secret"=clientSecret
    ) 
    token_request=httr::POST(
        url=url,
        body=postData,encode="form",
        httr::add_headers(.headers = c(postHeaders)),
        config=httr::config(connecttimeout=60) #config=httr::timeout(60)
    )
    token_body <- httr::content(token_request, as='parsed')
    if(verbose){
        print(paste("URL:", url))
        print(paste("Token:", token_body$access_token))
        print(paste("x-Correlation-Id:", token_request$headers$"x-correlationid"))
        print(paste("Cookies:", token_request$cookies$value))
    }
    return(list(
        access_token=token_body$access_token,
        correlationId=token_request$headers$"x-correlationid",
        clientCookies=token_request$cookies$value,
        data=token_request))
}


#------------------------------------------------------------------
# Get Data from https://web.arbeitsagentur.de/studiensuche/suche?sw=IT-Security-Manager
#------------------------------------------------------------------
# GET /infosysbub/studisu/pc/v1/studienangebote?uk=Bundesweit&sty=0&sw=IT-Security-# Manager&pg=1&at=kompakt&cb=://web.arbeitsagentur.de/studiensuche/main-es2015.134b23e0c29386cff693 # HTTP/1.1
# Host: rest.arbeitsagentur.de
# User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0
# Accept: application/json, text/plain, */*
# Accept-Language: de,en-US;q=0.7,en;q=0.3
# Accept-Encoding: gzip, deflate, br
# OAuthAccessToken: eyJhbGciOiJIUzUxMiJ9...
# Origin: https://web.arbeitsagentur.de
# DNT: 1
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
#------------------------------------------------------------------


getData=function(url="https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?sw=IT-Security-Manager",      
        accessToken="eyJhbGciOiJIUzUxMiJ9.eyAic3ViIjogIlI0amhFWGdOWW1yL21Cd1lFTi9oR0N...",
        correlationId=NULL,
        clientCookies=NULL,
        verbose=T){
    if(verbose) print("\nTrying to get data...\n")
    getHeaders=c(
        "Host"="rest.arbeitsagentur.de",
        "User-Agent"="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0",
        "Accept"="application/json, text/plain, */*",
        "Accept-Language"="de,en-US;q=0.7,en;q=0.3",
        "Accept-Encoding"="gzip, deflate, br",        
        "Origin"="https://web.arbeitsagentur.de",
        "DNT"="1",
        "Connection"="keep-alive",
        "Pragma"="no-cache",
        "Cache-Control"="no-cache"
    )
    if(!is.null(accessToken)) getHeaders=c(getHeaders,"OAuthAccessToken"=accessToken)
    if(!is.null(correlationId)) getHeaders=c(getHeaders,"Correlation-ID"=correlationId)
    if(!is.null(clientCookies)) getHeaders=c(getHeaders,"Cookie"=clientCookies)
    data_request=httr::GET(
        url=url, 
        httr::add_headers(.headers=getHeaders),
        config=httr::config(connecttimeout=60)
    )
    if(verbose){
        print(paste("URL:", url))
        print(nchar(httr::content(data_request)))
        print(substr(httr::content(data_request),1,100))

    }
    return(
        data_request
    )
}


#------------------------------------------------------------------
# Demo: get one page
#------------------------------------------------------------------

dataList=list()
if(T){ #get page 0
    url=paste0("https://web.arbeitsagentur.de/studiensuche/suche")
    credentials=getCredentials(url)
    token=getToken(
        url="https://rest.arbeitsagentur.de/oauth/gettoken_cc",
        clientId=credentials[[1]],
        clientSecret=credentials[[2]])
    data=getData(
        url=paste0("https://rest.arbeitsagentur.de/infosysbub/studisu/pc/v1/studienangebote?sw=IT-Security-Manager"),        
        accessToken=token[[1]])
    dataList[["page 0"]]=data
    writeLines(decodedData,paste0(Sys.Date(),"_stData_",0,".txt"))
    save.image(paste0(Sys.Date(),"_st_successfulRequest.RData"))
}


