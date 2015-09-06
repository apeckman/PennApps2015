$(document).ready(function() {
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

	$("#aboutDiv").hide();
	$("#finraDiv").hide();
	$("#contactDiv").hide();

	$("#about").click(function() {
		$("#wow").fadeOut(250);
		$("#aboutDiv").fadeIn(250);
	});

	$("#finra").click(function() {
		$("#wow").fadeOut(250);
		$("#finraDiv").fadeIn(250);
	});

	$("#contact").click(function() {
		$("#wow").fadeOut(250);
		$("#contactDiv").fadeIn(250);
	});

	$("#closeA").click(function() {
		$("#wow").fadeIn(250);
		$("#aboutDiv").fadeOut(250);
	});

	$("#closeF").click(function() {
		$("#wow").fadeIn(250);
		$("#finraDiv").fadeOut(250);
	});

	$("#closeC").click(function() {
		$("#wow").fadeIn(250);
		$("#contactDiv").fadeOut(250);
	});

	function wow_button() {
		alert(data.message);
	}

	$("#algButton").click(function() {
		console.log("STOCK");

	});

});

