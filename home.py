import flet as ft
from flet import Page,View,Theme
import sqlite3
import datetime
import speech_recognition as sr
import time
import random

banco=sqlite3.connect("caranguejo4.db",check_same_thread=False)
banco_questoes = sqlite3.connect("questoes.db",check_same_thread=False)
cursor_questoes = banco_questoes.cursor()
cursor = banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS usuarios3 (usuario text,senha text,level integer,pontuaçao integer,data text,consecutivos integer,exp float)')
def main(page: Page):
    texto_falado_indice = ft.Text("0")
    texto_pergunta = ft.Text("Questão 1/6",size=50,color="black",weight=ft.FontWeight.BOLD)
    texto_a_ser_falado = ft.Text("BONJOUR PRINCESSE FUDIDA ARROMBADA DO KRAI",size=25,color="white",weight=ft.FontWeight.BOLD)
    def close_dlg(e):
        dlg_modal.open = False
        page.update()
    def fechar_alerta_registro(e):
        erro_registro.open = False
        page.update()
    def voltar_pagina_usuario(e):
        texto_pergunta.value = 'Questão 1/5'
        page.go("/jogar")
    botao_falar = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="Aperte quando estiver pronto", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=350,
            height=60
        )
    
    botao_alternativa_A = ft.ElevatedButton(content=ft.Text("a) Bom dia princesa",size=20),width=500,height=50,color="black",bgcolor="white",style=ft.ButtonStyle(#botao para login
                shape=ft.RoundedRectangleBorder(radius=20)))
    botao_alternativa_B = ft.ElevatedButton(content=ft.Text("b) Bom dia princesa",size=20),width=500,height=50,color="black",bgcolor="white",style=ft.ButtonStyle(#botao para login
                shape=ft.RoundedRectangleBorder(radius=20),))
    botao_alternativa_C = ft.ElevatedButton(content=ft.Text("c) Bom dia princesa",size=20),width=500,height=50,color="black",bgcolor="white",style=ft.ButtonStyle(#botao para login
                shape=ft.RoundedRectangleBorder(radius=20),))
    botao_alternativa_D = ft.ElevatedButton(content=ft.Text("d) Bom dia princesa",size=20),width=500,height=50,color="black",bgcolor="white",style=ft.ButtonStyle(#botao para login
                shape=ft.RoundedRectangleBorder(radius=20),))
    
    container_botao_falar = ft.Container(
                                        botao_falar,
                                        alignment=ft.alignment.center,
                                        margin=ft.margin.only(top=50),
                                    )
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Tem certeza que deseja voltar?"),
        content=ft.Text("Todo progresso até aqui será perdido!!"),
        actions=[
            ft.TextButton("SIM", on_click=voltar_pagina_usuario),
            ft.TextButton("NÃO", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    def ir_para_proxima_questao(e):
        consulta = cursor_questoes.execute("SELECT * FROM questoes WHERE frances=?",(texto_a_ser_falado.value,))
        res = consulta.fetchall()
        botao_alternativa_A.content = ft.Text(res[0][1])
        botao_alternativa_B.content = ft.Text(res[0][2])
        botao_alternativa_C.content = ft.Text(res[0][3])
        botao_alternativa_D.content = ft.Text(res[0][4])
        texto_pergunta.value = f"Questão {int(texto_pergunta.value[8])+1}/6"
        page.go("/jogando_alternativa")
    def fechar_erro_audio(e):
        page.dialog = errou_audio
        errou_audio.open = False
        container_botao_falar.height = 60
        container_texto_falado.height = 0
        page.update()
    errou_audio = ft.AlertDialog(
        modal=True,
        title=ft.Text("Não foi possível compreender o áudio"),
        content=ft.Text("Tente novamente"),
        actions=[
            ft.TextButton("Ok", on_click=fechar_erro_audio),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    errou_questão = ft.AlertDialog(
        modal=True,
        title=ft.Text("Você errou!!"),
        content=ft.Text("Você falou Bonjour princess"),
        actions=[
            ft.TextButton("Próxima Questão", on_click=ir_para_proxima_questao),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    erro_registro = ft.AlertDialog(
        modal=True,
        title=ft.Text("Preencha todos os campos!!!"),
        content=ft.Text(""),
        actions=[
            ft.TextButton("OK", on_click=fechar_alerta_registro),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    def open_dlg_modal(e):
        page.dialog = dlg_modal
        dlg_modal.open = True
        page.update()
    botao_clicavel_jogando = ft.ElevatedButton("",opacity=0)
    botao_voltar_jogando = ft.Stack([
        ft.Image("Vector-removebg-preview.png",width=50,color="black"),
        botao_clicavel_jogando
    
    ])
    botao_facil =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="FÁCIL", size=30),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=200,
            height=60,bgcolor="#98f772",
            color="black"
        )
    botao_medio =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="MÉDIO", size=30),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=200,
            height=60,bgcolor="#f1f772",
            color="black"
        )
    botao_dificil =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="DIFÍCIL", size=30),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=200,
            height=60,bgcolor="#f77272",
            color="black"
        )
    text_dias_consecutivos = ft.Text("Você está jogando a 5 dias consecutivos",size=20,color="white")
    botao_clicavel = ft.ElevatedButton("",opacity=0)#botao em cima da seta de voltar
    botao_voltar = ft.Stack([
        ft.Image("Vector-removebg-preview.png",width=50),
        botao_clicavel
    
    ])#botao de voltar
    botao_voltar2 = ft.ElevatedButton("",opacity=0)
    botao_voltar_no_jogo = ft.Stack([
        ft.Image("Vector-removebg-preview.png",width=50,color="white"),
        botao_voltar2
    
    ])#botao de volta
    botao_voltar2.on_click = open_dlg_modal
    def voltar_usuario(e):
        page.go("/jogar")
    botao_clicavel_jogando.on_click = voltar_usuario
    botao_jogar =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="JOGAR", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=235,
            height=65
        )
    botao_configuracoes =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="CONFIGURAÇÕES", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=235,
            height=65
        )
    botao_sair =  ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(value="SAIR DA CONTA", size=20),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=5,
                ),
                padding=ft.padding.all(10),
            ),
            style=ft.ButtonStyle(#botao para login
            shape=ft.RoundedRectangleBorder(radius=20),color="black"),
            width=235,
            height=65
        )
    progressobar = ft.ProgressBar(value=0,width=250,height=30,color="#ffd600",border_radius=20,semantics_label="13/100")
    texto_exp = ft.Text("0/100",size=20)
    texto_estrela = ft.Container(ft.Icon(ft.icons.STAR,color="yellow"),alignment=ft.alignment.center,margin=ft.margin.all(0))
    texto_final = ft.Container(ft.Row([texto_exp,texto_estrela],alignment=ft.MainAxisAlignment.CENTER),alignment=ft.alignment.center,padding=0)
    progresso_bar = ft.Container(
        ft.Stack(
            [
            ft.Container(progressobar),
            ft.Container(texto_final,width=250,alignment=ft.alignment.center_right)
            ]
    
                 ),
        alignment=ft.alignment.center
        )
    page.fonts = {
        "Kanit": "https://raw.githubusercontent.com/google/fonts/master/ofl/kanit/Kanit-Bold.ttf",
        "Open Sans": "/fonts/OpenSans-Regular.ttf"
    }
    page.theme = Theme(font_family="Kanit")
    consulta = cursor.execute("SELECT * FROM usuarios3")
    consulta = consulta.fetchall()
    text_consecutivos = ft.Text("0",size=30)#caixa de texto para colocar quantidade de dias consecutivos
    text_mudar_usuario = ft.TextField(label = "Novo nome de usuário...",width=400,color=ft.colors.BLACK,border_color=ft.colors.BLACK)#caixa de seleção para mudar o nome de usuário
    botao_fechar_configuracoes = ft.IconButton(ft.icons.CLOSE)
    botao_novo_usuario = ft.ElevatedButton("CONFIRMAR",width=200)
    c = ft.Container(#Container da caixa de configurações
        content= ft.Column([ft.Row([ft.Container(botao_fechar_configuracoes,alignment=ft.alignment.top_right,width=700)]),ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                tab_content=ft.Container(ft.Text("MUDAR NOME DE USUÁRIO",color="black"),width=200,height=50,alignment=ft.alignment.center),
                content=ft.Container(ft.Column([
                ft.Container(ft.TextField(label="Novo nome de usuário...",text_align=ft.TextAlign.LEFT,width=400,label_style=ft.TextStyle(color="#7F7F7F"),border_color="black"),margin=ft.margin.only(top=20)),
                    ft.Container(content=ft.TextField(label="Confirmar nome de usuário...",text_align=ft.TextAlign.LEFT,width=400,label_style=ft.TextStyle(color="#7F7F7F"),border_color="black"))
                    ]),alignment=ft.alignment.center,margin=ft.margin.only(top=150))
            ),
            ft.Tab(
                tab_content=ft.Container(ft.Text("MUDAR SENHA",color="black"),width=200,height=50,alignment=ft.alignment.center),
                content=ft.Container(ft.Column([
                    ft.Container(ft.TextField(label="Senha atual...",text_align=ft.TextAlign.LEFT,width=400,label_style=ft.TextStyle(color="#7F7F7F")),alignment=ft.alignment.center),
                    ft.Container(content=ft.TextField(label="Nova senha...",text_align=ft.TextAlign.LEFT,width=400,label_style=ft.TextStyle(color="#7F7F7F")),alignment=ft.alignment.center),
                    ft.Container(content=ft.TextField(label="Confirmar nova senha...",text_align=ft.TextAlign.LEFT,width=400,label_style=ft.TextStyle(color="#7F7F7F")),alignment=ft.alignment.center),
                    ft.Container(ft.ElevatedButton("SALVAR",width=200),alignment=ft.alignment.center),
                    ]),alignment=ft.alignment.center,margin=ft.margin.only(top=150))
            ),
            ft.Tab(
                tab_content=ft.Container(ft.Text("MUDAR ÍCONE DE USUÁRIO",color="black"),width=200,height=50,alignment=ft.alignment.center),
                content=ft.Container(ft.Column([
                    ft.Container(content=ft.TextField(label = "Nova senha...",width=400),margin=ft.margin.only(top=20)),
                    ft.Container(content=ft.TextField(label ="Confirmar nova senha...",width=400))
                    ]),alignment=ft.alignment.center,margin=ft.margin.only(top=150))
            ),
        ],
        expand=1,
        indicator_tab_size=False,
        indicator_color="#E77A52"
    )]),
        width=700,
        height=0,
        animate=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT),
        alignment=ft.alignment.bottom_right,
        padding=ft.padding.only(top=0),
        bgcolor="white",
        border=ft.border.all(2,color=ft.colors.BLACK),
        border_radius=20
    )
    page.window_full_screen = True
    page.padding = 0
    page.title = "Routes Example"
    text_username: ft.TextField = ft.TextField(label="Usuário",text_align=ft.TextAlign.LEFT,width=240,label_style=ft.TextStyle(color="#E77A52"))
    text_password: ft.TextField = ft.TextField(label="Senha",text_align=ft.TextAlign.LEFT,width=240,password=True,label_style=ft.TextStyle(color="#E77A52"),can_reveal_password=True)
    button_submit: ft.ElevatedButton = ft.ElevatedButton(text="ENTRAR",width=200,color="white",bgcolor="#E77A52",style=ft.ButtonStyle(#botao para login
                shape=ft.RoundedRectangleBorder(radius=0),))
    
    botao_cadastro = ft.ElevatedButton(text="Cadastre-se",width=150,color="white",bgcolor="#C1846F",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),))
    text_confirmar_senha: ft.TextField = ft.TextField(label="Confirmar senha",text_align=ft.TextAlign.LEFT,width=240,password=True,label_style=ft.TextStyle(color="#E77A52"),can_reveal_password=True)
    button_registrar: ft.ElevatedButton = ft.ElevatedButton(text="Registrar",width=200,color="white",bgcolor="#E77A52",style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=0),))
    
    texto_ser_falado = ft.TextField(value=" ", text_align=ft.TextAlign.RIGHT, width=400)
    texto_certo_errado = ft.TextField(value=" ", text_align=ft.TextAlign.RIGHT, width=400)
    texto_erro = ft.Text(value="",color=ft.colors.RED_500)
    texto_acerto = ft.Text(value="",color=ft.colors.GREEN_500)
    progresso = ft.Slider(width=400,max=300)
    texto_pontuacao = ft.Text("0",size=30)#pontuacao do usuario
    text_level = ft.Text("0",size=30,color="white")#level do usuario
    text_nome_usuario = ft.Text("",size=30,color="white")
    level = ft.Text("0",size=30)
    pontuacao = ft.Text("0",size=30)
    def jogou(e):
            container_contagem.height = 50
            container_botao_falar.margin = ft.margin.only(top=0)
            for i in [3,2,1]:
                texto_contagem.value = f"{i}"
                time.sleep(1)
                page.update()
            time.sleep(1)
            container_botao_falar.height = 0
            container_contagem.height = 0
            container_texto_falado.height = 80
            page.update()
            page.dialog = errou_questão
            print("clicado")
            teste = texto_a_ser_falado.value
            r = sr.Recognizer()
            try:
                with sr.Microphone() as fonte:
                        r.adjust_for_ambient_noise(fonte,)
                        audio = r.listen(fonte, phrase_time_limit=3)
                        texto = r.recognize_google(audio, language="fr-FR")
                if texto.lower() == teste:
                    errou_questão.title = ft.Text("Parabéns você acertou!!")
                    errou_questão.content = ft.Text(f"Você falou {texto}")
                    errou_questão.open = True
                    page.go("/jogando_alternativa")
                    page.update()
                    
                    page.update()
                else:
                    page.dialog = errou_questão
                    errou_questão.title = ft.Text("Você errou!!")
                    errou_questão.content = ft.Text(f"Você falou {texto}")
                    errou_questão.open = True
                    page.update()
            except:
                    print("deu merda")
                    page.dialog = errou_audio
                    errou_audio.content = ft.Text(" ")
                    errou_audio.title = ft.Text("Não foi possível compreender o áudio")
                    errou_audio.open = True
                    texto_certo_errado.value = "não foi possível compreender o áudio"
                    page.update()
            page.update()
            
            page.update()
            page.update()
    botao_falar.on_click=jogou
    def update_usuario(e):#função para atualizar o nome do usuario no banco
        consulta = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_mudar_usuario.value,))
        sql = ''' UPDATE usuarios3
                SET usuario = ?
                WHERE usuario = ?'''
        cur = banco.cursor()
        res = consulta.fetchall()
        if len(res) == 0 and text_mudar_usuario.value != "":
            cur.execute(sql, (text_mudar_usuario.value,text_nome_usuario.value))
            banco.commit()
            text_mudar_usuario.value = ""
            page.update()
    botao_novo_usuario.on_click = update_usuario
    def progressoslider(e):
        progresso.value = texto_pontuacao.value
        page.update()
    def registrar_conta(e):#função para registrar uma conta
        consulta_usuarios = cursor.execute("SELECT usuario FROM usuarios3 WHERE usuario=?",(text_username.value,))
        res = consulta_usuarios.fetchall()
        if text_username.value != '' and text_password.value != '':
            if len(res) > 0:
                page.dialog = erro_registro
                erro_registro.open = True
                erro_registro.title = ft.Text("Usuario já cadastrado!!!",color="red")
                page.update()
            elif len(str(text_password.value)) < 5 or " " in str(text_password.value):
                page.dialog = erro_registro
                erro_registro.open = True
                erro_registro.title = ft.Text("Digite uma senha com no mínimo 5 dígitos!!!",color="red")
                page.update()
            elif text_password.value != text_confirmar_senha.value:
                page.dialog = erro_registro
                erro_registro.open = True
                erro_registro.title = ft.Text("As senhas não são iguais!!!",color="red")
                page.update()
            else:
                cursor.execute("INSERT INTO usuarios3(usuario,senha,level,pontuaçao,data,consecutivos,exp) VALUES (?,?,?,?,?,?,?)",(str(text_username.value),str(text_password.value),1,0,str(datetime.date.today()),0,0))
                banco.commit()
                texto_erro.value = ""
                texto_acerto.value = "Usuario cadastrado com sucesso,volte para o início para JOGAR!!"
                text_confirmar_senha.value = ''
                text_username.value = ''
                text_password.value = ''
                page.go("/")
                page.update()
                time.sleep(5)
                texto_acerto.value = ""   
        else:
            page.dialog = erro_registro
            erro_registro.open = True
            erro_registro.title = ft.Text("Preencha todos os campos!!!",color="red")
            page.update()
    def irParaRegistrar(e):
        page.go("/registrar")
    botao_cadastro.on_click = irParaRegistrar
    
    button_registrar.on_click = registrar_conta
    def ir_para_dificuldade(e):
        page.go("/dificuldade")
        page.update()
    def jogando(e):#função para aumentar a pontuação conforme o usuario vai jogando
        consulta = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_username.value,))
        pontuacao.value = str(int(pontuacao.value)+10)
       
        res = consulta.fetchall()
        if int(pontuacao.value) < 100:
            text_level.value = "level 1"
        elif int(pontuacao.value) < 1000 and int(pontuacao.value) >= 100:
            text_level.value = f"level {int(str(pontuacao.value)[0]) + 1}"
            
        elif int(pontuacao.value) >= 1000 and int(pontuacao.value) < 10000:
            text_level.value = f"level {int(str(pontuacao.value)[:2]) + 1}"
        elif int(pontuacao.value) >= 10000 and int(pontuacao.value) < 100000:
            text_level.value = f"level {int(str(pontuacao.value)[:3]) + 1}"
        else:
            text_level.value = f"level {int(str(pontuacao.value)[:4]) + 1}"
        if progressobar.value < 0.88:
            progressobar.value = progressobar.value + 0.1
            texto_exp.value = f"{str(int(round(progressobar.value*100)))}/100"
        else:
            progressobar.value = 0
            texto_exp.value = f"0/100"
        cursor.execute("UPDATE usuarios3 SET level=? WHERE usuario=?",(text_level.value[6:],text_nome_usuario.value))
        cursor.execute("UPDATE usuarios3 SET pontuaçao=? WHERE usuario=?",(pontuacao.value,text_nome_usuario.value))
        cursor.execute("UPDATE usuarios3 SET exp=? WHERE usuario=?",(progressobar.value,text_nome_usuario.value))
        consulta = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_username.value,))
        res = consulta.fetchall()
        data = res[0][4]
        string = data.split("-")
        ano = int(string[0])
        mes = int(string[1])
        dia = int(string[2])
        if datetime.date.today() - datetime.timedelta(days=1) == datetime.date(ano,mes,dia):
                    sql = ''' UPDATE usuarios3
                SET consecutivos = ?
                WHERE usuario = ?'''
                    consecutivos = int(res[0][5])
                    text_consecutivos.value = f"Dias seguidos:{consecutivos + 1}"
                    cursor.execute(sql,(consecutivos + 1,str(text_username.value)))
                    banco.commit()
        elif datetime.date.today() == datetime.date(ano,mes,dia):
                    consecutivos = int(res[0][5])
                    cursor.execute("UPDATE usuarios3 SET consecutivos = ? WHERE usuario = ?",(consecutivos,str(text_username.value)))
                    banco.commit()
        else:
                    cursor.execute("UPDATE usuarios3 SET consecutivos = ? WHERE usuario = ?",(0,str(text_username.value)))
                    banco.commit()
        cursor.execute("UPDATE usuarios3 SET data = ? WHERE usuario = ?",(str(datetime.date.today()),str(text_username.value)))
        banco.commit()
        page.update()
    botao_jogar.on_click = ir_para_dificuldade
    def jogar(e):#função para entrar na pagina de usuario confirmando o login
        consulta_usuarios = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_username.value,))
        res = consulta_usuarios.fetchall()
        if len(res) > 0:
            data = res[0][4]
            string = data.split("-")
            ano = int(string[0])
            mes = int(string[1])
            dia = int(string[2])
            if datetime.date.today() - datetime.timedelta(days=1) > datetime.date(ano,mes,dia):
                cursor.execute("UPDATE usuarios3 SET consecutivos = ? WHERE usuario = ?",(0,str(text_username.value)))
                banco.commit()
        else:
            page.dialog = erro_registro
            erro_registro.open = True
            erro_registro.title = ft.Text("Usuário não cadastrado!!!",color="red")
            page.update()
        
        contagem = len(res)
        if len(res) > 0:
            progresso.value = str(res[contagem-1][3])
            texto_pontuacao.value = f"Pontuação: {str(res[contagem-1][3])}"
            pontuacao.value = f"{str(res[contagem-1][3])}"
            text_level.value = f"Level {res[contagem-1][2]}"
            text_nome_usuario.value = text_username.value
            progressobar.value = float(res[0][6])
            texto_exp.value = f"{int(round(progressobar.value * 100))}/100"
            text_dias_consecutivos.value = f"Você está jogando a {res[0][5]} dias consecutivos"
        if len(res) > 0:
            jogador = str(res[0][1])
            if str(jogador) == str(text_password.value):
                page.go("/jogar")
                page.update()
            else:
                page.dialog = erro_registro
                erro_registro.open = True
                erro_registro.title = ft.Text("Senha incorreta!!!",color="red")
                page.update()
    def ir_para_jogando(e):#função para ir para a tela de jogo
        consulta_usuarios = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_nome_usuario.value,))
        res = consulta_usuarios.fetchall()
        contagem = len(res)
        progresso.value = str(texto_pontuacao.value)[11:]
        pontuacao.value = str(texto_pontuacao.value)[11:]
        level.value = str(text_level.value)[7:]
        
        page.update()
        page.go("/jogando")
    def fechar(e):#função para fechar a pagina
        page.go("/")
        text_username.value = ""
        text_password.value = ""
        page.update()
    botao_sair.on_click = fechar
    button_submit.on_click = jogar
    login = View(
                    "/",
                    [
                        ft.Container(ft.Stack([ #Container com imagem de fundo
                            ft.Image(
                src="./assets/Home Screan (3).png",
                fit="cover",
                height=770
            ),
                        ft.Container(ft.Container( #Container da caixa de login
                            content=ft.Column([
                                ft.Container(ft.Image(
                                                src=f"./assets/MicrosoftTeams-image__1_-removebg-preview.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.CONTAIN,
                                                )
                                     ,alignment=ft.alignment.center,width=300),
                                ft.Container(text_username,alignment=ft.alignment.center,width=300),
                        ft.Container(text_password,alignment=ft.alignment.center,width=300),
                        ft.Container(button_submit,alignment=ft.alignment.center,width=300),
                        ft.Container(botao_cadastro,alignment=ft.alignment.center,width=220,margin=ft.margin.only(bottom=30,left=(300-220)/2),
                                     opacity=1),
                    ],
                                              ft.MainAxisAlignment.CENTER),
                            alignment=ft.alignment.center,
                            bgcolor="#EBEAEA",width=600,
                            height=500,
                            opacity=1,
                            border=ft.border.all(3,color="#E77A52"),
                            border_radius=10),alignment=ft.alignment.center,height=page.window_height)]))
                                ]
                        
                )
    login.padding = 0
    opcoes_icones = [ft.Icon(ft.icons.HOME),ft.Icon(ft.icons.ABC),ft.Icon(ft.icons.MONEY_ROUNDED)]
    def animate_container(e):#função para abrir as configurações
        c.height = 600
        c.update()
        page.update()
    botao_configuracoes.on_click = animate_container
    def fechar_configuracoes(e):#função para fechar as configurações
        c.height = 0
        c.update()
        page.update()
    botao_fechar_configuracoes.on_click = fechar_configuracoes
    
    principal_jogo = View( #Não feita ainda
                    "/jogar",
                    [
                         ft.Container(
           ft.Stack([
                            ft.Image(
                src="./assets/Home Screan (3).png",
                fit="cover",
                height=770
            ),
                ft.Container(ft.Container(
                    ft.Column([
                        ft.Container(
                        ft.Container(ft.Row([
                            ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png",height=70),margin=ft.margin.only(left=15)),
                            ft.Container(ft.Container(text_nome_usuario,margin=ft.margin.only(right=50)),width=290,height=65,bgcolor="#E77A52",border_radius=40,margin=ft.margin.only(right=5),alignment=ft.alignment.center_right)
                        ]),bgcolor="white",width=400,height=70,border_radius=40,margin=ft.margin.only(right=0,top=10)),
                                     alignment=ft.alignment.top_right
                        )
                    ,ft.Column([
                        ft.Container(c,alignment=ft.alignment.center),
                    ft.Container( #Container da caixa de login
                        content=botao_jogar,
                            alignment=ft.alignment.center,
                            margin=ft.margin.only(top=(page.window_height-100)/3),
                            opacity=1,
                            border_radius=10),
                     ft.Container( #Container da caixa de login
                        content=botao_configuracoes,
                            alignment=ft.alignment.center,
                            opacity=1,
                            border_radius=10),
                      ft.Container( #Container da caixa de login
                        content=botao_sair,
                            alignment=ft.alignment.center,
                            opacity=1,
                            border_radius=10),
                    ft.Container(text_level,alignment=ft.alignment.center),
                    ft.Container(progresso_bar,alignment=ft.alignment.center),
                    ft.Container(text_dias_consecutivos,alignment=ft.alignment.center),])]),
                    alignment=ft.alignment.center)),
                
                
                    
                
                    ]),
                             
               alignment=ft.alignment.center ),
                    ]
                
    )
                    
                    
                    
    principal_jogo.padding = 0
    
    registrar =  View(
                    "/registrar",
                    [
                        ft.Container(ft.Stack([ #Container com imagem de fundo
                            ft.Container(ft.Image(
                src="./assets/Home Screan (3).png",
                fit="cover",
                height=770
                            )),
                        ft.Container(ft.Container( #Container da caixa de login
                            content=ft.Column([
                                ft.Container(botao_voltar,margin=ft.margin.only(bottom=0,left=15,top=15)),
                                ft.Container(ft.Image(
                                                src=f"./assets/MicrosoftTeams-image__1_-removebg-preview.png",
                                                width=300,
                                                height=200,
                                                fit=ft.ImageFit.CONTAIN,
                                                
                                                )
                                     ,alignment=ft.alignment.center,width=600,margin=ft.margin.only(bottom=0,top=-60)),
                                ft.Container(ft.Column([ft.Container(text_username,alignment=ft.alignment.center,width=300),
                        ft.Container(text_password,alignment=ft.alignment.center,width=300),
                        ft.Container(text_confirmar_senha,alignment=ft.alignment.center,width=300),
                        ft.Container(button_registrar,alignment=ft.alignment.center,width=220,margin=ft.margin.only(bottom=30,left=(300-220)/2),
                                     opacity=1)]),width=600,alignment=ft.alignment.center),
                    ]),
                            alignment=ft.alignment.center,
                            bgcolor="#EBEAEA",width=500,
                            margin=ft.margin.only(top=(page.window_height-400)/2,bottom=(page.window_height-200)/2),
                            opacity=1,
                            border=ft.border.all(3,color="#E77A52"),
                            border_radius=10),alignment=ft.alignment.center)]),
                                     )
                                ]
                        
                )
    selecionar_dificuldade = ft.View(
                "/dificuldade",
                [
                    
                    ft.Container(
           ft.Stack([
                            ft.Image(
                src="./assets/Home Screan (3).png",
                fit="cover",
                height=770
            ),        
                    ft.Container(
                        ft.Container(
                            ft.Container(ft.Row([
                            ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png",height=70),margin=ft.margin.only(left=15)),
                            ft.Container(ft.Container(text_nome_usuario,margin=ft.margin.only(right=50)),width=290,height=65,bgcolor="#E77A52",border_radius=40,margin=ft.margin.only(right=5),alignment=ft.alignment.center_right)
                        ]),bgcolor="white",width=400,height=70,border_radius=40),
                            width=400,
                            height=70,
                            alignment=ft.alignment.top_right,
                            bgcolor="white",
                            border_radius=40
                        ),
                        
                        
                        height=100,alignment=ft.alignment.center_right
                        
                        ),
                    ft.Container(
                        ft.Container(
                            ft.Column(
                                [
                                ft.Container(botao_voltar_jogando,margin=ft.margin.only(left=10,top=10)),
                                ft.Row([
                                    ft.Container(ft.Text("SELECIONE A DIFICULDADE",size=30,color="black"),margin=ft.margin.only(top=-50))
                                ],
                                    alignment=ft.MainAxisAlignment.CENTER),
                                ft.Column([
                                    ft.Container(botao_facil,alignment=ft.alignment.center,margin=ft.margin.only(bottom=20)),
                                    ft.Container(botao_medio,alignment=ft.alignment.center,margin=ft.margin.only(bottom=20)),
                                    ft.Container(botao_dificil,alignment=ft.alignment.center)
                                ]),
                                ft.Container(ft.Text("Obs: Quanto maior a dificuldade, mais estrelas você poderá ganhar!!",color="black",weight=ft.FontWeight.BOLD),margin=ft.margin.only(top=10,left=10))
                            ]),
                            width=600,
                            height=360,
                            bgcolor="white",
                            border_radius=20,
                            padding=0
                        ),height=page.window_height,alignment=ft.alignment.center
                       
                    )
             
                ],
            ))])
    
    def ir_para_jogo(e):
        texto = random.randint(0,4)
        texto_falado_indice.value = str(texto)
        print(texto_falado_indice.value)
        consulta = cursor_questoes.execute('SELECT * FROM questoes')
        res = consulta.fetchall()
        texto_questao = res[texto][0]
        texto_a_ser_falado.value = texto_questao
        page.update()
        page.go("/jogando")
    botao_facil.on_click = ir_para_jogo
    container_texto_falado = ft.Container(
                                        ft.Row([ft.Container(ft.Text("Fale: ",size=30,color="black",weight=ft.FontWeight.BOLD),margin=ft.margin.only(left=30)),ft.Container(texto_a_ser_falado,height=70,width=680,bgcolor="#E77A52",border_radius=50,alignment=ft.alignment.center)],alignment=ft.MainAxisAlignment.CENTER),
                                        height=0,
                                        border_radius=50,
                                        margin=ft.margin.only(top=50),
                                        bgcolor="white",
                                        alignment=ft.alignment.center_right
                                        
                                        )
    texto_contagem = ft.Text("",size=30,color="white")
    container_contagem = ft.Container(
        texto_contagem,
        height=0,
        alignment=ft.alignment.center
    )
    jogando_jogo_falando = ft.View(
                "/jogando",
                [
                    
           ft.Stack([
                            ft.Image(
                src="./assets/Game Screen (write).png",
                fit="cover",
                height=770
            ), 
                            
                    ft.Container(
                        ft.Container(
                            ft.Row([ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png"),alignment=ft.alignment.center,margin=ft.margin.only(left=10)),ft.Container(ft.Container(text_nome_usuario,margin=ft.margin.only(right=50)),width=295,height=65,bgcolor="#E77A52",border_radius=40,margin=ft.margin.only(right=5),alignment=ft.alignment.center_right)]),
                            width=400,
                            height=70,
                            alignment=ft.alignment.center_right,
                            bgcolor="white",
                            border_radius=40
                        ),
                        
                        
                        height=100,alignment=ft.alignment.center_right
                        
                        ),
                    
                    ft.Container(
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Stack([
                                    ft.Container(
                                        ft.Container(texto_pergunta,alignment=ft.alignment.center,width=500,bgcolor="white"),
                                        height=130,
                                        alignment=ft.alignment.center,
                                        margin=ft.margin.only(top=60)

                                    ),
                                    ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png",width=400,height=130),alignment=ft.alignment.center)
                                    ]),
                                    container_contagem,
                                    container_texto_falado
                                    ,
                                    container_botao_falar
                            ]),
                            width=800,
                            height=500,

                            border_radius=0,
                            padding=0
                        ),height=page.window_height,alignment=ft.alignment.center
                       
                    ),
                    ft.Container(botao_voltar_no_jogo,margin=ft.margin.only(left=10,top=10)),
             
                ],
            )])
    jogando_jogo_alternativa = ft.View(
                "/jogando_alternativa",
                [
                    
           ft.Stack([
                            ft.Image(
                src="./assets/Game Screen (write).png",
                fit="cover",
                height=770
            ), 
                            
                    ft.Container(
                        ft.Container(
                            ft.Row([ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png"),alignment=ft.alignment.center,margin=ft.margin.only(left=10)),ft.Container(ft.Container(text_nome_usuario,margin=ft.margin.only(right=50)),width=295,height=65,bgcolor="#E77A52",border_radius=40,margin=ft.margin.only(right=5),alignment=ft.alignment.center_right)]),
                            width=400,
                            height=70,
                            alignment=ft.alignment.center_right,
                            bgcolor="white",
                            border_radius=40
                        ),
                        
                        
                        height=100,alignment=ft.alignment.center_right
                        
                        ),
                    
                    ft.Container(
                        ft.Container(
                            ft.Column(
                                [
                                    ft.Stack([
                                    ft.Container(
                                        ft.Container(texto_pergunta,alignment=ft.alignment.center,width=500,bgcolor="white"),
                                        height=130,
                                        alignment=ft.alignment.center,
                                        margin=ft.margin.only(top=60)

                                    ),
                                    ft.Container(ft.Image("./assets/carangueijo_sem_fundo.png",width=400,height=130),alignment=ft.alignment.center)
                                    ]),
                                    ft.Container(
                                        ft.Row([ft.Container(ft.Text("Qual a tradução da frase: ",size=30,color="black",weight=ft.FontWeight.BOLD),margin=ft.margin.only(left=30)),ft.Container(texto_a_ser_falado,height=70,width=680,bgcolor="#E77A52",border_radius=50,alignment=ft.alignment.center)],alignment=ft.MainAxisAlignment.CENTER),
                                        height=75,
                                        border_radius=50,
                                        margin=ft.margin.only(top=50),
                                        bgcolor="white",
                                        alignment=ft.alignment.center_right
                                        
                                        ),
                                    ft.Container(botao_alternativa_A,alignment=ft.alignment.center,margin=ft.margin.only(top=30)),
                                    ft.Container(botao_alternativa_B,alignment=ft.alignment.center),
                                    ft.Container(botao_alternativa_C,alignment=ft.alignment.center),
                                    ft.Container(botao_alternativa_D,alignment=ft.alignment.center),
                                    
                            ]),
                            width=1100,
                            height=600,

                            border_radius=0,
                            padding=0
                        ),height=page.window_height,alignment=ft.alignment.center
                       
                    ),
                    ft.Container(botao_voltar_no_jogo,margin=ft.margin.only(left=10,top=10)),
             
                ],
            )])
    selecionar_dificuldade.padding=0
    registrar.window_full_screen = False
    def voltar_login(e):
        page.go("/")
    botao_clicavel.on_click = voltar_login
    registrar.padding = 0
    jogando_jogo_falando.padding = 0
    jogando_jogo_alternativa.padding = 0
    def route_change(e):
        page.views.clear()

        page.views.append(
            login
        )
        if page.route == "/":
            login.vertical_alignment = ft.MainAxisAlignment.CENTER
            login.horizontal_alignment =ft.CrossAxisAlignment.CENTER
            page.update()
            page.views.append(
                login
            )
        if page.route == "/jogar":
            consulta_usuarios = cursor.execute("SELECT * FROM usuarios3 WHERE usuario=?",(text_nome_usuario.value,))
            res = consulta_usuarios.fetchall()

            pontuacoes = res[0][3]
            levels = res[0][2]
            texto_pontuacao.value = f"Pontuação: {pontuacoes}"
            text_level.value = f"Level {levels}"
            text_level
            page.update()
            page.views.append(
                principal_jogo
            )
        if page.route == "/registrar":
            page.views.append(
                registrar
            )
        if page.route == "/dificuldade":
            page.views.append(
                selecionar_dificuldade
            )
        progresso.on_change = progressoslider
        if page.route == "/jogando":
            page.update()
            page.views.append(
                jogando_jogo_falando
            )
        if page.route == "/jogando_alternativa":
            page.update()
            page.views.append(
                jogando_jogo_alternativa
            )
    
        page.update()
    page.on_route_change = route_change
    page.go(page.route)
ft.app(main)