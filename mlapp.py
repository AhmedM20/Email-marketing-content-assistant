import cohere
import gradio as gr
co = cohere.Client('Place your Api key here') # This is your trial API key get it from cohere page on google

def write_email(tone="",goal="",industry="",text="",audience="",other=""):
    if goal=="Other":
        goal=other
    if audience=="" and industry=="":
        print(f'write 5 different {tone} emails to {goal} {text}')
        Message=f'write 5 different {tone} emails to {goal} {text}'       
    elif audience=="":
        print(f'write 5 different {tone} emails to {goal} in the {industry} industry {text}')
        Message=f'write 5 different {tone} emails to {goal} in the {industry} industry {text}'
    elif industry=="":
        print(f'write 5 different {tone} emails for {audience} to {goal} {text}')
        Message=f'write 5 different {tone} emails for {audience} to {goal} {text}'
    else:
        print(f'write 5 different {tone} emails for {audience} to {goal} in the {industry} industry {text}')
        Message=f'write 5 different {tone} emails for {audience} to {goal} in the {industry} industry {text}'   

    response = co.generate(
    model='command',
    prompt=Message,
    max_tokens=1208,
    temperature=1,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return(response.generations[0].text)



with gr.Blocks() as demo:
  def other_field(choice):
    if choice != "Other":
        return gr.update(visible=False)
    else:
        return gr.update(visible=True)
  gr.Markdown("Create your marketing emails with AI")
  inp1 = gr.Radio(
        ["Convince to buy a product", "Recover churned customers", "Teach a new concept","Onboard users","Share product updates","Other"], value="Convince to buy a product",label = "Campagin goal"
    )
  other=gr.Textbox(visible=False,placeholder="Please enter other text",label = "Other:")
  inp1.input(other_field,inp1, other)
  inp2 = gr.Radio(
        ["Formal", "Semi-formal", "Informal"], value="Formal",label = "Brand Tone"
    )
  inp3 = gr.Textbox(placeholder="Example: marketing agency" ,label = "Industry")
  inp4= gr.Textbox(placeholder="Example:Females aged between 18 and 30" ,label = "Target audience")
  inp5 = gr.Textbox(placeholder="Example: I am offering 10 dollars discount for customers who cancelled their subscription and want to find a way to bring them back ", label = "Tell us more about the email you want to send")
  btn = gr.Button("Generate 🚀")
  out = gr.Textbox(label = "Here is your 5 Generated emails")
  btn.click(fn=write_email, inputs=[inp2, inp1,inp3,inp5,inp4,other], outputs=out)

demo.launch(debug = True)
     
