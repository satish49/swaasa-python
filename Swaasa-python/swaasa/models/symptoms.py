# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class Symptoms(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Symptoms - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'cough_at_night': 'int',
            'frequent_cough': 'int',
            'pain_in_chest': 'int',
            'shortness_of_breath': 'int',
            'sputum': 'int',
            'wheezing': 'int'
        }

        self.attribute_map = {
            'cough_at_night': 'cough_at_night',
            'frequent_cough': 'frequent_cough',
            'pain_in_chest': 'pain_in_chest',
            'shortness_of_breath': 'shortness_of_breath',
            'sputum': 'sputum',
            'wheezing': 'wheezing'
        }

        self._cough_at_night = None
        self._frequent_cough = None
        self._pain_in_chest = None
        self._shortness_of_breath = None
        self._sputum = None
        self._wheezing = None

    @property
    def cough_at_night(self):
        """
        Gets the cough_at_night of this Symptoms.


        :return: The cough_at_night of this Symptoms.
        :rtype: int
        """
        return self._cough_at_night

    @cough_at_night.setter
    def cough_at_night(self, cough_at_night):
        """
        Sets the cough_at_night of this Symptoms.


        :param cough_at_night: The cough_at_night of this Symptoms.
        :type: int
        """
        self._cough_at_night = cough_at_night

    @property
    def frequent_cough(self):
        """
        Gets the frequent_cough of this Symptoms.


        :return: The frequent_cough of this Symptoms.
        :rtype: int
        """
        return self._frequent_cough

    @frequent_cough.setter
    def frequent_cough(self, frequent_cough):
        """
        Sets the frequent_cough of this Symptoms.


        :param frequent_cough: The frequent_cough of this Symptoms.
        :type: int
        """
        self._frequent_cough = frequent_cough

    @property
    def pain_in_chest(self):
        """
        Gets the pain_in_chest of this Symptoms.


        :return: The pain_in_chest of this Symptoms.
        :rtype: int
        """
        return self._pain_in_chest

    @pain_in_chest.setter
    def pain_in_chest(self, pain_in_chest):
        """
        Sets the pain_in_chest of this Symptoms.


        :param pain_in_chest: The pain_in_chest of this Symptoms.
        :type: int
        """
        self._pain_in_chest = pain_in_chest

    @property
    def shortness_of_breath(self):
        """
        Gets the shortness_of_breath of this Symptoms.


        :return: The shortness_of_breath of this Symptoms.
        :rtype: int
        """
        return self._shortness_of_breath

    @shortness_of_breath.setter
    def shortness_of_breath(self, shortness_of_breath):
        """
        Sets the shortness_of_breath of this Symptoms.


        :param shortness_of_breath: The shortness_of_breath of this Symptoms.
        :type: int
        """
        self._shortness_of_breath = shortness_of_breath

    @property
    def sputum(self):
        """
        Gets the sputum of this Symptoms.


        :return: The sputum of this Symptoms.
        :rtype: int
        """
        return self._sputum

    @sputum.setter
    def sputum(self, sputum):
        """
        Sets the sputum of this Symptoms.


        :param sputum: The sputum of this Symptoms.
        :type: int
        """
        self._sputum = sputum

    @property
    def wheezing(self):
        """
        Gets the wheezing of this Symptoms.


        :return: The wheezing of this Symptoms.
        :rtype: int
        """
        return self._wheezing

    @wheezing.setter
    def wheezing(self, wheezing):
        """
        Sets the wheezing of this Symptoms.


        :param wheezing: The wheezing of this Symptoms.
        :type: int
        """
        self._wheezing = wheezing

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other

