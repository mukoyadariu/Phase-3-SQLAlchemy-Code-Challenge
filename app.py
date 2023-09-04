from model import Restaurant, Customer, Review, session
from sqlalchemy.orm.exc import NoResultFound

def create_sample_data():
    restaurant_a = Restaurant(name="Restaurant A", price=3)
    restaurant_b = Restaurant(name="Restaurant B", price=2)
    customer_john = Customer(first_name="John", last_name="Doe")
    customer_jane = Customer(first_name="Jane", last_name="Smith")
    review1 = Review(customer=customer_john, restaurant=restaurant_a, star_rating=5)
    review2 = Review(customer=customer_john, restaurant=restaurant_b, star_rating=4)
    review3 = Review(customer=customer_jane, restaurant=restaurant_a, star_rating=3)



session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2, review3])
session.commit()
def get_fanciest_restaurant():
    fanciest_restaurant = Restaurant.fanciest(session)
    return fanciest_restaurant

def get_reviews_for_restaurant(restaurant_name):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if restaurant:
        return restaurant.all_reviews()
    else:
        return []

def create_new_customer(first_name, last_name):
    new_customer = Customer(first_name=first_name, last_name=last_name)
    session.add(new_customer)
    session.commit()

def add_review_for_restaurant(customer_id, restaurant_name, star_rating):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if restaurant:
        customer = session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            new_review = Review(customer=customer, restaurant=restaurant, star_rating=star_rating)
            session.add(new_review)
            session.commit()
            return True
    return False

def find_favorite_restaurant(customer_id):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        return customer.favorite_restaurant(session)
    return None

def delete_reviews_by_customer_for_restaurant(customer_id, restaurant_name):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if customer and restaurant:
        customer.delete_reviews(session, restaurant)
        session.commit()

def has_customer_reviewed_restaurant(customer_id, restaurant_name):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if customer and restaurant:
        return session.query(Review).filter(
            Review.customer_id == customer.id,
            Review.restaurant_id == restaurant.id
        ).first() is not None
    return False

def get_customers_for_restaurant(restaurant_name):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if restaurant:
        return restaurant.customers()
    return []

def update_customer_name(customer_id, new_first_name):
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        customer.first_name = new_first_name
        session.commit()

def get_review_count_for_restaurant(restaurant_name):
    restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
    if restaurant:
        return session.query(Review).filter_by(restaurant_id=restaurant.id).count()
    return 0

if name == "main":
    create_sample_data()
    fanciest_restaurant = get_fanciest_restaurant()
    print(f"Fanciest restaurant: {fanciest_restaurant.name}")

reviews_for_restaurant1 = get_reviews_for_restaurant("Restaurant A")
print("Reviews for Restaurant A:")
for review in reviews_for_restaurant1:
    print(review)

create_new_customer("Alice", "Johnson")
add_review_result = add_review_for_restaurant(5, "Restaurant A", 4)
if add_review_result:
    print("Added review for Restaurant A")
else:
    print("Restaurant A does not exist or the customer was not found.")

favorite_restaurant = find_favorite_restaurant(4)
if favorite_restaurant:
    print(f"Favorite restaurant for Jane Smith: {favorite_restaurant.name}")
else:
    print("Jane Smith has not reviewed any restaurants yet.")

delete_reviews_by_customer_for_restaurant(3, "Restaurant A")
has_reviewed = has_customer_reviewed_restaurant(3, "Restaurant A")
if not has_reviewed:
    print("Reviews by John Doe for Restaurant A were deleted")

has_reviewed = has_customer_reviewed_restaurant(5, "Restaurant A")
if has_reviewed:
    print("Alice Johnson has reviewed Restaurant A.")
else:
    print("Alice Johnson has not reviewed Restaurant A.")

customers_for_restaurant2 = get_customers_for_restaurant("Restaurant B")
print("Customers who have reviewed Restaurant B:")
for customer in customers_for_restaurant2:
    print(customer.full_name())

update_customer_name(1, "Johnathan")
print("Updated customer's first name to Johnathan")

review_count = get_review_count_for_restaurant("Restaurant A")
print(f"Number of reviews for Restaurant A: {review_count}")