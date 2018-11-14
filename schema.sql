-- todo/schema.sql

DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id integer primary key autoincrement, -- unical ID
    zadanie text not null, -- task description
    zrobione boolean not null, -- information if task is complete or not
    data_pub datetime not null -- date when added
);

-- example data
INSERT INTO zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Wyrzucić śmieci', 0, datetime(current_timestamp));
INSERT into zadania (id, zadanie, zrobione, data_pub)
VALUES (null, 'Nakarmić psa', 0, datetime(current_timestamp));
