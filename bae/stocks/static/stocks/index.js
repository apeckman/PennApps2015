$(document).ready(function() {
	$("#aboutDiv").hide();
	$("#finraDiv").hide();
	$("#contactDiv").hide();
});
$("#about").click(function() {
	console.log("wow");
	$("#wow").fadeOut(500);
	$("#aboutDiv").fadeIn(500);
});
$("#closeA").click(function() {
	console.log("lol");
	$("#wow").fadeIn(250);
	$("#aboutDiv").fadeOut(500);
});
$("#slider-scale").slider({
    animate: true,
    range: true,
    value: 5,
    min: 0,
    max: 4,
    step: 1,
    values: [0,1,2,3,4],
    // Gets a live reading of the value and prints it on the page
    slide: function( event, ui ) {
			var result = ui;
			$("#sliderResult").html(ui.values[1]);

    }
})
.each(function() {
var labels = ['very short', 'short', 'neutral', 'long', 'very long'];
for (var i = 0; i < 5; i++) {
    var left = i * 20 + 10;
    var el = $('<label class = "center-align">' + labels[i] + '</label>').css({left: left + '%'});
    $("#slider-scale").append(el);

	}
});