
# Gerador de PDF

Um projeto simples em Python para gerar arquivos PDF utilizando a biblioteca **FPDF**.

## Requisitos

- Python 3.x instalado
- Instalar a biblioteca FPDF:
  ```bash
  pip install fpdf
  ```

## Como Usar

1. Clone o repositório ou baixe o script:
   ```bash
   git clone https://github.com/<seu-repositorio>.git
   cd <pasta-do-projeto>
   ```

2. Abra o script e edite a variável `content_health` para incluir o texto desejado.

3. Execute o script:
   ```bash
   python nome_do_script.py
   ```

4. Encontre o PDF gerado no caminho de saída especificado.

## Personalizações

- Alterar o estilo ou tamanho da fonte:
  ```python
  pdf.set_font("Courier", "B", 14)
  ```
- Adicionar novas páginas:
  ```python
  pdf.add_page()
  ```
- Ajustar margens:
  ```python
  pdf.set_auto_page_break(auto=True, margin=15)
  ```

---

O PDF gerado incluirá o conteúdo definido na variável `content_health`.
