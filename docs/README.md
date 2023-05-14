# Documento Principal do Projeto

# OBSERVAÇÃO:

Recomenda-se fortemente a correção e/ou leitura do documento pelo <a href="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/T4_G5_V1_PLN_Document.pdf">T4_G5_V1_PLN_Document.pdf</a>, onde apresenta-se o conteúdo formatado e estruturado, mediante os critérios do escritório de projeto.

# Controle de documentação

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Controle%20de%20Documento.png"> 

# 1. Introdução

As redes sociais estão cada dia mais presentes no cotidiano dos indivíduos, e com essa crescente popularidade as empresas precisam se adequar a esse ambiente. Tais plataformas tornam possível a conexão entre as organizações e seus clientes, sendo um ponto alto para receber feedbacks sobre seus produtos e serviços. Antes, as organizações precisavam se limitar a pesquisas de mercado e estudos de opinião para entender as necessidades e desejos de seus clientes. Hoje, mais de 4,7 bilhões de pessoas têm acesso a essas redes, o que representa 59% da população mundial. Dito isso, o banco BTG Pactual, percebeu a importância dessa tendência e decidiu adotar uma abordagem inovadora para coletar e analisar os comentários dos usuários sobre suas campanhas.</p>

Com mais de 1.642 milhões de clientes, o BTG Pactual, um dos maiores bancos de investimento da América Latina, reconheceu o impacto que as redes sociais podem ter sobre seus negócios, reconhecendo que uma das formas mais eficazes de melhorar seus produtos e serviços, é ouvindo seus clientes. Para isso, cada campanha de marketing passa por um processo criativo extenso para garantir que os resultados esperados pelas postagens sejam atingidos. A fim de conseguir tais insights, o BTG firmou uma parceria com a Inteli para utilizar o Processamento de Linguagem Natural (PLN) e criar um modelo de análise de sentimentos e detecção de palavras-chave em comentários nas redes sociais. 

Com o modelo PLN em operação, o BTG Pactual poderá entender as opiniões dos usuários sobre determinadas campanhas de marketing e obter feedbacks valiosos. Essas informações permitirão que o banco amplifique os resultados de suas campanhas e melhore a qualidade de seus serviços para atender às necessidades dos clientes de forma mais eficiente. Além disso, será possível identificar tendências e padrões nos comentários dos usuários e, assim, ajustar suas campanhas em tempo real.
  
## 1.1 Parceiro de Negócios

O BTG Pactual é o maior Banco de investimentos da América Latina e atua nos mercados de Investment Banking, Corporate Lending, Sales & Trading, Wealth Management e Asset Management. Desde sua criação, em 1983, o BTG Pactual tem sido administrado com base na cultura meritocrática de partnership, com foco no cliente, excelência e visão de longo prazo. O Banco se consolidou como uma das empresas mais inovadoras do setor, tendo conquistado diversos prêmios nacionais e internacionais. Atualmente, conta com quase 3 mil colaboradores em escritórios espalhados pelo Brasil, Chile, Argentina, Colômbia, Peru, México, Estados Unidos, Portugal e Inglaterra. 

Os principais critérios para o desenvolvimento do projeto é a necessidade de analisar o desenvolvimento das campanhas de marketing da empresa, visando atrair maiores insights sobre padrões e tendências dos seus clientes. 

## 1.2 Definição do Problema

Segue a definição do problema, com uma descrição clara e objetiva da questão ou desafio que precisa ser resolvido. Incluindo informações sobre o contexto, a natureza do problema e o impacto esperado da solução. Tal definição é necessária para colaborar na eficiência e eficácia, pois ajuda a direcionar esforços, recursos e tempo para solucioná-lo. 

### 1.2.1 Problema

O BTG Pactual enfrenta o desafio de otimizar suas estratégias de marketing digital e entender melhor o comportamento e preferências dos consumidores nas redes sociais. Com o aumento do investimento em marketing digital e a crescente utilização das redes sociais, a análise de dados de mídia social é fundamental para obter informações relevantes e tomar decisões de negócios mais eficazes. O objetivo é utilizar PLN para rastrear dados e analisar a receptividade dos usuários às campanhas em redes sociais, identificar palavras-chave nos comentários e direcionar novas campanhas baseadas nos interesses dos consumidores.

# 2. Objetivos

Nesta seção, apresenta-se os objetivos do projeto que são as metas e resultados esperados a serem alcançados com a execução do mesmo. Servindo como uma referência para orientar as ações do projeto e ajudar a equipe a entender o que precisa ser feito e como avaliar o sucesso do projeto.

## 2.1 Objetivos Gerais

Sabendo que mais de 50% da população mundial que usa redes sociais por mais de 2 horas por dia e a crescente importância do marketing nas empresas (TAPI, 2023), o BTG Pactual em parceria com o Inteli está desenvolvendo o projeto de “Análise de Sentimento das Campanhas de Marketing em Redes Sociais”. Através da tecnologia de Processamento de Linguagem Natural (PLN), será desenvolvido uma ferramenta que ajudará a empresa a compreender a receptividade dos clientes às suas campanhas de marketing e nas tomadas de decisões das áreas de negócios, através da análise de sentimento e identificação de palavras-chave nos comentários dos usuários, permitindo uma resposta rápida a possíveis problemas ou oportunidades. 

## 2.2 Objetivos Específicos

1. Realizar um pré-processamento dos dados, visando remover palavras irrelevantes ou duplicadas. Além da conversão dos dados não estruturados em estruturados. 
2. Utilizar a técnica de análise de sentimentos, visando extrair informações dos comentários de redes sociais. 
3. Utilizar técnicas de mineração de texto e processamento de linguagem natural para realizar a extração de palavras-chave.
4. Realizar a classificação ternária (positiva, negativa ou neutra) de campanhas de marketing.
5. Desenvolver uma interface de usuário para realizar o monitoramento e análise de campanhas, através dos resultados obtidos com o processamento de linguagem natural.

