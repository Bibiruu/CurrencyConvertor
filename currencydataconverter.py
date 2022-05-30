
currency_data_list=[]

def load_data():
    filename=input("Give name of the data file: ")
    datafile=open(filename,"r")
    count=0
    for line in datafile:
        if count==0:
            count=count+1 
            continue
        if count==1:
            semicolon_position1=line.find(";")
            first=line[0:semicolon_position1]
        
        lst=line.split(";")
        if lst[1]!= "":
            lastval=lst[3]
            lst[3]=lastval[0:len(lastval)-1]
            currency_data_list.append(lst)
        count=count+1
    semicolon_position2=line.find(";")
    last=line[0:semicolon_position2]    
    
    print("Data loaded successfully!")
    print("Currency exchange data is from", count-1, "days between", first ,"and "+last+".")
    print()
    return currency_data_list
def average_currency_rate(currency_data_list):
    total_eur=0
    total_aud=0
    total_gbp=0
    for lst in currency_data_list:
        total_eur=total_eur+float(lst[1])
        total_aud=total_aud+float(lst[2])
        total_gbp=total_gbp+float(lst[3])
    eur_exchange_rate=total_eur/len(currency_data_list)
    aud_exchange_rate=total_aud/len(currency_data_list)
    gbp_exchange_rate=total_gbp/len(currency_data_list)
    result_list=[]
    result_list.append(eur_exchange_rate)
    result_list.append(aud_exchange_rate)
    result_list.append(gbp_exchange_rate)
    return result_list

def highest_currency_rate(currency_data_list):
    max_eur=0
    max_aud=0
    max_gbp=0
    for lst in currency_data_list:
        if float(lst[1])>max_eur:
            max_eur=float(lst[1])
        if float(lst[2])>max_aud:
            max_aud=float(lst[2])
        if float(lst[3])>max_gbp:
            max_gbp=float(lst[3])    
    eur_exchange_rate=max_eur
    aud_exchange_rate=max_aud
    gbp_exchange_rate=max_gbp
    result_list=[]
    result_list.append(eur_exchange_rate)
    result_list.append(aud_exchange_rate)
    result_list.append(gbp_exchange_rate)
    print("Using the highest currency exchange rate.")
    print()
    return result_list

def lowest_currency_rate(currency_data_list):
    min_eur=99999
    min_aud=99999
    min_gbp=99999
    for lst in currency_data_list:
        if float(lst[1])<min_eur:
            min_eur=float(lst[1])
        if float(lst[2])<min_aud:
            min_aud=float(lst[2])
        if float(lst[3])<min_gbp:
            min_gbp=float(lst[3])    
    eur_exchange_rate=min_eur
    aud_exchange_rate=min_aud
    gbp_exchange_rate=min_gbp
    result_list=[]
    result_list.append(eur_exchange_rate)
    result_list.append(aud_exchange_rate)
    result_list.append(gbp_exchange_rate)
    print("Using the lowest currency exchange rate.")
    print()
    return result_list
    
def usd_euro_conversion(eur_exchange_rate):
    usd=float(input("Give USD to convert: "))
    ans=usd*eur_exchange_rate
    print(usd,"USD in EUR is", round(ans,2) ,"EUR")
    print()

def usd_aud_conversion(aud_exchange_rate):
    usd=float(input("Give USD to convert: "))
    ans=usd*aud_exchange_rate
    print(usd,"USD in AUD is", round(ans,2) ,"AUD")
    print()

def usd_gbp_conversion(gbp_exchange_rate):
    usd=float(input("Give USD to convert: "))
    ans=usd*gbp_exchange_rate
    print(usd,"USD in GBP is", round(ans,2) ,"GBP")
    print()


eur_exchange_rate=0
aud_exchange_rate=0
gbp_exchange_rate=0
currency_data_list =[]
while True:
    print("ACME(tm) US DOLLAR EXCHANGE RATE APP")
    print("1) LOAD currency exchange rate data from a file")
    print("2) USE AVERAGE exchange rate")
    print("3) USE HIGHEST exchange rate")
    print("4) USE LOWEST exchange rate")
    print("5) CONVERT USD TO EUR")
    print("6) CONVERT USD TO AUD")
    print("7) CONVERT USD TO GBP")
    print("0) QUIT program")
    choice=int(input("Choose what to do: "))
    if choice==0:
        break
    if choice<0 or choice>7:
        print("Invalid Choice. Try Again")
        continue
    if choice==1:
        currency_data_list = load_data()
        result=average_currency_rate(currency_data_list)
        eur_exchange_rate=result[0]
        aud_exchange_rate=result[1]
        gbp_exchange_rate=result[2]
    elif choice==2:
        print("Using the average currency exchange rate.")
        print()
        result=average_currency_rate(currency_data_list)
        eur_exchange_rate=result[0]
        aud_exchange_rate=result[1]
        gbp_exchange_rate=result[2]
    elif choice==3:
        result=highest_currency_rate(currency_data_list)
        eur_exchange_rate=result[0]
        aud_exchange_rate=result[1]
        gbp_exchange_rate=result[2]
    elif choice==4:
        result=lowest_currency_rate(currency_data_list)
        eur_exchange_rate=result[0]
        aud_exchange_rate=result[1]
        gbp_exchange_rate=result[2]
    elif choice==5:
        usd_euro_conversion(eur_exchange_rate)
    elif choice==6:
        usd_aud_conversion(aud_exchange_rate)
    elif choice==7:
        usd_gbp_conversion(gbp_exchange_rate)    