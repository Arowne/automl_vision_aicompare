import glob

from AutoMLVisionClient import AutoMLVisionClient


def train_project():
    
    # # Init class
    client = AutoMLVisionClient(api_key='')

    print('Project creation...')
    project_id = client.create_project(project_name='Floor plans classifier', project_description='Automaticaly count number of rooms')


    # Add tag
    print('Tag creation ...')
    three_rooms_id = client.add_project_tag(project_id=project_id, tag_name='3')
    four_rooms_id = client.add_project_tag(project_id=project_id, tag_name='4')
    five_rooms_id = client.add_project_tag(project_id=project_id, tag_name='5')
    

    tags = [three_rooms_id, four_rooms_id, five_rooms_id]
    
    print('Image importation ...')
    # Add upload and add tag image
    for index in range(3):
        current_folder = "floor_plan_dataset/" + str(index) +"/*"
        counter = 0
        for img in glob.glob(current_folder):
            counter += 1
            if counter > 100:
                break
            print(str(counter*(index+1)) + '/300', end="\r")
            image_id = client.add_project_image(project_id=project_id, file_path=img)
            response = client.add_image_tag(image_id=image_id, tag_id=tags[index])
            print(response)

    print('Launch train ...')
    print(project_id)
    # You can switch provider between microsoft, google_cloud or aws
    train_id = client.train_project(project_id=project_id, training_name='Room classification google train', training_time=8000, provider='microsoft')

    prediction = client.predict(provider="microsoft", project_id=train_id, train_id=project_id, image_path="floor_plan_dataset/0/Cat9_9.jpg", )
    print(prediction)

if __name__ == "__main__":
    train_project()
    pass