## 2.3 Justificativa

A implementação de um projeto de PLN para análise de sentimentos nos comentários de usuários em campanhas é uma estratégia essencial para aprimorar a gestão de marketing e otimizar as estratégias de negócios. Atualmente as campanhas se tornaram uma das principais formas de interação com o público-alvo, porém, gerenciá-las e analisar o feedback dos usuários manualmente é uma tarefa complexa e demorada.

Para otimizar tal atividade, se faz necessário a adoção do PLN, garantindo automatização e fornecendo insights valiosos sobre a percepção dos usuários em relação à marca dos produtos/serviços. Sendo possível entender a reação dos usuários às campanhas, o que permite ajustes e melhorias necessárias para tornar as campanhas mais efetivas e alinhadas com os interesses dos consumidores. Além de, com informações obtidas, a área de negócio pode tomar decisões mais precisas e embasadas, o que impacta diretamente nos resultados das campanhas e na percepção dos usuários sobre a marca.

## (Sprint 1) Entendimento do Negócio

# 3. Compreensão do Problema

Apresenta-se nessa sessão as descrições das análises voltadas ao desenvolvimento de resultados do projeto, para a empresa BTG Pactual, a respeito da construção de um MVP (Produto mínimo viável) de um sistema de análise de sentimentos. Sendo exibido as identificações do mercado e produtos em comparação a solução prevista.

## 3.1 Análise de cenário: Matriz SWOT

A análise SWOT é uma ferramenta que possibilita a empresa a realizar análises de cenário ou de ambiente, sejam eles internos ou externos. Assim, é demonstrado as formas como ela atua no setor, suas fraquezas e forças (Iniciativas Internas), oportunidades e ameaças (inciativas externas). A Figura 1, exibe  uma imagem demonstrativa das quatro áreas que compõem a SWOT. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/SWOT.png"> 
Fonte: Autores

I. Pontos Fortes: <br>
    • A empresa está presente em vários países, o que ajuda a obter dados de análise de texto de diferentes fontes;  <br>
    • O BTG Pactual possui experiência em projetos de grande porte, o que pode auxiliar na implantação de projetos de NLP;  <br>
    • Dispõe de uma equipa de colaboradores de diversas especialidades, que poderão ajudar na concretização do projeto.  <br>
      
II. Pontos Fracos:  <br>
    • Este projeto pode ser difícil de realizar sem uma equipe de PNL dedicada; <br>
    • A empresa pode encontrar dificuldades em gerenciar a grande quantidade de dados gerados pelas redes sociais e garantir sua qualidade;  <br>
    • Pode ser necessário investir em infraestrutura e tecnologia para dar suporte ao projeto.  <br>

III. Oportunidades:  <br>
    • O uso do PLN pode ajudar as empresas a analisar rapidamente as respostas dos usuários nas mídias sociais. Aumentar o engajamento e a satisfação do cliente;  <br>
    • As palavras-chave achadas nas avaliações dos usuários podem ajudar as empresas a criar campanhas mais eficazes;  <br>
    • A análise de sentimentos pode ajudar as empresas a entender melhor as necessidades e tendências dos clientes.  <br>
      
IV. Ameaças:  <br>
    • Outras empresas podem usar o NLP para analisar dados de mídia social. o que aumenta a competição;  <br>
    • Pode ser difícil para o PLN analisar todos os idiomas usados nas redes sociais, o que limita a quantidade de dados que podem ser analisados;  <br>
    • Alterações políticas de privacidade de mídia social podem dificultar o acesso aos dados do usuário.  <br>
    
## 3.2 Proposta de Valor

A principal vantagem apresentada pela proposta de valor é conseguir auxiliar a empresa a compreender melhor os seus clientes e funcionários. Na Figura 2, é ilustrada a proposta construída para o BTG Pactual.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Proposta%20de%20valor.png"> 
Fonte: Autores

## 3.3 Matriz de Risco

É uma das principais ferramentas na análise de negócios, utilizada para o gerenciamento de riscos operacionais existentes na empresa. A Figura 3, ilustra a construção da matriz de risco para o projeto. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Matriz%20de%20Risco.png"> 
Fonte: Autores

Mitigar os riscos é essencial para garantir a estabilidade e a eficiência da do time, com isso, segue o plano criado entre os membros para prevenir tais riscos, na tabela 2 abaixo. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Tabela%20-%20Mitiga%C3%A7%C3%A3o%20de%20Risco.png"> 
Fonte: Autores


## 3.4 Matriz Oceano Azul

A Matriz de Oceano Azul é uma estratégia de negócios que ajuda a empresa a criar mercados, o “oceano azul” representa novos mercados ainda inexplorados, e a diferenciar-se da concorrência, aumentando a sua participação de mercado e, consequentemente, seu lucro. 

Com base na solução proposta da Natural five, realizou-se a matriz de “oceano azul”, com base em 6 concorrentes, IBM Watson Natural Language Understandinge, Google Cloud Natural Language, Google Cloud AutoML, Amazon Comprehend, Microsoft Azure Text Analytics e Python Natural Language Toolkit (NLTK). Apresenta-se na tabela 3 abaixo, os quesitos avaliados. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Tabela%20Oceano%20Azul.png"> 
Fonte: Autores

Abaixo se apresenta a descrição dos 8 atributos chave, sendo eles:

• Reduzir

