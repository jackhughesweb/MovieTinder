<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<link rel="stylesheet" href="style.css">
	<script src="script.js"></script>
	<script src="jquery-1.11.3.min.js"></script>
	<script>
		$(document).ready(function () {
			$('.likebtn').click(function() {
				console.log("btn clicked!");
				$.post(window.location.href, {
					"opinion": "like",
					"movie_id": "123"
				}, function (raw_data) {
					var data = $.parseJSON(raw_data);
					console.log(data['movie_id']);
				});
			});	
		});
	</script>
	<title>Movies</title>
</head>
<body>
	<header>MovieTinder</header>
	<section class="flex">
		<div class="test">abcd</div>
		<div class="test2">
			<div class="testbtn likebtn">like</div>
			<div class="testbtn">nw</div>
			<div class="testbtn">dislike</div>
		</div>
	</section>
</body>
</html>