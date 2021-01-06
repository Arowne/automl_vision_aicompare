import requests


class AutoMLVisionClient():

    def __init__(self, *args, **kwargs):
        self.api_key = kwargs['api_key']
        self.server_url = 'http://0.0.0.0:8000/v1/'
        self.headers = {
                'Authorization': 'Bearer ' + self.api_key
            }

    def create_project(self, project_name=None, project_description=None):

            payload = {
                'name': project_name,
                'description': project_description
            }

            response = requests.post(
                self.server_url + 'automl/vision/project', data=payload, headers=self.headers)
            data = response.json()
            print(response.json())
            return data['project_id']

    def add_project_image(self, project_id=None, file_path=None):

            files = {
                'files': open(file_path, 'rb')
            }

            response = requests.post(self.server_url + 'automl/vision/image/' +
                                     project_id + '/project', files=files, headers=self.headers)
            data = response.json()
            return data['image_id']

    def add_project_tag(self, project_id=None, tag_name=None):

            payload = {
                'name': tag_name,
            }

            response = requests.post(self.server_url + 'automl/vision/tag/' +
                                     project_id + '/project', data=payload, headers=self.headers)
            data = response.json()

            return data['tag_id']

    def add_image_tag(self, image_id=None, tag_id=None):

            response = requests.get(self.server_url + 'automl/vision/tag/' +
                                    tag_id + '/image/' + image_id, headers=self.headers)
            data = response.json()

            return data['response']

    def train_project(self, project_id=None, training_name=None, training_time=None, provider=None):

            payload = {
                "training_name": training_name,
                "training_time": training_time,
                "provider": provider
            }

            response = requests.post(self.server_url + 'automl/vision/train/' +
                                     project_id + '/project', data=payload, headers=self.headers)
            data = response.json()
            print(data)

            return data['results'][0]['training_state']['train_id']

    def predict(self, provider=None, image_path=None, train_id=None, project_id=None):

            files = {
                'files': open(image_path, 'rb')
            }


            payload = {
                "provider": provider
            }

            response = requests.post(self.server_url + 'automl/vision/prediction/project/' +
                                     project_id  +'/train/' + train_id, data=payload, files=files, headers=self.headers)
            data = response.json()
            return data['results'][0]['predictions']
