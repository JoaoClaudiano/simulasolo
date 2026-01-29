# Simula Solo

**Simula Solo** é um projeto de engenharia geotécnica computacional voltado para **análise de tensões no solo, dimensionamento de fundações rasas e profundas, verificação normativa e geração automática de relatórios técnicos**, com foco educacional e profissional.

O projeto foi concebido para separar claramente **engenharia (cálculo)** de **interface (visualização)**, garantindo confiabilidade técnica, modularidade e possibilidade de expansão contínua.

---

## 🎯 Objetivos do Projeto

* Apoiar o **ensino de Mecânica dos Solos e Fundações**
* Disponibilizar um **núcleo de cálculo geotécnico confiável e extensível**
* Permitir **simulações interativas** com visualizações claras
* Facilitar a **verificação normativa (NBR)**
* Gerar **relatórios técnicos automáticos**

---

## 🧠 Arquitetura do Sistema

O Simula Solo adota uma **arquitetura modular em camadas**, inspirada em boas práticas de engenharia de software:

* **Core geotécnico**: cálculos puros de engenharia
* **Camada de serviços**: orquestração dos cálculos
* **Interface (frontend)**: Streamlit (UI interativa)
* **Camada normativa**: verificação conforme NBR
* **Exportação**: geração de arquivos técnicos

Essa abordagem garante:

* Fonte única da verdade para os cálculos
* Independência entre cálculo e interface
* Facilidade de manutenção e expansão

---

## 📁 Estrutura do Repositório

```
simula_solo/
│
├── core/              # Núcleo geotécnico (engenharia pura)
├── services/          # API interna / orquestração
├── norms/             # Verificações normativas (NBR)
├── visualization/     # Gráficos e visualizações
├── exports/           # Exportação de resultados
├── app/               # Interface Streamlit
├── data/              # Bancos de dados (solos, SPT, etc.)
├── tests/             # Testes automatizados
├── docs/              # Documentação técnica
└── README.md
```

---

## 1️⃣ Análise de Solo e Tensões

* Círculo de Mohr interativo (critério de Mohr–Coulomb)
* Transformação de tensões (rotação de planos)
* Tensões principais (σ₁ e σ₃)
* Fator de segurança e mobilização
* Stress path (caminho das tensões)
* Relatório técnico automático

---

## 2️⃣ Fundações Superficiais – Sapatas

* Bulbo de tensões (Boussinesq – visualização 3D)
* Isóbaras corrigidas
* Capacidade de carga (Terzaghi)
* Fatores Nc, Nq, Nγ com correções
* Cálculo de recalques (solução elástica)
* Diagrama de interação pressão × FS
* Verificação conforme NBR 6122

---

## 3️⃣ Fundações Profundas – Estacas

* Método Aoki–Velloso (SPT)
* Método Décourt–Quaresma
* Análise por camadas de solo
* Capacidade por atrito e ponta
* Recalque de estacas
* Eficiência de grupo
* Perfil de tensões ao longo do fuste

---

## 4️⃣ Sistema de Exportação

* CSV – dados tabulares
* Excel – múltiplas planilhas
* PDF – relatório técnico formatado
* HTML – gráficos interativos
* JSON – dados estruturados
* Pacote completo do projeto

---

## 5️⃣ Validação Normativa

* NBR 6122:2019 – Fundações
* NBR 6118:2014 – Concreto armado
* Verificação de capacidade
* Verificação de recalques
* Verificação dimensional
* Relatório de conformidade normativa

---

## 6️⃣ Interface e Usabilidade

* Sidebar interativa
* Banco de solos típicos
* Criação de solos personalizados
* Sistema de unidades (SI, MKS, Inglês)
* Layout responsivo
* Documentação integrada

---

## 7️⃣ Visualização Gráfica

* Plotly (2D e 3D interativo)
* Isóbaras e contornos de tensões
* Diagramas de interação
* Perfis estratigráficos
* Zoom e navegação dinâmica

---

## 🔄 Expansões Planejadas

* Estabilidade de taludes (método das fatias)
* Empuxos de terra (Rankine e Coulomb)
* Recalques por adensamento (Terzaghi 1D)
* Método dos elementos finitos simplificado
* Interação solo–estrutura
* Análise probabilística e otimização

---

## 🧪 Testes e Confiabilidade

* Testes unitários para os modelos geotécnicos
* Validação cruzada de resultados
* Separação clara entre cálculo e interface

---

## 📌 Público-alvo

* Estudantes de Engenharia Civil
* Professores de Geotecnia
* Profissionais de fundações
* Pesquisadores
* Desenvolvedores de ferramentas técnicas

---

## ⚠️ Aviso Técnico

Este software **não substitui projetos executivos, sondagens ou pareceres técnicos profissionais**. Seu uso deve ser feito com critério técnico e validação por engenheiro habilitado.

---

## 👤 Autor

**João Claudiano**
Estudante de Engenharia Civil
Projeto desenvolvido com apoio de IA como ferramenta de desenvolvimento e validação lógica.

---

## 📄 Licença

Este projeto é distribuído sob licença **MIT**, permitindo uso acadêmico e educacional, com os devidos créditos.
