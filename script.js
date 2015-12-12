$(document).ready(function () {
	$('.likebtn').click(function(e) {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			$.post(window.location.href, {
				"opinion": "like",
				"movie_id": "123"
			}, function (raw_data) {
				var data = $.parseJSON(raw_data);
				console.log(data);
			});
		}
	});	

	$('.dislikebtn').click(function() {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			$.post(window.location.href, {
				"opinion": "dislike",
				"movie_id": "123"
			}, function (raw_data) {
				var data = $.parseJSON(raw_data);
				console.log(data);
			});
		}
	});

	$('.notseenbtn').click(function() {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			$.post(window.location.href, {
				"opinion": "notseen",
				"movie_id": "123"
			}, function (raw_data) {
				var data = $.parseJSON(raw_data);
				console.log(data);
			});
		}
	});
});