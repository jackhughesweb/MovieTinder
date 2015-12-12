<?php
if(isset($_POST["movie_id"])){
	?>

{
	"movie_id": "1234567890"
}

	<?php
}else{
	include('templates/header.php');
	include('templates/movies.php');
}
