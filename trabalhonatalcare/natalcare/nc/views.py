from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import usuario, clinica, endereco

# Create your views here.
class cadastrousuario(View):
    def get(self, request):
        return render(request, 'site/cadastro/cad.html')
    
    def post(self, request):
        nome = request.POST.get('nome')
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
            end = endereco.objects.create(logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, cep=cep, complemento=complemento)
            user = usuario.objects.create(nome=nome, email=email, senha=senha, telefone=telefone, endereco=end)
        except Exception as e:
            messages.error(request, 'Erro ao cadastrar usuário')
            clin = clinica.objects.get(email=email, senha=senha)
            if clin:
                messages.error(request, 'Usuário já cadastrado como clínica')
            return render(request, 'site/cadastro/cad.html')
        messages.success(request, 'Usuário cadastrado com sucesso')
        return render(request, 'site/menu/menu.html')

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
            end = endereco.objects.create(logradouro=logradouro, numero=numero, bairro=bairro, cidade=cidade, estado=estado, cep=cep, complemento=complemento)
            clin = clinica.objects.create(nome=nome, cnpj=cnpj, telefone=telefone, email=email, senha=senha, endereco=end)
        except:
            messages.error(request, 'Erro ao cadastrar clínica')
            user = usuario.objects.get(email=email, senha=senha)
            if user:
                messages.error(request, 'Clínica já cadastrado como usuário')
            return render(request, 'site/cadastro/cad.html')
        messages.success(request, 'Clínica cadastrado com sucesso')
        return render(request, 'site/menu/menu.html')

class logusuario(View):
    def get(self, request):
        return render(request, 'site/login/log.html')
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            user = usuario.objects.get(email=email, senha=senha)
        except:
            messages.error(request, 'Usuário não encontrado')
            return render(request, 'site/login/log.html')
        return render(request, 'site/menu/menu.html')
        
class logclinica(View):
    def get(self, request):
        return render(request, 'site/login/log.html')
    
    def post(self, request):
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        try:
            clin = clinica.objects.get(email=email, senha=senha)
        except:
            messages.error(request, 'Clínica não encontrada')
            return render(request, 'site/login/log.html')
        return render(request, 'site/menu/menu.html')

class menu(View):
    def get(self, request):
        return render(request, 'site/menu/menu.html')
    
    def post(self, request):
        try:
            clin = clinica.objects.get(nome=request.POST.get('clin_name').title())
            if clin == clinica.objects.get(nome=clin.nome):
                return render(request, 'site/menu/menu.html', {"clinica": clin})
        except:
            messages.error(request, 'Clínica não encontrada')
            return render(request, 'site/menu/menu.html')

