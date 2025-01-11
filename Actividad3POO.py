import flet as ft
import ejer19, ejer18
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

    #ejercicio 19
    lado=ft.TextField(label="LADO", hint_text="Porfavor ingresar el valor del lado")
    lad=ft.Text("", size=20)
    area=ft.Text("", size=20)
    Perimetro=ft.Text("", size=20)
    Altura=ft.Text("", size=20)

    def calcular_valores(e):
        if lado.value:
            triangulo=ejer19.Triangulo(int(lado.value))
            lad.value="El valor del Lado es: "+lado.value
            area.value="El valor del Area es: "+ str(triangulo.calcular_area(lado.value))
            Perimetro.value="El valor del Perimetro es: "+ str(triangulo.calcular_perimetro(lado.value))
            Altura.value="El valor de la Altura es: "+ str(triangulo.calcular_altura(lado.value))
            lado.value=None
            page.update()

    ejercicio19=ft.Column([
    ft.Row([
    lado,
    ft.ElevatedButton("Calcular Valores",on_click=calcular_valores)
            ]),
    lad,area,Perimetro,Altura
                        ])
    #ejercicio 19

    #ejercicio 18
    codigo=ft.TextField(label="CODIGO", hint_text="Porfavor ingresar el Codigo")
    nombres=ft.TextField(label="NOMBRES", hint_text="Porfavor ingresar los Nombres")
    valor_hora=ft.TextField(label="VALOR DE HORA", hint_text="Porfavor ingresar el Valor de hora")
    hor_tra=ft.TextField(label="NUMERO DE HORAS", hint_text="Porfavor ingresar el Numero de horas")
    porcentaje=ft.TextField(label="PORCENTAJE", hint_text="Porfavor ingresar el valor del Porcentaje")
    respuesta=ft.Text("", size=20)

    def calcular_salarios(e):
        if codigo.value and nombres.value and valor_hora.value and hor_tra.value and porcentaje.value:
            empleado=ejer18.Empleado(codigo.value,nombres.value,hor_tra.value,valor_hora.value,porcentaje.value)
            bruto=str(empleado.calcular_salario_bruto())
            neto=str(empleado.calcular_salario_neto())
            respuesta.value=f"Codigo: {codigo.value}\nNombres: {nombres.value}\nSalario Bruto={bruto}\nSalario Neto={neto}"
            for i in [codigo,nombres,valor_hora,hor_tra,porcentaje]:
                i.value=None
        else: 
            respuesta.value="Porfavor Ingrese todos los campos pedidos"
        page.update()
            
    ejercicio18=ft.Column([
        codigo,nombres,valor_hora,hor_tra,porcentaje,
        ft.ElevatedButton("Calcular Salarios",on_click=calcular_salarios),
        respuesta
                        ])
    #ejercicio 18

    #ejercicio 7
    A=ft.TextField(label="A", hint_text="Porfavor ingresar el Valor de A")
    B=ft.TextField(label="B", hint_text="Porfavor ingresar el Vaor de B")
    mayor=ft.Text("", size=20)

    def Comparar_AB(e):
        if A.value and B.value:
            if float(A.value)<float(B.value):
                mayor.value="B es mayor que A"
            elif float(A.value)>float(B.value):
                mayor.value="A es mayor que B"
            else: mayor.value="A es igual que B"
            A.value=None
            B.value=None
        else:
            mayor.value="Porfavor Ingrese todos los campos pedidos"
        page.update()

    ejercicio7=ft.Column([
        A,B,
        ft.ElevatedButton("Comparar Numeros",on_click=Comparar_AB),
        mayor
                        ])
    #ejercicio 7

    #ejercicio 10
    NI=ft.TextField(label="NUMERO INSCRIPCION", hint_text="Porfavor ingresar el Numero de Inscripción")
    NOM=ft.TextField(label="NOMBRE", hint_text="Porfavor ingresar el Nombre del Estudiante")
    PAT=ft.TextField(label="PATRIMONIO", hint_text="Porfavor ingresar el Patrimonio del Estudiante")
    EST=ft.TextField(label="ESTRATO", hint_text="Porfavor ingresar el Estrato del Estudiante")
    PAGMAT=ft.Text("", size=20)

    def Calcular_matricula(e):
        if NI.value and NOM.value and PAT.value and EST.value:
            matricula=50000
            if float(PAT.value)>2000000 and float(EST.value)>3:
                matricula=str(matricula+0.03*float(PAT.value))
            PAGMAT.value=f"EL estudiante con numero de inscripcion {NI.value} y nombre {NOM.value}\nDebe pagar: ${matricula}"
            for i in [NI,NOM,PAT,EST]:
                i.value=None
        else: 
            PAGMAT.value="Porfavor Ingrese todos los campos pedidos"
        page.update()

    ejercicio10=ft.Column([
        NI,NOM,PAT,EST,
        ft.ElevatedButton("Calcular Matricula",on_click=Calcular_matricula),
        PAGMAT
                        ])
    #ejercicio 10

    #ejercicio22
    nom_empleado=ft.TextField(label="NOMBRE", hint_text="Porfavor ingresar el Nombre del Empleado")
    sal_hora=ft.TextField(label="SALARIO HORA", hint_text="Porfavor ingresar el Salario por Hora")
    num_horas=ft.TextField(label="NUMERO HORAS", hint_text="Porfavor ingresar el Numero de Horas")
    mensaje=ft.Text("", size=20)

    def Calcular_salario(e):
        if nom_empleado.value and sal_hora.value and num_horas.value:
            salario=(int(num_horas.value))*(int(sal_hora.value))
            if salario>450000:
                mensaje.value=f"Empleado {nom_empleado.value} tiene un salario de ${salario}"
            else: mensaje.value="Empleado "+nom_empleado.value
            for i in [nom_empleado,sal_hora,num_horas]:
                    i.value=None
        else:
            mensaje.value="Porfavor Ingrese todos los campos pedidos"
        page.update()

    ejercicio22=ft.Column([
        nom_empleado,sal_hora,num_horas,
        ft.ElevatedButton("Calcular Salario",on_click=Calcular_salario),
        mensaje
                        ])
    #ejercicio22

    #ejercicio23
    a=ft.TextField(label="A", hint_text="Porfavor ingresar el valor de A")
    b=ft.TextField(label="B", hint_text="Porfavor ingresar el valor de B")
    c=ft.TextField(label="C", hint_text="Porfavor ingresar el valor de C")
    soluciones=ft.Text("", size=20)

    def Calcular_ecuacion(e):
        if a.value and b.value and c.value:
            x1=(-int(b.value)-((int(b.value)**2-4*int(a.value)*int(c.value))**0.5))/2*int(a.value)
            x2=(-int(b.value)+((int(b.value)**2-4*int(a.value)*int(c.value))**0.5))/2*int(a.value)
            soluciones.value=f"Las soluciones de la Ecuacion son {x1} y {x2}"
            for i in [a,b,c]:
                    i.value=None
        else:
            soluciones.value="Porfavor Ingrese todos los campos pedidos"
        page.update()

    ejercicio23=ft.Column([
        a,b,c,
        ft.ElevatedButton("Calcular Ecuacion",on_click=Calcular_ecuacion),
        soluciones
                        ])
    #ejercicio23


    #cambiar de ejercicio
    def change_view(e):
        selected=e.control.selected_index
        if selected==0:
            content_area.content=ejercicio19
        elif selected==1:
            content_area.content=ejercicio18
        elif selected==2:
            content_area.content=ejercicio7
        elif selected==3:
            content_area.content=ejercicio10
        elif selected==4:
            content_area.content=ejercicio22
        elif selected==5:
            content_area.content=ejercicio23
        content_area.update()
    content_area=ft.Container(
        content=ft.Text(
            "Solucion de los ejercicios de la actividad 3 POO\nParte 1\nAndres Esteban Montoya Suarez",
            size=25
        ),
        expand=True,
        padding=20
    )
    #cambiar de ejercicio


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
                label="Ejercicio Propuesto 19"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Ejercicio Propuesto 18"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Ejercicio Resuelto 7"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Ejercicio Resuelto 10"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Ejercicio Propuesto 22"
            ),
            ft.NavigationRailDestination(
                icon=ft.Icons.ISO,
                label="Ejercicio Propuesto 23"
            )
        ],
        on_change=change_view,
        bgcolor=ft.Colors.GREY_900
    )
    #menu lateral

    #objetos de la pagina
    page.add(
        ft.Row(
            [rail,
             ft.VerticalDivider(width=0.2),
             content_area
             ],
             expand=True
            )
        )
    #objetos de la pagina

#iniciar pagina
ft.app(target=main)