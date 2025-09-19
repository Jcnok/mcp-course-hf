import gradio as gr

def letter_counter(word: str, letter: str) -> int:
    """I
    Conta quantas vezes uma letra aparece em um texto.
    Args:
        word (str): O texto de entrada
        letter (str): Letra a procurar
    Returns:
        int: Número de ocorrências
    """
    return word.lower().count(letter.lower())

demo = gr.Interface(
    fn=letter_counter,
    inputs=["textbox", "textbox"],
    outputs="number",
    title="Contador de Letras",
    description="Entre um texto e uma letra para contar as ocorrências da letra no texto."
    )

if __name__ == "__main__":
    demo.launch(mcp_server=True)