A opção "Python Natural Language Toolkit" diminuiu o quesito “Maior preço” visto que ele é uma biblioteca gratuita, mesmo assim, também buscamos diminuir nossos custos em relação aos outros concorrentes Assim como o aspecto de “comodidade”, a opção “Python Natural Language Toolkit” diminui a praticidade do projeto pois ao usá-lo é necessário que o cliente tenha que criar por si próprio o modelo desejado, custando tempo, estrutura, planejamento e profissionais para desenvolver o modelo. Visto que todos os concorrentes são Big Tech's, diminuímos em relação a maior credibilidade, pois não possuímos a mesma estrutura de infraestrutura que elas, mesmo assim, acreditamos que não é uma perda, pois oferecemos funcionalidades personalizáveis focada no cliente.

• Eliminar

A NaturalFive optou por eliminar recursos de integração com diversas interfaces, incluindo a responsividade, para focar em uma entrega mais personalizada aos nossos clientes. Compreendemos que acrescentar essas funcionalidades poderia aumentar o preço e o tempo de entrega, o que não seria viável para atender às necessidades do mercado atual. Dessa forma, a eliminação desses recursos não foi sentida como uma perda pelos nossos clientes, pois nosso foco é oferecer soluções personalizadas e eficientes. 

• Aumentar

A análise do quesito "Maior Comodidade" evidencia que a opção "Python Natural Language Toolkit" teve a menor pontuação, com uma nota 3, devido ao fato de ser uma biblioteca que requer maior conhecimento técnico para a criação de um modelo de PLN. Nesse sentido, a Natural Five buscou aumentar a comodidade do processo de utilização da solução, tornando-a mais fácil e acessível para usuários (Marketing, Produto e Automação) com diferentes níveis de conhecimento técnico.
No quesito "Maior custo benefício" temos 2 principais agentes, "Python Natural Language Toolkit" e "Natural Five" visto que elevam o custo benefício por serem mais personalizáveis de acordo com as necessidades do cliente e serem mais baratas que seus concorrentes; além disso ao utilizá-los a empresa não ficará dependente de um terceiro como Google Cloud, IBM ou Amazon.Além disso o quesito de “Maior Escalabilidade” é considerado alto comparado as outras empresas, o NaturalFive, consegue ser escalável e personalizado, podendo ser utilizado em outras redes sociais. 
          
• Criar

Ao comparar com as grandes empresas de tecnologia que possuem soluções de PLN, podemos perceber que a Natural Five cria um nível de usabilidade personalizada muito superior para as equipes de marketing, produto e automação. Fornecendo um produto único para o cliente. Desenvolver uma plataforma pensando nas necessidades específicas de nossos clientes. Assim, fomos capazes de criar uma solução mais intuitiva, que se adapta melhor às necessidades dos usuários e é mais fácil de ser utilizada.

Esses atributos foram escolhidos com base na importância que o BTG Pactual atribui aos modelos de análise de linguagem natural como usar a tecnologia para facilitar esse processo de forma mais prática e barata, mantendo sempre uma alta qualidade. Apresenta-se abaixo um gráfico com a representação visual da tabela apresentada, na figura 4. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/Gr%C3%A1fico%20Oceano%20Azul.png"> 
Fonte: Autores

Analisando o gráfico é possível perceber que a solução proposta do “Natural Five” se sobressai nas categorias de “Maior usabilidade” e “Mais integrações” ambas com nota 10/10. Por outro lado a solução se igualou com outras opções de mercado nas categorias “Maior praticidade” com nota 9/10 e “Maior custo-benefício” com nota 8/10 (ambas as notas podem ser consideradas altas). Porém a categoria “Credibilidade” é a única onde a Natural Five sai com menor pontuação "6/10".

Logo, pode-se concluir que o produto a ser desenvolvido pelo Natural Five se destaca na maioria das categorias e seu diferencial principal é por ele ser um produto mais personalizado para o cliente de forma prática e cômoda sem gerar grande gasto do cliente.

## 3.6 Análise Financeira

A Análise de custo das ferramentas utilizadas para a criação da solução, pode ser definida como uma estratégia adotada pelas empresas e desenvolvedores para o ponderamento do custo e benefício, visando obter maior domínio e exatidão dos gastos para a produção e implementação do serviço. 

Estima-se para o desenvolvimento do MVP da solução os seguintes custos, participação de 2 desenvolvedores, hospedagem em um ambiente de cloud e tempo de desenvolvimento de 6 meses, totalizando em média de 250 à 300 mil reais. Tais dados, são apresentados, visando que o projeto fosse executado dentro da empresa, fornecidos pelo parceiro.

A projeção da receita não foi informada, portanto apresenta-se abaixo o raciocínio criado para realizar a estimativa do mesmo. Baseou-se os cálculos visando a receita, com o modelo atuando na retenção dos clientes do banco. 

A retenção de clientes dentro de uma empresa, principalmente um banco, pode ser de total importância, visto que pode gerar receitas adicionais a longo prazo, uma vez que, quanto mais satisfeitos os usuários mais propensos eles estão em utilizar os produtos e/ou serviços da organização. Dito isso, espera-se que o sistema de análise de sentimentos contribua para essa retenção, fornecendo os insights necessários para que a satisfação aconteça.

Sendo assim, o BTG Pactual conta com 2,5 milhões de clientes, segundo o informativo de setembro de 2021. O valor médio das tarifas cobradas por bancos, em cada cliente que possui conta-corrente é de R$ 23.45 por mês, de acordo com uma pesquisa realizada pelo Banco Central em 2021. Anualmente recebe-se R$ 281,40 por cliente, totalizando portanto uma receita de R$ 703.500.000,00 levando em conta todos os clientes do banco.

Entretanto, em uma pesquisa da Associação Brasileira de Defesa do Consumidor, em 2020, constatou-se que cerca de 13% dos brasileiros, em média, anualmente trocam de banco por insatisfações. Com isso, o BTG Pactual perde 325 mil clientes, por ano, com insatisfações de produtos e/ou serviços. Perdendo em média R$ 91.455.000,00 anuais com tarifas que poderiam ser cobradas de cada um desses clientes. 

