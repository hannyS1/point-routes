import os

OPENAPI_URL = os.environ.get('OPENAPI_URL', '/auth-openapi.json')
SERVICE_URL = os.environ.get('SERVICE_URL', '/auth-service')

OPENAPI_SCHEMA = {
    "openapi": "3.0.2",
    "info": {
        "title": "FastAPI",
        "version": "0.1.0"
    },
    "servers": [
        {
            "url": SERVICE_URL,
        },
        {
            "url": '/'
        }
    ],
    "paths": {
        "/api/jwt/signin": {
            "post": {
                "summary": "Signin",
                "operationId": "signin_api_jwt_signin_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AuthDataDTO"
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
                }
            }
        },
        "/api/jwt/signup": {
            "post": {
                "summary": "Signup",
                "operationId": "signup_api_jwt_signup_post",
                "requestBody": {
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/AuthDataDTO"
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
                }
            }
        },
        "/api/jwt/refresh": {
            "get": {
                "summary": "Refresh Token",
                "operationId": "refresh_token_api_jwt_refresh_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

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
        "/api/jwt/check-auth": {
            "get": {
                "summary": "Check Auth Middleware",
                "operationId": "check_auth_middleware_api_jwt_check_auth_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {

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
        "/api/users": {
            "get": {
                "summary": "Get All",
                "operationId": "get_all_api_users_get",
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "title": "Response Get All Api Users Get",
                                    "type": "array",
                                    "items": {
                                        "$ref": "#/components/schemas/UserDTO"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "/api/users/{user_id}": {
            "get": {
                "summary": "Get By Id",
                "operationId": "get_by_id_api_users__user_id__get",
                "parameters": [
                    {
                        "required": True,
                        "schema": {
                            "title": "User Id",
                            "type": "integer"
                        },
                        "name": "user_id",
                        "in": "path"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Successful Response",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "$ref": "#/components/schemas/UserDTO"
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
                }
            }
        }
    },
    "components": {
        "schemas": {
            "AuthDataDTO": {
                "title": "AuthDataDTO",
                "required": [
                    "username",
                    "password"
                ],
                "type": "object",
                "properties": {
                    "username": {
                        "title": "Username",
                        "type": "string"
                    },
                    "password": {
                        "title": "Password",
                        "type": "string"
                    }
                }
            },
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
            "UserDTO": {
                "title": "UserDTO",
                "required": [
                    "id",
                    "username"
                ],
                "type": "object",
                "properties": {
                    "id": {
                        "title": "Id",
                        "type": "integer"
                    },
                    "username": {
                        "title": "Username",
                        "type": "string"
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