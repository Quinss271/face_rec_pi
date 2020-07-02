<!DOCTYPE html>
<html>
<body>

<h2>HTML Forms</h2>

<form action="add.php" method="POST">
  First name:<br>
  <input type="text" name="fio" id="fio">
  <br>
  Select a file: <input type="file" name="image" id="image">
  <input type="submit" value="Submit">
</form> 
<?php
$conn = mysqli_connect("localhost","pi","12","verify_pi");
$sql = "SELECT MAX(id) FROM `verify_pi`"
res = mysqli_query($conn, $sql);
n_id = res[0]+1
if (mysqli_query($conn, $sql)) {
    print_r("New record created successfully". $n_id) ;
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

mysqli_close($conn);
?>
</body>
</html>
