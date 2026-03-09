FastAPI 

API REST desenvolvida com **FastAPI** para gerenciamento de **usuários, cursos e matrículas**.
---

Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

---

Estrutura do projeto

```
app/
 ├ controllers
 ├ services
 ├ repositories
 ├ entities
 ├ schemas
 ├ infrastructure
 └ utils
```

Cada camada possui responsabilidades bem definidas:

**Controllers** → endpoints da API
**Services** → regras de negócio
**Repositories** → acesso ao banco de dados
**Entities** → modelos ORM
**Schemas** → validação de dados
**Infrastructure** → configuração do banco

---

Instalação

Clone o repositório:

```
git clone https://github.com/AkiraWake/fast_curso_validacao.git
```

Entre na pasta do projeto:

```
cd fast_curso_validacao
```

Instale as dependências:

```
pip install fastapi uvicorn sqlalchemy pydantic
```

---

Executar a API

```
uvicorn app.main:app --reload
```

---

Documentação

Após iniciar a aplicação, acesse:

```
http://127.0.0.1:8000/docs
```
---

Funcionalidades

CRUD de usuários
CRUD de cursos
Criação de matrículas
Validação de email único
Prevenção de matrículas duplicadas
Validação de existência de usuário e curso

---

Autor

Gabriel Martins
