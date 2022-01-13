from fastapi import FastAPI

app = FastAPI()

food_items = {
    'indian': ['dosa', 'shahi paneer'],
    'italian': ['pizza', 'pasta'],
    'mexican': ['qusadila', 'burrito'],
}

@app.get('/get_items/{cuisine}')
async def items(cuisine):
    return f'Your order: {food_items[cuisine]}'