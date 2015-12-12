$(document).ready(function () {

	var name = "";
	var year = 0;

	$('.btn-like').click(function(e) {
		if (!$('.btn-like').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('like', name, year);
		}
	});	

	$('.btn-dislike').click(function() {
		if (!$('.btn-dislike').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('dislike', name, year);
		}
	});

	$('.btn-notseen').click(function() {
		if (!$('.btn-notseen').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('unseen', name, year);
		}
	});

	$('.btn-rec').click(function () {
		$('.overlay').show();
	});

	$('.btn-overlay-close').click(function () {
		$('.overlay').hide();
	});

	function ajaxReq(butto, name, year){
		$.ajax({
			url: "/opinion",

			data:{
				opinion: butto,
				mName: name
				mYear: year
			},

			type: "POST",

			dataType: "json",

			success: function( response ){
				name = response['Title'];
				year = response['Year']
				$('#movie-art-img').prop('src', response['Poster']);
				$('.btn-opinion').removeClass('disabled');
			},

			complete: function(){

			}
		});
	}

	$.getJSON('/status', function (data) {
		name = data['Title'];
		year = data['Year']
		$('#movie-art-img').prop('src', data['Poster']);
		$('.btn-opinion').removeClass('disabled');
	});

	function addRecommendation(movie) {
		$('ul.rec-list').append('<li><table><tr><td><img src="http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SX300.jpg" width="100%"></td><td><span>Gravity</span><br>0.912</td></tr></table></li>');
	}

	addRecommendation({});
	addRecommendation({});
});