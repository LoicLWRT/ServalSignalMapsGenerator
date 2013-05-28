#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
# Author: Loic Loewert for the servalproject.org

import string

address_list_full = [["Lab location",-35.029513,138.572897,"SignalTrace_around_campus.trace"],["Loic's place",-34.992246,138.597648,"SignalTrace_Loic_place_20130518.trace"],["The Kendall Hotel, Room 704",42.362244,-71.087281,"boston.trace"]]

debut_html = """---
layout: default_map
addresse: """

debut_html_home = """---
layout: default_home
addresse: """

fin_html = """
---
"""

debut_script = """ <script>
	 var image_0 = "" ;
	 var image_1 = "" ;
	 var image_2 = "" ;
	 var image_3 = "" ;
	 var image_4 = "" ;
	 var image_5 = "" ;
	 var image_6 = "" ;
	 var image_7 = "" ;
	 var image_8 = "" ;
	 var image_9 = "" ;
	 var image_10 = "" ;
	 var image_11 = "" ;
	 var show_low_signal = true;
	 
	var legend = document.getElementById('legend');
	var div = document.createElement('div');
	div.innerHTML = '<img src="assets/img/legend.png"> ';
	legend.appendChild(div);
	 
	 function toggleText(){
	 var text = document.getElementById('toggle_text');
		if (text.innerHTML=="Show"){
			text.innerHTML = "Hide";
		}
		else if (text.innerHTML=="Hide"){
			text.innerHTML = "Show";
		}
	 }
	 
	 function init_img() {
		 if (show_low_signal){
			 image_0 = 'assets/img/0.png';
			 image_1 = 'assets/img/1.png';
		}
		else {
			image_0 = ' ';
			image_1 = ' ';
		}
		 image_2 = 'assets/img/2.png';
		 image_3 = 'assets/img/3.png';
		 image_4 = 'assets/img/4.png';
		 image_5 = 'assets/img/5.png';
		 image_6 = 'assets/img/6.png';
		 image_7 = 'assets/img/7.png';
		 image_8 = 'assets/img/8.png';
		 image_9 = 'assets/img/9.png';
		 image_10 = 'assets/img/10.png';
		 image_11 = 'assets/img/11.png';
	 }
	 
      function initialize() {
		init_img();

        var mapOptions = {
          zoom: 15,
          center: new google.maps.LatLng(LOCATION_HERE),
	  panControl: false,
	  streetViewControl: false,
	  scaleControl: true,
          mapTypeId: google.maps.MapTypeId.ROADMAP
        };

        var map = new google.maps.Map(document.getElementById('map_canvas'),mapOptions);
"""

fin_script = """
map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
}   google.maps.event.addDomListener(window, 'load', initialize);	  
    </script>"""


debut_script_home = """<script>function loadURL(marker) {
    return function () {
        window.location.href = marker.url;
    }
}

function initialize() {
  var myOptions = {
    zoom: 1,
    center: new google.maps.LatLng(0,0),
    mapTypeId: google.maps.MapTypeId.ROADMAP,
  }
"""


fin_script_home = """
  var map = new google.maps.Map(document.getElementById('map_canvas'), myOptions);
  for (var i = 0; i < locations.length; i++) {
      var location = locations[i];
      var myLatLng = new google.maps.LatLng(location[1], location[2]);
      var marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: location[0],
          url: location[3]
      });
        google.maps.event.addListener(marker, 'click', loadURL(marker));
  } }  google.maps.event.addDomListener(window, 'load', initialize);	</script>"""


def get_icone(budget_link):
	if (budget_link < 0):
		budget_link = 0
	if (budget_link > 50):
		budget_link = 50
	return "image_"+ str(round((budget_link*11)/50)).replace('.0','')

for item in address_list_full:
	address = item[0]
	filename = string.translate(address, None, ' .,@#$').replace('é','e').replace('è','e').replace('ç','c').replace('ï','i')
	fread = open("traces/" + item[3], "r")
	fwrite = open(filename + ".html", "w")
	fwrite.write( debut_html + address + fin_html + debut_script.replace("LOCATION_HERE", str(item[1]) + "," + str(item[2])))
	fwrite.write("""var marker = new google.maps.Marker({position: new google.maps.LatLng(""" + str(item[1]) + "," + str(item[2]) + """), map: map,title: '""" + "Mesh extender location" + """'});""" + "\n")
	for line in fread:
		# line = line[:-1]
		table = line.split(";")
		if len(table)>5:
			gps_long= table[0]
			gps_lat= table[1]
			budget_link= table[6]
			fwrite.write("""var marker = new google.maps.Marker({position: new google.maps.LatLng(""" + gps_lat + "," + gps_long + """), map: map,title: '""" + "Budget link margin (dB): " + budget_link + """',icon:""" + str(get_icone(int(budget_link))) + """});""" + "\n")
	fwrite.write(fin_script)
	fread.close()
	fwrite.close()

str_to_write = "locations=["

f_index_write = open("index.html", "w")
f_index_write.write( debut_html_home + "Hi. Where is your Serval Mesh Extender?" + fin_html + debut_script_home + """ var marker = []; """ + "\n")
for index, item in enumerate(address_list_full):
	address = item[0]
	filename = string.translate(address, None, ' .,@#$').replace('é','e').replace('è','e').replace('ç','c').replace('ï','i')
	str_to_write = str_to_write + """[""" + "\"" + address + "\"," + str(item[1]) + "," + str(item[2]) + "," + "\"" + filename + ".html\"],"
f_index_write.write(str_to_write[:-1] + "];")
f_index_write.write(fin_script_home)
f_index_write.close()

