# rpa-denuncia-nao-me-ligue-procon-sp

Esse repositório mantém um RPA que elaborei para denunciar no sistema **Não Me Ligue** do **PROCON-SP** as operadoras que vem me ligando em torno de mais de 40 vezes por dia para me encher o saco oferecendo seus serviços (que eu já disse não estar interessado em adquirir).

### Objetivo

Eu espero fortemente que de certa forma isso ajude e incentive outras pessoas a denunciar situações como essa, que em minha visão já deveriam estar sendo resolvidas mais rapidamente pela nossa digníssima **ANATEL** por já possuir todo o sistema base necessário para multar a empresa nesse caso (como cadastro nos devidos sistemas para não me ligarem, solicitação legal junto à empresa pedindo para que meu número seja retirado da lista de marketing, denuncia nos órgãos competentes, etc, etc).

### Pré-requisitos

- Estar de saco cheio de ficar recebendo ligações de operadoras telecom ofertando produtos
- Cadastro do seu telefone no sistema [Não Me Ligue](https://bloqueio.procon.sp.gov.br/) com mais de 30 dias
- Python v3.9 (ou superior)
- pip (gerenciador de pacotes Python)

### Setup

No arquivo `auth_user.py`, preencha seu <u>usuário</u> e <u>senha</u> do sistema **Não Me Ligue**.

No arquivo `phone_number_list.csv` da pasta `files`, preencha os dados referentes aos números das empresas que não param de te encher o saco (**tem uns exemplos lá, lembre-se de seguir o mesmo padrão**).

Instale o módulo **requests**:

```bash
pip install requests
```

### Executando o RPA

Execute o programa conforme as operadoras que estão te enchendo o saco:

```bash
python generate_report_by_call_id.py
```

### Links importantes

- https://bloqueio.procon.sp.gov.br