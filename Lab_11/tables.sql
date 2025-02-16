DROP TABLE IF EXISTS 'group';
DROP TABLE IF EXISTS 'student';
DROP TABLE IF EXISTS 'student_marks';
CREATE TABLE "group" (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255) UNIQUE,
  description VARCHAR(1023));
INSERT INTO 'group' VALUES(1,'PRO','Best of the best');
INSERT INTO 'group' VALUES(2,'Losers','NOT Best of the best');
CREATE TABLE student (
  id INTEGER PRIMARY KEY,
  name VARCHAR(255),
  group_id INTEGER REFERENCES "group" (id));
INSERT INTO 'student' VALUES(1,'Golikov',1);
INSERT INTO 'student' VALUES(2,'Volkov',1);
INSERT INTO 'student' VALUES(3,'Klopov',2);
INSERT INTO 'student' VALUES(4,'Tarakanov',2);
CREATE TABLE student_marks (
  student_id INTEGER REFERENCES student(id),
  math_mark_average FLOAT,
  physics_mark_average FLOAT,
  python_mark_average FLOAT);
INSERT INTO 'student_marks' VALUES(1,4.9,4.8,5);
INSERT INTO 'student_marks' VALUES(2,4,4.3,4.2);
INSERT INTO 'student_marks' VALUES(3,4,3.1,3.3);
INSERT INTO 'student_marks' VALUES(4,2,2.8,2);
