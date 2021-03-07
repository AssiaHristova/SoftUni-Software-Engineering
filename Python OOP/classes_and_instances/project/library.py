class Library:
    user_records = []
    books_available = {}
    rented_books = {}

    def add_user(self, user):
        filtered_users = [u for u in self.user_records if u == user]
        if filtered_users:
            user = filtered_users[0]
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        filtered_users = [u for u in self.user_records if u == user]
        if not filtered_users:
            return "We could not find such user to remove!"
        user = filtered_users[0]
        self.user_records.remove(user)
        if user.username in self.rented_books:
            self.rented_books.pop(user.username)

    def change_username(self, user_id, new_username):
        filtered_users = [u for u in self.user_records if u.user_id == user_id]
        if not filtered_users:
            return f"There is no user with id = {user_id}!"
        user = filtered_users[0]
        if user.username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        user.username = new_username
        if user.username in self.rented_books:
            self.rented_books[user.username] = self.rented_books[new_username]
        return f"Username successfully changed to: {new_username} for userid: {user.user_id}"
