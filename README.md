# CRUD DB

## setting
- 데이터베이스 생성

```
psql -U postgres # 윈도우
psql -d postgres # 맥

postgres=# CREATE DATABASE board OWNER sd4;
```

- UV 프로젝트 생성
```
uv init crud_db --bare --python 3.14

uv add "fastapi[standard]" sqlalchemy "psycopg[binary]"
```

## ORM vs SQL

- read
```
db.get(Post, 1)
=> SELECT * FROM posts WHERE id = 1;

```

- create
```
post = Post(title='hihi', content='hihihi')
db.add(post)
db.commit()

INSERT INTO posts (title, content) VALUES (hihi, hihihi); 
```
- update
```
post.title = 'hello'
db.commit()

```
- delete
```
db.delete(post)
db.commit()

```


