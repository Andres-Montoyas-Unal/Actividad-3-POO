import math as mt
import flet as ft
import clases
Circulos=[]
Cuadrados=[]
Rectangulos=[]
Triangulos=[]

def main(page:ft.Page):
    #valores de la pagina
    page.title="Solucion de problemas"
    page.window.width=1000
    page.window.height=700
    page.padding=0
    page.bgcolor=ft.colors.BACKGROUND
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

    page.theme=ft.Theme(
        color_scheme_seed=ft.Colors.BLUE,
        visual_density=ft.VisualDensity.COMFORTABLE,
        color_scheme=ft.ColorScheme(
            primary=ft.Colors.BLUE,
            secondary=ft.Colors.ORANGE,
            background=ft.Colors.GREY_900,
            surface=ft.Colors.BLUE_GREY_900
        )
    )
    page.update()
    #valores de la pagina

    #Circulos
    radio=ft.TextField(label="Radio", hint_text="Porfavor ingresar el Valor del Radio")
    lbl_c=ft.Text("", size=20)
    def Crear_circulo(e):
        if radio.value:
            cir=clases.Circulo(int(radio.value))
            area_c=cir.calcularArea()
            per_c=cir.calcularPerimetro()
            lbl_c.value=f"El circulo con radio {radio.value} tiene Area={area_c} y perimetro={per_c}"
            radio.value=None
        else:
            lbl_c.value="Error al crear el circulo"
        page.update()

    Circulo=ft.Column([radio,
        ft.ElevatedButton("Calcular Circulo",on_click=Crear_circulo),lbl_c
                        ])
    #Circulos

    #Cuadrados
    lado=ft.TextField(label="Lado", hint_text="Porfavor ingresar el Valor del Lado")
    lbl_l=ft.Text("", size=20)
    def Crear_cuadrado(e):
        if lado.value:
            cua=clases.Cuadrado(int(lado.value))
            area_l=cua.calcularArea()
            per_l=cua.calcularPerimetro()
            lbl_l.value=f"El cuadrado con lado {lado.value} tiene Area={area_l} y perimetro={per_l}"
            lado.value=None
        else:
            lbl_l.value="Error al crear el cuadrado"
        page.update()

    Cuadrado=ft.Column([lado,
        ft.ElevatedButton("Calcular Cuadrado",on_click=Crear_cuadrado),lbl_l
                        ])
    #Cuadrados

    #Rectangulos
    base_r=ft.TextField(label="Base", hint_text="Porfavor ingresar el Valor de la Base")
    altura_r=ft.TextField(label="Altura", hint_text="Porfavor ingresar el Valor de la Altura")
    lbl_r=ft.Text("", size=20)
    def Crear_Rectangulo(e):
        if base_r.value and altura_r.value:
            rec=clases.Rectangulo(int(base_r.value),int(altura_r.value))
            area_r=rec.calcularArea()
            per_r=rec.calcularPerimetro()
            lbl_r.value=f"El Rectanglo con Base {base_r.value} y Altura {altura_r.value} tiene Area={area_r} y Perimetro={per_r}"
            base_r.value=None
            altura_r.value=None
        else:
            lbl_r.value="Error al crear el rectangulo"
        page.update()

    Rectangulo=ft.Column([base_r,altura_r,
        ft.ElevatedButton("Calcular Rectangulo",on_click=Crear_Rectangulo),lbl_r
                        ])
    #Rectangulos

    #Triangulos
    base_t=ft.TextField(label="Base", hint_text="Porfavor ingresar el Valor de la Base")
    altura_t=ft.TextField(label="Altura", hint_text="Porfavor ingresar el Valor de la Altura")
    lbl_t=ft.Text("", size=20)
    def Crear_Triangulo(e):
        if base_t.value and altura_t.value:
            tri=clases.TrianguloRectangulo(int(base_t.value),int(altura_t.value))
            area_t=tri.calcularArea()
            per_t=tri.calcularPerimetro(tri.calcularHipotenusa())
            lbl_t.value=f"El Rectanglo con Base {base_t.value} y Altura {altura_t.value} tiene Area={area_t} y Perimetro={per_t}"
            base_t.value=None
            altura_t.value=None
        else:
            lbl_t.value="Error al crear el rectangulo"
        page.update()

    Triangulo=ft.Column([base_t,altura_t,
        ft.ElevatedButton("Calcular Triangulo",on_click=Crear_Triangulo),lbl_t
                        ])
    #Triangulos

    #Rombos
    lado_R=ft.TextField(label="Lado", hint_text="Porfavor ingresar el Valor del Lado")
    D_R=ft.TextField(label="D", hint_text="Porfavor ingresar el Valor de D")
    d_R=ft.TextField(label="d", hint_text="Porfavor ingresar el Valor de d")
    lbl_R=ft.Text("", size=20)
    def Crear_rombo(e):
        if lado_R.value:
            rom=clases.Rombo(float(lado_R.value),float(D_R.value),float(d_R.value))
            area_R=rom.calcularArea()
            per_R=rom.calcularPerimetro()
            lbl_R.value=f"El rombo con lado {lado_R.value} tiene Area={area_R} y perimetro={per_R}"
            lado_R.value=None
            d_R.value=None
            D_R.value=None
        else:
            lbl_R.value="Error al crear el rombo"
        page.update()

    Rombo=ft.Column([lado_R,D_R,d_R,
        ft.ElevatedButton("Calcular Rombo",on_click=Crear_rombo),lbl_R
                        ])
    #Rombos

    #cambiar de figura
    def change_view(e):
        selected=e.control.selected_index
        if selected==0:
            content_area.content=Cuadrado
        elif selected==1:
            content_area.content=Circulo
        elif selected==2:
            content_area.content=Rectangulo
        elif selected==3:
            content_area.content=Triangulo
        elif selected==4:
            content_area.content=Rombo
        content_area.update()
    content_area=ft.Container(
        content=ft.Text(
            "Solucion de los ejercicios de la actividad 3 POO\nParte 2\nAndres Esteban Montoya Suarez",
            size=25
        ),
        expand=True,
        padding=20
    )
    #cambiar de figura


    #menu lateral
    rail=ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Cuadrados"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Circulos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Rectangulos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Triangulos"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Rombos"
            )
        ],
        on_change=change_view,
        bgcolor=ft.Colors.GREY_900
    )
    #menu lateral


    page.add(
        ft.Row(
            [rail,
             ft.VerticalDivider(width=0.2),
             content_area
             ],
             expand=True
            )
        )



ft.app(target=main)