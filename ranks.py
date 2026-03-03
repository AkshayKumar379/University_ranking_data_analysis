import csv

def readFiles(Unifile=r"C:\Users\AKSHAY KUMAR\akshay's folder\flm ds genai\mini_project-1\universities.csv",countryfile=r"C:\Users\AKSHAY KUMAR\akshay's folder\flm ds genai\mini_project-1\capitals.csv"):
    all_univ={}
    countries={}

    with open(Unifile) as file1:
        reader=csv.DictReader(file1)

        for row in reader:
            code=row["Code"]
            all_univ[code]={
                "institution name":row["Institution name"],
                "country":row["Country"],
                "world rank":row["World Rank"],
                "national rank":row["National Rank"],
                "degrees":row["Degrees Offered"],
                "score":row["Score"],
                "average cost":row["Average Cost"]
            }

    with open(countryfile) as file2:
        reader2=csv.DictReader(file2)

        for row in reader2:
            country=row["Country Name"]

            countries[country]={
                "capital":row["Capital"],
                "continent":row["Continent"],
                "country code":row["Country Code"],
                "latitude":row["Latitude"],
                "longitude":row["Longitude"]
            }
    
    for code,details in all_univ.items():
        co_country=details["country"]
        if co_country in countries:
            details["continent"]=countries[co_country]["continent"]
    
    return all_univ,countries




def findCountryByName(countryName,countries):
    for name,details in countries.items():
        if name.lower()==countryName.lower():
            return {name:details}
    return None


def getAllCodes(allUniversities):
    list_of_codes=[]
    for code,details in all_univs.items():
        list_of_codes.append(code)
    return list_of_codes
        

def getDistinctCountries(alluniversities):
    countryset=set()
    for code,details in all_univs.items():
        countryset.add(details["country"])
    return countryset


def getDistinctContinent(alluniversities):
    continentset=set()
    for code,details in all_univs.items():
        continentset.add(details["continent"])
    return continentset


def getTopIntRank(countryname,alluniversities):
    toprank=None
    topuniversity=None
    for code,details in all_univs.items():
        if countryname.lower()==details["country"].lower():
            rank=int(details["world rank"])
            if toprank is None or rank<toprank:
                toprank=rank
                topuniversity=details["institution name"]
    if topuniversity is not None:
        return (f"top university is {topuniversity} with rank {toprank}")
    else:
        return f"no university found for {countryname}"


def getTopNatRank(countryname,allunivs):
    natrank=None
    topuniversity=None

    for code,details in all_univs.items():
        if countryname.lower()==details["country"].lower():
            rank=int(details["national rank"])
            if natrank is None or rank<natrank:
                natrank=rank
                topuniversity=details["institution name"]
    return natrank,topuniversity


def getAvgScore(countryname,alluniversity):
    sum=0
    count=0
    for code,details in all_univs.items():
        if countryname.lower()==details["country"].lower():
            try:
                sum+=float(details["score"])
                count+=1
            except ValueError:
                continue

    return round(sum/count,2)


def getRelativeScoreContinent(countryname,allunivs):
    continent=None
    for code,details in allunivs.items():
        if countryname.lower()==details["country"].lower():
            continent=details["continent"]
            break
    if continent==None:
        return None
    
    sumscore=0
    count=0
    for code,details in allunivs.items():
        if countryname.lower()==details["country"].lower():
            score=float(details["score"])
            sumscore+=score
            count+=1
    averagescore=sumscore/count

    highestscore=None
    for code,details in allunivs.items():
        if details["continent"].lower()==continent.lower():
            score=float(details["score"])
            if highestscore is None or score>highestscore:
                highestscore=score


    return round(averagescore/highestscore,2)


def getUnivWithCapital(countryname,allunivs):
    codes=[]
    for code,details in all_univs.items():
        if details["country"].lower()==countryname.lower():
            codes.append(code)
    return codes



def studyInOnePlace(countryname,degrees,budget,alluniv):
    codes=[]
    for code,details in all_univs.items():
        if countryname.lower()==details["country"].lower():
            if all(degree in details["degrees"] for degree in degrees):
                if int(details["average cost"])<=budget:
                    codes.append(code)
    return codes





def studyinTwoplaces(firstcode,firstdegree,secondcode,seconddegree,budget,alluniv):
    if firstcode not in all_univs or secondcode not in all_univs:
        return False
    else:
        firstdetail=all_univs[firstcode]
        seconddetail=all_univs[secondcode]

        first_ok=(firstdegree in firstdetail["degrees"] and 
                  int(firstdetail["average cost"])<=budget
                  )
        second_ok=(seconddegree in seconddetail['degrees'] and
                   int(seconddetail["average cost"])<budget
                   )
        return first_ok and second_ok
    






if __name__=="__main__":
    # assigning dictionary to varibables
    all_univs,countries=readFiles()
    
    # findcountrybyname
    print(findCountryByName("Japan",countries))

    # get all codes
    print(getAllCodes(all_univs))

    # getdistinctcountries
    print(getDistinctCountries(all_univs))
    
    #getdistinctcontinent
    print(getDistinctContinent(all_univs))

    # gettoprank
    print(getTopIntRank("Germany",all_univs))

    #gettopnatrank
    print(getTopNatRank("Japan",all_univs))

    #getavgscore
    print(getAvgScore("United Kingdom",all_univs))

    #getrelativescore
    print(getRelativeScoreContinent("United Kingdom",all_univs))

    #getunivwithcapital
    print(getUnivWithCapital("Japan",all_univs))


    #studyinoneplace
    print(studyInOnePlace("Japan",["Diploma","PhD"],25000,all_univs))


    #studyintwoplaces
    print(studyinTwoplaces('JDBS', 'Diploma', 'OTTE', 
'PhD', 40000,all_univs))