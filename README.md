
# 📊🔗 Projeto DataTrio: Integração de SQL, Python e Power BI na Prática

Um pipeline completo de dados que:

Cria um banco SQL relacional (modelado do zero) 📈

Popula com dados realistas gerados via Python (Pandas + Faker) 🐍

Transforma em insights através de um dashboard interativo no Power BI. 🗃️

Código reproduzível e documentação clara.


## Para Quem É Útil?
👨‍💻 Para analistas de dados

🎓 Estudantes de SQL/Python

👔 Gestores que precisam de insights
## Aprendizados

Construir esse projeto foi como montar um quebra-cabeça onde algumas peças não se encaixavam de primeira. Precisei desmontar partes inteiras porque a modelagem do banco não conversava com as necessidades do dashboard. No Power BI, medidas DAX que pareciam lógicas no papel simplesmente não funcionavam na prática - foi na base do tentativa e erro.

No final, o que salvou foi:

Testar cada parte separadamente

Documentar tudo (até os erros)

Não confiar cegamente nos dados sintéticos.

## Desafios Comuns (e Como Resolvi) 
❌Chaves estrangeiras esquecidas no SQL → Descobri só quando o Python tentou inserir dados e quebrou. ✅Solução: Revisei o CREATE TABLE e adicionei as FOREIGN KEYs faltantes.

❌Dados duplicados no Python → O script de inserção gerava registros repetidos. 
✅Solução: Adicionei uma verificação com pandas.drop_duplicates().

❌Medida DAX que quebrava o PBI → Fórmula complexa travava o dashboard. ✅Solução: Dividi em medidas menores.

❌Nome de colunas inconsistentes → No SQL era produto_id, no Python id_produto. ✅Solução: Padronizei os nomes antes de começar.

❌Arquivo .pbix pesado → Dashboard lento ao abrir. ✅Solução: Removi visualizações não usadas e compactei os dados.

✔️ Git não é backup – Commitei arquivos temporários e baguncei o repositório. Agora uso .gitignore desde o começo e verifico com git status antes de enviar.
## 🛠️ Tecnologias Utilizadas
🗃️ Banco de Dados (SQL).
Banco relacional do zero com tabelas normalizadas.

🐍 Python (Tratamento de Dados)
Gerei dados realistas com a biblioteca Faker.
Tratamento com Pandas (limpeza, transformações).
Scripts automatizados para popular o banco

📊 Visualização (Power BI + DAX)
Dashboard interativo com KPIs estratégicos.
Fórmulas DAX personalizadas para métricas complexas.
Design focado em clareza e insights acionáveis.

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](www.linkedin.com/in/matheus-santana-7bb727318
)
