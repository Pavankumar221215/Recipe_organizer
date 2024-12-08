import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
CSV_FILE = 'recipes.csv'
def read_recipes():
    recipes = []
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipes.append(row)
    except FileNotFoundError:
        pass
    return recipes
def save_recipe(name, ingredients, instructions):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Ingredients", "Instructions"])
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow({"Name": name, "Ingredients": ingredients, "Instructions": instructions})
def search_recipes(keyword):
    recipes = read_recipes()
    found_recipes = []
    for recipe in recipes:
        if keyword.lower() in recipe["Name"].lower() or keyword.lower() in recipe["Ingredients"].lower():
            found_recipes.append(recipe)
    return found_recipes
def filter_by_ingredient(ingredient):
    recipes = read_recipes()
    found_recipes = []
    for recipe in recipes:
        if ingredient.lower() in recipe["Ingredients"].lower():
            found_recipes.append(recipe)
    return found_recipes

def add_recipe():
    name = simpledialog.askstring("Recipe Name", "Enter the name of the recipe:")
    if name:
        ingredients = simpledialog.askstring("Ingredients", "Enter ingredients (comma separated):")
        instructions = simpledialog.askstring("Instructions", "Enter the instructions:")
        if ingredients and instructions:
            save_recipe(name, ingredients, instructions)
            messagebox.showinfo("Success", "Recipe added successfully!")
        else:
            messagebox.showwarning("Input Error", "Ingredients and Instructions cannot be empty!")
    else:
        messagebox.showwarning("Input Error", "Recipe Name cannot be empty!")
def display_recipes(recipes):
    result_text.delete(1.0, tk.END) 
    if not recipes:
        result_text.insert(tk.END, "No recipes found.")
    for recipe in recipes:
        result_text.insert(tk.END, f"Name: {recipe['Name']}\n")
        result_text.insert(tk.END, f"Ingredients: {recipe['Ingredients']}\n")
        result_text.insert(tk.END, f"Instructions: {recipe['Instructions']}\n\n")
def search_action():
    keyword = search_entry.get()
    if keyword:
        found_recipes = search_recipes(keyword)
        display_recipes(found_recipes)
    else:
        messagebox.showwarning("Search Error", "Please enter a keyword to search.")

def filter_action():
    ingredient = filter_entry.get()
    if ingredient:
        found_recipes = filter_by_ingredient(ingredient)
        display_recipes(found_recipes)
    else:
        messagebox.showwarning("Filter Error", "Please enter an ingredient to filter.")
root = tk.Tk()
root.title("Recipe Organizer")
root.geometry("1550x850")
root.config(bg='#01c1ff')

button_frame = tk.Frame(root, bg='#01c1ff')
button_frame.pack(pady=20,padx=20)

add_button = tk.Button(button_frame, text="Add Recipe", command=add_recipe, bg='teal', fg='white', font=('Arial', 20), width=10, height=1)
add_button.grid(row=0, column=3, padx=50)

search_button = tk.Button(button_frame, text="Search", command=search_action, bg='teal', fg='white', font=('Arial', 20), width=10, height=1)
search_button.grid(row=0, column=1, padx=50)

filter_button = tk.Button(button_frame, text="Filter by Ingredient", command=filter_action, bg='#a601ff', fg='black', font=('Arial', 20), width=20, height=1)
filter_button.grid(row=0, column=2, padx=50)

search_label = tk.Label(root, text="Search by Name or Ingredients:", bg='#01c1ff', fg='black', font=('garamond', 20))
search_label.pack(padx=10, pady=5)

search_entry = tk.Entry(root, width=60, bg='black', fg='white', font=('Arial', 20))
search_entry.pack(padx=10, pady=10)

filter_label = tk.Label(root, text="Filter by Ingredient:", bg='#01c1ff', fg='black', font=('garamond', 20))
filter_label.pack(padx=10, pady=10)

filter_entry = tk.Entry(root, width=50, bg='black', fg='white', font=('Arial', 20))
filter_entry.pack(padx=10, pady=10)

result_text = tk.Text(root, height=15, width=80, bg='#0061ff', font=('Times new Roman', 25))
result_text.pack(padx=200, pady=30)

root.mainloop()