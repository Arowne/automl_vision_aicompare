import glob

from AutoMLVisionClient import AutoMLVisionClient



def train_project():
    
    # Init class
    client = AutoMLVisionClient(api_key='api_key')
    counter = 0

    print('Project creation...')
    project_id = client.create_project(project_name='Floor plans classifier', project_description='Automaticaly count number of rooms')


    # Add tag
    print('Tag creation ...')
    four_rooms_id = client.add_project_tag(project_id=project_id, tag_name='4')
    five_rooms_id = client.add_project_tag(project_id=project_id, tag_name='5')
    six_rooms_id = client.add_project_tag(project_id=project_id, tag_name='6')
    

    tags = [four_rooms_id, five_rooms_id, six_rooms_id]
    
    print('Image importation ...')
    # Add upload and add tag image
    for index in range(3):
        current_folder = "floor_plan_dataset/" + str(index) +"/*"

        for img in glob.glob(current_folder):
            counter += 1
            print(str(counter) + '/500', end="\r")
            image_id = client.add_project_image(project_id=project_id, file_path=img)
            response = client.add_image_tag(image_id=image_id, tag_id=tags[index])
            print(response)

    print('Launch train ...')
    print(project_id)
    response = client.train_project(project_id=project_id, training_name='Google train', training_time=1000, provider='google_cloud')
    print(response)

if __name__ == "__main__":
    train_project()
    pass