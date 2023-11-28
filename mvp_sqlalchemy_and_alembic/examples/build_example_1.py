from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from faker import Faker
from pprint import pprint

faker = Faker('pt_BR')

# Declarando credenciais OBS: Não é uma boa prática, não é aceitável, utilize
# variáveis de ambiente.

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "test_sqlalchemy_db"

# Construindo o endereço para conexão.

db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

# Crie uma instância do SQLAlchemy Engine, faz a conexão. O uso de 'echo' como
# True é usado para imprimir mensagens no console que representam as operações
# SQL executadas pelo SQLAlchemy. 

engine = create_engine(db_url, echo=True)

# 'sessionmaker' retorna uma classe, por esse motivo escrevemos em letra
# maiúscula. A função principal de 'sessionmaker' é configurar a forma como as
# sessões são criadas.

Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

# Criando uma tabela


class Clientes(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone_number = Column(String)
    email = Column(String)

    def __repr__(self):
        return (
            f'Clientes(name={self.name},'
            f'phone_number={self.phone_number},'
            f'email={self.email})'
        )

# O 'create_all' cria uma tabela caso ela não exista, porém não atualiza
# caso mais campos sejam adicionados.

Base.metadata.create_all(engine)

c1 = Clientes(
    name=faker.company(),
    phone_number=faker.cellphone_number(),
    email=faker.ascii_company_email()
)

c2 = Clientes(
    name=faker.company(),
    phone_number=faker.cellphone_number(),
    email=faker.ascii_company_email()
)

c3 = Clientes(
    name=faker.company(),
    phone_number=faker.cellphone_number(),
    email=faker.ascii_company_email()
)

c4 = Clientes(
    name=faker.company(),
    phone_number=faker.cellphone_number(),
    email=faker.ascii_company_email()
)

# .add adiciona apenas um dado.

session.add(c1)

# .add_all adiciona vários registros por meio de uma lista.

session.add_all([c2, c3])

# .commit persiste as alterações.

session.commit()

session.add(c4)

# .flush não persiste nada desde o último .commit
# Portanto, o .flush() é útil quando você deseja garantir que as alterações
# até um determinado ponto sejam enviadas ao banco de dados, mas ainda deseja
# manter a opção de fazer mais alterações antes de confirmar definitivamente 
# essas alterações.

session.flush()

# Realizando algumas querys, isso está relacionado com '__repr__'. Não tenho
# a mínima ideia de como isso funciona, apenas sei que tem relação como
# orientação a objetos.

pprint(session.query(Clientes).all())
pprint(session.query(Clientes).first())
