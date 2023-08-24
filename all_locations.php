<?php 

    require_once 'connection.php';
    $sql = "SELECT name,elevation,Location,temperature FROM cities";
    $result = $conn->query($sql);

?>

<!DOCTYPE html>
<html>
    <head>
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <title>WeatherStats</title>
        <link rel="stylesheet" href="../styles/styles.css">
        
        
    </head>
    <body>
        
        <main>
            <div class="container">
            <div class="tit">
                <h1><a href="index.php">All locations</a></h1>   
            </div>
                <div class="cards">
                    <?php
                        // Display or use the retrieved data
                        while ($row = $result->fetch_assoc()) {
                    ?>   
                        <div class="card">
                            <div class="cityname">
                                <p><?php echo $row["name"]; ?></p>   
                            </div>
                            <div class="detail">
                                <p>City name: <?php echo $row["name"]; ?></p>
                                <p>Elevation: <?php echo $row["elevation"]; ?> m n. m.</p>
                                <p>Location: <?php echo $row["Location"]; ?></p>
                                <p>Temperature: <?php echo $row["temperature"]; ?>°C</p>
                            </div>
                        </div>
                    
                    
                    <?php
                        }
                    ?>
                </div>    
            </div>
        </main> 
    </body>
</html>
