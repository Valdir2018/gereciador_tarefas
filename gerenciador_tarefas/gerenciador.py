from  fastapi import FastAPI


app = FastAPI()

TAREFAS = [
    {
        "id": 1,
        "Titulo": "Titulo",
        "Descricao": "Descrição",
        "Estado": "Finalizado"
    },
    {
        "id": 2,
        "Titulo": "Titulo",
        "Descricao": "Descrição",
        "Estado": "Finalizado"
    }
]

@app.get("/tarefas")
def listar_tarefas():
    return TAREFAS