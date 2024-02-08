-- Check if the table exists before creating it
CREATE TABLE IF NOT EXISTS users (
    -- Unique identifier for each user, auto-incremented
    id SERIAL PRIMARY KEY,
    -- Email of the user, must be unique and cannot be null
    email VARCHAR(255) NOT NULL UNIQUE,
    -- Name of the user, can be null
    name VARCHAR(255),
    -- Country of the user, enumeration with default value 'US'
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
