
#I HAVE USED GPT FOR CLEANING AND PROPER ORCHESTRATION OF THE CODE BLOCKS 

from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
import os


# =========================
# LOAD ENV VARIABLES
# =========================
load_dotenv()


# =========================
# LOAD LLM
# =========================
llm = OllamaLLM(
    model="llama3.2"
)


# =========================
# FUNCTION TO FETCH + TRANSLATE TRANSCRIPT
# =========================
def get_english_transcript(video_id):

    transcript_text = ""

    try:
        ytt_api = YouTubeTranscriptApi()

        # Get all transcripts
        transcript_list = ytt_api.list(video_id)

        try:
            # Try English transcript first
            fetched_transcript = transcript_list.find_transcript(['en']).fetch()

            print("English transcript found.")

            transcript_text = " ".join(
                chunk.text for chunk in fetched_transcript
            )

        except:
            # Otherwise use first available language
            available_transcript = next(iter(transcript_list))

            print(f"Original language: {available_transcript.language}")

            # Fetch original transcript
            fetched_transcript = available_transcript.fetch()

            original_text = " ".join(
                chunk.text for chunk in fetched_transcript
            )

            # Translate using LLM
            translation_prompt = f"""
            Translate the following text into English.

            Text:
            {original_text}
            """

            transcript_text = llm.invoke(translation_prompt)

            print("Transcript translated to English.")

    except TranscriptsDisabled:
        print("No captions available for this video.")

    except Exception as e:
        print("Error:", e)

    return transcript_text


# =========================
# VIDEO ID
# =========================
video_id = "etnLX7m2MiA"


# =========================
# GET TRANSCRIPT
# =========================
transcript = get_english_transcript(video_id)

if not transcript:
    print("Transcript could not be fetched.")
    exit()


# =========================
# SPLIT INTO CHUNKS
# =========================
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.create_documents([transcript])


# =========================
# CREATE EMBEDDINGS
# =========================
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# =========================
# STORE IN FAISS
# =========================
vector_store = FAISS.from_documents(chunks, embeddings)


# =========================
# RETRIEVER
# =========================
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)


# =========================
# PROMPT TEMPLATE
# =========================
prompt = PromptTemplate(
    template="""
    You are a helpful assistant.

    Answer ONLY from the provided transcript context.

    If the context is insufficient, just say you don't know.

    Context:
    {context}

    Question:
    {question}
    """,
    input_variables=['context', 'question']
)


# =========================
# USER QUESTION
# =========================
question = """
Is the topic of nuclear fusion discussed in this video?
If yes then what was discussed.
Also summarize the video.
"""


# =========================
# RETRIEVE RELEVANT DOCS
# =========================
retrieved_docs = retriever.invoke(question)

context_text = "\n\n".join(
    doc.page_content for doc in retrieved_docs
)


# =========================
# FINAL PROMPT
# =========================
final_prompt = prompt.format(
    context=context_text,
    question=question
)


# =========================
# GENERATE ANSWER
# =========================
answer = llm.invoke(final_prompt)


# =========================
# PRINT ANSWER
# =========================
print("\n\n===== ANSWER =====\n")
print(answer)