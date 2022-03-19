import os

OPENAPI_URL = os.environ.get('OPENAPI_URL', '/route-openapi.json')
SERVICE_URL = os.environ.get('SERVICE_URL', '/route-service')

OPENAPI_SCHEMA = {
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "servers": [
        {
            "url": SERVICE_URL
        },
        {
            'url': '/'
        }
    ],
    "paths": {
        "/api/points": {
            "get": {
                "summary": "Get All",
                "operationId": "get_all_api_points_get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "Limit",
                            "type": "integer",
                            "default": 100
                        },
                        "name": "limit",
                        "in": "query"
                        },
                        {
                        "required": False,
                        "schema": {
                            "title": "Offset",
                            "type": "integer",
                            "default": 0
                        },
                        "name": "offset",
                        "in": "query"
                        }
                    ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Get All Api Points Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/PointDTO"
                                    }
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            },
            "post": {
                "summary": "Create",
                "operationId": "create_api_points_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/PointCreateDTO"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/PointFullDTO"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            }
        },
        "/api/points/{point_id}": {
            "get": {
                "summary": "Get By Id",
                "operationId": "get_by_id_api_points__point_id__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Point Id",
                            "type": "integer"
                        },
                        "name": "point_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/PointFullDTO"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            },
            "delete": {
                "summary": "Delete",
                "operationId": "delete_api_points__point_id__delete",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Point Id",
                            "type": "integer"
                        },
                        "name": "point_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            }
        },
        "/api/routes": {
            "get": {
                "summary": "Get All",
                "operationId": "get_all_api_routes_get",
                "parameters": [
                    {
                        "required": False,
                        "schema": {
                            "title": "User Id",
                            "type": "integer"
                        },
                        "name": "user_id",
                        "in": "query"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Get All Api Routes Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/RouteDTO"
                                    }
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            },
            "post": {
                "summary": "Create",
                "operationId": "create_api_routes_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/RouteCreateDTO"
                            }
                        }
                    },
                    "required": True
                },
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RouteFullDTO"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            }
        },
        "/api/routes/{route_id}": {
            "get": {
                "summary": "Get By Id",
                "operationId": "get_by_id_api_routes__route_id__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "Route Id",
                            "type": "integer"
                        },
                        "name": "route_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/RouteFullDTO"
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            }
        },
        "/api/routes/my": {
            "get": {
                "summary": "My Routes",
                "operationId": "my_routes_api_routes_my_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response My Routes Api Routes My Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/RouteFullDTO"
                                    }
                                }
                            }
                        }
                    },
                    "422": {
                        "description": "Validation Error",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/HTTPValidationError"
                                }
                            }
                        }
                    }
                },
                "security": [
                    {
                        "HTTPBearer": [

                        ]
                    }
                ]
            }
        }
    },
    "components": {
        "schemas": {
            "HTTPValidationError": {
                "title": "HTTPValidationError",
                "type": "object",
                "properties": {
                    "detail": {
                        "title": "Detail",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/ValidationError"
                        }
                    }
                }
            },
            "PointCreateDTO": {
                "title": "PointCreateDTO",
                "required": [
                    "title",
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "properties": {
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "latitude": {
                        "title": "Latitude",
                        "type": "number"
                    },
                    "longitude": {
                        "title": "Longitude",
                        "type": "number"
                    }
                }
            },
            "PointDTO": {
                "title": "PointDTO",
                "required": [
                    "id",
                    "title",
                    "latitude",
                    "longitude"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "latitude": {
                        "title": "Latitude",
                        "type": "number"
                    },
                    "longitude": {
                        "title": "Longitude",
                        "type": "number"
                    }
                }
            },
            "PointFullDTO": {
                "title": "PointFullDTO",
                "required": [
                    "id",
                    "title",
                    "latitude",
                    "longitude",
                    "deleted"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "latitude": {
                        "title": "Latitude",
                        "type": "number"
                    },
                    "longitude": {
                        "title": "Longitude",
                        "type": "number"
                    },
                    "deleted": {
                        "title": "Deleted",
                        "type": "boolean"
                    }
                }
            },
            "RouteCreateDTO": {
                "title": "RouteCreateDTO",
                "required": [
                    "title",
                    "start_point_id",
                    "end_point_id"
                ],
                "type": "object",
                "properties": {
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "start_point_id": {
                        "title": "Start Point Id",
                        "type": "integer"
                    },
                    "end_point_id": {
                        "title": "End Point Id",
                        "type": "integer"
                    }
                }
            },
            "RouteDTO": {
                "title": "RouteDTO",
                "required": [
                    "id",
                    "title",
                    "user_id"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "user_id": {
                        "title": "User Id",
                        "type": "integer"
                    }
                }
            },
            "RouteFullDTO": {
                "title": "RouteFullDTO",
                "required": [
                    "id",
                    "title",
                    "user_id",
                    "points"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "title": {
                        "title": "Title",
                        "type": "string"
                    },
                    "user_id": {
                        "title": "User Id",
                        "type": "integer"
                    },
                    "points": {
                        "title": "Points",
                        "type": "array",
                        "items": {
                            "$ref": "#/components/schemas/RoutePartDTO"
                        }
                    }
                }
            },
            "RoutePartDTO": {
                "title": "RoutePartDTO",
                "required": [
                    "point",
                    "order"
                ],
                "type": "object",
                "properties": {
                    "point": {
                        "$ref": "#/components/schemas/PointDTO"
                    },
                    "order": {
                        "title": "Order",
                        "type": "integer"
                    }
                }
            },
            "ValidationError": {
                "title": "ValidationError",
                "required": [
                    "loc",
                    "msg",
                    "type"
                ],
                "type": "object",
                "properties": {
                    "loc": {
                        "title": "Location",
                        "type": "array",
                        "items": {
                            "type": "string"
                        }
                    },
                    "msg": {
                        "title": "Message",
                        "type": "string"
                    },
                    "type": {
                        "title": "Error Type",
                        "type": "string"
                    }
                }
            }
        },
        "securitySchemes": {
            "HTTPBearer": {
                "type": "http",
                "scheme": "bearer"
            }
        }
    }
}