Ao calcular o Retorno Sobre Investimento (ROI) da solução, levando em base que a única receita vinda para o projeto é a retenção dos 13% dos clientes do banco, que agora com a aplicação do modelo, não trocariam mais de agência, por suas necessidades estarem sendo atendidas, e o custo sendo o fornecido pelos parceiros de 300 mil reais, temos: 

OBS: Utilizou-se o valor de receita, para 6 meses, que é o tempo de desenvolvimento previsto. Ou seja, R$ 91.455.000,00 divido por 6, obtendo R$ 15.242.500,00. 

	ROI = (Receita – Custo) / Custo
	ROI = (15.242.500,00 – 300.000,00) /  300.000,00
	ROI = 14.942.500,00 / 300.000,00
	ROI = 49,808
	ROI (%) = 49,808 * 100
	ROI (%) = 4.980,8 %

A análise financeira aponta com base no resultado apresentado pelo calculo estimado do ROI, tal investimento gera a empresa um retorno bem-sucedido, mostrando que projeto é altamente rentável. Uma vez que, com isso à que a solução permite à empresa compreender melhor o público-alvo, identificar oportunidades de negócios e ainda atuar na retenção dos clientes que já possui.


## (Sprint 1) Lean Inception

# 4. Lean Inception

Nesta sessão, apresenta-se o Lean Inception, uma técnica baseada na metodologia ágil que visa definir o escopo e os requisitos do produto de forma colaborativa e eficiente, de todo o time e das partes interessadas na solução. 

## 4.1 Visão do Produto

Responsável pela definição do objetivo principal do produto e como ele se encaixa na estratégia geral do negócio. Devendo ser clara, inspiradora e compartilhada por todas as partes interessadas. No parágrafo abaixo, segue a visão do produto, criada para o projeto de análise de sentimentos. <br>

• Para o Banking and Trading Group (BTG), cujo à análise de dados de mídia social pode fornecer informações valiosas da criação de campanhas, produtos e/ou serviços. O projeto de Processamento de linguagem natural, para as áreas de automação, marketing e produto, é um, modelo capaz de analisar sentimentos e identificar palavras-chave nos comentários dos usuários com base nas postagens do instagram do banco, que ajuda a equipe de automação a analisar as suas campanhas realizadas durante o ano, e verificar além do seu alcance, a sensibilidade dos usuários. Diferentemente do GPT da OpenAI, do BERT do Google, da Siri da Apple e da Alexa da Amazon, o nosso produto oferece uma experiência única focada na cultura de inovação e foco no cliente, alinhada à cultura do BTG Pactual.

## 4.2 O Produto (É – Não É – Faz – Não Faz)

Definição das características principais do produto, especificando o que ele É e o que NÃO É, e o que ele FAZ e o que NÃO FAZ. Garantindo que todas as partes interessadas tenham uma compreensão comum do produto e evita mal-entendidos. Nas imagens 5, 6, 7 e 8 abaixo, exibe-se os critérios definidos para o produto, incluindo as condições as quais ele não atende.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/%C3%A9.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/n%C3%A3o%20%C3%A9.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/faz.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/n%C3%B5a%20faz.png"> 
Fonte: Autores

## 4.3 Brainstorming de Funcionalidades
Utilizado para gerar ideias de funcionalidades que o produto deve ter. Buscando garantir que o produto atenda às necessidades dos usuários e do negócio. Abaixo se exibe os Clusters criados para o mapeamento de funcionalidades. 
<br>

• Filtro: <br>
        &emsp; ◦ Classificação de campanhas em positivas, negativa e/ou neutra;  <br>
        &emsp; ◦ Visualizar palavras-chaves;  <br>
        &emsp; ◦ Possibilidade de filtros para os dados.  <br>
         
• Análise: <br>
        &emsp; ◦ Receptividade da campanha pelo usuário;  <br>
        &emsp; ◦ Avaliar performance das campanhas;  <br>
        &emsp; ◦ Analisar padrões de comportamento;  <br>
        &emsp; ◦ Considera todos os comentários textuais da publicação; <br>
        &emsp; ◦ Mensurar o nível de satisfação dos clientes;  <br>
        &emsp; ◦ Contempla verificar quantas curtidas cada comentário apresenta e sua relevância no modelo;  <br>
        &emsp; ◦ Disponibiliza casos de teste do sistema; <br>
        &emsp; ◦ Variação da polarização antes e depois da campanha;  <br>
        &emsp; ◦ Visualizar o conteúdo completo dos comentários.  <br>
        
• Visualização do projeto:  <br>
        &emsp; ◦ Visualização dos dados em dashboards e/ou gráficos;  <br>
        &emsp; ◦ Fornece protótipo de interface de usuário.  <br>
        
• Implementação extra:  <br>
       &emsp;  ◦ Rastrear dados em tempo real dos comentários das campanhas. <br>
       
## 4.5 Revisão Técnica, de Negócios e de UX

Utilizado para revisar as funcionalidades geradas na etapa anterior sob as perspectivas técnicas, de negócios e de experiência do usuário (UX). Buscando garantir que as funcionalidades sejam viáveis do ponto de vista técnico, agreguem valor ao negócio e proporcionem uma boa experiência ao usuário. Na figura 9 abaixo, exibe-se a estrutura criada e categorizada entre esforço (E), negócio ($) e UX (<3) para o projeto. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/tecnica%20UX.png"> 
Fonte: Autores

## 4.6 Sequenciador

Técnica utilizada para priorizar as funcionalidades e requisitos do produto. Ele é uma ferramenta de classificação simples que permite que as equipes definam a ordem de execução das funcionalidades com base em critérios pré-determinado, na figura 10 abaixo, exibe-se a estrutura de sequência criada para a solução. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/sequenciador.png"> 
Fonte: Autores

## 4.7 Canvas MVP

