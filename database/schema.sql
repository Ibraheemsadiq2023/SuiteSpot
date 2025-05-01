-- SQLite schema for SuiteSpot

CREATE TABLE Customer (
    ref TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    mother TEXT,
    gender TEXT NOT NULL,
    post TEXT,
    mobile TEXT NOT NULL,
    email TEXT NOT NULL,
    nationality TEXT,
    idproof TEXT,
    idnumber TEXT,
    address TEXT
);

CREATE TABLE room (
    contact TEXT NOT NULL,
    checkin TEXT,
    checkout TEXT,
    room_type TEXT,
    roomno TEXT PRIMARY KEY,
    Meal TEXT,
    NoOfdays TEXT,
    paid_tax INTEGER,
    sub_total INTEGER,
    total INTEGER
);

CREATE TABLE Detail (
    Floor TEXT NOT NULL,
    Roomno TEXT NOT NULL UNIQUE,
    RoomType TEXT
);

CREATE TABLE register (
    fname TEXT NOT NULL,
    lname TEXT NOT NULL,
    contact TEXT NOT NULL,
    email TEXT NOT NULL,
    security_q TEXT NOT NULL,
    security_a TEXT NOT NULL,
    password TEXT NOT NULL
);
