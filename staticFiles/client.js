var lastData = "Nothing";
var dataToString;

// Client Side Changing of the Slide

	//TODO

// Update Function
(function() {
 $.get("/getSlide", function(data) {
  if(data !== lastData) {
   $(".slide"+lastData.toString()).css("display","none");

   dataToString = data.toString();
   $(".slide"+dataToString).css("display","inline-block");

  }; 

  lastData = data;

 });
 
 setTimeout(arguments.callee, 250);

})();
