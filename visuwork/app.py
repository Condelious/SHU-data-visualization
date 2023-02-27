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
gdp2000 = utils.get_csv_column_data(utils.gdp,2)
gdppc2000 = utils.get_csv_column_data(utils.gdppc,2)
gdp2012 = utils.get_csv_column_data(utils.gdp,3)
gdppc2012 = utils.get_csv_column_data(utils.gdppc,3)
gdp2013 = utils.get_csv_column_data(utils.gdp,4)
gdppc2013 = utils.get_csv_column_data(utils.gdppc,4)
gdp2014 = utils.get_csv_column_data(utils.gdp,5)
gdppc2014 = utils.get_csv_column_data(utils.gdppc,5)
gdp2015 = utils.get_csv_column_data(utils.gdp,6)
gdppc2015 = utils.get_csv_column_data(utils.gdppc,6)
gdp2016 = utils.get_csv_column_data(utils.gdp,7)
gdppc2016 = utils.get_csv_column_data(utils.gdppc,7)
gdp2017 = utils.get_csv_column_data(utils.gdp,8)
gdppc2017 = utils.get_csv_column_data(utils.gdppc,8)
gdp2018 = utils.get_csv_column_data(utils.gdp,9)
gdppc2018 = utils.get_csv_column_data(utils.gdppc,9)
gdp2019 = utils.get_csv_column_data(utils.gdp,10)
gdppc2019 = utils.get_csv_column_data(utils.gdppc,10)
gdp2020 = utils.get_csv_column_data(utils.gdp,11)
gdppc2020 = utils.get_csv_column_data(utils.gdppc,11)
gdp2021 = utils.get_csv_column_data(utils.gdp,12)
gdppc2021 = utils.get_csv_column_data(utils.gdppc,12)



@app.route("/")
def home():
    return render_template("index.html")



@app.route("/map", methods=["get", "post"])
def getmapdata():
    year=['1990','2000','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    options = []
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

    

    gdp2000_s = []
    gdppc2000_s = []
    num = 266
    for i in range(0, num):
        gdp2000_s.append({"name":country.iloc[i],"value":gdp2000.iloc[i]})
        gdppc2000_s.append({"name":country1.iloc[i],"value":gdppc2000.iloc[i]})

    gdp2000_d = {"data": gdp2000_s}
    gdppc2000_d = {"data": gdppc2000_s}   


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
    options.append({"series": [gdp2000_d, gdppc2000_d]})
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
