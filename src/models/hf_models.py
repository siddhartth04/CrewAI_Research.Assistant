# src/models/hf_models.py 
import os
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

class HuggingFaceModel:
    """REAL Hugging Face Model Loader"""
    
    _instances = {}
    
    @classmethod
    def get_llm(cls, model_name="gpt2"):
        """Load a REAL Hugging Face model"""
        
        if model_name in cls._instances:
            return cls._instances[model_name]
        
        try:
            print(f"🔄 Loading REAL model: {model_name}...")
            
            from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
            from langchain.llms import HuggingFacePipeline
            import torch
            
            # Check if CUDA is available
            device = "cuda" if torch.cuda.is_available() else "cpu"
            print(f"📊 Using device: {device}")
            
            # Load tokenizer and model
            tokenizer = AutoTokenizer.from_pretrained(model_name)
            model = AutoModelForCausalLM.from_pretrained(
                model_name,
                torch_dtype=torch.float16 if device == "cuda" else torch.float32,
                device_map="auto" if device == "cuda" else None
            )
            
            # Create pipeline
            pipe = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=200,
                temperature=0.7,
                top_p=0.95,
                repetition_penalty=1.15,
                do_sample=True,
                device=device if device == "cuda" else -1
            )
            
            llm = HuggingFacePipeline(pipeline=pipe)
            cls._instances[model_name] = llm
            print(f"✅ REAL model loaded: {model_name}")
            return llm
            
        except Exception as e:
            print(f"⚠️ Error loading {model_name}: {e}")
            
            # Try fallback models
            fallbacks = ["gpt2", "distilgpt2"]
            for fallback in fallbacks:
                if fallback != model_name:
                    try:
                        print(f"🔄 Trying fallback: {fallback}")
                        return cls.get_llm(fallback)
                    except:
                        continue
            
            print("❌ Could not load any model")
            return None
    
    @classmethod
    def get_embedding_model(cls, model_name="all-MiniLM-L6-v2"):
        """Load a REAL embedding model"""
        try:
            from sentence_transformers import SentenceTransformer
            print(f"🔄 Loading embedding model: {model_name}")
            model = SentenceTransformer(model_name)
            print("✅ Embedding model loaded")
            return model
        except Exception as e:
            print(f"⚠️ Error loading embedding model: {e}")
            return None