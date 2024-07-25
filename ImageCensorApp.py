import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
import os
from datetime import datetime

class ImageCensorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Herramienta de Censura de Imágenes")
        self.image = None
        self.original_image = None
        self.history = []
        self.rect_start = None
        self.rect_end = None
        self.rect_id = None
        self.zoom_level = 1

        # Establecer el icono del programa usando icon.png
        self.icon_path = os.path.join(os.path.dirname(__file__), 'icon.png')
        try:
            icon_image = tk.PhotoImage(file=self.icon_path)
            self.master.iconphoto(False, icon_image)
        except Exception as e:
            print(f"Error al cargar el icono: {e}")

        # Crear el frame principal
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Crear el frame derecho para la ayuda
        self.help_frame = tk.Frame(self.main_frame, width=430, height=720, bd=2, relief=tk.SUNKEN, bg='white')
        self.help_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5)
        self.help_frame.pack_propagate(False)

        # Crear el botón para abatir la imagen de ayuda
        self.toggle_help_button = tk.Button(self.help_frame, text="Ocultar Ayuda", command=self.toggle_help, bg='white', fg='black')
        self.toggle_help_button.pack()

        # Cargar y mostrar la imagen de ayuda
        self.help_image_path = os.path.join(os.path.dirname(__file__), 'ejemplo.png')
        self.help_image = Image.open(self.help_image_path)
        self.help_photo = ImageTk.PhotoImage(self.help_image)
        self.help_label = tk.Label(self.help_frame, image=self.help_photo, bg='white')
        self.help_label.pack()

        # Crear la barra de herramientas
        self.toolbar = tk.Frame(self.main_frame, bd=1, relief=tk.RAISED, bg='white')
        self.toolbar.pack(side=tk.TOP, fill=tk.X)

        # Añadir botones a la barra de herramientas
        self.open_button = tk.Button(self.toolbar, text="Abrir", command=self.open_image, bg='white', fg='black')
        self.open_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.save_button = tk.Button(self.toolbar, text="Guardar", command=self.save_image, bg='white', fg='black')
        self.save_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.undo_button = tk.Button(self.toolbar, text="Deshacer", command=self.undo, bg='white', fg='black')
        self.undo_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.zoom_in_button = tk.Button(self.toolbar, text="Zoom In", command=self.zoom_in, bg='white', fg='black')
        self.zoom_in_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.zoom_out_button = tk.Button(self.toolbar, text="Zoom Out", command=self.zoom_out, bg='white', fg='black')
        self.zoom_out_button.pack(side=tk.LEFT, padx=2, pady=2)

        self.exit_button = tk.Button(self.toolbar, text="Salir", command=self.master.quit, bg='white', fg='black')
        self.exit_button.pack(side=tk.LEFT, padx=2, pady=2)

        # Crear el canvas para la imagen principal
        self.canvas = tk.Canvas(self.main_frame, cursor="cross", bg='white')
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        self.canvas.bind("<Button-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def toggle_help(self):
        if self.help_label.winfo_viewable():
            self.help_label.pack_forget()
            self.toggle_help_button.config(text="Mostrar Ayuda")
        else:
            self.help_label.pack()
            self.toggle_help_button.config(text="Ocultar Ayuda")

    def open_image(self):
        file_path = filedialog.askopenfilename(title="Abrir imagen", filetypes=[
            ("All files", "*.*"),
            ("JPEG files", "*.jpg;*.jpeg"),
            ("PNG files", "*.png"),
            ("BMP files", "*.bmp"),
            ("TIFF files", "*.tiff")
        ])
        if file_path:
            self.image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
            self.original_image = self.image.copy()
            self.history = [self.image.copy()]
            self.zoom_level = 1
            self.show_image()

    def save_image(self):
        if self.image is not None:
            reason = simpledialog.askstring("Marca de agua", "Ingrese el nombre de la entidad a la que se le entregará la imagen:")
            if reason:
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Archivos PNG", "*.png"), ("Todos los archivos", "*.*")])
                if file_path:
                    # Convertir la imagen a blanco y negro
                    gray_image = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
                    gray_image = cv2.cvtColor(gray_image, cv2.COLOR_GRAY2RGB)

                    # Escalar el tamaño de la fuente basado en la altura de la imagen
                    font_size = max(20, gray_image.shape[0] // 20)  # Ajusta el divisor según tus necesidades
                    font = ImageFont.truetype("arial.ttf", font_size)

                    # Obtener la fecha y hora actual
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                    # Agregar el texto en la esquina inferior derecha de la imagen
                    pil_image = Image.fromarray(gray_image)
                    draw = ImageDraw.Draw(pil_image)
                    text = f"Entregada a {reason}\n{current_time}"
                    text_bbox = draw.textbbox((0, 0), text, font=font)
                    text_width = text_bbox[2] - text_bbox[0]
                    text_height = text_bbox[3] - text_bbox[1]
                    text_x = pil_image.width - text_width - 10  # 10 píxeles de margen desde el borde derecho
                    text_y = pil_image.height - text_height - 10  # 10 píxeles de margen desde el borde inferior

                    # Obtener el color de fondo en la región donde se colocará el texto
                    region = gray_image[text_y:text_y+text_height, text_x:text_x+text_width]
                    avg_color = np.mean(region)

                    # Seleccionar el color del texto (blanco o negro) basado en el color de fondo
                    text_color = "white" if avg_color < 128 else "black"

                    draw.text((text_x, text_y), text, fill=text_color, font=font)

                    # Guardar la imagen
                    pil_image.save(file_path)

    def show_image(self):
        if self.image is not None:
            self.canvas.delete("all")
            zoomed_image = cv2.resize(self.image, (0, 0), fx=self.zoom_level, fy=self.zoom_level)
            self.tk_image = ImageTk.PhotoImage(image=Image.fromarray(zoomed_image))
            self.canvas.create_image(0, 0, anchor="nw", image=self.tk_image)
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def on_button_press(self, event):
        self.rect_start = (event.x, event.y)

    def on_mouse_drag(self, event):
        if self.rect_start:
            if self.rect_id:
                self.canvas.delete(self.rect_id)
            self.rect_end = (event.x, event.y)
            self.rect_id = self.canvas.create_rectangle(*self.rect_start, event.x, event.y, outline="red")

    def on_button_release(self, event):
        if self.rect_start and self.rect_end:
            x0, y0 = self.rect_start
            x1, y1 = self.rect_end
            self.censor_area(x0, y0, x1, y1)
            self.rect_start = None
            self.rect_end = None
            self.rect_id = None
            self.show_image()

    def censor_area(self, x0, y0, x1, y1):
        if self.image is not None:
            x0, x1 = sorted([x0, x1])
            y0, y1 = sorted([y0, y1])
            x0 = int(x0 / self.zoom_level)
            x1 = int(x1 / self.zoom_level)
            y0 = int(y0 / self.zoom_level)
            y1 = int(y1 / self.zoom_level)
            self.history.append(self.image.copy())
            self.image[y0:y1, x0:x1] = cv2.GaussianBlur(self.image[y0:y1, x0:x1], (51, 51), 0)

    def undo(self):
        if len(self.history) > 1:
            self.history.pop()
            self.image = self.history[-1].copy()
            self.show_image()

    def zoom_in(self):
        self.zoom_level *= 1.2
        self.show_image()

    def zoom_out(self):
        self.zoom_level /= 1.2
        self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageCensorApp(root)
    root.geometry("1250x800")
    root.mainloop()
