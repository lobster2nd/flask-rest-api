from marshmallow import Schema, fields


class OrderCreateDtoSchema(Schema):
    product_ids = fields.List(fields.Str(), required=True)


class OrderSchema(Schema):
    id = fields.String()
    product_ids = fields.List(fields.Str())
    total = fields.Float()


class OrderGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)


class ProductGetManyParams(Schema):
    page = fields.Int(missing=0)
    limit = fields.Int(missing=10)


class ProductCreateDtoSchema(Schema):
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductSchema(Schema):
    id = fields.String()
    name = fields.String()
    price = fields.Float()
