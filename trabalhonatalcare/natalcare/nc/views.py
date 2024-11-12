from django.shortcuts import *
from django.views import View
from django.contrib import messages
from .models import *
from django.contrib.auth import authenticate, login, logout
from .models import usuario
from django.contrib.auth.models import User

# Create your views here.
class cadastrousuario(View):
    def get(self, request):
        return render(request, 'site/cadastro/cad.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        telefone = request.POST.get('telefone')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')
        
        
        try:
            clin = clinica.objects.get(email=email, senha=senha)
            if clin:
                messages.error(request, 'Usuário já cadastrado como clínica')
                return render(request, 'site/cadastro/cad.html')
        except:
            try:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já está cadastrado.')
                    return render(request, 'site/cadastro/cad.html')
                else:
                    user = User.objects.create_user(
                    username=nome,
                    email=email,
                    first_name=nome,
                    password=senha
                    )
                    user.save()

                end = endereco.objects.create(logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, cep=cep, complemento=complemento)
                usu = usuario.objects.create(nome=nome, email=email, senha=senha, telefone=telefone, endereco=end, user=user, cpf=cpf)
                messages.success(request, 'Usuário cadastrado com sucesso')
                user = authenticate(request, username=usu.nome, password=senha)
                login(request, user)
                return render(request, 'site/menu/menu.html')
            except Exception as e:
                messages.error(request, 'Erro ao cadastrar usuário')
                return render(request, 'site/cadastro/cad.html')
            
class logusuario(View):
    def get(self, request):
        return render(request, 'site/login/log.html')
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            usu = usuario.objects.get(email=email, senha=senha)
            user = authenticate(request, username=usu.nome, password=senha)
            if user:
                login(request, user)
        except:
            messages.error(request, 'Usuário não encontrado')
            return render(request, 'site/login/log.html')
        return redirect('menu')

