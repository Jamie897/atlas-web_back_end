-- Ensure that the table is created only if it doesn't exist
CREATE TABLE IF NOT EXISTS users (
    -- Define the id column as an auto-incrementing primary key
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    -- Define the email column as a string with a maximum length of 255 characters, not nullable, and with a unique constraint
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Define the name column as a string with a maximum length of 255 characters
    name VARCHAR(255)
);
