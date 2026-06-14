CREATE TABLE IF NOT EXISTS basics.app_events (
    -- UUID (Universally Unique Identifier) column named "event_id" that serves as the primary key
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_name TEXT NOT NULL,

    -- JSONB (Binary JSON) column named "event_data" to store structured data about the event
    metadata JSONB DEFAULT '{}'::JSONB,

    created_at TIMESTAMP DEFAULT NOW()
);


-- -- insert data into the table
-- INSERT INTO basics.app_events (event_name, metadata) VALUES
-- ('sign_up', '{"browser": "Chrome"}'),
-- ('sign_in', '{"user": "Bob Smith"}');


-- SELECT * FROM basics.app_events;

SELECT 
event_name,
metadata->>'browser' AS browser
FROM basics.app_events
WHERE metadata ? 'browser';