CREATE TABLE posts (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    title text NOT NULL,
    content text NOT NULL
);

INSERT INTO posts (title, content) VALUES
('my first post', 'hello!!'), 
('안녕하세요', '반갑습니다');