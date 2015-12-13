$(document).ready(function () {
	var recnum = 1
	var name = "";
	var year = 0;
	var picks=0;
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
		console.log("hi");
		if (!$('.btn-notseen').hasClass('disabled')) {
			$('.btn-opinion').addClass('disabled');
			ajaxReq('unseen', name, year);
		}
	});

	$('.btn-rec').click(function () {
		$('.overlay').fadeIn();
		$('.overlay-panel .flex').addClass('animated slideInUp');
		
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

	$('.btn-opinion').click(function(){
		picks++;
		console.log("yo");
		if(picks>9){
				$.getJSON('/recommended', function(data){
				console.log("hello");
				$('ul.rec-list').html('');
				for(i=0; i< 3; i++){
					addRecommendation(data, i);
				}
			}); 
		}
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



	function addRecommendation(movie, num) {
		$('.count').text(recnum.toString());
		recnum +=1;
		$('ul.rec-list').append('<li><table><tr><td><a href="http://www.imdb.com/title/'+movie[num]['imdbID']+'/"><img src="' + movie[num]['Poster'] +'" width="100%"></td><td><span>'+movie[num]['Title']+'</span><br>'+movie[num]['Ratio']+'</td></tr></table></li>');
	}
});