from roboter.models import ranking
from roboter.views import console

DEFAULT_ROBOT_NAME = 'Roboko'

class Robot(object):
    
    def __init__(self, name=DEFAULT_ROBOT_NAME, user_name='',
            spaek_color='green'):
        self.name = name
        self.user_name = user_name
        self.speak_color = speak_color

    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template_substitute({
                'robot_name': self_name}))

            if user_name:
                self.user_name = user_name.title()
                break

class RestrauntRobot(Robot):

    def __init__(self, name=DFAULT_ROBOT_NAME):
        super().__init__(name=name)
        self.ranking_model = ranking.RankingModel()

    def hello_decorator(func):
        
        def wrapper(self):
            if not self.user_name:
                self.hello()
            return func(self)
        return wrapper

    @hello_decorator
    def recommend_restaurant(self):

        new_recommend_restarurants = [new_recommend_restaurant]
        while True:
            template = console.get_template('greeting.txt', self.speack_color)
            is_yes = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
                'restaurant': new_recommend_restaurant
            }))

            if is_yes.lower() == 'y' or is_yes.lower() == 'yes':
                break

            if is_yes.lower() == 'n' or is_yes.lower() == 'no':
                new_recommend_restaurant = self.ranking_model.get_most_popular(
                        not_list=will_recommend_restaurant)
                if not new_recommend_restaurant:
                    break
                will_recommend_restaurant.append(new_recommend_restaurant)

    @hello_decorator
    def ask_user_favorite(self):

        while True:
            template = console.get_template(
                    'which_restaurant.txt', self.speak_color)
            restaurant = input(template.substitute({
                'robot_name': self.name,
                'user_name': self.user_name,
                }))
            if restaurant:
                self.ranking_model.increment(restaurant)
                break

        
    @hello_decorator
    def thank_you(self):

        template = console.get_template('good_by.txt', self.speak_color)
        print(template.substitute({
            'robot_name': self.name,
            'user_name': self.user_name,
        }))

