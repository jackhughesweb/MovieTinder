$(document).ready(function () {

	var movie_id = "";

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

	function ajaxReq(butto, movie_id){
		$.ajax({
			url: "/opinion",

			data:{
				opinion: butto,
				movie_id: movie_id
			},

			type: "POST",

			dataType: "json",

			success: function( response ){
				movie_id = response['imdbID'];
				$('#movie-art-img').prop('src', response['Poster']);
				$('.btn-opinion').removeClass('disabled');
			},

			complete: function(){

			}
		});
	}

	$.getJSON('/status', function (data) {
		movie_id = data['imdbID'];
		$('#movie-art-img').prop('src', data['Poster']);
		$('.btn-opinion').removeClass('disabled');
	});

	function addRecommendation(movie) {
		$('ul.rec-list').append('<li><table><tr><td><img src="http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SX300.jpg" width="100%"></td><td><span>Gravity</span><br>0.912</td></tr></table></li>');
	}

	addRecommendation({});
	addRecommendation({});
});