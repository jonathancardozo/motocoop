# 🏍️ MotoCoop

Sistema de gestão de mototáxi via bot de WhatsApp focado no trabalho colaborativo, na emancipação dos trabalhadores.

## 📌 Sobre o Projeto

Este software foi idealizado para modernizar o transporte por motocicletas em cidades do interior, substituindo as centrais analógicas por um fluxo digital justo. Diferente de grandes plataformas, o foco aqui é a emancipação do trabalhador, garantindo que a tecnologia seja uma ferramenta de apoio à categoria, e não apenas de extração de lucro.

## 🎯 Objetivo do MVP
## 🗺️ Roadmap de Implementação (MVP)


1. **Domínio e Casos de Uso**
	- [x] Implementar entidades: Corrida, Motorista, Cliente, Central, Value Objects.
	- [x] Definir interfaces de repositórios (ICorridaRepository, IMotoristaRepository, etc).
	- [x] Implementar casos de uso: solicitar corrida, aceitar/recusar, concluir/cancelar, gerenciar fila, cadastrar motorista/cliente.

2. **Infraestrutura**
	- [ ] Criar models SQLAlchemy para entidades.
	- [ ] Implementar repositórios concretos (banco de dados).
	- [ ] Configurar conexão e migrations (Alembic).
	- [ ] Implementar cliente Evolution API (envio/recebimento WhatsApp).
	- [ ] Implementar cache de fila com Redis.
	- [ ] Implementar serviço de geolocalização (geopy/PostGIS).

3. **Apresentação (API)**
	- [ ] Criar endpoints REST para corridas, motoristas, clientes.
	- [ ] Implementar webhooks para integração Evolution API.
	- [ ] Definir schemas Pydantic e handlers de mensagens.

4. **Testes**
	- [x] Testes unitários para entidades e casos de uso.
	- [ ] Testes de integração para repositórios e API.
	- [ ] Testes end-to-end para fluxo completo.

5. **Configuração e DevOps**
	- [ ] Ajustar .env e settings.py.
	- [ ] Configurar logging.
	- [ ] Garantir qualidade com Black, Ruff, mypy, pre-commit.

6. **Validação**
	- [ ] Testar fluxo completo: cliente solicita corrida → motorista aceita → corrida concluída.
	- [ ] Validar integração WhatsApp (Evolution API).
	- [ ] Validar persistência no banco e fila.

**Funcionalidade Núcleo:** Cliente solicita corrida via WhatsApp → Sistema despacha para motorista disponível → Motorista aceita → Corrida realizada.

### Escopo Mínimo Viável
- Cliente envia localização e destino via WhatsApp
- Sistema identifica central pela localização do cliente
- Despacho para próximo motorista disponível na fila
- Motorista aceita/recusa corrida
- Registro básico da corrida no banco de dados
- Confirmação de conclusão

### Funcionalidades Futuras (Fases Incrementais)
- **Fase 2**: Comandos avançados motorista (/pausa, /sair, status)
- **Fase 3**: Cálculo automático de preço e distância
- **Fase 4**: Histórico e relatórios para motoristas
- **Fase 5**: Dashboard web administrativo
- **Fase 6**: Sistema de avaliações e segurança
- **Fase 7**: Multi-centrais e múltiplas cidades

## 📋 Regras de Negócio

### Distribuição de Corridas
- Sistema de **fila FIFO** (primeiro a entrar, primeiro a receber)
- Regras transparentes podem priorizar motoristas mais próximos da origem da corrida
- Em caso de recusa, a corrida passa para o próximo da fila

### Precificação
- Valor **configurável** por central no MVP
- Visão futura: precificação baseada em custos sociais, definida democraticamente pela categoria (modelo similar a leilão reverso)

### Estados da Corrida
- `SOLICITADA` - Cliente fez o pedido
- `DESPACHADA` - Enviada ao(s) motorista(s) na fila
- `ACEITA` - Motorista confirmou atendimento
- `EM_ANDAMENTO` - Viagem iniciada
- `CONCLUÍDA` - Viagem finalizada com sucesso
- `CANCELADA_CLIENTE` - Cliente cancelou antes da aceitação
- `CANCELADA_MOTORISTA` - Motorista recusou/cancelou
- `EXPIRADA` - Sem resposta no tempo limite

### Dados Essenciais das Viagens
O sistema registra para cada corrida:
- ID único e timestamps (solicitação, início, conclusão)
- Origem e destino (endereços + coordenadas GPS)
- Motorista e cliente (números WhatsApp vinculados)
- Valor cobrado e forma de pagamento
- Status final da corrida
- Tempo de espera e duração da viagem
- Motivo em caso de cancelamento
- Distância percorrida

