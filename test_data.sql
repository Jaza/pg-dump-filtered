INSERT INTO world (name, created_at, updated_at, active, uuid, id) VALUES ('Krypton', '2015-06-01 09:00:00.000000', '2015-06-06 09:00:00.000000', true, '\x478a43577ebe4b07ba8631ca228ee42a', 1);
INSERT INTO world (name, created_at, updated_at, active, uuid, id) VALUES ('Romulus', '2015-06-01 10:00:00.000000', '2015-06-05 13:00:00.000000', true, '\x82e2c0ac3ba84a34a1ad3bbbb2063547', 2);

INSERT INTO country (name, created_at, updated_at, active, uuid, id, world_id, bigness) VALUES ('Crystalland', '2015-06-02 09:00:00.000000', '2015-06-08 09:00:00.000000', true, '\xcd0338cf2e3b40c3a3751b556a237152', 1, 1, 3.86);
INSERT INTO country (name, created_at, updated_at, active, uuid, id, world_id, bigness) VALUES ('Greenbloodland', '2015-06-03 11:00:00.000000', '2015-06-07 13:00:00.000000', true, '\x17591321d1634bcf986d0966a539c970', 2, 2, NULL);

INSERT INTO city (name, created_at, updated_at, active, uuid, id, country_id, weight, is_big, pseudonym, description) VALUES ('Kryptonopolis', '2015-06-05 09:00:00.000000', '2015-06-11 09:00:00.000000', true, '\x13659f9301d24ea4ae9c534d70285edc', 1, 1, 100, true, 'Pointyville', 'Nice place, once you get used to the pointiness.');

INSERT INTO city (name, created_at, updated_at, active, uuid, id, country_id, weight, is_big, pseudonym, description) VALUES ('Rom City', '2015-06-04 09:00:00.000000', '2015-06-13 09:00:00.000000', true, '\xc45a9fb0a92a43df91791b11d65f5096', 2, 2, 200, false, '', 'Gakkkhhhh!');

INSERT INTO person (name, created_at, updated_at, active, uuid, city_id, person_type) VALUES ('Superman', '2015-06-14 09:00:00.000000', '2015-06-15 22:00:00.000000', true, '\xbadd1ca153994deca0f78a5158215cf6', 1, 'Awesome Heroic Champ');
INSERT INTO person (name, created_at, updated_at, active, uuid, city_id, person_type) VALUES ('General Zod', '2015-06-14 10:00:00.000000', '2015-06-15 23:00:00.000000', true, '\x796031428b0a46c2a9391eb5dc45008a', 1, 'Bad Bloke');

INSERT INTO person (name, created_at, updated_at, active, uuid, city_id, person_type) VALUES ('Mister Funnyears', '2015-06-14 11:00:00.000000', '2015-06-15 22:30:00.000000', false, '\x22380f6dc82d47f488a58153215864cb', 2, 'Mediocre Dude');
INSERT INTO person (name, created_at, updated_at, active, uuid, city_id, person_type) VALUES ('Captain Greeny', '2015-06-15 05:00:00.000000', '2015-06-16 08:30:00.000000', true, '\x485e31758528425dbabc598caaf86fa4', 2, 'Weirdo');
