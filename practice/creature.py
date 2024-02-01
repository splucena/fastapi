from data_grouping import Creature, get_creatures
from fastapi import FastAPI


app = FastAPI()


@app.get("/creature")
def get_all_creature() -> list[Creature]:
    return get_creatures()
