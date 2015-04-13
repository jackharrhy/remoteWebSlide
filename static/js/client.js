var lastData = "Nothing";
var dataToString;

function update() {
 $.get("/getSlide", function(data) {
  if(data !== lastData) {
   $(".slide"+lastData.toString()).css("display","none");

   dataToString = data.toString();
   $(".slide"+dataToString).css("display","inline-block");

  }; 

  lastData = data;
	console.log(data);
 });
 
 setTimeout(update, 250);
}
update();

