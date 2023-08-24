<html>
    <head>
        <meta name="viewport" content="width-device-width, initial-scale=1.0">
        <title>WeatherStats</title>
        <link rel="stylesheet" href="../styles/styles.css">

        
        
    </head>
    <body>
        
        <div class="container">
            <div class="tit">
                <h1><a href="index.php">Add location</a></h1>   
            </div>
            <div class="form">
                <form   method="post">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name">

                    <label for="elevation">Elevation:</label>
                    <input type="text" id="elevation" name="elevation">

                    <label for="location">Location:</label>
                    <input type="text" id="location" name="location">

                    <br><button type="submit">ADD</button>
                </form>
            </div>
            <div class="avail">
                <p><a href="all_locations.php">All locations</a></p>
            </div>
        </div>

        <?php

        require_once 'connection.php';
        $name = $_POST["name"];
        $elevation = $_POST["elevation"];
        $location = $_POST["location"];

        $sql = "INSERT INTO cities(name,elevation,Location,temperature,stormdays) 
                VALUES ('$name',$elevation,'$location',0,0)";


        $stmt = mysqli_stmt_init($conn);

        if (!mysqli_stmt_prepare($stmt,$sql) ) {
            die(mysqli_error($conn));
        }


        mysqli_stmt_execute($stmt);


        ?>

    </body>
</html>