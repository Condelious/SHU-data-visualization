

function getmapdata() {
    $.ajax({
        url: "/map",
        type: "POST",
        dataType: "json",
        success: function (data) {
             //alert("Success")
            // console.log(data);
            // mapoption.options[0].series[0].data = data.new_case;
            // mapoption.options[0].series[1].data=data.new_death;
            // mapoption.options[0].series[2].data = data.total_case;
            // mapoption.options[0].series[3].data = data.total_death;
            mapoption.options=data.options
            mapoption.baseOption.timeline.data = data.timeline;
            ec_map.setOption(mapoption);
        },
        // error: function () {
        //     alert("GetDataError!")
        //}
    })
}






getmapdata();

// setInterval(updatetime(), 60000);