<?php 

    require_once 

?>



<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <title>WeatherStats</title>
        <link rel="stylesheet" href="../styles/styles.css">
        <h1><a href="../php/index.php">Results</a></h1>
        
    </head>
    <body>
        
       
    
    

    <div class="container" style="
    margin-top: 0px;">
        
            <?php

        $command = escapeshellcmd('C:\Users\Tatinko\PycharmProjects\rainNotifier\main.py');
        $command = escapeshellcmd('C:\Users\Tatinko\PycharmProjects\rainNotifier\dbconn.py');
   
        // Retrieve the user input from the form
        $user_input = $_POST['name'];

        // Create a MySQL connection
        $servername = "localhost";
                $username = "root";
                $password = "";
                $dbname = "weather";
                $conn = new mysqli($servername, $username, $password, $dbname);

        // Check connection
        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        // Use the user input in a MySQL query
        $sql = "SELECT name,elevation,Location,temperature FROM cities WHERE name = '$user_input'";
        $result = $conn->query($sql);
        ?>

        <main>
        <?php
            if ($result->num_rows > 0) {
                // Display or use the retrieved data
                while ($row = $result->fetch_assoc()) {
        ?>   
                <div class="card">
                    <div class="cityname">
                        <p><?php echo $row["name"]; ?></p>   
                    </div>
                    <div class="detail">
                        <p>City name:<?php echo $row["name"]; ?></p>
                    </div>
                </div>
        
        
        <?php
                                                }
            } else {
                echo "No results found.";
               }
        $conn->close();
        ?>
        
            </main> 
    </div>
    </body>
</html>


