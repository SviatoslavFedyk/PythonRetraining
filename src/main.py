from src.data.reader import read_json_file
from serializers.beer_serializer import serialize_beer_class, serialize_beer_namedtuple, serialize_beer_dynamic_class

file_path = 'data/Beer_recipe_orignal.json'
serializer_method = None
def choose_exit(user_input):
    if not user_input or user_input.lower() == 'exit':
        print("Exiting")
        exit()
def choose_serializer():
    print("Choose a serializer method:")
    print("1. Class Serializer")
    print("2. NamedTuple Serializer")
    print("3. Dynamic Class Serializer")
    print("4. Exit")

    serializer_choice = input("Enter the number of your choice: ")

    serializer_methods = {
        '1': serialize_beer_class,
        '2': serialize_beer_namedtuple,
        '3': serialize_beer_dynamic_class,
        '4': exit
    }

    return serializer_methods.get(serializer_choice.lower(), None)


while not serializer_method:
    serializer_method = choose_serializer()
    if serializer_method is None:
        print("Invalid choice. Try again.")


beers = read_json_file(file_path, serializer_method)

while True:
    print('\n' * 80)
    for beer in beers:
        print(f'{beer.id}.{beer.name}')

    print('\n\nInput the ID of the beer (type "exit" to exit app or input "serializer" to choose different serializer):')
    input_id = input()
    choose_exit(input_id)

    if input_id.lower() == 'serializer':
        serializer_method = choose_serializer()
        if serializer_method is None:
            print("Invalid choice. Try again.")
    
        beers = read_json_file(file_path, serializer_method)
    else:
        try:
            input_id = int(input_id)
            selected_beer = next((beer for beer in beers if beer.id == input_id), None)

            if selected_beer:
                print(f'Name: {selected_beer.name}')
                print(f'Description: {selected_beer.description}')
                print('Press enter to continue (type "exit" to exit app):')
                user_input = input()
                choose_exit(user_input)
            else:
                print('Invalid beer ID. Press enter to continue (type "exit" to exit app):')
                user_input = input()
                choose_exit(user_input)
        except ValueError:
            print('Invalid input. Please enter a valid beer ID (type "exit" to exit app):')
            user_input = input()
            choose_exit(user_input)
