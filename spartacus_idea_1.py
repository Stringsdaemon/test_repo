import tkinter as tk
from tkinter import messagebox, scrolledtext, PhotoImage, filedialog

class RecipeBookApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Kochbuch")
        self.master.geometry("700x850")
        self.master.resizable(False, False)
        self.master.configure(bg="#908E13")

        self.recipes = {
            "Spaghetti Bolognese": {"ingredients": "Spaghetti, Hackfleisch, Tomatensauce, Zwiebeln, Knoblauch", "price": "8,50€", "feedback": []},
            "Pizza Margherita": {"ingredients": "Pizza Teig, Tomatensauce, Mozzarella, Basilikum", "price": "7,00€", "feedback": []},
            "Caesar Salad": {"ingredients": "Römersalat, Croutons, Parmesan, Caesar-Dressing", "price": "6,50€", "feedback": []},
            "Ratatouille": {"ingredients": "Aubergine, Zucchini, Paprika, Tomaten, Zwiebeln", "price": "7,50€", "feedback": []},
            "Sushi": {"ingredients": "Reis, Nori, Lachs, Avocado, Sojasauce", "price": "12,00€", "feedback": []},
            "Curry": {"ingredients": "Hühnchen, Kokosmilch, Currypaste, Gemüse", "price": "9,00€", "feedback": []},
            "Tacos": {"ingredients": "Tortillas, Hackfleisch, Käse, Salat, Salsa", "price": "8,00€", "feedback": []},
            "Pancakes": {"ingredients": "Mehl, Milch, Eier, Zucker, Backpulver", "price": "5,00€", "feedback": []},
        }

        self.selected_recipe = None

        self.frame = tk.Frame(master, bg="#2D2C06", bd=5, relief="raised")
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.title_label = tk.Label(self.frame, text="Kochbuch", font=("Helvetica", 24, "bold"), bg="#161603", fg="#A1A1A0")
        self.title_label.pack(pady=10)

        self.info_label = tk.Label(self.frame, text="Menü des Tages: 'Ratatouille'", bg="#4C4C0A", fg="#062229", font=("Arial", 16, "bold"))
        self.info_label.pack(pady=10)
        self.blink_text()

        self.recipe_frame = tk.Frame(self.frame, bg="#2D2C06", bd=5, relief="raised")
        self.recipe_frame.pack(side=tk.LEFT, padx=(10, 5), fill="both", expand=True)

        self.canvas = tk.Canvas(self.recipe_frame, bg="#63620D", width=300, height=400)
        self.canvas.pack(pady=10)

        self.create_recipe_list()

        self.select_button = tk.Button(self.recipe_frame, text="Zutaten und Preis anzeigen", command=self.show_recipe_details, bg="#2E0E06", fg="#964B00", font=("Arial", 12, "bold"), activebackground="#4A4A4A")
        self.select_button.pack(pady=5)

        self.feedback_label = tk.Label(self.recipe_frame, text="Feedback hinterlassen:", bg="#0C570E", fg="#A4A4A4", font=("Comic Sans", 12))
        self.feedback_label.pack(pady=10)

        self.feedback_entry = tk.Entry(self.recipe_frame, width=40, font=("Comic Sans", 12), bg="#908E13", fg="Black", bd=2, relief="groove")
        self.feedback_entry.pack(pady=5)

        self.submit_feedback_button = tk.Button(self.recipe_frame, text="Feedback senden", command=self.submit_feedback, bg="#2E0E06", fg="#E6E445", font=("Arial", 12, "bold"), activebackground="#964B00")
        self.submit_feedback_button.pack(pady=5)

        self.feedback_display = scrolledtext.ScrolledText(self.recipe_frame, width=40, height=10, bg="#908E13", font=("Arial", 12, "bold"), fg="white")
        self.feedback_display.pack(pady=10)

        self.image_frame = tk.Frame(self.frame, bg="#908E13", width=200)
        self.image_frame.pack(side=tk.RIGHT, padx=(5, 10), fill="both", expand=True)

        self.image_label = tk.Label(self.image_frame, bg="#2D2C06")
        self.image_label.pack(pady=10)

        self.load_image_button = tk.Button(self.image_frame, text="Bild hochladen", command=self.load_image, bg="#2E0E06", fg="#E6E445", font=("Arial", 12, "bold"), activebackground="#964B00")
        self.load_image_button.pack(pady=5)

        self.bottom_label = tk.Label(self.recipe_frame, text="Guten Appetit!", bg="#964B00", fg="white", font=("Arial", 12))
        self.bottom_label.pack(side=tk.BOTTOM, padx=10, pady=10)

    def blink_text(self):
        current_color = self.info_label.cget("fg")
        new_color = "red" if current_color == "#062229" else "#062229"
        self.info_label.config(fg=new_color)
        self.master.after(500, self.blink_text)

    def create_recipe_list(self):
        for i, (recipe, details) in enumerate(self.recipes.items()):
            y_position = 30 + i * 40
            self.canvas.create_rectangle(10, y_position, 280, y_position + 30, fill="#67660E" if i % 2 == 0 else "#4C4C0A", outline="")
            self.canvas.create_text(150, y_position + 15, text=recipe, font=("Arial", 12, "bold"), fill="black")
            self.canvas.tag_bind(f"recipe_{i}", "<Button-1>", lambda e, i=i: self.select_recipe(i))

    def select_recipe(self, index):
        self.selected_recipe = list(self.recipes.keys())[index]
        self.canvas.delete("highlight")
        self.canvas.create_rectangle(10, 30 + index * 40, 280, 30 + (index + 1) * 40, fill="yellow", outline="", tags="highlight")

    def show_recipe_details(self):
        if self.selected_recipe:
            details = self.recipes[self.selected_recipe]
            messagebox.showinfo("Rezeptdetails", f"Zutaten: {details['ingredients']}\nPreis: {details['price']}")
        else:
            messagebox.showwarning("Warnung", "Bitte wählen Sie ein Rezept aus.")

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image = PhotoImage(file=file_path)
            self.image_label.config(image=self.image)

    def submit_feedback(self):
        feedback = self.feedback_entry.get()
        if feedback and self.selected_recipe:
            self.recipes[self.selected_recipe]["feedback"].append(feedback)
            self.feedback_display.insert(tk.END, f"Feedback für {self.selected_recipe}: {feedback}\n")
            self.feedback_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warnung", "Bitte geben Sie Ihr Feedback ein und wählen Sie ein Rezept.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeBookApp(root)
    root.mainloop()