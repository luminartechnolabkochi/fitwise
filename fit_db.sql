create database fitwise_db;

use fitwise_db;


CREATE TABLE food_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    meal_type ENUM('break_fast', 'lunch', 'snacks', 'dinner') NOT NULL,
    calories DECIMAL(8,2) NOT NULL,
    serving_size VARCHAR(50) NOT NULL,
    consumed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    owner varchar(200) not null
);


create database codebenchv2_db;
