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
		$('.overlay').fadeIn();
		$('.overlay-panel .flex').addClass('animated slideInUp');
		$.getJSON('/recommended', function(data){
			addRecommendation(data);
		}); 
	});

	$('.btn-overlay-close').click(function () {
		$('.overlay-panel .flex').addClass('animated slideOutUp');
	});

	$('.overlay-panel .flex div').click(function (e) {
		e.stopPropagation();
	});

	$('.overlay-panel .flex').click(function () {
		$('.overlay-panel .flex').addClass('animated slideOutUp');
		$('.overlay').fadeOut(function () {
			$('.overlay-panel .flex').removeClass('animated');
			$('.overlay-panel .flex').removeClass('slideInUp');
			$('.overlay-panel .flex').removeClass('slideOutUp');
		});
	});

	function ajaxReq(butto, reqname, reqyear){
		$.ajax({
			url: "/opinion",

			data:{
				opinion: butto,
				mName: reqname,
				mYear: reqyear
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
		$('ul.rec-list').append('<li><table><tr><td><a href="http://www.imdb.com/title/'+movie['imdbID']+'/"><img src="' + movie['Poster'] +'" width="100%"></td><td><span>'+movie['Title']+'</span><br>'+movie['imdbRating']+'</td></tr></table></li>');
	}
});