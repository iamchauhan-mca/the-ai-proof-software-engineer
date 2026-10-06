"""
Station 7: Production-Grade LLM API Interaction & SSE Streaming
The AI-Proof Software Engineer - Vivek Chauhan
"""

import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

def run_streaming_session():
    # 1. Isolate and load configurations cleanly from environment parameters
    # Looks for a root .env file or fallback locations
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    # Secure Architecture Check: Stop executing instantly if security keys are absent
    if not api_key or api_key == "your_sk_live_openai_api_key_goes_here":
        print("❌ SECURITY ERROR: 'OPENAI_API_KEY' environment variable not set.")
        print("Please create a '.env' file using the template provided in the toolkit.")
        sys.exit(1)

    # 2. Instantiate the standardized API engine interface
    # Automatically tracks keys populated inside the OS environment layer
    client = OpenAI()

    # 3. Define structured role instructions and learner queries
    # Utilizing the book's specific RTCFE structuring framework
    system_role = "You are a senior systems architect delivering highly direct, technical answers."
    user_query = "Explain the structural difference between Basic RAG and Advanced Production-Grade RAG paths in two sentences."
    
    # Fixed policy audit note: Replaced non-existent model placeholders with the current industry standard 'gpt-4o'
    model_tier = "gpt-4o" 

    print("=" * 60)
    print(f"🤖 Interfacing with Model Tier: {model_tier}")
    print(f"💬 Query: '{user_query}'")
    print("=" * 60)
    print("⚡ Streamed Server-Sent Events (SSE) Response:\n")

    try:
        # 4. Initialize a live stream channel connection mapping directly into the interface endpoint
        stream = client.chat.completions.create(
            model=model_tier,
            messages=[
                {"role": "system", "content": system_role},
                {"role": "user", "content": user_query}
            ],
            stream=True, # Active streaming triggers server token processing instantly
            temperature=0.2 # Lower structural variance keeps code/architecture context consistent
        )

        # 5. Iteratively process live token data chunks incoming from the server connection buffer
        for chunk in stream:
            # Safely navigate dictionary payloads ensuring variations across data packets do not cause system failures
            if chunk.choices and chunk.choices[0].delta.content is not None:
                token_text = chunk.choices[0].delta.content
                # Stream directly into standard output stream without breaking text lines apart prematurely
                sys.stdout.write(token_text)
                sys.stdout.flush()

        print("\n\n" + "=" * 60)
        print("✅ Transaction Process Complete. Secure network pipeline safely disconnected.")
        print("=" * 60)

    except Exception as error_context:
        print(f"\n❌ Network or API Error Encountered: {error_context}")
        print("Troubleshooting Tip: Verify network connection stability, API credits, or account limits.")

if __name__ == "__main__":
    run_streaming_session()