Ferramenta para estimar qual é o produto, com o menor conjunto de recursos que ainda atende às necessidades básicas dos clientes. Além de determinar como testar e validar o produto com os clientes. Na figura 11 abaixo se apresenta o Canvas MVP criado para a solução.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/canvas%20mvp.png"> 
Fonte: Autores

## (Sprint 1) Entendimento da Experiência do Usuário

# 5. Análise de Experiência do Usuário 

Nesta sessão, apresenta-se a análise de experiência do usuário, a qual através da aplicação de estratégias, visa compreender como os usuários interagem com sistemas, produtos e serviços. O objetivo é melhorar a satisfação e a eficiência dessas interações, levando em conta aspectos subjetivos como emoções, percepções e expectativas dos usuários.

## 5.1 Personas

As personas do projeto são baseadas em 3 setores principais, sendo eles, 1) Analista de Automação; 2) Analista de Marketing; 3) Analista de produto. Estes representam a ideia de cliente ideal, porém fictícia, e os dados apresentados (comportamentos e características), são equivalentes ao contexto em que o BTG Pactual se encontra. As Figuras 12, 13 e 14 exibem as personas construídas. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/persona%201.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/persona%202.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/persona%203.png"> 
Fonte: Autores

## 5.2 Jornada do Usuário

A jornada do usuário construída consiste na representação das etapas principais que envolvem 1) Análise dos dados das campanhas; 2) Visualização da análise e melhoria nas campanhas de marketing; e 3) Visualização da análise e melhoria na criação e/ou modificação dos produtos e serviços do banco. Divididas em 3 estruturas, exibidas nas figuras 15, 16 e 17 sendo elas respectivamente: <br> 
    &emsp; 1. Analista de Automação;  <br> 
    &emsp; 2. Analista de Marketing;  <br> 
    &emsp; 3. Analista de produto.  <br> 
    
<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/jornada%201.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/jornada%202.png"> 
Fonte: Autores

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/jornada%203.png"> 
Fonte: Autores
    
## 5.3 User Stories

Pode-se definir User Stories como descrições simplificadas das funcionalidades possíveis que o usuário possui e deseja dentro da aplicação, escrita com a visão dele. Além de transparecer como o sistema espera alcançar tais objetivos. As tabelas abaixo estão divididas em 6 partes: Número, Título, Personas, História, Critérios de Aceitação e Testes de Aceitação. O número e título servem para identificação, já as personas servem para associar a quem a história pertence. Os dois últimos tópicos descrevem quais são os critérios que aquele usuário deve passar no sistema para realizar a ação descrita na “história”, já o teste diz como o sistema deve agir de acordo com o critério estipulado. Nas tabelas 4,5,6,7,8 e 9 abaixo. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%201.png"> 
Fonte: Autores


A primeira User Story está direcionada para a primeira etapa a ser cumprida pelo time de desenvolvimento, focado em processamento dos dados, com sua leitura, limpeza e correção para que sejam interpretadas por uma IA, partindo assim para a segunda User Story. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%202.png"> 
Fonte: Autores

A segunda User Story tem como objetivo a implementação de uma interface gráfica de usuário para exibir os resultados gerados pela IA a partir dos dados processados na primeira User Story. Essa interface deve ser intuitiva e fácil de usar, permitindo que os usuários possam visualizar e interagir com as informações de forma clara e objetiva. Para isso, o time de desenvolvimento trabalhará na construção de uma interface com recursos de seleção e visualização dos dados, a fim de atender às necessidades dos usuários finais. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%203.png"> 
Fonte: Autores

A terceira User Story tem como objetivo construir um modelo de análise de sentimento e palavras-chave automatizado para os comentários do Instagram do BTG Pactual, a fim de fornecer insights valiosos para o analista de produto. O analista de automação será o responsável por criar esse modelo. Nossa interface realizará a análise de sentimento e demonstrar quais são as palavras-chaves, indicando para quem for utilizar quais são elas. Os testes de aceitação incluem verificação da correta apresentação das informações e uso dos modelos definidos. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%204.png"> 
Fonte: Autores

A quarta User Story voltada para o analista de marketing, busca permitir a análise por meio de uma interface que permita a seleção de campanhas baseada nos dados disponibilizados na base. Além disso, a interface deve apresentar gráficos e estatísticas para auxiliar na visualização, garantindo uma análise mais eficiente e precisa. Os critérios de aceitação dessa User Story garante que a plataforma apresente feedback adequado ao usuário, informando caso a seleção escolhida não exista e permitindo a visualização dos resultados de maneira clara e objetiva. 


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%205.png"> 
Fonte: Autores

Na quinta User Story, o analista de produto deseja analisar o rendimento de cada campanha de marketing para obter insights do produto, além de realizar uma análise de sentimentos e palavras-chave. É importante que a interface permita a seleção de várias opções de campanha e produto ao mesmo tempo na mesma pesquisa.

O critério de aceitação estabelece que a interface deve permitir a seleção de várias opções de campanha e produto na mesma pesquisa, e caso isso não seja possível, deve-se retornar um erro e o processo deve ser revisto. Portanto, a interface deve ser capaz de lidar com seleções múltiplas de campanha e produto e apresentar resultados precisos e coerentes com os critérios de aceitação estabelecidos.


<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/user%206.png"> 
Fonte: Autores

A sexta User Story se trata da necessidade do analista de marketing em ter uma plataforma que permita selecionar a visualização de produtos e sentimentos para analisar o andamento de uma campanha de marketing. O critério de aceitação envolve a seleção da forma de visualização e a apresentação das informações de forma adequada. O time de desenvolvimento trabalhará para atender essas necessidades e garantir a satisfação do usuário final.

A partir das definições de todas as User Stories definidas para este projeto, foca-se na hierarquização das tarefas e priorização de cada uma delas, a fim de atender aos critérios de aceitação definidos. Dessa forma, completa-se cada User Story uma a uma, garantindo que o projeto seja entregue com todos os requisitos cumpridos e dentro do prazo estabelecido.

