import re
from numpy import extract
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import torch, gc

class TextClassifier:
    def __init__(self, *, case_sensitive=False):
        self.case_sensitive = case_sensitive

    def classify(self, text):
        raise NotImplementedError("Subclasses must implement classify method")
    
    def get_matches(self):
        raise NotImplementedError("Subclasses must implement get_matches method")

class RegexClassifier(TextClassifier):
    def __init__(self, keywords, *, case_sensitive=False):
        self.keywords = keywords
        super().__init__(case_sensitive=case_sensitive)

    def classify(self, text):
        pattern = r"\b(?:{})\w*".format("|".join(map(re.escape, self.keywords)))
        flags = 0 if self.case_sensitive else re.IGNORECASE

        self. matches = re.findall(pattern, text, flags)
        
        return bool(self.matches)
    
    def get_matches(self):
        return self.matches
    

class SimpleSubstringClassifier(TextClassifier):
    def __init__(self, keywords, *, case_sensitive=False):
        self.keywords = keywords
        super().__init__(case_sensitive=case_sensitive)

    def classify(self, text):
        if not self.case_sensitive:
            text = text.lower()
            keywords = {w.lower() for w in self.keywords}
        else:
            keywords = self.keywords

        self.matches = [keyword for keyword in keywords if keyword in text]
        
        return bool(self.matches)
    
    def get_matches(self):
        return self.matches
    

class LLMClassifier(TextClassifier):
    def __init__(self, prompt, model_name="openai/gpt-oss-20b", pos_word = "performance"):
        super().__init__(case_sensitive=False)
        self.prompt_template = prompt
        self.model_name = model_name
        self.prediction = "None"
        self.pos_word = pos_word

        max_mem = {i: "78GiB" for i in range(torch.cuda.device_count())}
        max_mem[0] = "65GiB"

        self.pipe = pipeline(
            "text-generation",
            model=self.model_name,
            device_map="balanced_low_0", 
            model_kwargs = {
                "max_memory":max_mem,
                "offload_folder": "./offload"
            },
        )

        self.pipe.tokenizer.padding_side = "left"
        if self.pipe.tokenizer.pad_token is None:
            self.pipe.tokenizer.pad_token = self.pipe.tokenizer.eos_token

        self.pipe.model.eval()
        torch.set_grad_enabled(False)
        
    def extract_result_for_gptoss(self, text):
        first_word = text
        if "assistantfinal" in text:
            pattern = r"\bassistantfinal\w*"
            first_word = re.findall(pattern, text)[0].replace("assistantfinal", "").lower()
            return first_word
        else:
            return None
    
    def classify(self, text):
        prompt = self.prompt_template.copy()
        prompt.append({
            "role": "user",
            "content": text
        })
        
        with torch.inference_mode():
            output = self.pipe(prompt, max_new_tokens=100000, do_sample=False)
            self.prediction = output[0]["generated_text"][-1]["content"]

        result = False
        if "gpt-oss" in self.llm_model:
            verdict = self.extract_result_for_gptoss(self.prediction)
            if verdict == None:
                result = False
            else:
                result = self.pos_word in verdict
        else:
            result = self.pos_word in self.prediction   

        return result
    
    def get_prediction(self):
        if self.prediction == None:
            raise ValueError("Call classify() first")
        return self.prediction
    
    def get_matches(self):
        raise ModuleNotFoundError("This function is not available for LLMClassifier")
    

class EmbeddingClassifier(TextClassifier):
    def __init__(self, base_text, embedding_model="google/embeddinggemma-300m", similarity_threshold=0.7):
        super().__init__(case_sensitive=False)
        self.base_text = base_text
        self.embedding_model = embedding_model
        self.similarity_threshold = similarity_threshold

        self.model = SentenceTransformer(embedding_model)
        self.base_embeddings = self.model.encode_query(self.base_text)

    def reset(self):
        self.similarities = None
        self.similarity_score = None

    def classify_str(self, text):
        text_embeddings = self.model.encode_document([text])
        self.similarity_score = self.model.similarity(self.base_embeddings, text_embeddings).tolist()[0][0]

        return self.similarity_score > self.similarity_threshold
    
    def classify_docs(self, documents):
        document_embeddings = self.model.encode_document(documents)
        self.similarities = self.model.similarity(self.base_embeddings, document_embeddings).tolist()[0]

        return [val > self.similarity_threshold for val in self.similarities]

    def classify(self, data):
        self.reset()
        if isinstance(data, str):
            return self.classify_str(data)
        elif isinstance(data, list):
            return self.classify_docs(data)
        else:
            raise ValueError("Data can be string of list of strings")

    def get_score(self):
        if self.similarity_score:
            return self.similarity_score
        elif self.similarities:
            return self.similarities
        else:
            raise ValueError("Call classify() first")
        
    def get_matches(self):
        raise ModuleNotFoundError("This function is not available for EmbeddingClassifier")