# Inteligência Artificial – Data Science e Machine Learning  
**Prof. Dr. Manuel Gonçalves da Silva Neto**  
📧 manuel@ifpi.edu.br  

---

## 🧠 Objetivos da Aula

- Introduzir os **conceitos fundamentais de Aprendizado de Máquina (Machine Learning)**.
- Apresentar os **tipos de aprendizado** e o **fluxo básico de desenvolvimento de modelos**.
- Explorar o uso de **ferramentas e dados para projetos de IA**.

---

## 📚 Conceito Central

> “Um programa aprende a partir da experiência E, em relação a uma classe de tarefas T, com medida de desempenho P, se seu desempenho em T, medido por P, melhora com E.”  
> — *Tom Mitchell, 1997*

---

## 🛠️ Ferramentas Recomendadas

### Edição de Código:
- [Google Colab](https://colab.research.google.com)
- [Replit](https://replit.com)
- Spyder3, VSCode (Requerem instalação local)

### Repositórios de Dados:
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

### Outros:
- [Draw.io](http://draw.io) – para criação de diagramas
- Anaconda – distribuição Python para Data Science

---

## 📊 Tipos de Tarefas em Machine Learning

| Problema                | Tarefa (T)                                 | Medida (P)                                     | Experiência (E)                              |
|------------------------|---------------------------------------------|------------------------------------------------|---------------------------------------------|
| Filtragem de emails     | Classificar como spam ou legítimo           | % de spam corretamente identificados           | Base de emails rotulados                    |
| Diagnóstico médico      | Diagnosticar pacientes                     | % de diagnósticos corretos                     | Prontuários médicos                         |
| Análise de crédito      | Classificar clientes como bons/mau pagadores| % de classificações corretas                   | Base histórica de pagamentos                |


---

## 🧬 Conjunto de Dados

- **Exemplo (registro)**: linha com dados de um paciente.
- **Atributos (X)**: variáveis descritivas como idade, sintomas, temperatura.
- **Alvo (y)**: atributo de saída (ex.: diagnóstico).

> ❗ Atributos como ID e Nome não devem ser usados como preditores.

### Exemplo de Dados:

```
| Id   | Nome   | Idade | Sexo | Temp | Manchas    | Diagnóstico |
|------|--------|-------|------|------|------------|-------------|
| 4201 | João   | 28    | M    | 38.0 | Concentradas | Doente     |
| 4039 | Luiz   | 49    | M    | 38.0 | Espalhadas   | Saudável   |
| 2301 | Ana    | 22    | F    | 38.0 | Inexistentes | Doente     |
```
---

## ⚙️ Tipos de Aprendizado

### Supervisionado
- Usa pares (X, y)
- Exemplos: Classificação e Regressão
- Algoritmos: Árvores de Decisão, Redes Neurais, SVM, kNN

### Não-Supervisionado
- Apenas X (sem rótulos y)
- Exemplo: Clusterização
- Algoritmos: K-means, C-means, SOM

### Semi-Supervisionado
- Poucos dados rotulados + muitos não rotulados
- Estratégia: combinação de técnicas supervisionadas e não-supervisionadas

---

## 🔁 Fluxo Básico de Machine Learning

1. **Coleta de Dados**
2. **Pré-processamento**: tratar dados faltantes, normalização, etc.
3. **Divisão em treino e teste**
4. **Treinamento** do modelo
5. **Avaliação**: comparação y vs. y’
6. **Ajuste do modelo**
7. **Predição em dados novos**

---

## 🚧 Problemas Comuns

- **Overfitting**: modelo memoriza os dados, mas não generaliza.
- **Underfitting**: modelo falha mesmo nos dados de treino.

---

## 📌 Resumo dos Tipos

```
| Aprendizado             | Dados de Treinamento         | Exemplo                        |
|------------------------|------------------------------|--------------------------------|
| Supervisionado         | Todos os dados rotulados      | Diagnóstico médico             |
| Não-supervisionado     | Nenhum rótulo                 | Agrupamento de clientes        |
| Semi-supervisionado    | Alguns rótulos                | Aplicações com dados escassos  |
```

---

## 🧪 Prática Recomendável

### Pesquise sobre:
- Algoritmos supervisionados (Classificação, Regressão)
- Algoritmos não-supervisionados (Clusterização)
- Bibliotecas: `scikit-learn`, `TensorFlow`
- Alternativas: MATLAB, R, APIs em nuvem

---

## ❓ What’s Next?

- Momento para dúvidas e prática com dados reais
