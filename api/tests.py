#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements. See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership. The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied. See the License for the
# specific language governing permissions and limitations
# under the License.
#

from django.test import TestCase
from rest_framework.test import APIClient

test_data = {
    "age": 22,
    "sex": "female",
    "job": 2,
    "housing": "own",
    "credit_amount": 5951,
    "duration": 48,
    "purpose": "radio/TV"
}

expected_output = 'bad'


class AlgorithmTests(TestCase):
    def test_predict_view(self):
        client = APIClient()

        classifier_url = "/api/v1/algorithms/predict?classifier=RandomForestClassifier&version=0.0.1"
        response = client.post(classifier_url, test_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["label"], expected_output)
        self.assertTrue("request_id" in response.data)
