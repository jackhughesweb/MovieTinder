$(document).ready(function () {

	var movie_id = 0;

	$('.btn-like').click(function(e) {
		if (!$('.btn-like').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('like', movie_id);
		}
	});	

	$('.btn-dislike').click(function() {
		if (!$('.btn-dislike').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('dislike', movie_id);
		}
	});

	$('.btn-notseen').click(function() {
		if (!$('.btn-notseen').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('unseen', movie_id);
		}
	});

	$('.btn-rec').click(function () {
		$('.overlay').show();
	});

	$('.btn-overlay-close').click(function () {
		$('.overlay').hide();
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
});