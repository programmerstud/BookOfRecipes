# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from logic.backend.swagger_server.models.base_model_ import Model
from logic.backend.swagger_server import util


class Recipe(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: int=None, title: str=None, category_id: int=None, image: str=None, recipe_text: str=None, author_id: int=None):  # noqa: E501
        """Recipe - a model defined in Swagger

        :param id: The id of this Recipe.  # noqa: E501
        :type id: int
        :param title: The title of this Recipe.  # noqa: E501
        :type title: str
        :param category_id: The category_id of this Recipe.  # noqa: E501
        :type category_id: int
        :param image: The image of this Recipe.  # noqa: E501
        :type image: str
        :param recipe_text: The recipe_text of this Recipe.  # noqa: E501
        :type recipe_text: str
        :param author_id: The author_id of this Recipe.  # noqa: E501
        :type author_id: int
        """
        self.swagger_types = {
            'id': int,
            'title': str,
            'category_id': int,
            'image': str,
            'recipe_text': str,
            'author_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'category_id': 'category_id',
            'image': 'image',
            'recipe_text': 'recipe_text',
            'author_id': 'author_id'
        }
        self._id = id
        self._title = title
        self._category_id = category_id
        self._image = image
        self._recipe_text = recipe_text
        self._author_id = author_id

    @classmethod
    def from_dict(cls, dikt) -> 'Recipe':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Recipe of this Recipe.  # noqa: E501
        :rtype: Recipe
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """Gets the id of this Recipe.


        :return: The id of this Recipe.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """Sets the id of this Recipe.


        :param id: The id of this Recipe.
        :type id: int
        """

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Recipe.


        :return: The title of this Recipe.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Recipe.


        :param title: The title of this Recipe.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def category_id(self) -> int:
        """Gets the category_id of this Recipe.


        :return: The category_id of this Recipe.
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id: int):
        """Sets the category_id of this Recipe.


        :param category_id: The category_id of this Recipe.
        :type category_id: int
        """
        if category_id is None:
            raise ValueError("Invalid value for `category_id`, must not be `None`")  # noqa: E501

        self._category_id = category_id

    @property
    def image(self) -> str:
        """Gets the image of this Recipe.


        :return: The image of this Recipe.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this Recipe.


        :param image: The image of this Recipe.
        :type image: str
        """
        if image is None:
            raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def recipe_text(self) -> str:
        """Gets the recipe_text of this Recipe.


        :return: The recipe_text of this Recipe.
        :rtype: str
        """
        return self._recipe_text

    @recipe_text.setter
    def recipe_text(self, recipe_text: str):
        """Sets the recipe_text of this Recipe.


        :param recipe_text: The recipe_text of this Recipe.
        :type recipe_text: str
        """
        if recipe_text is None:
            raise ValueError("Invalid value for `recipe_text`, must not be `None`")  # noqa: E501

        self._recipe_text = recipe_text

    @property
    def author_id(self) -> int:
        """Gets the author_id of this Recipe.


        :return: The author_id of this Recipe.
        :rtype: int
        """
        return self._author_id

    @author_id.setter
    def author_id(self, author_id: int):
        """Sets the author_id of this Recipe.


        :param author_id: The author_id of this Recipe.
        :type author_id: int
        """
        if author_id is None:
            raise ValueError("Invalid value for `author_id`, must not be `None`")  # noqa: E501

        self._author_id = author_id
