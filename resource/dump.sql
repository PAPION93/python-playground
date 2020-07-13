BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdate text);
INSERT INTO "users" VALUES(1,'Jun','test@naver.com','000111','test.com','2020-07-13 23:39:31');
INSERT INTO "users" VALUES(2,'Son','email@eaf','010-2345-1234','.com','2020-07-13 23:39:31');
INSERT INTO "users" VALUES(3,'lee1','lee1@naver.com','010-1234-1231','lee1.com','2020-07-13 23:39:31');
INSERT INTO "users" VALUES(4,'lee2','lee2@naver.com','010-1234-1232','lee2.com','2020-07-13 23:39:31');
INSERT INTO "users" VALUES(5,'lee3','lee3@naver.com','010-1234-1233','lee3.com','2020-07-13 23:39:31');
COMMIT;
