from user import User
from card import Card

Ivan = User("Ivan")

Ivan.sayName()
Ivan.setAge(33)
Ivan.sayAge()

card = Card("2589 2589 3214 5287", "11/28", "Ivan P")

Ivan.addCard(card)
Ivan.getCard().pay(1000)







