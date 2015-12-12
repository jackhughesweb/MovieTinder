$(document).ready(function () {
	
	var movie_id = 0;

	$('.likebtn').click(function(e) {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			ajaxReq('like', movie_id);
		}
	});	

	$('.dislikebtn').click(function() {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			ajaxReq('dislike', movie_id);
		}
	});

	$('.notseenbtn').click(function() {
		if (!$('.likebtn').hasClass('disabled')) {
			$('.testbtn').addClass('disabled');
			ajaxReq('unseen', movie_id);
		}
	});

});


function ajaxReq(button, movie_id){
	$.ajax({
		url: "/opinion",

		data:{
			opinion: button,
			movie_id: movie_id
		},

		type: "POST",

		dataType: "json",

		success: function( response ){
			//change webpage
		},

		complete: function(){

		}
	});
}