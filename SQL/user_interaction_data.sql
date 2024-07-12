-- schema for storing user interaction data in a SQL database 
CREATE TABLE user_interactions (
    interaction_id SERIAL PRIMARY KEY,
    user_id INT,
    product_id INT,
    action VARCHAR(255),
    timestamp TIMESTAMP,
    interaction_count INT
);

-- sample Data insertion
INSERT INTO user_interactions (user_id, product_id, action, timestamp, interaction_count)
VALUES
(101, 1001, 'click', '2023-07-11 12:35:10', 5),
(102, 1002, 'view', '2023-07-11 12:35:10', 3),
(103, 1003, 'purchase', '2023-07-11 12:35:24', 2),
(101, 1001, 'view', '2023-07-11 12:35:38', 5),
(102, 1002, 'click', '2023-07-11 12:35:52', 3),
(104, 1004, 'view', '2023-07-11 12:36:06', 4),
(104, 1002, 'purchase', '2023-07-11 12:36:20', 2),
(105, 1001, 'click', '2023-07-11 12:36:48', 3),
(103, 1004, 'purchase', '2023-07-11 12:38:12', 1),
(105, 1002, 'purchase', '2023-07-11 12:38:33', 2),
(105, 1001, 'click', '2023-07-11 12:38:40', 3);


-- Total number of interation per day 
SELECT 
    DATE(timestamp) AS interaction_date,
    COUNT(*) AS total_interactions
FROM 
    user_interactions
GROUP BY 
    DATE(timestamp)
ORDER BY 
    interaction_date;


-- Top 5 users by the number of interactions
SELECT 
    user_id,
    COUNT(*) AS interaction_count
FROM 
    user_interactions
GROUP BY 
    user_id
ORDER BY 
    interaction_count DESC
LIMIT 5;

-- Most interacted products based on the number of interactions 
SELECT 
    product_id,
    COUNT(*) AS interaction_count
FROM 
    user_interactions
GROUP BY 
    product_id
ORDER BY 
    interaction_count DESC;


-- Create indexes on frequently used columns to speed up query execution.
CREATE INDEX idx_user_id ON user_interactions(user_id);
CREATE INDEX idx_product_id ON user_interactions(product_id);
CREATE INDEX idx_timestamp ON user_interactions(timestamp);

