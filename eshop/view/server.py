from flask import Flask, request
from marshmallow import ValidationError
from werkzeug.exceptions import NotFound

from eshop.businsess_logic.order_usecases import order_create, order_get_many, order_get_by_id
from eshop.businsess_logic.product_usecases import product_create, \
    product_get_many, product_get_by_id
from eshop.view.order_schemas import OrderCreateDtoSchema, OrderSchema, \
    OrderGetManyParams, ProductCreateDtoSchema, ProductGetManyParams, \
    ProductSchema

app = Flask(__name__)


@app.post("/api/v1/order")
def order_create_endpoint():
    try:
        order_create_dto = OrderCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        order = order_create(
            product_ids=order_create_dto['product_ids']
        )
    except Exception as e:
        return {
            "error": str(e)
        }

    return OrderSchema().dump(order)


@app.get("/api/v1/order")
def order_get_many_endpoint():
    try:
        order_get_many_params = OrderGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    order = order_get_many(
        page=order_get_many_params['page'],
        limit=order_get_many_params['limit'],
    )

    return OrderSchema(many=True).dump(order)


@app.get("/api/v1/order/<id>")
def order_get_by_id_endpoint(id):
    order = order_get_by_id(id)

    if order is None:
        return {
            "error": 'Not found'
        }, 404

    return OrderSchema().dump(order)


@app.post("/api/v1/product")
def product_create_endpoint():
    try:
        product_dto = ProductCreateDtoSchema().load(request.json)
    except ValidationError as err:
        return err.messages, 400

    try:
        product = product_create(product_dto)
    except Exception as e:
        return {"error": str(e)}, 500

    return ProductSchema().dump(product), 201


@app.get("/api/v1/products")
def product_get_many_endpoint():
    try:
        params = ProductGetManyParams().load(request.args)
    except ValidationError as err:
        return err.messages, 400

    products = product_get_many(page=params['page'], limit=params['limit'])
    return ProductSchema(many=True).dump(products)


@app.get("/api/v1/product/<string:id>")
def product_get_by_id_endpoint(id):
    try:
        product = product_get_by_id(id)
        if product is None:
            raise NotFound(f"Product with id not found")
    except NotFound as e:
        return {"error": str(e)}, 404
    except Exception as e:
        return {"error": str(e)}, 500

    return ProductSchema().dump(product)


def run_server():
    app.run()
