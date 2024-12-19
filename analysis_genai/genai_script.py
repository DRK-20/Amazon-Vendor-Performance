import google.generativeai as genai

def get_genai_response(product_data):
    prompt = f'''
    Product name - {product_data['product_name']}
    Analyze the product based on customer reviews and feedback:
    1. Identify major issues or problems customers have highlighted.
    2. Suggest ways to resolve these issues and improve the product.

    Give the answer in the following format:
    Issues:
    <1. issues>
    Suggestions:
    <2. suggestions>

    Strictly follow the format without any extra texts before this.
    '''
    genai.configure(api_key='AIzaSyB2e1etzK26R3R0AnkwV3dHeDJ66FWurUc')

    generation_config = {
        'temperature': 0.85,
        'top_p': 0.95,
        'top_k': 64,
        'max_output_tokens': 8192,
        'response_mime_type': 'text/plain',
    }

    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        generation_config=generation_config,
    )

    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(prompt)

    return response.text
