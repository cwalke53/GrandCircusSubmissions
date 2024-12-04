from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI()

# Example facts database
facts = [
    {"id": 12, "fact": "The Governor of Moscow trained a large bear to serve pepper Vodka to his guests."},
    {"id": 22, "fact": "Canadian Northwest Territories License plates are shaped like polar bears."},
]

# Pydantic model for new facts
class Fact(BaseModel):
    id: int
    fact: str

@app.get("/fact")
async def get_fact(id: int = None):
    
   
        return random.choice(facts)

@app.get("/fact/{id}")
async def get_fact_by_path(id: int):
@app.post("/fact")


async def add_fact(new_fact: Fact):
  
    new_id = max(f["id"] for f in facts) + 1 if facts else 1
    fact_obj = {"id": new_id, "fact": new_fact.fact}
    facts.append(fact_obj)
    return fact_obj



