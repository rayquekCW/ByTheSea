from fastapi import FastAPI, HTTPException
from database import init_db
from pydantic import BaseModel
import models
import openai
import os

app = FastAPI()


@app.on_event("startup")
def on_startup():
    """
    The `on_startup` function is called when the application starts up and it initializes the database.
    """
    init_db()


@app.get("/")
async def root():
    return {"message": "The API has started successfully"}

class prompt(BaseModel):
    content: str
@app.post("/api/safe")
async def get_activities(prompt: prompt):
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages=[
            {"role":"user","content":prompt.content}
        ]
    )
    return completion.choices[0].message.content
class OpenAIRequest(BaseModel):
    content: str

@app.post("/generate_chat")
async def generate_chat(openai_request: OpenAIRequest):
    try:
        # Set the OpenAI API key from the request
        openai.api_key = os.environ["OPENAI_API_KEY"]
        # Create the chat completion
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
{
  "role": "system",
  "content": "Our system allows users to input their job interests and job requirements, encompassing both technical and soft skill descriptions. Your primary responsibility is to assess the user's job_fit and offer valuable recommendations for technical_skills_recommendations, soft_skills_recommendations, and provide a personalise_career_roadmap. Please return a JSON Object structured as follows: { job_fit: 'highly suitable/ suitable/ just right/ not suitable', technical_skills_recommendations: [ 'NA' ], soft_skills_recommendations: [ 'NA'], personalise_career_roadmap: ['NA']}. Ensure that you include your recommendations for each corresponding key."
},
                 
                {"role": "user", "content": "I am interested in the Cargo Handling Supervisor role. We're hiring a Cargo Handling Supervisor to manage warehousing and logistics operations efficiently. It is also required that I have Cargo Handling and Warehousing, Supply Chain Management, Logistics and Inventory Control.These are the technical skills I have: Professional in Cargo Handling and Warehousing, Expert in Logistics and Inventory Control, Expert in Maritime Operations, .When asked about Communication Skills, How comfortable are you when speaking in public or giving presentations? I answered, Very comfortable. When asked about Communication Skills, Do you actively listen to others during conversations? I answered, Yes, I actively listen and engage in conversations. When asked about Communication Skills, How well do you express your ideas and thoughts in writing? I answered, I am proficient in expressing ideas in writing. When asked about Communication Skills, Are you able to adapt your communication style to different audiences? I answered, I can adapt my communication style to suit different audiences. When asked about Communication Skills, How effectively do you provide feedback to colleagues or team members? I answered, I can adapt my communication style to suit different audiences. When asked about Teamwork and Collaboration, How do you handle conflicts within a team? I answered, I address conflicts by facilitating open communication and finding common ground. When asked about Teamwork and Collaboration, Are you open to others' ideas and willing to compromise? I answered, Yes, I value others' ideas and am willing to compromise for the team's success. When asked about Teamwork and Collaboration, Do you take on different roles within a team to support its goals? I answered, I take on various roles to contribute to the team's success. When asked about Teamwork and Collaboration, How do you contribute to a positive team atmosphere? I answered, I promote a positive atmosphere through encouragement and support. When asked about Teamwork and Collaboration, Are you skilled at building relationships and networks within your organization? I answered, I promote a positive atmosphere through encouragement and support. When asked about Adaptability and Flexibility, How well do you handle change and uncertainty? I answered, I adapt well to change and thrive in uncertain situations. When asked about Adaptability and Flexibility, Are you open to trying new approaches and methods? I answered, I adapt well to change and thrive in uncertain situations. When asked about Adaptability and Flexibility, Can you adjust to shifting priorities and work on multiple tasks simultaneously? I answered, I can efficiently manage shifting priorities and multitask. When asked about Adaptability and Flexibility, How do you respond to unexpected challenges or setbacks? I answered, I see setbacks as opportunities for growth and problem-solving. When asked about Adaptability and Flexibility, Are you willing to learn and adapt in response to new information? I answered, I am always eager to learn and adapt based on new information. When asked about Leadership and Influence, Have you taken on leadership roles in the past, even informally? I answered, Yes, I have taken on informal leadership roles. When asked about Leadership and Influence, How do you motivate and inspire others to achieve common goals? I answered, I motivate through setting a clear vision and leading by example. When asked about Leadership and Influence, Are you comfortable making decisions and taking responsibility for outcomes? I answered, I am comfortable making decisions and taking responsibility. When asked about Leadership and Influence, Do you actively seek opportunities to lead or influence within your team or organization? I answered, I actively seek opportunities to lead and influence. When asked about Leadership and Influence, How well do you manage conflicts and resolve disputes as a leader? I answered, I effectively manage conflicts and resolve disputes as a leader. When asked about Problem Solving and Decision-Making, How do you approach complex problems or challenges? I answered, I break down complex problems and tackle them step by step. When asked about Problem Solving and Decision-Making, Are you skilled at gathering information and analyzing data to make decisions? I answered, I excel at gathering information and data analysis. When asked about Problem Solving and Decision-Making, Can you identify creative solutions to problems? I answered, I am creative in finding innovative solutions to problems. When asked about Problem Solving and Decision-Making, How do you prioritize tasks and make decisions in high-pressure situations? I answered, I prioritize tasks and make decisions calmly under pressure. When asked about Problem Solving and Decision-Making, Do you involve others in the decision-making process when appropriate? I answered, I involve others in decision-making when it benefits the outcome. When asked about Emotional Intelligence, Are you aware of your own emotions and how they impact your behavior? I answered, I am highly self-aware of my emotions and their impact. When asked about Emotional Intelligence, How well do you recognize and empathize with the emotions of others? I answered, I am highly self-aware of my emotions and their impact. When asked about Emotional Intelligence, Can you manage and regulate your emotions effectively in stressful situations? I answered, I effectively manage and regulate my emotions in stress. When asked about Emotional Intelligence, Are you skilled at building rapport and establishing trust with colleagues? I answered, I excel at building rapport and establishing trust. When asked about Emotional Intelligence, How do you handle difficult or emotional conversations with sensitivity? I answered, I approach difficult conversations with sensitivity and empathy."}
            ]
        )

        # Extract and return the response message
        response_message = completion.choices[0].message["content"]
        print(response_message)
        return response_message
    except Exception as e:
        raise HTTPException(status_code=500, detail=str("hello world " + e ))
