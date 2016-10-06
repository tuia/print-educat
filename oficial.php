<?php
include('arrays.php');
?>
<!DOCTYPE html>
<head>

	<meta charset="utf-8">
</head>
<body>
<form action="index.php" method="get">
<?php

 $id = 0;

foreach($alunos as $key => $value)
	{
		
        echo "<br>".$key.', '.$value;
		ECHO "<input type='submit' name='butao' value='$id'>";
		
		$id++;


    }
   

?>
</form>

</body>
</html>