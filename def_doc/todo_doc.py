todo_list = {
    "parameters": [
        {
            "name": "title",
            "in": "query",
            "type": "string",
            "required": False,
            "default": None
        },
        {
            "name": "per_page",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": None
        },
        {
            "name": "page",
            "in": "query",
            "type": "integer",
            "required": False,
            "default": None
        }
    ],
    "definitions": {
        "Task": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "required": True,
                },
                "text": {
                    "type": "string",
                    "required": True,
                },
                "todo_id": {
                    "type": "integer",
                    "required": True,
                },
                "complete": {
                    "type": "boolean",
                    "required": True,
                    "default": False
                },
            }
        },
        "Todo": {
            "type": "object",
            "properties": {
                "id": {
                    "type": "integer",
                    "required": True,
                },
                "name": {
                    "type": "string",
                    "required": True,
                },
                "task_list": {
                    "type": "array",
                    "items": {
                        "$ref": "#/definitions/Task"
                    }
                }
            }
        },
    },
    "responses": {
        "200": {
            "description": "Список TODO элементов",
            "schema": {
                "type": "array",
                "items": {
                    "$ref": "#/definitions/Todo"
                }
            },
        }
    }
}
todo_get = {
    "parameters": [
        {
            "name": "todo_id",
            "in": "path",
            "type": "integer",
            "required": True,
            "default": None
        },
    ],
    "responses": {
        "200": {
            "description": "Элемент TODO",
            "schema": {
                "$ref": "#/definitions/Todo"
            },
        }
    }
}
todo_create = {
    "parameters": [{
        "name": "body",
        "in": "body",
        "required": True,
        "schema": {
            "id": "TodoCreate",
            "required": ["title", "task_list"],
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Заголовок группы задач",
                },
                "task_list": {
                    "type": "array",
                    "description": "Список задач",
                    "items": {
                        "type": "object",
                        "properties": {
                            "text": {
                                "type": "string",
                                "required": True,
                                "description": "Описание задачи",
                            },
                            "complete": {
                                "type": "boolean",
                                "description": "Флаг активности задачи",
                                "required": False,
                                "default": False,
                            },
                        }

                    }
                },
            },
        }
    }],
    "responses": {
        "200": {
            "description": "Элемент TODO",
            "schema": {
                "$ref": "#/definitions/Todo"
            },
        }
    },
}
