from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def getGeminiCompletion(arabic_text):
    #define our prompt template
    template=f"""En se basant sur le document juridique fournis qui est en arabe , donnez-moi les informations suivantes : Dates, Parties impliquéesMots clés,Éléments d'action,Les sujets.
        Important :1) le résultat doit être en arabe et au format json.
        2) en cas d'absence d'une information, veuillez le mentionner.
        Cecci le document juridique :
        {arabic_text} 
    """
    #model inference
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    #invoke the model
    result=llm.invoke(template)
    #convert the result to json in case of error convert it to string
    try :
        parser=JsonOutputParser()
        result=parser.invoke(result.content)
    except:
        result=result.content
    return result