class cadastroclinica(View):
    def get(self, request):
        return render(request, 'site/cadastro/cad.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
        cnpj = request.POST.get('cnpj')
        telefone = request.POST.get('telefone')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        logradouro = request.POST.get('logradouro')
        numero = request.POST.get('numero')
        bairro = request.POST.get('bairro')
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        cep = request.POST.get('cep')
        complemento = request.POST.get('complemento')

        try:
            user = usuario.objects.get(email=email, senha=senha)
            if user:
                messages.error(request, 'Clínica já cadastrado como usuário')
            return render(request, 'site/cadastro/cad.html')
        except:
            try:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email já está cadastrado.')
                    return render(request, 'site/cadastro/cad.html')
                else:
                    user = User.objects.create_user(
                    username=nome,
                    email=email,
                    first_name=nome,
                    password=senha
                    )
                    user.save()

                end = endereco.objects.create(logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, cep=cep, complemento=complemento)
                clin = clinica.objects.create(nome=nome, cnpj=cnpj, telefone=telefone, email=email, senha=senha, endereco=end, user=user)
                messages.success(request, 'Clínica cadastrado com sucesso')
                user = authenticate(request, username=clin.nome, password=senha)
                login(request, user)
                return redirect('clind', id=clin.id)
            except Exception as e:
                messages.error(request, 'Erro ao cadastrar clínica')
                return render(request, 'site/cadastro/cad.html')
           
    
class logclinica(View):
    def get(self, request):
        return render(request, 'site/login/log.html')
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            usu = clinica.objects.get(email=email, senha=senha)
            user = authenticate(request, username=usu.nome, password=senha)
            if user:
                login(request, user)
        except:
            messages.error(request, 'Clínica não encontrada')
            return render(request, 'site/login/log.html')
        return redirect('clind', id=usu.id)

class logoutu(View):
    def get(self, request):
        logout(request)
        return render(request, 'site/login/log.html')

class menu(View):
    def get(self, request):
        if request.user.is_authenticated:
            hist = historico.objects.filter(usuario=request.user.usuario)
            return render(request, 'site/menu/menu.html', {"hist_usu": hist})
        else:
            return render(request, 'site/menu/menu.html')
    
    def post(self, request):
        try:
            clin = clinica.objects.get(nome=request.POST.get('pesqi'))
            if clin == clinica.objects.get(nome=clin.nome):
                hist = historico.objects.filter(usuario=request.user.usuario)
                if hist.count() == 3:
                    hist.first().delete()
                historico.objects.create(clinica=clin, usuario=request.user.usuario)
                hist = historico.objects.filter(usuario=request.user.usuario)
                return render(request, 'site/menu/menu.html', {"clinica": clin, "hist_usu": hist})
        except Exception as e:
            messages.error(request, f'Clínica não encontrada{e}')
            return render(request, 'site/menu/menu.html')
        

class mudar_senha_clin(View):
    def get(self, request):
        return render(request, 'site/senha/sen.html')
    
    def post(self, request):
        try:
            clin = clinica.objects.get(email=request.POST.get('email'))
            if request.POST.get('nsenha') == request.POST.get('csenha'):
                # breakpoint()
                clin.senha = request.POST.get('csenha')
                clin.save()
                return render(request, 'site/login/log.html')
            else:
                messages.error(request, 'As senhas tem que ser iguais')
                return render(request, 'site/senha/sen.html')
        except:
            messages.error(request, 'Clínica não encontrada')
            return render(request, 'site/senha/sen.html')

class perfil(View):
    def get(self, request):
        return render(request, 'site/perfil/perfil.html')
    
    def post(self, request):
        try:
            usu = request.user.usuario
            nome = request.POST.get('nome')
            telefone = request.POST.get('telefone')
            cpf = request.POST.get('cpf')
            email = request.POST.get('email')
            logradouro = request.POST.get('logradouro')
            numero = request.POST.get('numero')
            complemento = request.POST.get('complemento')
            cep = request.POST.get('cep')
            bairro = request.POST.get('bairro')
            cidade = request.POST.get('cidade')
            estado = request.POST.get('estado')
            usu.nome = nome
            usu.telefone = telefone
            usu.cpf = cpf
            usu.email = email
            usu.endereco.logradouro = logradouro
            usu.endereco.numero = numero
            usu.endereco.complemento = complemento
            usu.endereco.cep = cep
            usu.endereco.bairro = bairro
            usu.endereco.cidade = cidade
            usu.endereco.estado = estado
            usu.endereco.save()
            usu.save()
            messages.success(request, "Dados atualizados!")
            return render(request, 'site/perfil/perfil.html')
        except:
            messages.error(request, "deu bo familia")
            return render(request, 'site/perfil/perfil.html')

class resultados(View):
    def get(self, request):
        return render(request, 'site/pesquisa/pesq.html', {"esp": especialidades.objects.all(), "plan": plano.objects.all()})
    
    def post(self, request):
        i = request.POST.get("pesqi")
        p = request.POST.get("plan")
        e = request.POST.get("esp")
        # respe = clinica.objects.filter(plano=p, especialidades=e)
        resp = clinica.objects.filter(plano__in=plano.objects.filter(id=p))
        rese = clinica.objects.filter(especialidades__in=especialidades.objects.filter(id=e))
        resi = clinica.objects.filter(nome=i)
        return render(request, 'site/pesquisa/pesq.html', {"espec": rese, "plano": resp, "inpu": resi, "esp": especialidades.objects.all(), "plan": plano.objects.all()})
    
class clin_dados(View):
    def get(self, request, id):
        idclin = id
        clind = clinica.objects.get(id=idclin)
        esp = []
        plan = []
        for i in especialidades.objects.all():
            clin = clinica.objects.filter(id=idclin, especialidades__in=especialidades.objects.filter(id=i.id))
            if clin:
                esp.append(i)

        for i in plano.objects.all():
            clin = clinica.objects.filter(id=idclin, plano__in=plano.objects.filter(id=i.id))
            if clin:
                plan.append(i)

        teste = historico.objects.get(clinica=clind, usuario=request.user.usuario)
        if not teste:
            hist = historico.objects.filter(usuario=request.user.usuario)
            if hist.count() == 3:
                hist.first().delete()
            historico.objects.create(clinica=clind, usuario=request.user.usuario)


        

        return render(request, 'site/clinica/clin.html', {"clind": clind, "esp": esp, "plan": plan})
    

    