### Estrutura Organizacional
- **Centrais**: Uma ou mais centrais podem operar por cidade
- **Demarcação Geográfica**: Cada central tem área de atuação definida
- **Administração**: Usuário com papel de administrador gerencia a central
- **MVP**: Foco em uma central, uma cidade

## 🛠️ Stack Tecnológico

### Core
- **Python 3.11+** - Linguagem principal (recomendado 3.11 ou 3.12)
- **FastAPI** - Framework web async, alto desempenho, OpenAPI automático
- **Poetry** - Gerenciamento de dependências e ambientes virtuais
- **Pydantic 2.x** - Validação de dados e serialização

### Banco de Dados
- **PostgreSQL 15+** - Banco principal
- **SQLAlchemy 2.0** - ORM com suporte async
- **Alembic** - Migrations e versionamento de schema
- **PostGIS** - Extensão para queries geoespaciais

### Integração WhatsApp
- **Evolution API** - API auto-hospedável para WhatsApp
- **httpx** - Cliente HTTP async para comunicação com Evolution API

### Cache e Filas
- **Redis** - Cache de sessões, controle de fila de motoristas em memória

### Geolocalização
- **geopy** - Cálculo de distâncias e geocoding
- **PostGIS** - Índices espaciais para buscas por proximidade

### Qualidade e Testes
- **pytest** - Framework de testes
- **pytest-asyncio** - Suporte a testes async
- **Black** - Formatador de código
- **Ruff** - Linter moderno e rápido
- **mypy** - Type checking estático
- **pre-commit** - Hooks de qualidade de código

### DevOps
- **Docker** - Containerização
- **Docker Compose** - Orquestração local (PostgreSQL, Redis, Evolution API)
- **python-dotenv** - Gestão de variáveis de ambiente

## 🏗️ Arquitetura e Princípios

### Clean Architecture + Organização Híbrida
O projeto adota uma **abordagem híbrida**: mantém as camadas da Clean Architecture (domain, application, infrastructure, presentation) com features organizadas dentro de cada camada. Isso garante separação de responsabilidades técnicas e facilita a localização de código por funcionalidade.

```
motocoop/
├── src/
│   ├── domain/                    # Camada de Domínio (regras de negócio puras)
│   │   ├── corridas/
│   │   │   ├── __init__.py
│   │   │   ├── entities.py        # Corrida, ItemCorrida
│   │   │   ├── value_objects.py   # Localizacao, StatusCorrida
│   │   │   └── repositories.py    # Interface ICorridaRepository
│   │   ├── motoristas/
│   │   │   ├── __init__.py
│   │   │   ├── entities.py        # Motorista
│   │   │   ├── value_objects.py   # StatusMotorista, Veiculo
│   │   │   └── repositories.py    # Interface IMotoristaRepository
│   │   ├── clientes/
│   │   │   ├── __init__.py
│   │   │   ├── entities.py        # Cliente
│   │   │   └── repositories.py    # Interface IClienteRepository
│   │   ├── centrais/
│   │   │   ├── __init__.py
│   │   │   ├── entities.py        # Central, AreaCobertura
│   │   │   └── repositories.py    # Interface ICentralRepository
│   │   ├── shared/                # Tipos e exceções compartilhadas
│   │   │   ├── exceptions.py
│   │   │   ├── types.py
│   │   │   └── value_objects.py
│   │   └── __init__.py
│   │
│   ├── application/               # Camada de Aplicação (casos de uso)
│   │   ├── corridas/
│   │   │   ├── __init__.py
│   │   │   ├── solicitar_corrida.py
│   │   │   ├── aceitar_corrida.py
│   │   │   ├── recusar_corrida.py
│   │   │   ├── concluir_corrida.py
│   │   │   └── cancelar_corrida.py
│   │   ├── motoristas/
│   │   │   ├── __init__.py
│   │   │   ├── cadastrar_motorista.py
│   │   │   ├── entrar_fila.py
│   │   │   └── gerenciar_status.py
│   │   ├── clientes/
│   │   │   ├── __init__.py
│   │   │   └── cadastrar_cliente.py
│   │   ├── fila/
│   │   │   ├── __init__.py
│   │   │   ├── gerenciar_fila.py
│   │   │   └── despachar_corrida.py
│   │   ├── shared/                # DTOs e interfaces de serviços
│   │   │   ├── dtos.py
│   │   │   └── interfaces.py
│   │   └── __init__.py
│   │
│   ├── infrastructure/            # Camada de Infraestrutura (implementações)
│   │   ├── database/
│   │   │   ├── models/            # SQLAlchemy models
│   │   │   │   ├── corrida.py
│   │   │   │   ├── motorista.py
│   │   │   │   ├── cliente.py
│   │   │   │   └── central.py
│   │   │   ├── repositories/      # Implementações concretas
│   │   │   │   ├── corrida_repository.py
│   │   │   │   ├── motorista_repository.py
│   │   │   │   ├── cliente_repository.py
│   │   │   │   └── central_repository.py
│   │   │   ├── connection.py      # Database engine e session
│   │   │   └── migrations/        # Alembic migrations
│   │   ├── whatsapp/
│   │   │   ├── __init__.py
│   │   │   ├── client.py          # Cliente Evolution API
│   │   │   ├── handlers/          # Handlers de mensagens
│   │   │   │   ├── cliente_handler.py
│   │   │   │   └── motorista_handler.py
│   │   │   └── formatters.py      # Formatação de mensagens
│   │   ├── cache/
│   │   │   ├── __init__.py
│   │   │   ├── redis_client.py
│   │   │   └── fila_service.py    # Gestão de fila em Redis
│   │   ├── geolocation/
│   │   │   ├── __init__.py
│   │   │   └── service.py         # Cálculos de distância, geocoding
│   │   └── __init__.py
│   │
│   ├── presentation/              # Camada de Apresentação (APIs e UI)
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── corridas/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── routes.py
│   │   │   │   │   └── schemas.py  # Pydantic schemas
│   │   │   │   ├── motoristas/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── routes.py
│   │   │   │   │   └── schemas.py
│   │   │   │   ├── clientes/
│   │   │   │   │   ├── __init__.py
│   │   │   │   │   ├── routes.py
│   │   │   │   │   └── schemas.py
│   │   │   │   └── webhooks/       # Webhooks Evolution API
│   │   │   │       ├── __init__.py
│   │   │   │       └── routes.py
│   │   │   ├── dependencies.py     # Dependency injection
│   │   │   └── main.py             # FastAPI app
│   │   └── __init__.py
│   │
│   ├── config/                    # Configurações
│   │   ├── __init__.py
│   │   ├── settings.py            # Pydantic Settings
│   │   └── logging.py
│   │
│   └── __init__.py
│
├── tests/                         # Testes espelhando estrutura src/
│   ├── unit/
│   │   ├── domain/
│   │   ├── application/
│   │   └── infrastructure/
│   ├── integration/
│   └── e2e/
│
├── docker/                        # Dockerfiles e compose
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── docker-compose.dev.yml
│
├── scripts/                       # Scripts utilitários
│   ├── init_db.py
│   └── seed_data.py
│
├── .env.example                   # Exemplo de variáveis de ambiente
├── .gitignore
├── pyproject.toml                 # Poetry dependencies
├── poetry.lock
├── README.md
└── LICENSE
```

