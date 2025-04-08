import flet as ft
import mysql.connector

# def main(page: ft.Page):
#     page.title = "Flet & MySQL Example"

#     # Connect to MySQL
#     try:
#         connection = mysql.connector.connect(
#             host="103.172.92.27",
#             user="czpqmrra_office_user",
#             password="BSTe4cnZX4ZL",
#             database="czpqmrra_office"
#         )
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM user")
#         data = cursor.fetchall()

#         # Display data in Flet
#         for row in data:
#             page.add(ft.Text(f"Row: {row}"))
#     except mysql.connector.Error as err:
#         page.add(ft.Text(f"Error: {err}"))
#     finally:
#         if connection.is_connected():
#             connection.close()

#     page.add(ft.Text("Done!"))

# import flet as ft

def main(page: ft.Page):
    page.title = "My App"
    page.add(ft.Text("Hello, World!"))

ft.app(target=main, host="0.0.0.0", port=8000)