CREATE TABLE post (
	id INTEGER NOT NULL, 
	title VARCHAR(150), 
	content TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE question (
	id INTEGER NOT NULL, 
	content TEXT, 
	answer TEXT, 
	PRIMARY KEY (id)
);