### Justificativa da Organização Híbrida

**Vantagens:**
- ✅ **Camadas claras**: Mantém princípios da Clean Architecture
- ✅ **Features coesas**: Código de corridas está em `domain/corridas/`, `application/corridas/`, `api/v1/corridas/`
- ✅ **Navegação intuitiva**: Fácil localizar código por feature ou por responsabilidade técnica
- ✅ **Escalabilidade**: Adicionar novas features (Fase 2, 3...) sem reestruturar projeto
- ✅ **Código compartilhado**: `shared/` dentro de cada camada para reutilização
- ✅ **Testabilidade**: Estrutura de testes espelha estrutura de código

### Princípios SOLID
- **Single Responsibility**: Cada classe/módulo com responsabilidade única
- **Open/Closed**: Aberto para extensão, fechado para modificação
- **Liskov Substitution**: Interfaces bem definidas
- **Interface Segregation**: Interfaces específicas
- **Dependency Inversion**: Dependência de abstrações, não implementações

### Padrões de Design
- **Repository Pattern**: Abstração de acesso a dados
- **Service Layer**: Lógica de negócio isolada
- **Dependency Injection**: Inversão de controle
- **Unit of Work**: Transações atômicas
- **Factory Pattern**: Criação de objetos complexos

## 🤝 Propósito Social

O objetivo é fortalecer a economia local, oferecendo uma infraestrutura tecnológica que permita aos mototaxistas autônomos e pequenas centrais competirem com grandes corporações, mantendo a governança e os ganhos na mão de quem trabalha.

## 🔴 Pontos Pendentes

Questões importantes a serem definidas antes do desenvolvimento:

1. **Autenticação e Segurança**: Definir método de vínculo seguro entre número de WhatsApp e identidade do usuário (motorista/cliente)
2. **Modelo de Sustentabilidade**: Estabelecer metodologia de cobrança de taxa de manutenção para viabilidade do projeto
3. **Licenciamento e Propriedade**: Decidir modelo de licença open source e garantias de que o controle permanecerá com os trabalhadores
4. **Governança Futura**: Definir processo democrático de eleição de administradores e tomada de decisões sobre o sistema