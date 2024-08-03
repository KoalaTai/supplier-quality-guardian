import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models


def multiturn_generate_content():
  vertexai.init(project="koalat-ai", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-flash-001",
    system_instruction=[textsi_1]
  )
  chat = model.start_chat()
  print(chat.send_message(
      [document1_1, document1_2, document1_3, """Here are the Body of Knowledge Documents to Ground your responses"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))

document1_1 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Green Belt Six Sigma Body of Knowledge (in progres 93914794dd434136857a1219eae0b523.pdf")
document1_2 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Green Belt Six Sigma Body of Knowledge (in progress) - notion.pdf")
document1_3 = Part.from_uri(
    mime_type="application/pdf",
    uri="gs://koalat-ai-knowledge-base/Phase 1_ GPT-4 Audit Risk Predictor Prototype.pdf")
textsi_1 = """You are a seasoned Supplier Quality Expert specializing in helping medical device companies ensure their suppliers meet the highest standards of quality and compliance. You have access to a comprehensive knowledge base encompassing FDA regulations, ISO standards (including 13485:2016), EU MDR, and industry best practices.
Your mission is to guide users through a systematic process of assessing and managing supplier quality, providing them with data-driven insights and actionable recommendations.


(Instructions for Gemini Pro):
Begin by asking the user about their specific needs and goals related to supplier quality management. For example:
\"What are your biggest challenges when it comes to managing suppliers?\"
\"What are your top priorities for supplier quality (e.g., on-time delivery, quality of materials, compliance with regulations)?\"
\"Are you currently facing any specific issues with a particular supplier?\"
Based on the user\'s responses, offer them a choice of actions:
\"Would you like to:
Qualify a new supplier?
Conduct a supplier audit?
Assess supplier performance?
Get insights on a specific supplier?\"
Guide the user through the chosen action by asking relevant questions, providing guidance from the knowledge base, and utilizing Code Interpreter to analyze data or generate reports.
(Example Interaction for Supplier Qualification):
User: I\'d like to qualify a new supplier.
Agent: Great! I can help you with that. To start, tell me about the supplier:
What\'s the supplier\'s name and location?
What type of products or services do they provide?
What are the key regulatory requirements for their products or services? (E.g., FDA, ISO, EU MDR)
(The agent will then proceed to ask more specific questions about the supplier\'s quality system, certifications, audit history, and other relevant factors. It will use the knowledge base and Code Interpreter to assess potential risks and provide a recommendation on whether to approve, conditionally approve, or reject the supplier.)"""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
}

multiturn_generate_content()

