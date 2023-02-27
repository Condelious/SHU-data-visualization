var ec_map = echarts.init(document.getElementById('map'));
// ec_map.showLoading()

let worlddata = [
    { name: 'China', value: '100' }, { name: 'United States', value: '2000', groupId: 0 }, { name: 'Democratic Republic of Congo', value: '50', groupId: 1 }
];

let worlddata2 = [
    { name: 'China', value: '200' }, { name: 'United States', value: '3000' }, { name: 'United Kingdom', value: '500' }
];

var nameMap = {
    
    'Central African Rep.': 'Central African Republic',
    'S. Sudan': 'South Sudan',
    'Dominican Rep.': 'Dominican Republic',
    'Antigua and Barb.': 'Antigua and Barbuda',
    'Dem. Rep. Korea': 'North Korea',
    'Korea': 'South Korea',
    'Côte d\'Ivoire': 'Cote d\'Ivoire'
}

var mapoption = {
    baseOption: {
        backgroundColor: '#FFFFFF',
        legend: {
            show: true,
            orient: 'vertical',
            selectedMode: 'single',
            left: 'top',
            top: "60px"
        },
        title: {
            text: 'Global GDP',
            subtext: '',
            x: 'left',
            textStyle: {
                fontFamily: "HarmonyOS_Sans_SC_Bold",
                fontWeight: "bolder",
                fontSize: 35,
            }
        },
        tooltip: {
            trigger: 'item'
        },
        
        
        visualMap: {
            type: 'piecewise',
            show: true,
            pieces: [
                {min:5000000000000,max:100000000000000},
                {min:1000000000000,max:50000000000000},
                {min:500000000000,max:10000000000000},
                {min:100000000000,max:5000000000000},
                {min:50000000000,max:1000000000000},
                {min:20000000000,max:500000000000},
                {min:10000000000,max:20000000000},
                {min:5000000000,max:10000000000},
                {min:1000000000,max:5000000000},
                {min:500000001,max:1000000000},
                {min:100000000,max:500000000},
                {min:70000.1,max:300000},
                { min: 60000.1,max:70000},
                { min: 50000.1,max:60000},
                { min: 40000.1, max: 50000 },
                { min: 30000.1, max: 40000 },
                { min: 20000.1, max: 30000 },
                { min: 10000.1, max: 20000 },
                { min: 8000.1, max: 10000 },
                { min: 7000.1, max: 8000 },
                { min: 6000.1, max: 7000 },
                { min: 5000.1, max: 6000 },
                { min: 4000.1, max: 5000 },
                { min: 3000.1, max: 4000 },
                { min: 2000.1, max: 3000 },
                { min: 1000.1, max: 2000 },
                { min: 800.1, max: 1000 },
                { min: 500.1, max: 800 }, 
                { min: 300.1, max: 500 },
                { min: 50.1, max: 300 },
                { max: 50 }
            ],
            text: "",
            x: 'right',
            y: 'bottom',
            calculable: true,
            inRange: {
                color: ['#fffea2', '#ffae70', '#ff726f', '#aa4b49', '#420000','#aacee2',"#65a8c4","#004159"],
            },
        },
        timeline: {
            show: true,
            axisType: 'category',
            data: 
            ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
        },
        series: [
            {
                name: 'GDP',
                type: 'map',
                map: 'world',
                nameMap: nameMap,
                roam: true,
                x: 'rightt',
                y: 'bottom',
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: true,
                        fontSize: 22
                    }
                },
                showLegendSymbol: false

                
            },
            {
                name: 'GDPPC',
                type: 'map',
                map: 'world',
                nameMap: nameMap,
                roam: true,
                x: 'rightt',
                y: 'bottom',
                label: {
                    normal: {
                        show: false
                    },
                    emphasis: {
                        show: true,
                        fontSize: 22
                    }
                },
                showLegendSymbol: false
            },
     
        ]
    },

};

ec_map.setOption(mapoption);

//点击触发事件
ec_map.on("click", function (params) {
    if (params.componentType != 'series') {
        return
    }
    // alert(params.name);
    lineoption.dataset[1].transform.config["="]=params.name;
    lineoption.title.subtext=params.name;
    ec_line.setOption(lineoption)
})