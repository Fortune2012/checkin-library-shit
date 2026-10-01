books = ["matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}

chosen_book = input("Which book do you want to borrow? ").strip().lower()

if chosen_book not in library or library[chosen_book] == 0:
    print(f"{chosen_book} is not available! Stopping the checker.")
    raise SystemExit

late_fees = [5, 8, 4, 6, 7]
extra_fee = int(input("Enter the extra library fee to add to every book: "))

updated_fees = [fee + extra_fee for fee in late_fees]
book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]

library[chosen_book] -= 1

print("Book Borrowed:", chosen_book)
print("Late Fee:", chosen_fee)
print("Updated Library Stock:", library)