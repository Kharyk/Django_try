import django_setup

from game.models import User, Category, Product, Players, Games, MyModel

#user1 = User(name="Alina",
#             bio='...',
#             email='alina@gmail.com',
#             birthday="2009-03-10"
#             )
#user2 = User(name="Oleg",
#             bio='...',
#             email='oleg@gmail.com',
#             birthday="2008-04-12"
#             )

#user1.save()
#user2.save()

#user = User.objects.filter(id=1).all()#user = User.objects.get(id=1)
#print(user)
#print(user[0],email)

#not_needed_user = User.objects.get(id=2)
#not_needed_user.delete()

#user_to_update = User.objects.get(id=1)
#user_to_update.name = "Another name"
#user_to_update.bio = "I love sleep"
#user_to_update.email = "test@gmail.com"
#user_to_update.save()

#users = User.objects.all()
#for user in users:
#    print(user.email)

#fantastic_category = Category(name = "fantastic games")
#fantastic_category.save()

#new_product = Product(
#    name = "Mortal Kombat 1",
#    price = 19.99,
#    description = "...",
#    category =fantastic_category ,
#).save()

#product = Product.objects.filter(id=1).first()
#print(product.name)
#print(product.category.name)

#category = Category.objects.get(id=1)
#print(callable.product_set.all())

Players(name="Cat123").save()
Players(name="Fish123").save()

Games(title="Snake").save()
Games(title="Pin-Pong").save()

player_1  = Players.objects.get(id=1)
player_2  = Players.objects.get(id=2)

game_1  = Games.objects.get(id=1)
game_2  = Games.objects.get(id=2)

player_1.games.add(game_1)
player_1.games.add(game_2)

player_2.games.add(game_1)
player_2.games.add(game_2)

print(player_1.games.all())
pritn(game_1.players_settings.all())


MyModel.objects.create(
    short_text="asdfgh",
    long_text = "dhcfvg4587879yougifzew46e57idtu",
    number = 2344,
    float_numder=18.88,
    date = '2024-06-12',
    #date_time= "2024-06-12 22:25",
    related= game_1,
    
)