<!DOCTYPE html>
<meta charset="utf-8">
<body>
  <script src="http://d3js.org/d3.v3.min.js"></script>
  <script src="http://d3js.org/topojson.v1.min.js"></script>
  <!-- I recommend you host this file on your own, since this will change without warning -->
  <script src="js/datamaps.world.min.js"></script>
  <div id="container" style="position: relative; width: 1200px; height: 650px;"></div>
  <script>
    
    var oReq = new XMLHttpRequest(); //New request object
    election = new Datamap({
        scope: 'world',
        element: document.getElementById('container'),
        projection: 'mercator'
      });
    var presidentialTrips;
    oReq.onload = function() {
	presidentialTrips = this.responseText;
	// presidentialTrips = JSON.parse(presidentialTrips);
	alert(presidentialTrips);
	election.arc(presidentialTrips, {strokeWidth: 2});
    };
    
    function reqListener () {
      console.log(this.responseText);
    }
    oReq.open("get", "returnvalue.php?domain=<?php echo $_GET['domain'];?>", true);
    oReq.send();
</script>

</body>
