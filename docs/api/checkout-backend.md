# checkout_backend: API

As it was developed using DRF, you can access to `http://localhost:8000/api/` to interact with the API. Anyway, in the root of the project you can find a postman collection if you prefer it.

Supports:
- Create cart
- Delete cart
- Add product to cart
- Remove product from cart

## Create cart

**Request**:

`POST` `http://localhost:8000/api/cart/`

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created

{
    "cart": {
        "id": "12459c7a-32f6-445c-aeff-e619281c6e7b",
        "items": []
    },
    "total_amount": "0,00 €"
}
```

## Delete cart

**Request**:

`DELETE` `http://localhost:8000/api/cart/:cart_id/delete/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
cart_id      | string | Yes      | Cart id to be deleted

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK
```

## Add product to cart

**Request**:

`POST` `http://localhost:8000/api/cart/:cart_id/add-product/:product_code/`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
cart_id          | string | Yes      | Cart_id to interact
product_code     | string | Yes      | Product code to be added to the cart

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "cart": {
        "id": "12459c7a-32f6-445c-aeff-e619281c6e7b",
        "items": [
            {
                "product": {
                    "id": "1",
                    "code": "PEN",
                    "name": "Lana Pen",
                    "price": "5,00 €"
                },
                "quantity": ""
            }
        ]
    },
    "total_amount": "5,00 €"
}
```

## Remove product from cart

**Request**:

`DELETE` `http://localhost:8000/api/cart/:cart_id/remove-product/:product_code/`

Parameters:

Name             | Type   | Required | Description
-----------------|--------|----------|------------
cart_id          | string | Yes      | Cart_id to interact
product_code     | string | Yes      | Product code to be removed from the cart

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "cart": {
        "id": "12459c7a-32f6-445c-aeff-e619281c6e7b",
        "items": [
            {
                "product": {
                    "id": "1",
                    "code": "PEN",
                    "name": "Lana Pen",
                    "price": "5,00 €"
                },
                "quantity": "1"
            }
        ]
    },
    "total_amount": "5,00 €"
}
```