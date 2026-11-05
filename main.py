from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

DB_URL = "postgresql+psycopg://sd4:sd4@localhost:5432/board"
engine = create_engine(DB_URL)
# engine = create_engine(DB_URL, echo=True)

class Base(DeclarativeBase):
    pass

class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.get('/')
def home():
    return {'hello': 'hi'}

@app.get('/posts')
def post_list(request: Request):
    with Session(engine) as db:
        posts = db.scalars(select(Post)).all()
        return templates.TemplateResponse(
            request=request,
            name='list.html',
            context={'posts': posts}
        )


@app.get('/posts/new')
def post_new(request: Request):
    return templates.TemplateResponse(
        request=request,
        name='new.html'
    )


@app.post('/posts/create')
def post_create(title: str = Form(), content: str = Form()):
    with Session(engine) as db:
        post = Post(title=title, content=content)
        # print(f'add 전 : {post.id}')
        db.add(post)
        # print(f'add 후 : {post.id}')
        db.commit()
        # print(f'commit 후 : {post.id}')

       
        # from fastapi.responses import RedirectResponse
        return RedirectResponse(f'/posts/{post.id}', status_code=303)

    
# /posts/new 와 동작이 겹쳐서 
# 우선순위를 낮추기 위해 아래로 이동
@app.get('/posts/{post_id}')
def post_detail(request: Request, post_id: int):
    with Session(engine) as db:
        post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail='게시물이 없어요')
        # return templates.TemplateResponse('error.html')

    return templates.TemplateResponse(
        request=request,
        name='detail.html',
        context={'post': post}
    )


@app.get('/posts/{post_id}/edit')
def post_edit(request: Request, post_id: int):
    with Session(engine) as db:
        post = db.get(Post, post_id)

    if post is None:
        raise HTTPException(status_code=404, detail='없는게시물')

    return templates.TemplateResponse(
        request=request,
        name='edit.html',
        context={'post': post}
    )


@app.post('/posts/{post_id}/update')
def post_update(post_id: int, title: str = Form(), content: str = Form()):
    with Session(engine) as db:
        post = db.get(Post, post_id)

        post.title = title
        post.content = content

        db.commit()

    return RedirectResponse(f'/posts/{post_id}', status_code=303)


@app.post('/posts/{post_id}/delete')
def post_delete(post_id: int):
    with Session(engine) as db:
        post = db.get(Post, post_id)
        db.delete(post)
        db.commit()

    return RedirectResponse('/posts', status_code=303)
