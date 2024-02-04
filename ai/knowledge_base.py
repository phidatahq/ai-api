from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.combined import CombinedKnowledgeBase
from phi.knowledge.pdf import PDFUrlKnowledgeBase, PDFKnowledgeBase
from phi.vectordb.pgvector import PgVector2

from db.session import db_url

pdf_knowledge_base = CombinedKnowledgeBase(
    sources=[
        PDFUrlKnowledgeBase(
            urls=["https://www.family-action.org.uk/content/uploads/2019/07/meals-more-recipes.pdf"]
        ),
        PDFKnowledgeBase(path="data/pdfs"),
    ],
    # Store this knowledge base in ai.pdf_documents
    vector_db=PgVector2(
        schema="ai",
        db_url=db_url,
        collection="pdf_documents",
        embedder=OpenAIEmbedder(model="text-embedding-3-small"),
    ),
    # 2 references are added to the prompt
    num_documents=2,
)