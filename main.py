from fastapi import FastAPI

from routes import main

app = FastAPI()

app.include_router(main.router, prefix="/api/v1")

# @app.get("/")
# def read_root(shop_client: ShopConnectionDepend):
#     try:
#         shop = ShopSchema(name="test shop", email='trungtdd@gmail.com', password='123123')
#         shop.save()
#     except ValidationError as e:
#         print(e)
#         raise HTTPException(400, e.message)
#     return {"Hello": "World"}
