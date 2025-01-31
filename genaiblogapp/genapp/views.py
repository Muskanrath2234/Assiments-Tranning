from django.shortcuts import render, redirect
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from .forms import BlogForm
from .models import *
import re

# Initialize the LLM
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",  # Add your API key
    model_name="llama3-70b-8192"
)

def blog_Generator(Blog_Topic, Blog_Keyword, Blog_Tone, Blog_Numberofwords, Blog_Target_audiance):
    system_Promt = """
    You are an expert blog writer. Strictly follow the instructions below and generate a high-quality blog:

    1. Write a blog post on the following topic , post write around the given topic: {Blog_Topic}.
    2. Mention the following keywords in the blog: {Blog_Keyword}.
    3. Use the tone specified: {Blog_Tone}.
    4. Limit the blog to {Blog_Numberofwords} words.
    5. Tailor the content for the following target audience: {Blog_Target_audiance}.
    6. Ensure that the blog has a clear introduction, body, and conclusion.
    7. Do not omit any information from the instructions provided.
    8. Write in a formal tone, without using informal language or filler words.
    9. Be concise but informative. Avoid unnecessary repetition and verbosity.
    10. Ensure that the content is easy to read and grammatically correct.
    

    Follow these instructions strictly without deviation. 
    """

    user_Promt = f"Write a blog on {Blog_Topic}, include the following keywords: {Blog_Keyword}, use tone: {Blog_Tone}, the number of words should be: {Blog_Numberofwords}, and the target audience is: {Blog_Target_audiance}. Do not give me any preamble"
    
    # Generate the response from Groq
    response = llm.invoke([
        SystemMessage(content=system_Promt),
        HumanMessage(content=user_Promt)
    ])
    
    # Get the content from the response and format it for HTML
    return response.content

def format_blog_content(blog_content):
    """Format the generated blog content to include basic HTML structure."""
    formatted_content = blog_content.strip()

    # Replace newlines or breaks with <p> for paragraphs
    formatted_content = re.sub(r'(\n|\r|\r\n)+', '</p><p>', formatted_content)
    
    # Wrap content in <div> or <article> for better styling
    formatted_content = f"<div class='blog-content'><p>{formatted_content}</p></div>"
    
    return formatted_content

def Blog_Generator_View(request):
    if request.method == "POST":
        # Get the topic directly from POST request
        Blog_Topic = request.POST.get('Blog_Topic', '')
        Blog_Keyword = request.POST.get('Blog_Keyword', '')
        Blog_Tone = request.POST.get('Blog_Tone', '')
        Blog_Numberofwords = request.POST.get('Blog_Numberofwords', '')
        Blog_Target_audiance = request.POST.get('Blog_Target_audiance', '')
        
        # Ensure the topic is not empty
        if Blog_Topic:
            # Generate the blog content
            blog_content = blog_Generator(Blog_Topic, Blog_Keyword, Blog_Tone, Blog_Numberofwords, Blog_Target_audiance)
            
            # Format the content
            formatted_content = format_blog_content(blog_content)
            
            # Render the result page with formatted content
            return render(request, 'blog_Input_Form.html', {'content': formatted_content})
        else:
            # If no topic is provided, you can show an error message or re-render the form
            error_message = "Please enter a topic."
            return render(request, 'blog_Input_Form.html', {'error_message': error_message})

    return render(request, 'blog_Input_Form.html')
