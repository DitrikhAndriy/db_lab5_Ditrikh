DO $$
BEGIN
    FOR i IN 1..20 LOOP
    	INSERT INTO Animation_studio (studio_id, founded, country, name) VALUES (i, '2023.12.14', 'test' || i, 'test' || i);
    END LOOP;
END $$;

-- select * from animation_studio;
-- delete from animation_studio
-- where founded='2023.12.14';
-- select * from animation_studio;