## (Sprint 1) Programação

# 6. Arquitetura Macro da Solução

A arquitetura macro da solução, apresenta os blocos responsáveis pelo funcionamento da solução, independente da tecnologia que será adotada ao desenvolvimento, comunicando-se entre si, apresentam a estrutura e ligações mínimas que a solução tem que exibir para ter o funcionamento previsto ao MVP. Abaixo na Figura 18, encontra-se a visualização inicial prevista da arquitetura macro. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/main/docs/outros/arquiteturaMacro.png"> 
Fonte: Autores
  
A arquitetura macro proposta, conta com 5 módulos, sendo eles 1) Usuário; 2) Interface; 3) back-end; 4) Banco de Dados; e 5) Notebook. Nos módulos Usuário e Interface, apresenta-se as personas do projeto em conjunto com as interfaces as quais terão acesso no projeto. O back-end é o módulo responsável por realizar o gerenciamento das rotas de consulta da aplicação, além das que são necessárias para acessar o modelo e suas análises. No módulo Banco de Dados, será localizado todos os dados dos arquivos CSV recebido da interface, utilizado para guardar novos dados e fornecê-los para o treinamento do modelo, quando requisitado. Por fim, o módulo do Notebook é responsável pelo processamento, implementação e avaliação do modelo de análise dos comentários e sentimentos da aplicação, obtendo os dados do banco, transformando em CSV, realizando os procedimentos necessários e exportando com uma biblioteca para o back-end que em conjunto com a interface, exibe para os usuários os resultados, em um dashboard. 

## Referências (Sprint 1)

# 9. Referências

BANCO CENTRAL DO BRASIL (Brasil).Tarifas Bancárias. [S. l.], 2023. Disponível em: 
https://www.bcb.gov.br/estabilidadefinanceira/tarifas_bancarias. Acesso em: 25 abr. 2023. 

BTG PACTUAL (São Paulo - Brasil).Relatório Anual 2021: Negócios, estratégia e desempenho. Com efetiva 
integração ESG.. [S. l.], 2021. Disponível em: https://static.btgpactual.com/media/rs2021-btgpactual-vf1.pdf. 
Acesso em: 25 abr. 2023.

JUROS%BAIXO (Brasil).Compare as tarifas de 6 bancos: conta corrente. [S. l.], 17 dez. 2018. Disponível 
em: https://jurosbaixos.com.br/conteudo/compare-as-tarifas-de-6-bancos-para-abrir-uma-conta-corrente/. 
Acesso em: 24 abr. 2023. 

SIQUEIRA, Andressa. Conta corrente: quais são os melhores bancos para abrir conta? Descubra aqui!. [S. 
l.], 20 abr. 2021. Disponível em: https://blog.magnetis.com.br/conta-corrente/. Acesso em: 24 abr. 2023. 

TORRES, Vitor.O que é ROI?: como calcular retorno sobre o investimento?. Contabilizei.blog, 11 out. 2022. 
Disponível em: https://www.contabilizei.com.br/contabilidade-online/o-que-e-roi-como-calcular-retorno-sobreo-investimento/. Acesso em: 24 abr. 2023

# (Sprint 2) Modelo de Bag of Words (IPYNB)

Colocar o link do artefato (deve estar na pasta src do repositório do projeto).

# (Sprint 2) Documentação do Modelo de Bag of Words

# Metodologia
Nesta sessão é apresentado as metodologias utilizadas como base para a criação do modelo de processamento de linguagem natural como um todo.

## CRISP-DM
Exibe-se as etapas que correspondem a metodologia do CRISP-DM. Na figura X abaixo, encontra-se uma imagem ilustrando como funciona a sequência de processos a serem exercidos quando a metodologia é implementada.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/CRISP_DM.png">



### Entendimento do negócio
Busca-se ter uma visão clara do problema que se precisa resolver, é nesta fase que se deve traçar os objetivos do negócio, buscar mais detalhes do problema, listar os recursos disponíveis e o impacto esperado. Tem como características estabelecer métricas e os critérios quantitativos para os possíveis resultados. Priorizando aqueles que influenciam sua meta e também criar uma análise da vantagem do projeto, além do custo-benefício. Define-se os modelos, relatórios, apresentações e os dados.

### Entendimento dos dados
Nesta segunda fase, se obtêm os dados e verifica-se se eles são adequados às suas necessidades. É importante ter feito uma boa fase 1, para que nesta fase não tenha que revisar o entendimento do negócio, nem repensar metas e planos.
Os objetivos desta fase são coletar os dados, descrevê-los, explorá-los e verificar a qualidade dos mesmos. Estabelecer formato para esses dados, é possível que seja necessário reunir novos dados, enfrentar limitações de software ou hardware. E encontrar imperfeições nos dados.
Na parte da documentação é importante estabelecer o feature selection, especificar os campos relevantes e criar uma descrição geral dos dados que possui, assim como os formatos, variáveis, técnicas estatísticas e qualquer informação que possa ser relevante. É o lugar para criar, testar e documentar hipóteses geradas após a exploração dos dados.

### Preparação dos dados
Agora que a maioria dos dados usados já foram coletados, necessita de refinamento antes de ser usado na modelagem. Esta fase possui cinco principais tarefas:

1. Selecionar os dados: É o momento de justificar quais dados serão ou não
utilizados, documentar a relevância desses para seu objetivo, os problemas
técnicos,
2. Limpar esses dados: Corrigir alguns dados específicos, excluir ou substituir por
valores padrões para uma técnica de modelagem mais sofisticada.
3. Documentar bem detalhadamente os processos utilizados nesta etapa e o
possível impacto gerado por essa escolha
4. Construção dos dados: Criar campos e documentá-los explicando os motivos.
5. Integração dos dados: Diversos conjuntos de dados, para mesclá-los e prepará-los para a fase de modelagem. Formatar os dados para o formato mais conveniente para o projeto.

