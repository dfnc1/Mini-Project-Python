from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter(prefix="/post", tags=["post"])

@router.get("/todos")
async def get_todos():
    return "get_all_todos"

@router.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    return f"get_todo {todo_id}"

@router.post("/todos")
async def add_todo(todo: str):
    return todo

@router.patch("/todos/{todo_id}")
async def update_todo(todo_id: int):
    return f"updated{todo_id}"

@router.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    return f"deleted{todo_id}"