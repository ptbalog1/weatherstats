<?php

require_once 'connection.php';
$name = $_POST["name"];
$elevation = $_POST["elevation"];
$location = $_POST["location"];

$sql = "INSERT INTO cities(name,elevation,Location,temperature) 
        VALUES ('$name',$elevation,'$location',0)";


$stmt = mysqli_stmt_init($conn);

if (!mysqli_stmt_prepare($stmt,$sql) ) {
    die(mysqli_error($conn));
}


mysqli_stmt_execute($stmt);


echo "Data inserted.";

?>