### Modelagem
Nesta fase serão escolhidas as técnicas mais adequadas para modelagem, ou seja, está etapa envolve a seleção e a utilização de técnicas e algoritmos que atendam as necessidades do negócio. Geralmente os dados são divididos em duas partes: um de treino (que são gerados os modelos) e um de teste (que se refere a validação do modelo). Com base nisso, é definido se continua o desenvolvimento da modelagem (avaliação) ou se retorna para a fase de preparação de dados.

### Avaliação
Nesta fase será avaliada a qualidade e a segurança dos resultados obtidos na etapa anterior. De modo que seja possível verificar se esse resultado corresponde às expectativas do projeto. Caso não atenda, devem ser realizadas as modificações necessárias (como correção na entrada de dados, correção no tratamento dos atributos, entre outros).

### Implementação
Nesta fase é realizada o desenvolvimento dos modelos criados e avaliados. Durante essa etapa são realizadas tarefas, como: implantação da solução, monitoramento e manutenção, geração de relatórios e avaliação os resultados finais. Vale ressaltar que essa forma de implementação depende do tipo de modelo e projeto. Além disso, é preciso que o usuário final consiga interpretar e operar o produto com facilidade

## Ferramentas 
As ferramentas utilizadas para a construção da solução, consiste em aquelas utilizadas para o desenvolvimento, organização e compartilhamento de arquivos. Primeiramente, definiu-se uma ferramenta para a organização, tendo como base o aplicativo Notion, que permite organizar, através de cards, todas as tarefas da equipe, sendo possível visualizar o que está sendo feito pelos integrantes e gerenciar as entregas já concluídas. Em paralelo a isso, tem-se a ferramenta de desenvolvimento. Para isso, utilizou-se o Google Collaboratory, onde criou-se o notebook do projeto, o qual é utilizado para criação, organização e execução do código.
As ferramentas de compartilhamento de arquivos. Para os arquivos de desenvolvimento do trabalho, é utilizado o Google Drive, que possui integração com o Google Collaboratory. Assim, sendo possível compartilhar em tempo real os arquivos referentes ao desenvolvimento. E por fim, é utilizado o Github, que possibilita compartilhar todos os arquivos do projeto, referente a descrição, organização e desenvolvimento em um ambiente que será possível ter uma visão ampla do que foi desenvolvido

## Compreensão dos dados

As sessões abaixo apresenta o conjunto de dados trabalhado, seus principais atributos, descrições e análises estatísticas.

## Descrição dos dados utilizados

Neste tópico apresenta-se os dados disponibilizados na “2-base_10052023”. A base de dados a ser trabalhada foi disponibilizada pela empresa BTG Pactual, possuindo 12355 linhas de conteúdo. Na tabela 10 abaixo, é descrita os principais atributos, suas descrições e tipos da planilha.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/Descricao_dados_utilizados.png">
Fonte: Autores

## Descrição dos conjuntos de dados

Abaixo apresenta-se a descrição dos riscos e contingências relacionados aos dados:

- Os dados não oferecem grandes riscos de falta de confiabilidade, isto se deve ao fato de todos os dados serem coletados e disponibilizados pela própria empresa. Ou seja, a chance de serem falsos ou imprecisos é extremamente baixa, portanto de alta qualidade. Eles cobrem todos os aspectos que o parceiro considerou importante para o desenvolvimento do projeto, já que eles selecionaram os dados a serem repassados.

## Preparação dos dados

Nesta seção, colocou-se em prática a análise exploratória dos dados fornecidos pela empresa, de acordo com a execução proposta pelo modelo CRISP-DM, a fim de tornar nossa base de dados mais adequada para o sistema de processamento de linguagem natural para análise de sentimentos. 

### Exclusão de Colunas não utilizadas

Nesta sessão, descrevemos as colunas relevantes selecionadas para o modelo de análise de sentimentos, como data de publicação, autor, texto, sentimento e tipo de interação. Também explicamos por que colunas como anomalia, probabilidade de anomalia, link do post, processado e contém hyperlink não são relevantes para a análise de sentimentos proposta.

Colunas Utilizadas:

1. **dataPublicada**: A data de publicação é relevante, pois permite identificar a cronologia dos comentários e compreender possíveis tendências ou mudanças nos sentimentos ao longo do tempo.
2. **autor**: A identificação do autor é relevante para analisar a inclinação dele na expressão dos sentimentos positivos, negativos ou neutros em cada publicação.
3. **texto**: O texto do comentário em si é o elemento central para a análise de sentimentos. É por meio do texto que podemos extrair informações linguísticas e identificar palavras, frases ou padrões.
4. **sentimento**: Essa coluna é a variável-alvo da análise de sentimentos. A classificação de sentimento atribui uma categoria (positivo, negativo ou neutro) a cada comentário com base na análise do seu conteúdo textual.
5. **tipoInteracao**: A categoria de interação do texto do comentário pode fornecer informações adicionais sobre o contexto em que o comentário foi feito. 

Colunas Descartadas:

1. **anomalia**: Essa coluna não é relevante para a análise de sentimentos, pois está relacionada à classificação de possíveis comportamentos maliciosos ou golpes nos comentários, não ao sentimento expresso neles.
2. **probabilidadeAnomalia**: Essa coluna também está relacionada à classificação de possíveis anomalias ou comportamentos maliciosos, não sendo relevante para a análise de sentimentos.
3. **linkPost**: O link da postagem do Instagram não está diretamente relacionado ao sentimento expresso nos comentários e, portanto, não é relevante para a análise de sentimentos.
4. **processado**: Essa coluna indica se a análise de sentimentos já foi realizada na linha. Embora seja útil para rastrear o progresso do processamento dos dados, não contribui diretamente para a análise de sentimentos em si.
5. **contemHyperlink**: Essa coluna indica se um comentário possui um hyperlink. Embora possa ser relevante para outras análises, como a detecção de spam, não é diretamente relevante para a análise de sentimentos dos comentários.

