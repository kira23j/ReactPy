from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

origins=[
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"] 
)

# get route
@app.get("/",tags=["root"])
async def read_root()->dict:
    return {"message":"welcome to fastapi"}


todos=[
    {"id":"1",
     "item":"something 1"
        },
  {"id":"2",
     "item":"something 2"
        },
  {"id":"3",
     "item":"something 3"
        }
]
# get todo route
@app.get("/todo",tags=["todos"])
async def get_todos()->dict:
    return {"data":todos}

# post route
@app.post("/todo",tags=["todos"])
async def add_todo(todo:dict)->dict:
    todos.append(todo)
    return {
        "data":{"Todo has been added!"}
    }
    
# put route
@app.put("/todo/{id}",tags=["todos"] )
async def update_todo(id:int,body:dict)->dict:
    for todo in todos:
        if int(todo["id"])==id:
            todo["item"]=body["item"]
            return {
                "data":f"Todo with id {id} has been updated"
            }
    return {
            "data":f"Todo with this {id} number has not been found!"
        }
        
