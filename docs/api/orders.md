# Orders: API

## Index

- [Specs](/README.md) 
- [Instructions](/docs/instructions.md) 
- [How it was developed](/docs/how-it-was-developed.md) 
- [API doc](/docs/api/orders.md) 

## Overview

As it was developed using DRF, you can access to `http://localhost:8000/api/` to interact with the API.

Supports:
- Get orders
- Get order
- Create order
- Delete order
- Create order line
- Delete order line

## Get orders

**Request**:

`GET` `http://localhost:8000/api/v1/orders/`

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

[
    {
        "id": "83c07bad-c888-45df-b846-d34e23d4bcd9",
        "lines": [
            {
                "id": "a7f1b94c-a604-4db4-8156-389224fd5e7e",
                "product_id": "30268bd4-62c0-40ca-b7d6-44677fe4e028",
                "product_name": "Patatas",
                "product_base_price": 2.0,
                "product_options": [
                    {
                        "id": "d7f729a5-4505-4c42-b53e-4bbffd322a4c",
                        "label": "Tipo",
                        "values": [
                            "Deluxe",
                            "Gajo",
                            "De la abuela"
                        ],
                        "stock": true,
                        "extra_price": 0.0,
                        "value": "Deluxe"
                    },
                    {
                        "id": "d0d23894-7446-49d0-b411-5aff61d1a18a",
                        "label": "Tamaño",
                        "values": [
                            "Grandes"
                        ],
                        "stock": true,
                        "extra_price": 2.5,
                        "value": "Grandes"
                    }
                ],
                "subproducts": [],
                "subtotal": 4.5
            }
        ],
        "offer_id": null,
        "offer_name": null,
        "total": 4.5,
        "created_at": "2020-11-15T08:31:22.977423Z"
    }
]
```

## Get order

**Request**:

`GET` `http://localhost:8000/api/v1/orders/<str:order_uuid>/`

Parameters:

Name              | Type   | Required | Description
------------------|--------|----------|------------
order_uuid        |  uuid  | Yes      | Order id

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK

{
    "id": "83c07bad-c888-45df-b846-d34e23d4bcd9",
    "lines": [
        {
            "id": "a7f1b94c-a604-4db4-8156-389224fd5e7e",
            "product_id": "30268bd4-62c0-40ca-b7d6-44677fe4e028",
            "product_name": "Patatas",
            "product_base_price": 2.0,
            "product_options": [
                {
                    "id": "d7f729a5-4505-4c42-b53e-4bbffd322a4c",
                    "label": "Tipo",
                    "values": [
                        "Deluxe",
                        "Gajo",
                        "De la abuela"
                    ],
                    "stock": true,
                    "extra_price": 0.0,
                    "value": "Deluxe"
                },
                {
                    "id": "d0d23894-7446-49d0-b411-5aff61d1a18a",
                    "label": "Tamaño",
                    "values": [
                        "Grandes"
                    ],
                    "stock": true,
                    "extra_price": 2.5,
                    "value": "Grandes"
                }
            ],
            "subproducts": [],
            "subtotal": 4.5
        }
    ],
    "offer_id": null,
    "offer_name": null,
    "total": 4.5,
    "created_at": "2020-11-15T08:31:22.977423Z"
}
```

## Create order

**Request**:

`POST` `http://localhost:8000/api/v1/orders/<str:order_uuid>/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
order_uuid   |  uuid  | Yes      | Order id to be created

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
201 Created
```

## Delete order

**Request**:

`DELETE` `http://localhost:8000/api/v1/orders/<str:order_uuid>/`

Parameters:

Name         | Type   | Required | Description
-------------|--------|----------|------------
order_uuid   |  uuid  | Yes      | Order id to be created

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK
```

## Create order line

**Request**:

`POST` `http://localhost:8000/api/v1/orders/<str:order_uuid>/<str:order_line_uuid>/`

Parameters:

Name              | Type   | Required | Description
------------------|--------|----------|------------
order_uuid        |  uuid  | Yes      | Order id
order_line_uuid   |  uuid  | Yes      | Order line id to be created

*Note:*

- Not Authorization Protected

**Request payload:**

```json
Content-Type application/json

{
    "product_id": "12459c7a-32f6-445c-aeff-e619281c6e7b",
    "product_options": [
        {
            "product_option_id": "14689c7a-32f6-095c-aeff-e619121c6e7b",
            "value": "Grandes",
        }
    ],
    "subproducts": [
        {
            "subproduct_id": "15679c7a-32f6-565c-aeff-e6567281c6e7b",
            "subproduct_options": [
                {
                    "product_option_id": "14689c7a-32f6-095c-aeff-e619121c6e7b",
                    "value": "Mediano",
                }
            ]
        }
    ]
}
```

**Response**:

```json
Content-Type application/json
201 OK
```

## Delete order line

**Request**:

`DELETE` `http://localhost:8000/api/v1/orders/<str:order_uuid>/<str:order_line_uuid>/`

Parameters:

Name              | Type   | Required | Description
------------------|--------|----------|------------
order_uuid        |  uuid  | Yes      | Order id
order_line_uuid   |  uuid  | Yes      | Order line id to be created

*Note:*

- Not Authorization Protected

**Response**:

```json
Content-Type application/json
200 OK
```
