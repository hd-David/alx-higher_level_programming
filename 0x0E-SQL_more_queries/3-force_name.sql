-- Create the force_name table if it doesn't already exist
CREATE TABLE IF NOT EXISTS force_name (
    id INT AUTO_INCREMENT PRIMARY KEY, -- An auto-incremented integer for the primary key
    name VARCHAR(256) NOT NULL -- A non-null VARCHAR(256) column for names
);
