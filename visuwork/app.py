from flask import Flask
from flask import render_template
import utils
import pandas as pd
from flask import jsonify

app = Flask(__name__)


country = utils.get_csv_column_data(utils.gdp,0)
country1 = utils.get_csv_column_data(utils.gdppc,0)
gdp1990 = utils.get_csv_column_data(utils.gdp,1)
gdppc1990 = utils.get_csv_column_data(utils.gdppc,1)
gdp1991 = utils.get_csv_column_data(utils.gdp,2)
gdppc1991 = utils.get_csv_column_data(utils.gdppc,2)
gdp1992 = utils.get_csv_column_data(utils.gdp,3)
gdppc1992 = utils.get_csv_column_data(utils.gdppc,3)
gdp1993 = utils.get_csv_column_data(utils.gdp,4)
gdppc1993 = utils.get_csv_column_data(utils.gdppc,4)
gdp1994 = utils.get_csv_column_data(utils.gdp,5)
gdppc1994 = utils.get_csv_column_data(utils.gdppc,5)
gdp1995 = utils.get_csv_column_data(utils.gdp,6)
gdppc1995 = utils.get_csv_column_data(utils.gdppc,6)
gdp1996 = utils.get_csv_column_data(utils.gdp,7)
gdppc1996 = utils.get_csv_column_data(utils.gdppc,7)
gdp1997 = utils.get_csv_column_data(utils.gdp,8)
gdppc1997 = utils.get_csv_column_data(utils.gdppc,8)
gdp1998 = utils.get_csv_column_data(utils.gdp,9)
gdppc1998 = utils.get_csv_column_data(utils.gdppc,9)
gdp1999 = utils.get_csv_column_data(utils.gdp,10)
gdppc1999 = utils.get_csv_column_data(utils.gdppc,10)
gdp2000 = utils.get_csv_column_data(utils.gdp,11)
gdppc2000 = utils.get_csv_column_data(utils.gdppc,11)
gdp2001 = utils.get_csv_column_data(utils.gdp,12)
gdppc2001 = utils.get_csv_column_data(utils.gdppc,12)
gdp2002 = utils.get_csv_column_data(utils.gdp,13)
gdppc2002 = utils.get_csv_column_data(utils.gdppc,13)
gdp2003 = utils.get_csv_column_data(utils.gdp,14)
gdppc2003 = utils.get_csv_column_data(utils.gdppc,14)
gdp2004 = utils.get_csv_column_data(utils.gdp,15)
gdppc2004 = utils.get_csv_column_data(utils.gdppc,15)
gdp2005 = utils.get_csv_column_data(utils.gdp,16)
gdppc2005 = utils.get_csv_column_data(utils.gdppc,16)
gdp2006 = utils.get_csv_column_data(utils.gdp,17)
gdppc2006 = utils.get_csv_column_data(utils.gdppc,17)
gdp2007 = utils.get_csv_column_data(utils.gdp,18)
gdppc2007 = utils.get_csv_column_data(utils.gdppc,18)
gdp2008 = utils.get_csv_column_data(utils.gdp,19)
gdppc2008 = utils.get_csv_column_data(utils.gdppc,19)
gdp2009 = utils.get_csv_column_data(utils.gdp,20)
gdppc2009 = utils.get_csv_column_data(utils.gdppc,20)
gdp2010 = utils.get_csv_column_data(utils.gdp,21)
gdppc2010 = utils.get_csv_column_data(utils.gdppc,21)
gdp2011 = utils.get_csv_column_data(utils.gdp,22)
gdppc2011 = utils.get_csv_column_data(utils.gdppc,22)
gdp2012 = utils.get_csv_column_data(utils.gdp,23)
gdppc2012 = utils.get_csv_column_data(utils.gdppc,23)
gdp2013 = utils.get_csv_column_data(utils.gdp,24)
gdppc2013 = utils.get_csv_column_data(utils.gdppc,24)
gdp2014 = utils.get_csv_column_data(utils.gdp,25)
gdppc2014 = utils.get_csv_column_data(utils.gdppc,25)
gdp2015 = utils.get_csv_column_data(utils.gdp,26)
gdppc2015 = utils.get_csv_column_data(utils.gdppc,26)
gdp2016 = utils.get_csv_column_data(utils.gdp,27)
gdppc2016 = utils.get_csv_column_data(utils.gdppc,27)
gdp2017 = utils.get_csv_column_data(utils.gdp,28)
gdppc2017 = utils.get_csv_column_data(utils.gdppc,28)
gdp2018 = utils.get_csv_column_data(utils.gdp,29)
gdppc2018 = utils.get_csv_column_data(utils.gdppc,29)
gdp2019 = utils.get_csv_column_data(utils.gdp,30)
gdppc2019 = utils.get_csv_column_data(utils.gdppc,30)
gdp2020 = utils.get_csv_column_data(utils.gdp,31)
gdppc2020 = utils.get_csv_column_data(utils.gdppc,31)
gdp2021 = utils.get_csv_column_data(utils.gdp,32)
gdppc2021 = utils.get_csv_column_data(utils.gdppc,32)





