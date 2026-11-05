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
```