### Formatação de datas

Para a manipulação correta das datas e horários na base de dados, todas precisam estar no mesmo formato, sendo o modelo escolhido dd-mm-yyyy (Exemplo: 03-04-2022). A coluna afetada pela formatação foi a “dataPublicada”. Essa Feature foi selecionada pois sem a formatação das datas resultaria em um difícil manuseio dos dados. A Figura 17, ilustra o antes e o depois da formação, sendo o lado esquerdo da imagem o antes da aplicação e o lado direito o depois.

ANTES

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/dataPublicada_antes.png">
Fonte: Autores

DEPOIS

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/dataPublicada_depois.png">

Fonte: Autores
# Gráfico de Tendência Temporal dos Sentimentos

O gráfico de tendência temporal dos sentimentos foi utilizado para explorar a evolução dos sentimentos (positivos, negativos e neutros) ao longo do tempo com base na coluna "dataPublicada". Com ele, identifica-se picos de comentários positivos, negativos e neutros ao longo dos três últimos meses antes da última inserção de comentários na base (11-12-2022). A figura X abaixo ilustra o gráfico.

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/tendenciatemporalsentimentos.png">
Fonte: Autores


Ao analisar o período de 02-12-2022 a 15-12-2022, observamos um padrão de comportamento nos comentários positivos. Durante esse período, houve um aumento notável na contagem de comentários positivos, atingindo um pico de 100 comentários. Esse pico pode ser um indicativo de um evento ou acontecimento especial que gerou um grande número de reações positivas dos usuários. Inclusive porque durante o mês de Dezembro o BTG realiza o evento de Natal, o que pode atrair uma maior quantidade de acessos, por conta de shows e decorações no local. 

# Gráfico de Dispersão para Sentimento e Autor

O Gráfico de Dispersão para Relação entre Sentimento e Autor é utilizado para explorar a relação entre o sentimento expresso nos comentários e os respectivos autores. Nesse gráfico, o eixo x representa os autores e o eixo y representa a polaridade do sentimento, com valores negativos, neutros e positivos. Na figura X abaixo exibe-se o gráfico. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/sentimentoAutor.png">
Fonte: Autores


Ao observar o gráfico, podemos identificar a interação entre os autores e o sentimento expresso em seus comentários. Notamos que os comentários neutros ainda são os mais recorrentes, sugerindo uma tendência de neutralidade predominante nas interações. No entanto, é importante ressaltar a necessidade de realizar um balanceamento dos dados, uma vez que a alta recorrência de comentários neutros pode influenciar a análise geral. A sequência de comentários positivos, é notória e merece uma análise mais aprofundada. Essa sequência de comentários positivos pode revelar insights sobre a satisfação dos autores, a eficácia de determinadas ações ou até mesmo a qualidade do conteúdo gerado.

# Gráfico de Nuvem de Palavras

O Gráfico de Nuvem de Palavras, também conhecido como Word Cloud, é uma ferramenta para analisar e visualizar as palavras mais frequentes em um texto. Nesse contexto, o uso se mostra especialmente útil para identificar as palavras mais recorrentes nos comentários expresso pelos usuários.

Para começar, foi criada uma nuvem de palavras considerando a base geral de dados. Essa nuvem de palavras mostra as palavras mais frequentes em todos os comentários, independentemente do período em que foram feitos. É uma forma de entender os temas e tópicos mais abordados pelos usuários de maneira geral. Palavras maiores indicam uma frequência maior na base de dados, enquanto palavras menores indicam uma frequência menor. Pode-se visualiza-lo na figura X abaixo. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/nuvemPalavras1.png">
Fonte: Autores


Além disso, foi criada uma segunda nuvem de palavras focada no período específico de 02-12 a 15-12 de 2022, no qual foi identificado um pico significativo de comentários positivos. Essa nuvem de palavras permite analisar as palavras mais frequentes nesse período específico e identificar possíveis mudanças nos temas e tópicos discutidos pelos usuários. Através dessa análise, é possível compreender melhor os fatores que levaram a esse pico de comentários positivos e explorar as causas prováveis. Na imagem X abaixo pode-se visualiza-lo. 

<img src="https://github.com/2023M6T4-Inteli/Projeto5/blob/dev/docs/outros/nuvemPalavras2.png">
Fonte: Autores


Outro aspecto importante é que pretende-se remover o nome "BTG Pactual" da nuvem de palavras, a fim de focar em palavras mais claras e específicas do assunto. Isso permite uma análise mais precisa e a identificação de termos relacionados ao sentimento dos usuários, sem a interferência do nome da empresa. 

## (Sprint 3) Modelo utilizando Word2Vec (IPYNB)

Colocar o link do artefato (deve estar na pasta src do repositório do projeto).

## (Sprint 3) Documentação do Modelo utilizando Word2Vec

Preencher conforme a descrição do artefato na Adalove.

## (Sprint 4) Proposta de uma nova modelagem utilizando novas features (IPYNB)

Colocar o link do artefato (deve estar na pasta src do repositório do projeto).

## (Sprint 4) Documentação da proposta de uma nova modelagem

Preencher conforme a descrição do artefato na Adalove.

## (Sprint 5) Apresentação Final

Colocar o link do artefato (deve estar na pasta apresentacoes do repositório do projeto).

## (Sprint 5) Deploy do melhor modelo

Colocar o link dos artefatos (devem estar nas pastas videos e src do repositório do projeto).

## (Sprint 5) Documentação da Solução

Preencher conforme a descrição do artefato na Adalove.