@app.route("/")
def home():
    return render_template("index.html")



@app.route("/map", methods=["get", "post"])
def getmapdata():
    year=['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    options = []

#     gdp=[]
#     gdppc=[]
#     gdp_s = []
#     gdppc_s = []
#     gdp_d=[]
#     gdppc_d=[]
#     num = 267
#     for i in range(1,31):

#         gdp[i] = utils.get_csv_column_data(utils.gdp,i)
#         gdppc[i] = utils.get_csv_column_data(utils.gdp,i)
    
      
#         for j in range(0, num):

#             gdp_s[i].append({"name":country.iloc[j],"value":gdp[i].iloc[j]})
#             gdppc_s[i].append({"name":country1.iloc[j],"value":gdppc[i].iloc[j]})

#         gdp_d[i] = {"data": gdp_s[i]}
#         gdppc_d[i] = {"data": gdppc_s[i]}  

#         options.append({"series": [gdp_d[i], gdppc_d[i]]})

        
    
#     return jsonify({"options": options, "timeline": year})
# if __name__ == '__main__':
#      app.run()
    # length = 12
    # nc, nd, tcpm, tdpm = utils.get_map_data(length)
   
    # gdp = utils.get_csv_column_data(utils.gdp,7)
    # gdppc = utils.get_csv_column_data(utils.gdppc,8)
      # for  col in utils.gdp.iteritems():
        #     gdp_s.append({"name": country.iloc[i], "value": str(col.iloc[i])})
        # for  col in utils.gdppc.iteritems():
        #     gdppc_s.append({"name":country.iloc[i], "value": str(col.iloc[i])})
       
        # gdp_d = {"data": gdp_s}
        # gdppc_d = {"data": gdppc_s}
    
    # utils.gdp.drop(labels='Country Name', axis=0, inplace=True)
    # utils.gdppc.drop(labels='Country Name', axis=0, inplace=True)
#1990
    gdp1990_s = []
    gdppc1990_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1990_s.append({"name":country.iloc[i],"value":gdp1990.iloc[i]})
        gdppc1990_s.append({"name":country1.iloc[i],"value":gdppc1990.iloc[i]})

    gdp1990_d = {"data": gdp1990_s}
    gdppc1990_d = {"data": gdppc1990_s}  



    gdp1991_s = []
    gdppc1991_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1991_s.append({"name":country.iloc[i],"value":gdp1991.iloc[i]})
        gdppc1991_s.append({"name":country1.iloc[i],"value":gdppc1991.iloc[i]})

    gdp1991_d = {"data": gdp1991_s}
    gdppc1991_d = {"data": gdppc1991_s}  

    gdp1992_s = []
    gdppc1992_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1992_s.append({"name":country.iloc[i],"value":gdp1992.iloc[i]})
        gdppc1992_s.append({"name":country1.iloc[i],"value":gdppc1992.iloc[i]})

    gdp1992_d = {"data": gdp1992_s}
    gdppc1992_d = {"data": gdppc1992_s}   

    gdp1993_s = []
    gdppc1993_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1993_s.append({"name":country.iloc[i],"value":gdp1993.iloc[i]})
        gdppc1993_s.append({"name":country1.iloc[i],"value":gdppc1993.iloc[i]})

    gdp1993_d = {"data": gdp1993_s}
    gdppc1993_d = {"data": gdppc1993_s}   

    gdp1994_s = []
    gdppc1994_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1994_s.append({"name":country.iloc[i],"value":gdp1994.iloc[i]})
        gdppc1994_s.append({"name":country1.iloc[i],"value":gdppc1994.iloc[i]})

    gdp1994_d = {"data": gdp1994_s}
    gdppc1994_d = {"data": gdppc1994_s}   

    gdp1995_s = []
    gdppc1995_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1995_s.append({"name":country.iloc[i],"value":gdp1995.iloc[i]})
        gdppc1995_s.append({"name":country1.iloc[i],"value":gdppc1995.iloc[i]})

    gdp1995_d = {"data": gdp1995_s}
    gdppc1995_d = {"data": gdppc1995_s}   

    gdp1995_s = []
    gdppc1995_s = []
    num = 266
    
       
      
    gdp1996_s = []
    gdppc1996_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1996_s.append({"name":country.iloc[i],"value":gdp1996.iloc[i]})
        gdppc1996_s.append({"name":country1.iloc[i],"value":gdppc1996.iloc[i]})

    gdp1996_d = {"data": gdp1996_s}
    gdppc1996_d = {"data": gdppc1996_s}   


    gdp1997_s = []
    gdppc1997_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1997_s.append({"name":country.iloc[i],"value":gdp1997.iloc[i]})
        gdppc1997_s.append({"name":country1.iloc[i],"value":gdppc1997.iloc[i]})

    gdp1997_d = {"data": gdp1997_s}
    gdppc1997_d = {"data": gdppc1997_s}   

    gdp1998_s = []
    gdppc1998_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1998_s.append({"name":country.iloc[i],"value":gdp1998.iloc[i]})
        gdppc1998_s.append({"name":country1.iloc[i],"value":gdppc1998.iloc[i]})

    gdp1998_d = {"data": gdp1998_s}
    gdppc1998_d = {"data": gdppc1998_s}   

    gdp1999_s = []
    gdppc1999_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp1999_s.append({"name":country.iloc[i],"value":gdp1999.iloc[i]})
        gdppc1999_s.append({"name":country1.iloc[i],"value":gdppc1999.iloc[i]})

    gdp1999_d = {"data": gdp1999_s}
    gdppc1999_d = {"data": gdppc1999_s}   

    gdp2000_s = []
    gdppc2000_s = []
    num = 266
    for i in range(0, num):
        gdp2000_s.append({"name":country.iloc[i],"value":gdp2000.iloc[i]})
        gdppc2000_s.append({"name":country1.iloc[i],"value":gdppc2000.iloc[i]})

    gdp2000_d = {"data": gdp2000_s}
    gdppc2000_d = {"data": gdppc2000_s}   


    gdp2001_s = []
    gdppc2001_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2001_s.append({"name":country.iloc[i],"value":gdp2001.iloc[i]})
        gdppc2001_s.append({"name":country1.iloc[i],"value":gdppc2001.iloc[i]})

    gdp2001_d = {"data": gdp2001_s}
    gdppc2001_d = {"data": gdppc2001_s}   


    gdp2002_s = []
    gdppc2002_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2002_s.append({"name":country.iloc[i],"value":gdp2002.iloc[i]})
        gdppc2002_s.append({"name":country1.iloc[i],"value":gdppc2002.iloc[i]})

    gdp2002_d = {"data": gdp2002_s}
    gdppc2002_d = {"data": gdppc2002_s}   



    gdp2003_s = []
    gdppc2003_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2003_s.append({"name":country.iloc[i],"value":gdp2003.iloc[i]})
        gdppc2003_s.append({"name":country1.iloc[i],"value":gdppc2003.iloc[i]})

    gdp2003_d = {"data": gdp2003_s}
    gdppc2003_d = {"data": gdppc2003_s}   


    gdp2004_s = []
    gdppc2004_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2004_s.append({"name":country.iloc[i],"value":gdp2004.iloc[i]})
        gdppc2004_s.append({"name":country1.iloc[i],"value":gdppc2004.iloc[i]})

    gdp2004_d = {"data": gdp2004_s}
    gdppc2004_d = {"data": gdppc2004_s}   



    gdp2005_s = []
    gdppc2005_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2005_s.append({"name":country.iloc[i],"value":gdp2005.iloc[i]})
        gdppc2005_s.append({"name":country1.iloc[i],"value":gdppc2005.iloc[i]})

    gdp2005_d = {"data": gdp2005_s}
    gdppc2005_d = {"data": gdppc2005_s}   


    gdp2006_s = []
    gdppc2006_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2006_s.append({"name":country.iloc[i],"value":gdp2006.iloc[i]})
        gdppc2006_s.append({"name":country1.iloc[i],"value":gdppc2006.iloc[i]})

    gdp2006_d = {"data": gdp2006_s}
    gdppc2006_d = {"data": gdppc2006_s}   


    gdp2007_s = []
    gdppc2007_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2007_s.append({"name":country.iloc[i],"value":gdp2007.iloc[i]})
        gdppc2007_s.append({"name":country1.iloc[i],"value":gdppc2007.iloc[i]})

    gdp2007_d = {"data": gdp2007_s}
    gdppc2007_d = {"data": gdppc2007_s}   



    gdp2008_s = []
    gdppc2008_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2008_s.append({"name":country.iloc[i],"value":gdp2008.iloc[i]})
        gdppc2008_s.append({"name":country1.iloc[i],"value":gdppc2008.iloc[i]})

    gdp2008_d = {"data": gdp2008_s}
    gdppc2008_d = {"data": gdppc2008_s}   



    gdp2009_s = []
    gdppc2009_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2009_s.append({"name":country.iloc[i],"value":gdp2009.iloc[i]})
        gdppc2009_s.append({"name":country1.iloc[i],"value":gdppc2009.iloc[i]})

    gdp2009_d = {"data": gdp2009_s}
    gdppc2009_d = {"data": gdppc2009_s}   




    gdp2010_s = []
    gdppc2010_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2010_s.append({"name":country.iloc[i],"value":gdp2010.iloc[i]})
        gdppc2010_s.append({"name":country1.iloc[i],"value":gdppc2010.iloc[i]})

    gdp2010_d = {"data": gdp2010_s}
    gdppc2010_d = {"data": gdppc2010_s}   



    gdp2011_s = []
    gdppc2011_s = []
    num = 266
    
       
      
    for i in range(0, num):

        gdp2011_s.append({"name":country.iloc[i],"value":gdp2011.iloc[i]})
        gdppc2011_s.append({"name":country1.iloc[i],"value":gdppc2011.iloc[i]})

    gdp2011_d = {"data": gdp2011_s}
    gdppc2011_d = {"data": gdppc2011_s}   







    gdp2012_s = []
    gdppc2012_s = []
    num = 266
    for i in range(0, num):    
        gdp2012_s.append({"name":country.iloc[i],"value":gdp2012.iloc[i]})
        gdppc2012_s.append({"name":country1.iloc[i],"value":gdppc2012.iloc[i]})

    gdp2012_d = {"data": gdp2012_s}
    gdppc2012_d = {"data": gdppc2012_s}  

    gdp2013_s = []
    gdppc2013_s = []
    num = 266
    for i in range(0, num):
        gdp2013_s.append({"name":country.iloc[i],"value":gdp2013.iloc[i]})
        gdppc2013_s.append({"name":country1.iloc[i],"value":gdppc2013.iloc[i]})
    gdp2013_d = {"data": gdp2013_s}
    gdppc2013_d = {"data": gdppc2013_s}    

    gdp2014_s = []
    gdppc2014_s = []
    num = 266
    for i in range(0, num):
        gdp2014_s.append({"name":country.iloc[i],"value":gdp2014.iloc[i]})
        gdppc2014_s.append({"name":country1.iloc[i],"value":gdppc2014.iloc[i]})
    gdp2014_d = {"data": gdp2014_s}
    gdppc2014_d = {"data": gdppc2014_s}   


    gdp2015_s = []
    gdppc2015_s = []
    num = 266
    for i in range(0, num):
        gdp2015_s.append({"name":country.iloc[i],"value":gdp2015.iloc[i]})
        gdppc2015_s.append({"name":country1.iloc[i],"value":gdppc2015.iloc[i]})
    gdp2015_d = {"data": gdp2015_s}
    gdppc2015_d = {"data": gdppc2015_s}   


    gdp2016_s = []
    gdppc2016_s = []
    num = 266
    for i in range(0, num):
        gdp2016_s.append({"name":country.iloc[i],"value":gdp2016.iloc[i]})
        gdppc2016_s.append({"name":country1.iloc[i],"value":gdppc2016.iloc[i]})
    gdp2016_d = {"data": gdp2016_s}
    gdppc2016_d = {"data": gdppc2016_s}   

    gdp2017_s = []
    gdppc2017_s = []
    num = 266
    for i in range(0, num):
        gdp2017_s.append({"name":country.iloc[i],"value":gdp2017.iloc[i]})
        gdppc2017_s.append({"name":country1.iloc[i],"value":gdppc2017.iloc[i]})
    gdp2017_d = {"data": gdp2017_s}
    gdppc2017_d = {"data": gdppc2017_s} 

    gdp2018_s = []
    gdppc2018_s = []
    num = 266
    for i in range(0, num):
        gdp2018_s.append({"name":country.iloc[i],"value":gdp2018.iloc[i]})
        gdppc2018_s.append({"name":country1.iloc[i],"value":gdppc2018.iloc[i]})
    gdp2018_d = {"data": gdp2018_s}
    gdppc2018_d = {"data": gdppc2018_s} 


    gdp2019_s = []
    gdppc2019_s = []
    num = 266
    for i in range(0, num):
        gdp2019_s.append({"name":country.iloc[i],"value":gdp2019.iloc[i]})
        gdppc2019_s.append({"name":country1.iloc[i],"value":gdppc2019.iloc[i]})
    gdp2019_d = {"data": gdp2019_s}
    gdppc2019_d = {"data": gdppc2019_s} 

    gdp2020_s = []
    gdppc2020_s = []
    num = 266
    for i in range(0, num):
        gdp2020_s.append({"name":country.iloc[i],"value":gdp2020.iloc[i]})
        gdppc2020_s.append({"name":country1.iloc[i],"value":gdppc2020.iloc[i]})
    gdp2020_d = {"data": gdp2020_s}
    gdppc2020_d = {"data": gdppc2020_s} 

    gdp2021_s = []
    gdppc2021_s = []
    num = 266
    for i in range(0, num):
        gdp2021_s.append({"name":country.iloc[i],"value":gdp2021.iloc[i]})
        gdppc2021_s.append({"name":country1.iloc[i],"value":gdppc2021.iloc[i]})
    gdp2021_d = {"data": gdp2021_s}
    gdppc2021_d = {"data": gdppc2021_s} 

    options.append({"series": [gdp1990_d, gdppc1990_d]})
    options.append({"series": [gdp1991_d, gdppc1991_d]})
    options.append({"series": [gdp1992_d, gdppc1992_d]})
    options.append({"series": [gdp1993_d, gdppc1993_d]})
    options.append({"series": [gdp1994_d, gdppc1994_d]})
    options.append({"series": [gdp1995_d, gdppc1995_d]})
    options.append({"series": [gdp1996_d, gdppc1996_d]})
    options.append({"series": [gdp1997_d, gdppc1997_d]})
    options.append({"series": [gdp1998_d, gdppc1998_d]})
    options.append({"series": [gdp1999_d, gdppc1999_d]})
    options.append({"series": [gdp2000_d, gdppc2000_d]})
    options.append({"series": [gdp2001_d, gdppc2001_d]})
    options.append({"series": [gdp2002_d, gdppc2002_d]})
    options.append({"series": [gdp2003_d, gdppc2003_d]})
    options.append({"series": [gdp2004_d, gdppc2004_d]})
    options.append({"series": [gdp2005_d, gdppc2005_d]})
    options.append({"series": [gdp2006_d, gdppc2006_d]})
    options.append({"series": [gdp2007_d, gdppc2007_d]})
    options.append({"series": [gdp2008_d, gdppc2008_d]})
    options.append({"series": [gdp2009_d, gdppc2009_d]})
    options.append({"series": [gdp2010_d, gdppc2010_d]})
    options.append({"series": [gdp2011_d, gdppc2011_d]})
    options.append({"series": [gdp2012_d, gdppc2012_d]})
    options.append({"series": [gdp2013_d, gdppc2013_d]})
    options.append({"series": [gdp2014_d, gdppc2014_d]})
    options.append({"series": [gdp2015_d, gdppc2015_d]})
    options.append({"series": [gdp2016_d, gdppc2016_d]})
    options.append({"series": [gdp2017_d, gdppc2017_d]})
    options.append({"series": [gdp2018_d, gdppc2018_d]})
    options.append({"series": [gdp2019_d, gdppc2019_d]})
    options.append({"series": [gdp2020_d, gdppc2020_d]})
    options.append({"series": [gdp2021_d, gdppc2021_d]})
    return jsonify({"options": options, "timeline": year})
if __name__ == '__main__':
     app.run()
   # app.run(host='127.0.0.1',port=5001)    
