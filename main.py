import flet as ft

def main(page: ft.Page):
  
    page.title = "Calculadora de Calorías"
    
    def validar_campos():
        """Valida que todos los campos requeridos estén completos y sean válidos"""
        try:
            if not sexo.value:
                raise ValueError("Por favor seleccione su sexo")
            if not pesoKg.value or float(pesoKg.value) <= 0:
                raise ValueError("Por favor ingrese un peso válido")
            if not alturaCm.value or float(alturaCm.value) <= 0:
                raise ValueError("Por favor ingrese una altura válida")
            if not edad.value or int(edad.value) <= 0:
                raise ValueError("Por favor ingrese una edad válida")
            return True
        except ValueError as e:
            visualizador.value = f"Error: {str(e)}"
            page.update()
            return False

    def calcular_calorias(peso, altura, edad, es_masculino):
        """Calcula las calorías basales según la fórmula de Harris-Benedict"""
        if es_masculino:
            return 66 + (13.7 * peso) + (5 * altura) - (6.8 * edad)
        return 655 + (9.6 * peso) + (1.8 * altura) - (4.7 * edad)

    def button_clicked(e):
        if not validar_campos():
            return
            
        try:
            peso = float(pesoKg.value)
            altura = float(alturaCm.value)
            edad2 = int(edad.value)
            es_masculino = sexo.value == "Masculino"
            
            calorias = calcular_calorias(peso, altura, edad2, es_masculino)
            visualizador.value = f"Calorías recomendadas: {calorias:.2f} kcal"
            page.update()
        except Exception as e:
            visualizador.value = f"Error en el cálculo: {str(e)}"
            page.update()

    # Componentes UI
    logo = ft.Container(
        content=ft.Image(
            src="https://cdn-icons-png.flaticon.com/512/5222/5222103.png",
            width=50,
            height=50
        ),
        padding=20,
        border_radius=999,
        bgcolor="#c6fff5"
    )

    title = ft.Row(
        controls=[
            ft.Container(padding=10),
            ft.Text("Calculadora de calorías", size=24, weight=ft.FontWeight.BOLD),
            logo
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    sexo = ft.Dropdown(
        width=300,
        options=[
            ft.dropdown.Option("Masculino"),
            ft.dropdown.Option("Femenino"),
        ],
        label="Sexo",
        hint_text="Seleccione su sexo",
        autofocus=True
    )

    pesoKg = ft.TextField(
        label="Peso",
        hint_text="Ingrese su peso en kg",
        width=300,
        suffix_text="kg",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    alturaCm = ft.TextField(
        label="Altura",
        hint_text="Ingrese su altura en cm",
        width=300,
        suffix_text="cm",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    edad = ft.TextField(
        label="Edad",
        hint_text="Ingrese su edad",
        width=300,
        suffix_text="años",
        keyboard_type=ft.KeyboardType.NUMBER
    )

    visualizador = ft.TextField(
        label="Resultado",
        width=300,
        value="Ingrese sus datos y presione Calcular",
        read_only=True,
        text_align=ft.TextAlign.CENTER
    )
    
    calcButton = ft.ElevatedButton(
        text="Calcular",
        on_click=button_clicked,
        style=ft.ButtonStyle(
            color={
                ft.MaterialState.DEFAULT: ft.colors.WHITE,
            },
            bgcolor={
                ft.MaterialState.DEFAULT: ft.colors.BLUE,
                ft.MaterialState.HOVERED: ft.colors.BLUE_700,
            },
        ),
        width=200
    )

    contenedor = ft.Column(
        controls=[
            title,
            ft.Container(padding=10),
            sexo,
            ft.Container(padding=10),
            pesoKg,
            ft.Container(padding=10),
            alturaCm,
            ft.Container(padding=10),
            edad,
            ft.Container(padding=15),
            visualizador,
            ft.Container(padding=10),
            calcButton
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER 
    )

    vista = ft.View(
        route="/",
        controls=[
            ft.Stack(
                [contenedor],
                width=page.width,
                alignment=ft.alignment.center
            )
        ],
        padding=0,
        vertical_alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )
    
    page.views.append(vista)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)